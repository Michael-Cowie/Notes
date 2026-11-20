<div align='center'>
    <h1> Functions </h1>
</div>

The concept of a function occupies a central position in modern mathematics. Functions provide a framework for describing relationships between quantities and serve as the foundation of algebra, analysis, calculus and mathematical modelling. Although the notation used to represent functions is compact, it encodes several distinct ideas that are often expressed using the same symbols. A precise distinction between a function, the variables used in its definition, the arguments supplied to it and the quantities produced as output clarifies the structure underlying differentiation and the chain rule.

A function may be regarded as a rule that assigns exactly one output to each valid input. For example,

```math
f(x)=x^2
```

defines a function that maps an input to its square. The symbol $x$ in this expression **does not denote a fixed quantity**. It serves as a formal parameter used to describe the rule. The function itself is the operation "take an input and square it", independent of any particular value.

This is evident from the fact that

```math
f(x)=x^2 \qquad f(z)=z^2 \qquad f(q)=q^2
```

all describe the same function. The symbols $x$, $z$ and $q$ are interchangeable because they serve only as placeholders within the definition. Such symbols are referred to as formal parameters or bound variables. This idea corresponds closely to local variables in programming. A function such as

```python
def square(x):
    return x*x
```

behaves identically to

```python
def square(q):
    return q*q
```

The parameter name exists only within the function definition and carries **no meaning outside it**. It is a structural placeholder rather than a global object.

The situation changes when a function is evaluated. Suppose

```math
p(q)=q^2
```

Here, $q$ is a formal parameter. When we write

```math
p(x)
```

the symbol $x$ is an actual argument supplied to the function. Evaluation consists of substituting the argument $x$ for the parameter $q$, giving

```math
p(x)=x^2
```

Similarly,

```math
p(t+1)=(t+1)^2
```

and

```math
p(\sin r)=\sin^2(r)
```

The distinction is that formal parameters belong to the definition of the function, whereas arguments belong to the context in which the function is applied. An argument does not have to be a fixed number; it may itself be a variable or an expression involving other variables.

In applied settings, function outputs are often assigned their own variable names. For example,

```math
y=f(x)
```

represents a relationship in which $x$ is the independent variable and $y$ is the dependent variable obtained by applying $f$ to $x$. This introduces the variable $y$ to represent the output of the function. It does not change the function's definition.

The derivative of this relationship may be written in several equivalent forms,

```math
\frac{dy}{dx}
\qquad
\frac{d(f(x))}{dx}
\qquad
f'(x)
```

Each notation expresses the derivative of the same relationship. The first emphasises the variables, the second emphasises the function's application and the third emphasises the function itself. The notation used depends on what we want to make explicit.

The distinction between formal parameters and actual arguments becomes particularly important in function composition. Suppose

```math
h=j(x)
\qquad
y=f(h)
```

To clarify the meaning of these expressions, consider a concrete example. Let

```math
j(x)=2x
\qquad
f(u)=u^2
```

and choose a specific value of the independent variable,

```math
x=3
```

Here, $x$ is a single fixed number, not a placeholder.

First compute $h$:

```math
h=j(3)=2\cdot 3=6
```

Then compute $y$:

```math
y=f(6)=36
```

Thus a single input value propagates through the system:

```math
x=3\longrightarrow h=6\longrightarrow y=36
```

This illustrates that $h$ is an intermediate quantity determined by $x$, while $u$ in the definition $f(u)=u^2$ is the formal parameter of the function. The value of $h$ is supplied as the actual argument when the function is evaluated.

In general form, this structure is written as

```math
x\longrightarrow h\longrightarrow y
```

which expresses dependency rather than merely listing variables. Because $h$ depends on $x$ and $y$ depends on $h$, the total rate of change of $y$ with respect to $x$ is given by the chain rule:

```math
\frac{dy}{dx}
=
\frac{dy}{dh}\frac{dh}{dx}
```

This expression reflects the propagation of variation through intermediate variables.

A different situation arises when multiple quantities depend independently on the same variable. Suppose

```math
y=f(x)
\qquad
h=j(x)
```

In this case, both quantities depend directly on $x$, producing the dependency structure

```math
x\longrightarrow y
\qquad
x\longrightarrow h
```

Neither quantity is defined as a function of the other. Consequently, there is no direct chain-rule relationship between $dy/dx$ and $dh/dx$. The shared presence of the symbol $x$ does not imply a compositional relationship.

