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

Whenever a fraction appears **inside a pair of parentheses, square brackets, or braces**, use `\left` and `\right` for that pair so the delimiters grow to fit the fraction. Apply this rule to each enclosing pair that contains the fraction. Do not automatically enlarge other pairs that do not contain a fraction.

For example, use scalable parentheses around the fraction-containing coordinate:

```math
p = (0, 0, 0) + \frac{2}{3}\left(1, 0, 0\right)
```

Here, the first coordinate tuple does not contain a fraction, so its parentheses remain ordinary. The second pair contains a fraction and therefore uses `\left(` and `\right)`.

Use matching pairs: `\left(` with `\right)`, `\left[` with `\right]`, and `\left\{` with `\right\}`. For a delimiter that should be invisible on one side, use `\left.` or `\right.`.

## Literal Percent Signs

In LaTeX math, write a percentage as `\%`, not a bare `%`. For example:

```math
20\% = \frac{20}{100} = 0.2
```

For inline math, use `$20\%$`. A bare percent sign starts a LaTeX comment and can cause the rest of the expression to disappear. If the percent sign is ordinary prose outside math delimiters, write it normally (for example, `20%`).


## Indented Questions

When presenting a standalone question or statement that should be indented within an explanation, use a normal HTML paragraph and begin its text with four non-breaking spaces (`&nbsp;`). GitHub's Markdown renderer may ignore inline CSS indentation, whereas non-breaking spaces visibly indent the text while preserving normal paragraph spacing.

Use this pattern:

```html
<p>
&nbsp;&nbsp;&nbsp;&nbsp;Your indented question or statement goes here.
</p>
```

- Use four `&nbsp;` entities at the start of the question or statement to indent it.
- Keep the text inside a normal `<p>` element so it retains ordinary paragraph spacing.
- Do not use inline CSS for indentation, blockquotes, extra `<br>` tags, or spacer elements.
- Continue with the next paragraph normally.


## Punctuation in Displayed Mathematics

Do not place a full stop at the end of a displayed mathematical expression. Keep terminal punctuation in the surrounding prose instead; displayed equations should end with the mathematical expression itself, not a trailing period. Apply this consistently to single-line and multiline `math` blocks.
