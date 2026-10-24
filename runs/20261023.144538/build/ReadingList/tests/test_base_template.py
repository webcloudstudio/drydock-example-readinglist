"""Base layout template: title block, main content block, and error region."""

from html.parser import HTMLParser

from flask import render_template

from app_server import create_app


class _Page(HTMLParser):
    """Collects the title text and the text of every role="alert" element."""

    def __init__(self) -> None:
        super().__init__()
        self.title = ""
        self.alerts: list[str] = []
        self._in_title = False
        self._alert_depth = 0
        self._alert_text: list[str] = []

    def handle_starttag(self, tag, attrs):
        if tag == "title":
            self._in_title = True
        if self._alert_depth:
            self._alert_depth += 1
        elif ("role", "alert") in attrs:
            self._alert_depth = 1
            self._alert_text = []

    def handle_endtag(self, tag):
        if tag == "title":
            self._in_title = False
        if self._alert_depth:
            self._alert_depth -= 1
            if self._alert_depth == 0:
                self.alerts.append("".join(self._alert_text))

    def handle_data(self, data):
        if self._in_title:
            self.title += data
        if self._alert_depth:
            self._alert_text.append(data)


def _parse(html: str) -> _Page:
    page = _Page()
    page.feed(html)
    page.close()
    return page


def test_base_template_loads_from_application_template_folder():
    app = create_app()

    template = app.jinja_env.get_template("base.html")

    assert template is not None


def test_base_template_renders_supplied_error_text_in_alert_region():
    app = create_app()
    message = "bound error reason"

    with app.test_request_context("/"):
        html = render_template("base.html", error=message)

    assert _parse(html).alerts == [message]


def test_base_template_renders_without_alert_region_when_error_absent():
    app = create_app()

    with app.test_request_context("/"):
        html = render_template("base.html")

    assert _parse(html).alerts == []


def test_base_template_renders_without_alert_region_when_error_is_empty():
    app = create_app()

    with app.test_request_context("/"):
        html = render_template("base.html", error="")

    assert _parse(html).alerts == []


def test_base_template_renders_without_alert_region_when_error_is_none():
    app = create_app()

    with app.test_request_context("/"):
        html = render_template("base.html", error=None)

    assert _parse(html).alerts == []


def test_base_template_error_text_is_html_escaped():
    app = create_app()
    hostile = "<script>alert(1)</script>"

    with app.test_request_context("/"):
        html = render_template("base.html", error=hostile)

    page = _parse(html)
    assert page.alerts == [hostile]
    assert "<script>" not in html


def test_base_template_title_defaults_to_reading_list():
    app = create_app()

    with app.test_request_context("/"):
        html = render_template("base.html")

    assert _parse(html).title == "Reading List"


def test_child_template_overrides_title_block():
    app = create_app()
    child = app.jinja_env.from_string(
        '{% extends "base.html" %}'
        "{% block title %}Shelf{% endblock %}"
        "{% block content %}<p>body</p>{% endblock %}"
    )

    with app.test_request_context("/"):
        html = child.render()

    assert _parse(html).title == "Shelf"


def test_child_template_fills_main_content_block():
    app = create_app()
    child = app.jinja_env.from_string(
        '{% extends "base.html" %}{% block content %}<p id="marker">filled</p>{% endblock %}'
    )

    with app.test_request_context("/"):
        html = child.render()

    assert '<p id="marker">filled</p>' in html
    assert html.index('<main>') < html.index('id="marker"') < html.index('</main>')


def test_child_template_error_appears_in_alert_region_above_content():
    app = create_app()
    child = app.jinja_env.from_string(
        '{% extends "base.html" %}{% block content %}<p>body</p>{% endblock %}'
    )

    with app.test_request_context("/"):
        html = child.render(error="rejected: title is empty")

    assert _parse(html).alerts == ["rejected: title is empty"]
    assert html.index('role="alert"') < html.index("<p>body</p>")
