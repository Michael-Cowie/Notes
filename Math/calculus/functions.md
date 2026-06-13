<div align='center'>
    <h1> Functions </h1>
</div>

The concept of a function occupies a central position in modern mathematics. Functions provide a framework for describing relationships between quantities and serve as the foundation of algebra, analysis, calculus and mathematical modelling. Although the notation is used to represent functions is compact, it encodes several distinct ideas that are often expressed using the same symbols. A precise distinction between a function, the variables used in its definition, the arguments supplied to it and the quantities produced as output clarifies the structure underlying differentiation and the chain rule.

A function may be regarded as a rule that assigns exactly one output for its given inputs. For example,

```math
f(x) = x^2
```

defines a function that maps an input to its square. The symbol $x$ in this expression **does not denote a fixed quantity**. It serves as a formal parameter used to describe the rule. The function itself is the operation "take an input and square it", independent of any particular value.

This is evident from the fact that

```math
f(x) = x^2 \qquad f(z) = z^2 \qquad f(q) = q^2
```

all describe the same function. The symbols $x$, $z$ and $q$ are interchangeable because they serve only as placeholders within the definition. Such symbols are referred to as formal parameters or bound variables. This idea corresponds closely to local variables in programming. A function such as,

```python
def square(x):
    return x*x
```

behaves identically to

```python
def square(q):
    return q*q
```

The parameter name exists only within the function definition and carries **no meaning outside it**. It is a structural placeholder rather than a global object. The situation changes when a function is evaluated. Suppose

```math
p(q) = q^2
```

Here $q$ is a formal parameter. When we write

```math
p(x)
```

the symbol $x$ is no longer a placeholder from the definition. It is an actual input supplied to the function. Evaluation consists of substituting the argument $x$ for the parameter $q$, giving

```math
p(x) = x^2
```

Similarly,

```math
p(t + 1) = (t + 1)^2 \qquad p(\sin r) = \sin^2(r)
```

The distinction is that formal parameters belong to the definition of the function, whereas arguments belong to the context in which the function is applied. In applied settings, function outputs are often assigned their own variable names. For example,

```math
y = f(x)
```

represents a relationship in which $x$ is the independent variable and $y$ is the dependent variable obtained by applying $f$ to $x$. This does not define a new function, it evaluates an existing one and assigns the result to a quantity $y$.

The derivative of this relationship may be written in several equivalent forms,

```math
\frac{dy}{dx} \qquad \frac{d(f(x))}{dx} \qquad f'(x)
```

Each notation expresses the same quantity. The first emphasises variables, the second emphasises structure and the third emphasises the function itself. The distinction between formal parameters and actual arguments becomes essential in function composition. Suppose

```math
h = j(x) \qquad y = f(h)
```

To clarify the meaning of these expressions, consider a concrete example. Let,

```math
j(x) = 2x \qquad f(h) = h^2
```

and choose a specific value of the independent variable,

```math
x = 3
```

Here $x$ is a single fixed number, not a placeholder.

First compute $h$,

```math
h = j(3) = 2 \cdot 3 = 6
```

Then compute $y$

```math
y = f(6) = 36
```

Thus a single input value propagates through the system.

```math
x = 3 \to h = 6 \to y = 36
```

This illustrates that $h$ is not a symbolic placeholder inside the definition $f$, but an intermediate quantity determined by $x$, and that $x$ itself is a concrete value once an evaluation is performed. In general form, this structure is written as

```math
x \to h \to y
```

which expresses dependency rather than symbolic substitution. Because $h$ depends on $x$ and $y$ depends on $h$, the total rate of change of $y$ with respect to $x$ is given by the chain rule,

```math
\frac{dy}{dx} = \frac{dy}{dh} \frac{dh}{dx}
```

This expression reflects the propagation of variation through intermediate variables. A different situation arises when multiple quantities depend independently on the same variable. Suppose,

```math
y = f(x) \qquad h = j(x)
```

In this case both quantities  depend directly on $x$, producing the dependency structure

```math
x \to y \qquad x \to h
```

Neither quantity depends on the other, and therefore no chain-rule relationship exists between $\frac{dy}{dx}$ and $\frac{dh}{dx}$. The shared presence of the symbol $x$ does not imply any compositional relationship.

#### Ambiguity in Function Notation

Consider the previous example which includes,

```math
h = j(x) \qquad y = f(h) \qquad f(h) = h^2
```

The following **defines variables**.

```math
h = j(x) \qquad y = f(h)
```

The following **defines functions**.

```math
f(h) = h^2
```

The $h$ inside of $f(h) = h^2$ has no assoication to the other $h$ previously defined as a variable. If both were complete in a single assignment

```math
g = j(y) = y^2
```

then $g$ is a variable at the exact point $y$.  Here, $y$ is not an input placeholder, it must has been previously defined as a variable and a quantity as it determines the value of $g$.

The difficulty is that mathematicians often reuse the same letter. For example, if someone writes

```math
h = j(x)
```

and later writes

```math
f(h) = h^2
```

the symbol $h$ is being used in two completely different roles.

1. As a variable in the first equation.
2. As a formal parameter in the second equation.

This is legal, but stylistically poor because it obscures the distinction. A clearer presentation would be

```math
h = j(x)
```

and

```math
f(u) = u^2
```

Now there is no ambiguity. A more careful version is,

```math
\begin{aligned}
h &= j(x) \\
f(u) &= u^2 \\
y &= f(h)
\end{aligned}
```

Now,

- $u$ is the formal parameter of the function.
- $h$ is an actual variable in the problem.
- $y$ is the output.

The roles are visually separated.

<div align='center'>
    <h1> All Notations </h1>
</div>

### Function Notation

```math
f(u) = u^2
```

Here,

- $f$ is the functions name.
- $u$ is a formal parameter, a dummy variable.
- No actual value has been supplied.

This statement defines the rule "Take an input and square it". The symbol $u$ could be renamed without changing anything.

#### Function Application with a Dependent Variable

```math
y = f(x)
```

Here,

- $f$ is an already-defined function.
- $x$ is an actual argument being supplied to the function.
- $y$ is the resulting output.

This statement does **not** define $f$. It uses $f$. A useful ways to read it is "Let $y$ be the value obtained by applying $f$ to $x$".

#### Function Application and Substitution Combined

```math
y = f(x) = x^2
```

This is really a shorthand for two statements.

```math
f(u) = u^2
```

and

```math
h = f(x)
```

The second equality comes from substituting $x$ into the definition. More explicitly

```math
\begin{aligned}
f(u) &= u^2 \\
y &= f(x) \\
y &= x^2
\end{aligned}
```

When written as

```math
y = f(x) = x^2
```

the notation compresses all of these steps into one line.