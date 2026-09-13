const toggle = document.querySelector(".menu-toggle");
const nav = document.querySelector(".top-nav");
if (toggle && nav) {
  toggle.addEventListener("click", () => {
    const expanded = toggle.getAttribute("aria-expanded") === "true";
    toggle.setAttribute("aria-expanded", expanded ? "false" : "true");
    nav.classList.toggle("open");
  });
}

// Keep the referral URL consistent across every page using the shared script.
const TOWER_RUSH_REF = "https://w-one973.com/v3/5768/tower-rush?p=0o47";
const OLD_TOWER_RUSH_REF = "https://one-vv793.com/v3/5768/tower-rush?p=0o47";

document.querySelectorAll('a[href]').forEach((link) => {
  const href = link.getAttribute("href");
  if (href === OLD_TOWER_RUSH_REF || (href && href.includes("one-vv793.com/v3/5768/tower-rush"))) {
    link.setAttribute("href", TOWER_RUSH_REF);
  }
});

if (!document.querySelector(`a[href="${TOWER_RUSH_REF}"]`)) {
  const footer = document.querySelector(".site-footer") || document.body;
  const wrap = document.createElement("div");
  wrap.className = "ref-link";
  wrap.style.marginTop = "12px";
  wrap.innerHTML = `<a href="${TOWER_RUSH_REF}" target="_blank" rel="nofollow sponsored noopener">Играть в Tower Rush</a>`;
  footer.appendChild(wrap);
}
