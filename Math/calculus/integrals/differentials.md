<div align='center'>
<h1>Integration of Differentials</h1>
</div>

Integration is commonly introduced as the inverse operation of differentiation. While differentiation measures the instantaneous rate of change of a function, integration accumulates these changes to recover the original function, up to an arbitrary constant.

When studying integration, it is common to encounter expressions such as,

```math
\int dy = \int 2x\,dx
```

This notation can initially appear confusing because the original differential equation may have been obtained by differentiating both sides with respect to $x$. Consequently, it is reasonable to question why the left-hand side is subsequently described as being integrated with respect to $y$, while the right-hand side is integrated with respect to $x$.

To understand this notation, it is necessary to establish what a differential represents, what it means to integrate with respect to a particular variable, and how differential notation relates to the derivative.

A differential describes an infinitesimal change in a variable. More formally, if $y$ is a differentiable function of $x$, its differential is defined by,

```math
dy = \frac{dy}{dx}\,dx
```

This relationship is fundamental to understanding integration of differentials. It establishes that $dy$ is not an independent quantity when $y$ is a function of $x$, but rather represents the change in $y$ resulting from a change in $x$.

## Integration with Respect to a Variable

Before examining the integration of differentials, it is important to understand what integration with respect to a particular variable means. The integration variable determines the quantity over which we accumulate values. For example, consider the integral,

```math
\int 2x\,dx
```

Here, $x$ is the integration variable, and $dx$ indicates that we are integrating with respect to $x$. We seek a function whose derivative with respect to $x$ is $2x$.

Therefore,

```math
\int 2x\,dx = x^2+C
```

The same principle applies when integrating with respect to another variable. For example,

```math
\int 2y\,dy = y^2+C
```

Here, $y$ is the integration variable, and we seek a function whose derivative with respect to $y$ is $2y$.

The integration variable is identified by the differential appearing at the end of the integral. For example, consider the following expressions,

```math
\int 2x\,dx=x^2+C
```

```math
\int 2y\,dy=y^2+C
```

Both integrals follow the same integration principles, but the variable with respect to which integration occurs determines the resulting antiderivative.

The differential $dx$ identifies $x$ as the integration variable, while $dy$ identifies $y$ as the integration variable. In the context of a definite integral, the differential also forms part of the description of the infinitesimal intervals over which the function is accumulated.

More generally, the relationship between differentiation and integration can be expressed as,

```math
\int \frac{d}{dx}f(x)\,dx = f(x)+C
```

This is a consequence of the fundamental theorem of calculus. It establishes that integrating a derivative with respect to the same variable reverses differentiation, recovering the original function up to an arbitrary constant.

## The Mathematical Meaning of Integrating a Differential

Consider the function,

```math
y=x^2
```

Differentiating both sides with respect to $x$ gives,

```math
\frac{d}{dx}(y)=\frac{d}{dx}(x^2)
```

Therefore,

```math
\frac{dy}{dx}=2x
```

By rearranging this expression, we obtain,

```math
dy=2x\,dx
```

This rearrangement follows directly from the definition of a differential. Since $y$ is a function of $x$, its differential is defined as the derivative of $y$ with respect to $x$, multiplied by the differential of $x$.

Consequently,

```math
dy=\frac{dy}{dx}\,dx
```

This relationship is particularly important when integrating differentials because it allows us to express a differential entirely in terms of the original integration variable.

For example, consider integrating $dy$. Since $y$ is a function of $x$, we can substitute its differential definition,

```math
\int dy = \int \frac{dy}{dx}\,dx
```

This is the formal interpretation of integrating the differential $dy$ when $y$ is dependent on $x$.

Applying the fundamental theorem of calculus,

```math
\int \frac{dy}{dx}\,dx = y+C
```

Therefore,

```math
\int dy = y+C
```

The important observation is that **we have not changed the original integration variable from $x$ to $y$ in order to reverse differentiation**. Instead, we have integrated the derivative of $y$ with respect to $x$, multiplied by $dx$. This distinction becomes particularly important when interpreting the notation used in separation of variables.

## Understanding the Notation of Integrating Both Differentials

Consider the differential equation,

```math
\frac{dy}{dx}=2x
```

We can rearrange the equation to obtain,

```math
dy=2x\,dx
```

A common teaching approach is to express the integration of both sides as,

```math
\int dy=\int 2x\,dx
```

This is frequently explained by saying that the left-hand side is integrated with respect to $y$, while the right-hand side is integrated with respect to $x$. Since the integral of $1$ with respect to $y$ is $y$, the left-hand side becomes $y$, while the right-hand side becomes $x^2$.

The resulting expression is,

```math
y=x^2+C
```

Although this explanation is convenient, **it can obscure the mathematical reasoning behind the notation**. In particular, it can give the impression that we have independently chosen to integrate the left-hand side with respect to $y$, despite **originally differentiating both sides with respect to $x$**. A more precise explanation is obtained by returning to the definition of the differential.

Since $y$ is a function of $x$,

```math
dy=\frac{dy}{dx}\,dx
```

Therefore, the expression,

```math
\int dy
```

**is shorthand for**,

```math
\int \frac{dy}{dx}\,dx
```

Consequently, integrating both sides of the differential equation can be expressed more explicitly as,

```math
\int \frac{dy}{dx}\,dx=\int 2x\,dx
```

Applying the fundamental theorem of calculus gives,

```math
y=x^2+C
```

This demonstrates that the integration on both sides is performed with **respect to $x$**. The notation $\int dy$ condenses the expression $\int \frac{dy}{dx}\,dx$, rather than requiring us to introduce a separate integration process with respect to an independent variable $y$. The notation $\int dy$ is nevertheless mathematically meaningful. It can also be interpreted through the substitution rule for integration.

Consider,

```math
\int dy
```

Since $dy$ represents the differential of $y$, this can be expressed as,

```math
\int 1\,dy
```

The integral of $1$ with respect to $y$ is,

```math
y+C
```

This is consistent with the previous result because the substitution rule allows us to transform between integration variables when the appropriate differential relationship is established. For example, if $y=y(x)$, then,

```math
dy=\frac{dy}{dx}\,dx
```

Therefore,

```math
\int 1\,dy
=
\int 1\cdot\frac{dy}{dx}\,dx
```

Which simplifies to,

```math
\int \frac{dy}{dx}\,dx
```

Both expressions describe the same integration process when the appropriate substitution is valid. Thus, saying that we integrate $1$ with respect to $y$ is a convenient interpretation of the differential notation, rather than an entirely separate operation from integrating the derivative with respect to $x$.

It is important to distinguish between the two interpretations. The expression $\int 1\,dy$ is a legitimate integral with respect to $y$, while the expression $\int \frac{dy}{dx}\,dx$ explicitly demonstrates how that integral relates to the original independent variable $x$.


The integration of differentials becomes considerably easier to understand once the relationship between a differential and its derivative is established. When $y$ is a differentiable function of $x$, its differential is defined as,

```math
dy=\frac{dy}{dx}\,dx
```

Consequently, integrating $dy$ can be understood as integrating the derivative of $y$ with respect to $x$, multiplied by $dx$,

```math
\int dy=\int\frac{dy}{dx}\,dx
```

This explains why integrating a differential recovers the original function, up to an arbitrary constant.

Although it is common to describe $\int dy$ as integrating $1$ with respect to $y$, this explanation alone can conceal the underlying relationship between the dependent and independent variables. In the context of a differential equation, the more explicit interpretation demonstrates that the integration is consistent with the original differentiation.