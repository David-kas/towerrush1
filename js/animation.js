const toggle = document.querySelector(".menu-toggle");
const nav = document.querySelector(".top-nav");
if (toggle && nav) {
  toggle.addEventListener("click", () => {
    const expanded = toggle.getAttribute("aria-expanded") === "true";
    toggle.setAttribute("aria-expanded", expanded ? "false" : "true");
    nav.classList.toggle("open");
  });
}
