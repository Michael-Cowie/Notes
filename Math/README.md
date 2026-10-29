<div align='center'>
    <h1> GitHub Markdown MathJax Rendering Notes
</div>

When writing LaTeX math in Markdown, rendering may differ between local preview tools and the GitHub website. Formats that render locally will not always display correctly when viewing them on the GitHub website, below is a series of guidelines to ensure proper rendering when using MathJax.

## Inline Expressions

**Use** `$...$` **only**!

Avoid `\(...\)` for inline math expressions. Additionally, ensure there is **no whitespace inside the delimiters**. This means `$...$` is the only valid expression. While other expressions such as `$ ...$` and `$ ... $` may render locally, it will not render correctly on the GitHub website.

## Block / Multiline Expressions

To render math blocks, **the only acceptable format** is to use a fenced block using `ˋˋˋmath`.

```
ˋˋˋmath
a + b = c
ˋˋˋ
```

For multiline expressions, **avoid any other styles** such as the commonly used

```text
\[
a + b = c
\]
```

and

```
$$
a + b = c
$$
```

Although these may render locally, they are **unreliable on GitHub** and may be flattened into inline text or fail to render consistently.


## Scalable Brackets and Parentheses

When an expression contains a fraction, summation, integral, matrix, or other tall expression inside parentheses or brackets, use `\left` and `\right` so the delimiters grow to fit the contents.

```math
\left(\frac{a+b}{c+d}\right)
\qquad
\left[\frac{n!}{k!(n-k)!}\right]
```

Use matching pairs: `\left(` with `\right)`, `\left[` with `\right]`, and `\left\{` with `\right\}`. For a delimiter that should be invisible on one side, use `\left.` or `\right.`. Do not add `\left` and `\right` to every small inline expression; use them when the contents need larger delimiters.

## Literal Percent Signs

In LaTeX math, write a percentage as `\%`, not a bare `%`. For example:

```math
20\% = \frac{20}{100} = 0.2
```

For inline math, use `$20\%$`. A bare percent sign starts a LaTeX comment and can cause the rest of the expression to disappear. If the percent sign is ordinary prose outside math delimiters, write it normally (for example, `20%`).

## Checking Inline Math Delimiters

Every inline math expression must have a matching opening and closing dollar sign on the same line, for example `$P(A)$` or `$20\%$`. Check for missing closing dollar signs, especially before punctuation. Do not put a complete math expression inside another pair of dollar signs. Keep prose outside the delimiters and mathematical notation inside them.
