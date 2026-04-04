<div align='center'>
    <h1> GitHub Markdown MathJax Rendering Notes
</div>

When writing LaTeX math in Markdown, rendering may differ between local preview tools and the GitHub website. Formats that render locally will not always display correctly when viewing them on the GitHub website, below is a series of guidelines to ensure proper rendering when using MathJax.

## Inline Expressions

**Use** \$...\$ **only**!

Avoid \\(...\\) for inline math expressions. Additionally, ensure there is **no whitespace inside the delimiters**. This means \$...\$ is the only valid expression. While other expressions such as \$ ...\$ and \$ ... \$ may render locally, it will not render correctly on the GitHub website.

## Block / Multiline Expressions

To render math blocks, **the only acceptable format is to use a fenced block \```math**.


\```math
a + b = c
\```


For multiline or display-style equations, **avoid any other style** such as the commonly used

\\[
... 
\\]


and

\$\$
...
\$\$

Although these may render locally, they are **unreliable on GitHub** and may be flattened into inline text or fail to render consistently.
