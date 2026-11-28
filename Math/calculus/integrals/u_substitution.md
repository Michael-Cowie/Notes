<div align='center'>
    <h1> U-Substitution </h1>
</div>

U-substitution is a technique used to simplify integration by replacing part of an expression with a new variable. It is particularly useful when an integrand contains a composite function, where one function is nested inside another.

For example, consider expressions such as,

```math
(x^2+3)^4 \qquad \sin(3x) \qquad e^{x^2}
```

Rather than integrating these expressions directly, we can identify an inner function, substitute it with a new variable $u$, and rewrite the integral in a simpler form. The purpose of u-substitution is therefore to transform a complicated integral into one that can be evaluated using familiar integration rules.


U-substitution is closely related to the chain rule in differentiation. In fact, it can be understood as reversing the chain rule. Recall that the chain rule allows us to differentiate a composite function by introducing an intermediate variable. For example, suppose,

```math
y=(x^2+3)^4
```

We can introduce an intermediate variable,

```math
u=x^2+3
```

This gives us the transition,

```math
x \xrightarrow{\frac{du}{dx}} u
\xrightarrow{\frac{dy}{du}} y
```

Applying the chain rule,

```math
\begin{aligned}
\frac{dy}{dx}
&=\frac{du}{dx}\cdot\frac{dy}{du}\\
&=2x\cdot4u^3\\
&=8x(x^2+3)^3
\end{aligned}
```

Notice that differentiating the composite function produces two components,

-  The derivative of the inner function
-  The derivative of the outer function. 
  
U-substitution works in the opposite direction. When we encounter an integral containing these same components, we can identify the inner function, replace it with $u$, and use its derivative to simplify the integral.

```math
\begin{gathered}
\textbf{Differentiate — Chain Rule}\\[6pt]
u=g(x)
\qquad
\frac{du}{dx}=g'(x)\\[4pt]
\frac{dy}{dx}
=
\frac{dy}{du}
\cdot
\underbrace{\frac{du}{dx}}_{\text{Multiply by derivative}}
\\[12pt]
\downarrow\qquad
\text{Reverse process}
\qquad\uparrow
\\[12pt]
\textbf{Integrate — U-Substitution}\\[6pt]
du=g'(x)\,dx\\[4pt]
dx=
\frac{du}{\underbrace{g'(x)}_{\text{Divide by derivative}}}
\end{gathered}

```

The general relationship is,

```math
\begin{aligned}
u&=g(x)\\
du&=g'(x)\,dx
\end{aligned}
```

Therefore, an integral of the form,

```math
\int f(g(x))g'(x)\,dx
```

can be rewritten as,

```math
\boxed{\int f(u)\,du}
```


The process generally follows four steps,

1. **Identify** an inner function and substitute it with $u$.
2. **Differentiate** the substitution to find $du$.
3. **Rewrite** the entire integral in terms of $u$.
4. **Integrate** and substitute the original expression back in terms of $x$.

An important part of this process is ensuring that the entire integral is expressed using the new variable. This means replacing both the original function and its corresponding differential.

### Changing the Limits of Definite Integrals

When using u-substitution with a definite integral, we must remember that changing the integration variable also requires changing the integration limits. For example, suppose we choose the substitution,

```math
u=g(x)
```

Our original integral uses $x$ as its integration variable, with lower and upper limits $a$ and $b$. Once we substitute $u=g(x)$, the limits must also be expressed in terms of $u$.

The transformation can be represented as,

```math
\boxed{
\int_{x=a}^{x=b}
\quad\xrightarrow{\quad u=g(x)\quad}\quad
\int_{u=g(a)}^{u=g(b)}
}
```

To obtain our new limits, we simply substitute the original lower and upper limits into our expression for $u$.

For example, if,

```math
u=x^2+1
```

and our original integration limits are $x=0$ and $x=1$, our new limits become,

```math
\begin{aligned}
x=0 &\implies u=0^2+1=1\\
x=1 &\implies u=1^2+1=2
\end{aligned}
```

Therefore, our integration limits change from $0$ and $1$ to $1$ and $2$.

```math
\int_{x=0}^{x=1}
\quad\xrightarrow{\quad u=x^2+1\quad}\quad
\int_{u=1}^{u=2}
```

This is essential because the entire integral must be expressed using the same integration variable. We cannot change the integrand and differential from $x$ to $u$ while leaving the original $x$-based limits unchanged.

