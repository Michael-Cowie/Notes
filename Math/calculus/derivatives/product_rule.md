<div align='center'>
    <h1> Product Rule — Differentiating Multiplication </h1>
</div>

When two functions are multiplied, differentiation becomes more structured. The product rule states,

```math
\frac{d}{dx}[f(x)g(x)] = f'(x)g(x) + f(x)g'(x)
```

This rule shows that the derivative of a product is not simply the product of the derivatives.

Take $x^2, \cdot x^5$. For each function we can observe

```math
f(x) = x^2 \qquad g(x) = x^5
```

Then,

```math
f'(x) = 2x \qquad g'(x) = 5x^4
```

Now apply the product rule,

```math
\frac{d}{dx}[x^2 \cdot x^5] = (2x)(x^5) + (x^2)(5x^4)
```

Simplifying each term,

```math
\begin{aligned}
&= 2x^6 + 5x^6 \\
&= 7x^6
\end{aligned}
```

This matches the direct simplification approach,

```math
x^2 \cdot x^7 = x^7 \Rightarrow \frac{d}{dx}(x^7) = 7x^6
```

#### Product Rule - Visualized

Often, it is very difficult to visualize the behaviour of 2 functions multiplying, instead it is conceptually more intuitive to instead visualize it geometrically.

Let,

```math
f(x) = \sin(x) \cdot x^2
```

Now, consider $\sin(x)$ as the width and $x^2$ as the height. Therefore $\sin(x) \cdot x^2 = \text{Area}$. Below is a visualization of what is occurring geometrically when introducing $dx$, from here we attempt to calculate the newly added area $df$.

<div align='center'>
    <img src='../images/product_rule_visualized.gif' width='600'>
</div>

As illustrated above where $df$ represents the new area by the introduced $dx$,

<div align='center'>
    <img src='../images/17.png' width='300'>
</div>

```math
df = d(\sin(x)) x^2 + \sin(x) d(x^2) + d(x^2)
```

Because

```math
\lim_{x \to 0} d(x^2) = 0
```

The expression is simplified to

```math
df = d(\sin(x)) x^2 + \sin(x) d(x^2)
```

Now we use the differential identities

```math
\begin{aligned}
d(\sin(x)) &= \cos(x)\,dx = \frac{dy}{dx}\,dx \\
d(x^2) &= 2x\,dx = \frac{dy}{dx}\,dx
\end{aligned}
```

Substituting gives

```math
\begin{aligned}
df &= (\cos(x)\,dx)x^2 + \sin(x)(2x\,dx) \\
df &= \cos(x)\,x^2\,dx + \sin(x)\,2x\,dx \\
f'(x) = \frac{df}{dx} &= \cos(x)\,x^2 + \sin(x)\,2x
\end{aligned}
```

Another visual interpretation of the product rule is directing labelling the derivatives.

<div align='center'>
    <img src='../images/23.png' width='300'>
</div>

Here, we label the derivative $\frac{df}{dx}$ as the width increase $df$ because the input has increased by an amount $dx$, which represents the function output increase $df$.

#### Product Rule - Algebraic Intuition

For a composite function,

```math
y = f(u) \qquad u = g(x)
```

Has the behaviour,

```math
\frac{dy}{dx} = \frac{dy}{du} \frac{du}{dx}
```

This works because there is one path of dependence.

```math
x \to u \to y
```

So there is only one chain of change. Now consider,

```math
y = u(x) v(x)
```

- $y$ depends on $u$
- $y$ depends on $v$
- Both depend on $x$

So the dependency structure is,

```math
x \to u \to y
```

and

```math
x \to v \to y
```

While the following is not considered a formal definition, it does intuitively explain where the addition occurs from the product rule.

We start with,

```math
y = uv
```

Suppose $u$ changes by a small amount $\Delta u$ and $v$ changes by a small amount $\Delta v$. Where,

```math
\Delta u = u(x + \Delta x) - u(x) \\
\Delta v = v(x + \Delta x) - v(x)
```

The old value of $y$ is

```math
uv
```

The new value of $y$ is

```math
(u + \Delta u)(v + \Delta v)
```

Therefore a tiny change $\Delta y$ is the new value minus the old value,

```math
\Delta y = (u + \Delta u)(v + \Delta v) - uv
```

Expanding the brackets

```math
\begin{aligned}
\Delta y
&= uv + u \Delta v + v \Delta u + \Delta u \Delta v - uv \\
&= u \Delta v + v \Delta u + \Delta u \Delta v
\end{aligned}
```

Now divide by $\Delta x$,

```math
\frac{\Delta y}{\Delta x} = u \frac{\Delta v}{\Delta x} + v \frac{\Delta u}{\Delta x} + \frac{\Delta u \Delta v}{\Delta x}
```

Now, take the limit of the **entire expression**.

```math
\lim_{\Delta x \to 0} \frac{\Delta y}{\Delta x} = \lim_{\Delta x \to 0} \left( u \frac{\Delta v}{\Delta x} +  v \frac{\Delta u}{\Delta x} + \frac{\Delta u \Delta v }{\Delta x} \right)
```

##### Term 1

```math
\lim_{\Delta x \to 0} u \frac{\Delta v}{\Delta x}
```

Notice that $u = u(x)$ is evaluated at the original point $x$. Therefore, as $\Delta x \to 0$, $u$ does not change. So it behaves like a contant,

```math
u \lim_{\Delta x \to 0} \frac{\Delta v}{\Delta x}
```

By the definition of the derivative,

