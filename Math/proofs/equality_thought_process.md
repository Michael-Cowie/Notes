<div align='center'>
    <h1> Equality Proofs Thought Process </h1>
</div>

Mathematics is often presented as a collection of formulas and symbolic manipulations, but equality proofs operate on a deeper principle, the preservation of truth through logically justified transformations. When writing,

```math
A = B
```

the claim being made is that both expressions represent exactly the same mathematical object or quantity.

This perspective changes the entire nature of algebraic work. A proof is no longer a process of "moving symbols around until the expressions look similar". Instead, it becomes a process of preserving equivalence while uncovering the underlying structure connecting both sides of the equation.

Mathematical reasoning during equality proofs is fundamentally a process of controlled logical transformation. At every stage the following questions guide the proof.

- What structure is present?
- Which definitions apply?
- Does this operation preserve equivalance?
- Is the step reversible?
- Were any restrictions introduced or ignored?
- Does the transformation preserve the domain?

In advanced mathematics, the goal is rarely to manipulate symbols mechanically. The goal is to preserve truth while revealing the deeper relationships hidden within the expressions themselves. The process is usually not "How do I manipulate this symbol?" but rather **"What is this expression fundamentally built from?"**.

- A rational expression suggests factoring and cancellation structure.
- A trigonometric identity suggests angle or geometric structure.
- A derivative suggests a limiting ratio

The thinking process is often therefore

1. Identify the mathematical object involved.
2. **Reduce it to foundational definitions or known structures.**
3. Use operations that preserve equivalence.
4. Rebuild the expression toward the target form.

When encountering an equality such as

```math
\log_b (x^n) = n \log_b (x)
```

the important question is not whether the identity has been memorised before, but rather "Why should these two expressions represent the same quantity?".

Mathematical thinking begins by **identifying structure**. In this example,

- Logarithms represent exponents.
- Exponentiation and logarithms are inverse operations.
- Powers inside logairthms are often related to multiplication outside them.

**Most successful proofs begin by reducing unfamiliar expressions to their definitions**. Definitions provide the logical foundation from which algebraic rules emerge.

Consider again,

```math
\log_b(x^n) = n \log_b(x)
```

A productive first observation is that logarithms are usually easier to understand in exponential form. Define

```math
y = \log_b(x)
```

By the definition of logarithms

```math
b^y = x
```

At this stage, the structure of the target expression becomes important. The original equality contains $x^n$, suggesting that raising both sides to the power $n$ may help produce the desired form.

```math
\begin{aligned}
(b^y)^n &= x^n \\
b^{yn} &= x^n
\end{aligned}
```

Now another structural relationship appears. Since logarithms and exponentials are inverse functions, applying $\log_b$ to both sides should simplify the exponential. Additionally, applying $\log_b$ to both sides is how we change $x^n$ to $\log_b(x^n)$, which gives the desired expression.

```math
\log_b(b^{yn}) = \log_b(x^n)
```

This becomes,

```math
yn = \log_b(x^n)
```

Substituting back,

```math
y = \log_b(x)
```

gives

```math
n \log_b(x) = \log_b(x^n)
```

or equivalently

```math
\boxed{\log_b(x^n) = n \log_b(x)}
```

The important feature of this proof is not the algebra itself, but the reason motivating each step.

- Logarithms were converted into exponentials.
- Exponent laws were used, **foundational definitions**.
- The inverse relationship between logarithms and exponentials was exploited.
- Substitution restored the original notation.

The manipulations were guided entirely by structure and definition.

<div align='center'>
    <h1> Equality Proofs Thought Process </h1>
</div>

An essential part of equality proofs is determining whether each operation preserves equivalnce. Many valid algebraic operations are reversible.

```math
a = b \Rightarrow a + c = b + c
```

Adding the same quantity to both sides preserves equality because the process can be reversed by subtraction. However, not all operations behave this way. Squaring both sides is not fully reversible.

```math
a = b \Rightarrow a^2 = b^2
```

However, $a^2 = b^2$ does not necessarily imply $a=b$. For example, $(-3)^2 = 3^2$. The operation destroyed sign information. Mathematical thinking therefore involves constant awareness of whether a transformation preserves all information or loses part of it. This concern becomes especially important when dividing expressions, cancelling factors, applying square roots or manipulating logarithms.

<div align='center'>
    <h1> Detecting False Equalities </h1>
</div>

The same structural thinking used to prove identities can also disprove them.

Consider

```math
\log(x + y) = \log(x) + \log(y)
```

A structural observation immediately creates suspicion.

1. Logarithms convert multiplication into addition.
2. The expression contains addition inside the logarithm.

This mismatch suggests the equality may not hold. **A single counterexample** is enough to disprove a universal statement. Choosing $x = 1$ and $y = 1$ gives

```math
\log(1 + 1) = \log(1) + \log(1)
```

Whereas

```math
\log(2) \neq 0 + 0
```

The equality fails. Disproving an identity therefore requires far less work than proving one. A proof must establish truth in all valid cases, **whereas a disproof requires only one contradiction**.

<div align='center'>
    <h1> Hidden Illegal Operations </h1>
</div>

Some algebraic manipulations appear valid while secretly violating fundamental rules. Consider,

```math
\frac{x^2 - 9}{x - 3} = x + 3
```

Factoring gives

```math
\frac{(x - 3)(x + 3)}{x - 3}
```
Cancelling $(x-3)$ gives $x + 3$. However, cancellation is equivalent to division. If

```math
x - 3 = 0
```

then the cancellation step divides by zero, which is undefined. Thus the equality is only valid when $x \neq 3$. This illustrates an important principle, algebraic manipulations must preserve not only numerical equality, but also domain validity. If this was not kept in check, false proofs can exist such as proving $2 = 1$.

Suppose

```math
a = b
```

Then

```math
\begin{aligned}
a &= b \\
a^2 &= ab \\
a^2 - b^2 &= ab - b^2 \\
(a-b)(a+b) &= b(a-b)
\end{aligned}
```

Now cancel $(a - b)$

```math
a + b = b
```

Since $a = b$, it follows $2b = b$. Then dividing by $b$ gives $2 = 1$.

The algebra appears convincing, yet the conclusion is absurd. The critical observation is,

```math
a = b \Rightarrow a - b = 0
```

So cancelling $(a - b)$ is a division by zero and therefore is not a valid operation. This example illustrates why mathematical thinking requires more than symbolic manipulation. Every transformation must be checked for legality.



<div align='center'>
    <h1> Structure Recognition in Equations </h1>
</div>

Many proofs become simple once structural similarities are recognized.

Consider,

```math
2^{x + 1} = 16
```

The important observation is that

```math
16 = 2^4
```

The equation becomes

```math
2^{x + 1} = 2^4
```

Now both sides share the same base. This structure immediately implies

```math
x + 1 = 4
```

giving $x = 3$. The solution emerges not from trial-and-error manipulation, but from **recognising compatible forms**.