#### Ambiguity in Function Notation

Consider the previous example:

```math
h=j(x)
\qquad
y=f(h)
\qquad
f(u)=u^2
```

The following expressions establish relationships between **variables**:

```math
h=j(x)
\qquad
y=f(h)
```

The following expression defines a **function**:

```math
f(u)=u^2
```

The $u$ in $f(u)=u^2$ is not an actual variable that must have been previously defined. It is a formal parameter used to describe the function's input. The $h$ in $h=j(x)$, on the other hand, is an intermediate quantity whose value depends on $x$.

The difficulty is that mathematicians often reuse the same letter. For example, if someone writes

```math
h=j(x)
```

and later writes

```math
f(h)=h^2
```

the symbol $h$ is being used in two different roles:

1. As an intermediate variable in the first expression.
2. As a formal parameter in the second expression.

This is legal, but stylistically poor because it obscures the distinction. A clearer presentation would be

```math
h=j(x)
```

and

```math
f(u)=u^2
```

A more careful version is

```math
\begin{aligned}
h&=j(x)\\
f(u)&=u^2\\
y&=f(h)
\end{aligned}
```

Now,

- $u$ is the formal parameter of the function, a placeholder used to describe its input.
- $h$ is an intermediate variable determined by $x$.
- $y$ is the output of the function when evaluated at $h$.

The roles are visually separated.

# Derivative Notation

Derivative notation introduces another distinction, the variable with respect to which a derivative is calculated is not necessarily the same as the formal parameter originally used to define the function. Consider the function

```math
g(u)=u^2
```

The symbol $u$ is a formal parameter. Differentiating the function with respect to its input gives

```math
\frac{dg}{du}=2u
```

This describes how quickly the output of $g$ changes as its input $u$ changes. **The letter used for the input is arbitrary and a placeholder.** We could instead define

```math
g(t)=t^2
```

and obtain

```math
\frac{dg}{dt}=2t
```

These expressions describe the same function and its derivative. The notation changes because the formal parameter has been renamed. The derivative is always taken with respect to the function's input.

However, a different situation arises when the input itself is defined as a function of another variable. Suppose

```math
t=f(x)
```

Now $t$ is no longer merely a formal parameter in the context of the problem. It represents an **actual quantity** whose value depends on $x$. Its derivative is therefore

```math
\frac{dt}{dx}=f'(x)
```

The distinction is important:

```math
\frac{dg}{du}
\qquad\text{and}\qquad
\frac{dt}{dx}
```

describe two different rates of change.

- $dg/du$ describes how the output of $g$ changes with respect to its input.
- $dt/dx$ describes how the intermediate quantity $t$ changes with respect to $x$.

The letter $t$ appears in both relationships because it is the output of the inner function and the actual input supplied to the outer function. **Its role is determined by the relationship being described, not by the letter itself.**

In $g(u)=u^2$, the symbol $u$ is a generic placeholder representing the function's input. Consequently, $dg/du=2u$ is the general derivative of the outer function, expressed in terms of its formal parameter. Once we supply an actual input, such as $t=f(x)$, the derivative must be evaluated at that input.

We do not need to redefine the function $g$ or rename its formal parameter. Instead, we explicitly substitute the actual input into its derivative:

```math
\left.\frac{dg}{du}\right|_{u=t}=2t
```

The expression on the left means that we take the derivative with respect to the formal parameter $u$, then evaluate the resulting derivative at the actual input $t$.

Since

```math
t=f(x)
```

we also have

```math
\frac{dt}{dx}=f'(x)
```

The chain rule combines these two relationships:

```math
\frac{d}{dx}g(f(x))
=
\left.\frac{dg}{du}\right|_{u=t}
\frac{dt}{dx}
```

Substituting the derivatives gives

```math
\frac{d}{dx}g(f(x))
=
2t\cdot f'(x)
```

Since $t=f(x)$, this can also be written as

```math
\boxed{
\frac{d}{dx}g(f(x))
=
2f(x)f'(x)
}
```

This is the derivative of the composite function $g(f(x))$.

The chain rule therefore connects the rate of change of the outer function with respect to its input to the rate of change of that input with respect to the independent variable. The intermediate variable provides the link between the two rates.

It is worth noting that the notation $dg/du$ does not have to be mechanically changed into $dg/dt$ in every derivation. We may retain the original notation and explicitly substitute $u=t$. For example,