```math
\lim_{\Delta x \to 0} \frac{\Delta v}{\Delta x} = v'(x)
```

Therefore,

```math
u \lim_{\Delta x \to 0} \frac{\Delta v}{\Delta x} = u v'(x)
```

Now, it's very important to understand why this term stays. Let's example,

```math
v(x) = x^2
```

Then,

```math
\Delta v = (x + \Delta x)^2 - x^2
```

Which follows by expanding,

```math
\Delta v = 2x \Delta x + (\Delta x)^2
```

This follows,

```math
\lim_{\Delta x \to 0} \Delta v = \lim_{\Delta x \to 0} (2x \Delta x + \Delta x^2) = 0
```

This limit converges to $0$ because because each term contains $\Delta x$. However when we observe,

```math
\lim_{\Delta x \to 0} \frac{\Delta v}{\Delta x}
```

Substitute the same expression.

```math
\begin{aligned}
\lim_{\Delta x \to 0}
\frac{2x\Delta x + \Delta x^2}{\Delta x}
&=
\lim_{\Delta x \to 0}
\left(2x + \Delta x\right) \\
&=
2x
\end{aligned}
```

##### Term 2

```math
\lim_{\Delta x \to 0} v \frac{\Delta u}{\Delta x} = v \lim_{\Delta x \to 0} \frac{\Delta u}{\Delta x} 
```

By definition,

```math
\lim_{\Delta x \to 0} \frac{\Delta u}{\Delta x} = u'(x)
```

Therefore,

```math
\lim_{\Delta x \to 0} v \frac{\Delta u}{\Delta x} = v u'(x)
```

##### Term 3

```math
\lim_{\Delta x \to 0}
```

To explain why this third is kept, we will first rewrite it.

```math
\frac{\Delta u \Delta v}{\Delta x} = \left( \frac{\Delta u}{\Delta x} \right) \Delta v
```

Now we take the limit,

```math
\lim_{\Delta x \to 0} \left( \frac{\Delta u}{\Delta x} \right) \Delta v
```

Because $u$ is differentiable,

```math
\lim_{\Delta x \to 0} \frac{\Delta u}{\Delta x} = u'(x)
```

Now we move towards the $\Delta v$. Since $v$ is differentiable, it is continuous. Therefore,

```math
\Delta v = v(x + \Delta x) - v(x) 
```

As $\Delta x \to 0$, $v \to 0$. Therefore,

```math
\lim_{\Delta x \to 0} \Delta v = 0
```

Putting these together,

```math
\lim_{\Delta x \to 0} \left( \frac{\Delta u}{\Delta x} \cdot \Delta v \right) = u'(x) \cdot 0 = 0
```

Therefore,

```math
\lim_{\Delta x \to 0} \frac{\Delta u \Delta v}{\Delta x} = 0
```


##### Putting everything together

We now have,

```math
\lim_{\Delta x \to 0} \frac{\Delta y}{\Delta x} = uv'(x) + vu'(x) + 0
```

Which finally gives us,

```math
\lim_{\Delta x \to 0} \frac{\Delta y}{\Delta x} = uv'(x) + vu'(x)
```

because

```math
\lim_{\Delta x \to 0} \frac{\Delta y}{\Delta x} = \frac{dy}{dx}
```

We obtain

```math
\frac{dy}{dx} = u \frac{dv}{dx} + v \frac{du}{dx}
```

#### Product Rule - Algebraic Proof

Here, we will prove the product rule algebraically which is a more rigorous proof than the conceptual geometric approach.

```math
\frac{d}{dx}[f(x)g(x)] = f'(x)g(x) + f(x)g'(x)
```

Let,

```math
F(x) = f(x) \cdot g(x)
```

According to the definition,

```math
f'(x) = \lim_{h \to 0} \frac{f(x + h) - f(x)}{h}
```

Therefore,

```math
F'(x) = \lim_{h \to 0} \frac{F(x + h) - F(x)}{h}
```

Which follows,

```math
F'(x) = \lim_{h \to 0} \frac{f(x+h) \cdot g(x+h) - f(x) \cdot g(x)}{h}
```

Now, we're going to subtract and add $f(x + h) \cdot g(x)$ to the numerator. This is a completely valid operation as it is equivalent to adding $0$ on the numerator.

```math
\begin{aligned}
F'(x)
&= \lim_{h \to 0}
\frac{
f(x+h)g(x+h) - f(x)g(x)
\boxed{+\, f(x+h)g(x) - f(x+h)g(x)}
}{h}
\\

&= \lim_{h \to 0}
\frac{
f(x+h)g(x+h)
\boxed{-\, f(x+h)g(x)}
}{h}
+
\lim_{h \to 0}
\frac{
\boxed{f(x+h)g(x)}
- f(x)g(x)
}{h}
\\

&= \lim_{h \to 0}
f(x+h)
\frac{g(x+h)-g(x)}{h}
+
\lim_{h \to 0}
g(x)
\frac{f(x+h)-f(x)}{h}
\end{aligned}
```

Because,

```math
\lim_{h \to 0} f(x + h) = f(x)
```

and multiplying the limit by a constant $g(x)$ can be factored out. It follows,

```math
F'(x) = f(x) \cdot \lim_{h \to 0} \frac{g(x + h) -g(x) }{h} + g(x) \cdot \lim_{h \to 0} \frac{f(x+h) -f(x)}{h}
```

These two terms follow the definition of derivatives. It follows,

```math
F'(x) = f(x) \cdot g'(x) + g(x) \cdot f'(x)
```