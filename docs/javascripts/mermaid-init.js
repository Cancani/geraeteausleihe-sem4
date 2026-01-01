document.addEventListener("DOMContentLoaded", function () {
  const getMermaidTheme = () => {
    const scheme = document.body.getAttribute("data-md-color-scheme");
    return scheme === "slate" ? "dark" : "default";
  };

  const initMermaid = () => {
    if (typeof mermaid === "undefined") return;

    mermaid.initialize({
      startOnLoad: false,
      theme: getMermaidTheme()
    });

    document.querySelectorAll(".mermaid").forEach((el) => {
      el.removeAttribute("data-processed");
    });

    mermaid.init(undefined, document.querySelectorAll(".mermaid"));
  };

  if (window.document$) {
    document$.subscribe(() => initMermaid());
  } else {
    initMermaid();
  }

  const observer = new MutationObserver(() => initMermaid());
  observer.observe(document.body, { attributes: true, attributeFilter: ["data-md-color-scheme"] });
});