Unlike indefinite integration, where we substitute back into our original variable after integrating, definite integration allows us to keep the new variable throughout the calculation, provided we have converted both limits.

<div align='center'>
    <h1> Examples </h1>
</div>

### Example 1 — Basic Substitution

Consider the integral,

```math
\int 8x(x^2+3)^3\,dx
```

We can identify the inner function as $x^2+3$, so let,

```math
\begin{aligned}
u&=x^2+3\\
du&=2x\,dx
\end{aligned}
```

There are two ways we can approach the substitution.

##### Approach 1 — Replace the matching expression

We know that,

```math
du=2x\,dx
```

Our original integral contains $8x\,dx$, which is four times our expression for $du$. Therefore,

```math
4du=8x\,dx
```

We can now replace both the inner function and the corresponding differential,

```math
\begin{aligned}
\int 8x(x^2+3)^3\,dx
&=4\int u^3\,du\\
&=4\left(\frac{u^4}{4}\right)+C\\
&=u^4+C
\end{aligned}
```

##### Approach 2 — Replace $dx$ directly

Alternatively, we can rearrange our expression for $du$ to make $dx$ the subject,

```math
\begin{aligned}
du&=2x\,dx\\
dx&=\frac{du}{2x}
\end{aligned}
```

We can then substitute $u$ and $dx$ directly into our original integral,

```math
\begin{aligned}
\int 8x(x^2+3)^3\,dx
&=\int 8x(u)^3\left(\frac{du}{2x}\right)\\
&=\int 4u^3\,du\\
&=4\left(\frac{u^4}{4}\right)+C\\
&=u^4+C
\end{aligned}
```

Notice that the $x$ terms cancel, leaving an integral entirely in terms of $u$. Both approaches produce the same result. Finally, substitute our original expression back in place of $u$,

```math
\boxed{
\int 8x(x^2+3)^3\,dx
=(x^2+3)^4+C
}
```

The first approach replaces the matching expression $8x\,dx$ directly, while the second replaces $dx$ and simplifies the resulting expression. Both are valid ways of performing u-substitution.

### Example 2 — Trigonometric Substitution

U-substitution is not limited to polynomial expressions. It can also simplify trigonometric functions, particularly when their arguments contain a multiple of $x$.

Consider,

```math
\int\cos(3x)\,dx
```

We identify the inner function as $3x$, so let,

```math
\begin{aligned}
u&=3x\\
du&=3\,dx\\
dx&=\frac{1}{3}\,du
\end{aligned}
```

Substituting into the integral,

```math
\begin{aligned}
\int\cos(3x)\,dx
&=\frac{1}{3}\int\cos(u)\,du\\
&=\frac{1}{3}\sin(u)+C\\
&=\boxed{\frac{1}{3}\sin(3x)+C}
\end{aligned}
```

Notice that the derivative of the inner function introduces a factor of 3. Since our original integral does not contain this factor, we compensate by multiplying by its reciprocal, $\frac{1}{3}$.

Remember, $du$ tells us the variable of integration. It is essential while setting up and evaluating the integral, but it is not part of the resulting anti-derivative.

### Example 3 — Missing Derivative Factor

Sometimes the derivative of our chosen substitution is not immediately present in the integral. However, it may still be possible to rearrange the expression to obtain the required factor.

Consider,

```math
\int xe^{x^2}\,dx
```

The inner function of the exponential is $x^2$, so let,

```math
\begin{aligned}
u&=x^2\\
du&=2x\,dx
\end{aligned}
```

We want to isolate $dx$, so rearrange our expression for $du$,

```math
\begin{aligned}
du&=2x\,dx\\
\frac{du}{2x}&=dx
\end{aligned}
```

We can now substitute $u=x^2$ and $dx=\frac{du}{2x}$ directly into our original integral,

```math
\begin{aligned}
\int xe^{x^2}\,dx
&=\int xe^u\left(\frac{du}{2x}\right)\\
&=\frac{1}{2}\int e^u\,du\\
&=\frac{1}{2}e^u+C\\
&=\boxed{\frac{1}{2}e^{x^2}+C}
\end{aligned}
```

Notice that the $x$ terms cancel, leaving an integral entirely in terms of $u$.

The important observation is that we do not need the derivative of the inner function to appear exactly as written. We can rearrange the differential to isolate $dx$, substitute it into the integral, and simplify.

### Example 4 — Logarithmic integration

