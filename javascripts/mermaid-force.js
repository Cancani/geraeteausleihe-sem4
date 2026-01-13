document.addEventListener("DOMContentLoaded", () => {
  if (!window.mermaid) return;

  mermaid.initialize({
    startOnLoad: false,
    theme: "default",
    securityLevel: "loose"
  });

  document.querySelectorAll("pre > code.language-mermaid").forEach((block, i) => {
    const container = document.createElement("div");
    container.className = "mermaid";
    container.textContent = block.textContent;

    block.parentElement.replaceWith(container);
  });

  mermaid.run();
});