```math
\frac{d}{dx}g(f(x))
=
\left.\frac{dg}{du}\right|_{u=t}
\frac{dt}{dx}
```

Both approaches express the same relationship. What matters is that the derivative of the outer function is evaluated at the actual input supplied by the inner function.

When we define

```math
t=f(x)
```

- $x$ is the input.
- $t$ is the output.

Therefore, the derivative is

```math
\frac{dt}{dx}=f'(x)
```

Now consider the outer function, which remains defined as

```math
g(u)=u^2
```

Here,

- $u$ is the formal parameter representing the input.
- $g(u)$ is the output of the function.

Therefore,

```math
\frac{dg}{du}=2u
```

When the actual input is $t$, we evaluate this derivative at $u=t$:

```math
\left.\frac{dg}{du}\right|_{u=t}=2t
```

We have not changed the function. We have simply supplied it with an actual input.

<div align='center'>
    <h1> All Notations </h1>
</div>

### Function Notation

```math
f(u)=u^2
```

Here,

- $f$ is the function's name.
- $u$ is a formal parameter, or placeholder.
- No particular actual argument has been supplied.

This statement defines the rule "Take an input and square it". The symbol $u$ could be renamed without changing anything.

### Function Application with a Dependent Variable

```math
y=f(x)
```

Here,

- $f$ is an already-defined function.
- $x$ is an argument supplied to the function.
- $y$ is the resulting output, represented by a dependent variable.

This statement does not redefine $f$. It uses $f$. A useful way to read it is "Let $y$ be the value obtained by applying $f$ to $x$".

### Function Application and Substitution Combined

```math
y=f(x)=x^2
```

This is shorthand for two statements,

```math
f(u)=u^2
```

and

```math
y=f(x)
```

The second equality comes from substituting $x$ into the definition. More explicitly,

```math
\begin{aligned}
f(u)&=u^2\\
y&=f(x)\\
y&=x^2
\end{aligned}
```

When written as $y=f(x)=x^2$, the notation compresses all of these steps into one line.

### Derivative of a Function

```math
g(u)=u^2
```

```math
\frac{dg}{du}=2u
```

Here,

- $u$ is the formal input parameter of $g$.
- $dg/du$ is the derivative of $g$ with respect to its input.
- $2u$ describes the rate of change of the output as the input changes.

The input parameter could be renamed without changing the function:

```math
\begin{aligned}
g(t)&=t^2\\
\frac{dg}{dt}&=2t
\end{aligned}
```

### Derivative of a Dependent Variable

```math
y=f(x)
```

```math
\frac{dy}{dx}=f'(x)
```

Here,

- $x$ is the independent variable.
- $y$ is the dependent variable.
- $dy/dx$ describes the rate of change of $y$ with respect to $x$.
- $f'(x)$ is another notation for the same derivative.

Unlike the formal parameter in a function definition, $x$ is now part of a specific relationship between dependent and independent variables.

### Chain Rule

Suppose the outer function is defined as

```math
g(u)=u^2
```

and the actual input supplied to it is defined by

```math
t=f(x)
```

Here, $u$ is the formal parameter used to define the outer function, while $t$ is the actual intermediate variable determined by $x$.

The outer function is differentiated with respect to its formal parameter:

```math
\frac{dg}{du}=2u
```

The inner function is differentiated with respect to $x$:

```math
\frac{dt}{dx}=f'(x)
```

The outer derivative is then evaluated at the actual input $t$:

```math
\left.\frac{dg}{du}\right|_{u=t}=2t
```

The chain rule combines the two derivatives:

```math
\frac{d}{dx}g(f(x))
=
\left.\frac{dg}{du}\right|_{u=t}
\frac{dt}{dx}
```

Therefore,

```math
\frac{d}{dx}g(f(x))
=
2t f'(x)
```

Since $t=f(x)$, we obtain

```math
\boxed{
\frac{d}{dx}g(f(x))
=
2f(x)f'(x)
}
```

This illustrates the distinction between the formal parameter used to define a function and the actual variable supplied to it. The derivative of the outer function must be evaluated using the actual input before it is combined with the derivative of the inner function.

The same intermediate variable is often given the same letter as the formal parameter in ordinary calculus notation. For example, we could write $u=f(x)$ instead of $t=f(x)$. This is a convenient shorthand, provided we understand that the letter is serving two related but distinct roles: first as the formal input in the function definition, and then as the actual intermediate quantity in the composition.