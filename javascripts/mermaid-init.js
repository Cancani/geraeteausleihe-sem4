document.addEventListener("DOMContentLoaded", function () {
  const initMermaid = () => {
    if (typeof mermaid === "undefined") return;

    mermaid.initialize({
      startOnLoad: false,
      theme: "dark"
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
});