U-substitution is also useful when the resulting integral contains a reciprocal function, because we can then apply the logarithmic integration rule.

Consider,

```math
\int\frac{x}{x^2+4}\,dx
```

The denominator is our natural choice for the substitution,

```math
\begin{aligned}
u&=x^2+4\\
du&=2x\,dx
\end{aligned}
```

We want to isolate $dx$, so rearrange our expression for $du$,

```math
\begin{aligned}
du&=2x\,dx\\
\frac{du}{2x}&=dx
\end{aligned}
```

We can now substitute $u=x^2+4$ and $dx=\frac{du}{2x}$ directly into our original integral,

```math
\begin{aligned}
\int\frac{x}{x^2+4}\,dx
&=\int\frac{x}{u}\left(\frac{du}{2x}\right)\\
&=\frac{1}{2}\int\frac{1}{u}\,du\\
&=\frac{1}{2}\ln|u|+C\\
&=\frac{1}{2}\ln|x^2+4|+C
\end{aligned}
```

Since $x^2+4$ is always positive, we can simplify the absolute value,

```math
\boxed{
\int\frac{x}{x^2+4}\,dx
=\frac{1}{2}\ln(x^2+4)+C
}
```

Notice that the $x$ terms cancel, leaving an integral entirely in terms of $u$. This allows us to apply the logarithmic integration rule.

### Example 5 — Definite integration

So far, we have used u-substitution to evaluate indefinite integrals. However, the same technique can also be applied to definite integrals. The main difference is that when we change our variable from $x$ to $u$, we must also convert our integration limits.

Consider,

```math
\int_0^1 2x(x^2+1)^3\,dx
```

We begin by identifying the inner function,

```math
\begin{aligned}
u&=x^2+1\\
du&=2x\,dx
\end{aligned}
```

In this case, we can isolate $dx$,

```math
\begin{aligned}
du&=2x\,dx\\
dx&=\frac{du}{2x}
\end{aligned}
```

Before substituting, we must also convert our original integration limits into the new variable.

```math
\int_{x=0}^{x=1}
\quad\xrightarrow{\quad u=x^2+1\quad}\quad
\int_{u=1}^{u=2}
```

When $x=0$,

```math
u=0^2+1=1
```

When $x=1$,

```math
u=1^2+1=2
```

Our new integration limits are therefore $1$ and $2$. We can now substitute $u=x^2+1$ and $dx=\frac{du}{2x}$ into our original integral,

```math
\begin{aligned}
\int_0^1 2x(x^2+1)^3\,dx
&=\int_1^2 2x(u)^3\left(\frac{du}{2x}\right)\\
&=\int_1^2 u^3\,du\\
&=\left[\frac{u^4}{4}\right]_1^2\\
&=\frac{2^4}{4}-\frac{1^4}{4}\\
&=\frac{16-1}{4}\\
&=\boxed{\frac{15}{4}}
\end{aligned}
```

Notice that the $x$ terms cancel, leaving an integral entirely in terms of $u$. We also use the converted limits rather than the original limits, ensuring that the entire integral is expressed consistently using the new variable.

### Example 6 — A more complicated algebraic expression

Finally, consider an integral involving a square root,

```math
\int x^2\sqrt{x^3+1}\,dx
```

Although the expression looks more complicated, we can identify the inner function beneath the square root as our natural choice for substitution,

```math
\begin{aligned}
u&=x^3+1\\
du&=3x^2\,dx
\end{aligned}
```

We want to isolate $dx$, so rearrange our expression for $du$,

```math
\begin{aligned}
du&=3x^2\,dx\\
dx&=\frac{du}{3x^2}
\end{aligned}
```

We can now substitute $u=x^3+1$ and $dx=\frac{du}{3x^2}$ directly into our original integral,

```math
\begin{aligned}
\int x^2\sqrt{x^3+1}\,dx
&=\int x^2\sqrt{u}\left(\frac{du}{3x^2}\right)\\
&=\frac{1}{3}\int u^{1/2}\,du\\
&=\frac{1}{3}\left(\frac{u^{3/2}}{3/2}\right)+C\\
&=\frac{2}{9}u^{3/2}+C
\end{aligned}
```

Notice that the $x^2$ terms cancel, leaving an integral entirely in terms of $u$.

Finally, substitute our original expression back in place of $u$,

```math
\boxed{
\int x^2\sqrt{x^3+1}\,dx
=\frac{2}{9}(x^3+1)^{3/2}+C
}
```
