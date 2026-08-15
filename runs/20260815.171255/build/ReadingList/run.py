"""Development entry point for ReadingList."""

from app import create_app

application = create_app()


if __name__ == "__main__":
    application.run()
