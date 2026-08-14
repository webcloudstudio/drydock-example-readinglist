"use strict";

document.querySelectorAll("[data-loading-form]").forEach((form) => {
  form.addEventListener("submit", () => {
    const state = document.querySelector("[data-loading-state]");
    if (state) state.hidden = false;
    form.querySelectorAll("button").forEach((button) => {
      button.disabled = true;
      button.setAttribute("aria-busy", "true");
    });
  });
});
