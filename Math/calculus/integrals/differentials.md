# Understanding Integration and the Meaning of Differential Integration

## Introduction

Expressions such as \(\int dy\), \(\int 2x\,dx\), and \(\int dy=\int 2x\,dx\) can be confusing when first encountered. In particular, it may seem that \(\int dy\) requires us to integrate with respect to \(y\), whereas \(\int 2x\,dx\) requires us to integrate with respect to \(x\). However, when these expressions arise from differentiating a relationship between \(x\) and \(y\), there is an important connection between them.

To understand this connection, we must first understand what integration means, what it means to integrate with respect to a particular variable, and how differentiation and integration relate to one another. We can then introduce differentials and explain why the notation \(\int dy\) can represent the same integration process as \(\int 2x\,dx\) in the appropriate context.

Throughout this explanation, we will use the relationship \(y=x^2\) as an example. The purpose is not simply to memorise a procedure, but to understand why each step is mathematically valid.

## 1. Prerequisite: What does integration mean?

Integration is commonly introduced in two connected ways: as the reverse of differentiation and as a way of accumulating quantities over an interval.

### 1.1 Integration as the reverse of differentiation

Differentiation tells us how a function changes. For example, consider

\[
y=x^2.
\]

Differentiating \(y\) with respect to \(x\) gives

\[
\frac{dy}{dx}=2x.
\]

This tells us the rate at which \(y\) changes as \(x\) changes.

Integration can reverse this process. If we know that the derivative of a function is \(2x\), we can ask which function has that derivative. Since

\[
\frac{d}{dx}(x^2)=2x,
\]

we obtain

\[
\int 2x\,dx=x^2+C.
\]

The symbol \(\int\) represents integration, while \(dx\) specifies that we are integrating with respect to \(x\). The constant \(C\) is included because the derivative of any constant is zero. Consequently, every function of the form \(x^2+C\) has derivative \(2x\).

An indefinite integral therefore represents a family of antiderivatives rather than a single numerical answer.

### 1.2 What does “with respect to \(x\)” mean?

The variable written after the integral sign matters. For example,

\[
\int 2x\,dx=x^2+C
\]

means that we seek a function of \(x\) whose derivative with respect to \(x\) is \(2x\).

By contrast,

\[
\int 2y\,dy=y^2+C
\]

means that we seek a function of \(y\) whose derivative with respect to \(y\) is \(2y\).

These expressions use the same integration operation, but they ask different questions because the variable of integration is different.

This distinction is important when we encounter an expression involving \(dy\). We must not automatically assume that we should switch to integrating with respect to \(y\). Instead, we must consider how the expression arose and what variable the original calculation uses.

### 1.3 Integration as accumulation and area

Integration also provides a way to accumulate quantities over an interval. For a function \(f(x)\), the definite integral

\[
\int_a^b f(x)\,dx
\]

can represent the signed area between the graph of \(f(x)\) and the \(x\)-axis from \(x=a\) to \(x=b\).

The \(dx\) is associated with small changes in the horizontal variable \(x\). Informally, we can imagine dividing the interval into many narrow strips, each with a small width \(\Delta x\). Adding the contributions \(f(x)\Delta x\) and taking the limit as the widths approach zero gives the definite integral.

However, area is only one interpretation of integration. Integration can also represent accumulated distance from velocity, total mass from a density, or total change from a rate of change.

It is also important to distinguish definite and indefinite integrals. A definite integral produces a numerical value when its integrand and limits are specified, whereas an indefinite integral produces a family of antiderivatives. Both are connected by the fundamental theorem of calculus.

## 2. Prerequisite: Understanding \(y\) as a function of \(x\)

Suppose we are given

\[
y=x^2.
\]

This equation tells us that the value of \(y\) depends on the value of \(x\). We can therefore describe \(y\) as a function of \(x\), sometimes written as

\[
y=y(x)
\]

or

\[
y=f(x).
\]

These notations emphasise that \(y\) is not being treated as an unrelated quantity: its value is determined by the input \(x\).

For our example, we could write

\[
y(x)=x^2.
\]

The notation \(y(x)\) is read as “\(y\) as a function of \(x\)”. It does not mean that we multiply \(y\) by \(x\). Similarly, \(f(x)\) means the value returned by the function \(f\) when its input is \(x\).

Because \(y\) depends on \(x\), we can differentiate \(y\) with respect to \(x\):

\[
\frac{dy}{dx}=2x.
\]

The notation \(\frac{dy}{dx}\) describes the derivative of \(y\) with respect to \(x\). In this example, it tells us how quickly \(y\) changes as \(x\) changes.

The fact that \(y\) is a function of \(x\) will be essential when we introduce differentials. It explains why a change in \(y\) can be related to a change in \(x\), and why an expression involving \(dy\) can still be integrated using \(x\).

## 3. Differentiating both sides with respect to \(x\)

Begin with the original relationship:

\[
y=x^2.
\]

Differentiate both sides with respect to \(x\):

\[
\frac{d}{dx}(y)=\frac{d}{dx}(x^2).
\]

Since \(y\) is a function of \(x\), its derivative is \(\frac{dy}{dx}\). The derivative of \(x^2\) is \(2x\). Therefore,

\[
\frac{dy}{dx}=2x.
\]

At this stage, the equation describes the relationship between the rate of change of \(y\) and the value of \(x\).

Suppose we now want to reverse this differentiation and recover \(y\). We must be consistent with the variable used in the differentiation. We differentiated both sides with respect to \(x\), so we initially integrate both sides with respect to \(x\).

Thus,

\[
\int \frac{dy}{dx}\,dx
=
\int 2x\,dx.
\]

This is the clearest starting point for understanding differential integration. Rather than beginning with the shorter expression \(\int dy\), we first write the complete derivative \(\frac{dy}{dx}\) and explicitly show that we are integrating with respect to \(x\).

The right-hand side is straightforward:

\[
\int 2x\,dx=x^2+C_2.
\]

On the left-hand side, we are integrating the derivative of \(y\) with respect to \(x\), using \(x\) as the variable of integration. Integration reverses the differentiation, so

\[
\int \frac{dy}{dx}\,dx=y+C_1.
\]

Therefore,

\[
y+C_1=x^2+C_2.
\]

Rearranging and combining the constants gives

\[
y=x^2+C.
\]

This recovers the original relationship, allowing for an arbitrary constant. If we know the original function was exactly \(y=x^2\), then the constant is zero.

Notice the important point: **we integrated both sides with respect to \(x\)**. We did not change the left-hand side to an integral with respect to \(y\) simply because the numerator of the derivative contains \(dy\). The complete expression \(\frac{dy}{dx}\), together with \(dx\), tells us that the integration is being performed with respect to \(x\).

## 4. What is a differential?

We can now introduce differentials to explain why textbooks often shorten

\[
\int \frac{dy}{dx}\,dx
\]

to

\[
\int dy.
\]

For a differentiable function \(y=f(x)\), the differential \(dy\) is defined by

\[
dy=f'(x)\,dx.
\]

Since \(f'(x)=\frac{dy}{dx}\), we can also write

\[
dy=\frac{dy}{dx}\,dx.
\]

This relationship connects the differential \(dy\) to the derivative \(\frac{dy}{dx}\) and the differential \(dx\).

The differential \(dx\) represents a chosen infinitesimal change in the independent variable in the differential framework. The corresponding differential \(dy\) is the change predicted by the derivative's local linear relationship. In particular,

\[
dy=\frac{dy}{dx}\,dx
\]

says that the differential change in \(y\) is the derivative multiplied by the differential change in \(x\).

For example, if

\[
\frac{dy}{dx}=2x,
\]

then multiplying by \(dx\) gives

\[
dy=2x\,dx.
\]

This equation does not introduce a new function or change the original relationship. It expresses the same derivative relationship using differential notation.

A useful distinction is that \(dy\) is not generally identical to a finite change \(\Delta y\). For a finite change from \(x\) to \(x+\Delta x\), the actual change is

\[
\Delta y=f(x+\Delta x)-f(x).
\]

The differential instead gives the derivative-based linear change

\[
dy=f'(x)\,dx.
\]

For sufficiently small changes, the differential can approximate the actual change, but the two are not generally equal for a nonlinear function.

## 5. Why can \(\int dy\) replace \(\int \frac{dy}{dx}\,dx\)?

Return to the equation

\[
\frac{dy}{dx}=2x.
\]

We established that multiplying both sides by \(dx\) gives

\[
dy=2x\,dx.
\]

Now integrate both sides:

\[
\int dy=\int 2x\,dx.
\]

This is the differential form of the equation we integrated earlier. The notation is shorter because the expression \(dy\) already represents \(\frac{dy}{dx}\,dx\) in this context.

In other words,

\[
\boxed{
\int dy
=
\int \frac{dy}{dx}\,dx
}
\]

when \(y\) is being treated as a differentiable function of \(x\) and the integral is understood along that function.

Consequently,

\[
\int dy=\int 2x\,dx
\]

is a valid shorthand for the integration we performed in the previous section.

The important detail is that we have not abandoned integration with respect to \(x\). The differential \(dy\) has replaced the combined expression \(\frac{dy}{dx}\,dx\). The dependence on \(x\) remains present through the relationship \(y=y(x)\).

This is why it is helpful to introduce differential integration only after writing the longer expression explicitly. If we begin immediately with \(\int dy\), students may reasonably wonder why the left side is being integrated with respect to \(y\) while the right side is being integrated with respect to \(x\). The longer expression makes the original variable of integration visible and removes that ambiguity.

## 6. Multiple interpretations of \(\int dy\)

The notation \(\int dy\) can be understood in related ways, but these interpretations must not be confused.

### 6.1 As shorthand for integrating a derivative with respect to \(x\)

When \(y\) is a function of \(x\), we can interpret

\[
\int dy
\]

as shorthand for

\[
\int \frac{dy}{dx}\,dx.
\]

This is the interpretation relevant to our example. Since

\[
\frac{dy}{dx}=2x,
\]

we obtain

\[
\int dy=\int 2x\,dx.
\]

The left side reverses the differentiation of \(y\), while the right side reverses the differentiation of \(x^2\). Both sides must describe the same relationship, apart from the arbitrary constants introduced by indefinite integration.

### 6.2 As an ordinary antiderivative with respect to \(y\)

There is also a familiar way to evaluate \(\int dy\) by interpreting \(dy\) as \(1\,dy\):

\[
\int dy=\int 1\,dy=y+C.
\]

This is ordinary antiderivative notation with respect to \(y\), because the integrand is the constant function \(1\) and the variable of integration is \(y\).

This calculation is mathematically valid. However, it is not the best first explanation of why

\[
\int dy=\int 2x\,dx
\]

appears when we have differentiated \(y=x^2\) with respect to \(x\).

For that purpose, the more direct explanation is that \(dy\) represents \(\frac{dy}{dx}\,dx\). We can then see that both sides are being integrated in the context of the same relationship between \(x\) and \(y\).

These interpretations are compatible in this setting. The first makes the original variable of integration explicit; the second shows why the antiderivative of \(1\) with respect to \(y\) is \(y\). They should not be treated as unrelated rules or as evidence that the original calculation arbitrarily switches variables.

### 6.3 Using definite integrals to make the relationship explicit

Definite integrals provide another way to understand the relationship between \(dy\) and \(dx\). Suppose \(y=f(x)\), and \(x\) changes from \(a\) to \(b\). Then

\[
\int_a^b \frac{dy}{dx}\,dx
=
y(b)-y(a).
\]

This follows from the fundamental theorem of calculus: integrating the derivative of a function over an interval gives the net change in that function.

Using differential notation, the same relationship can be written as

\[
\int_{y(a)}^{y(b)}dy
=
\int_a^b \frac{dy}{dx}\,dx
=
y(b)-y(a).
\]

The limits on the left describe the starting and ending values of \(y\); the limits on the right describe the corresponding starting and ending values of \(x\). Both integrals express the same net change in \(y\).

For example, let \(y=x^2\), with \(x\) increasing from \(1\) to \(3\). Then

\[
\int_1^3 2x\,dx
=
[\,x^2\,]_1^3
=
9-1
=
8.
\]

The corresponding values of \(y\) are \(1\) and \(9\), so

\[
\int_1^9dy=9-1=8.
\]

The two definite integrals agree because both calculate the change in \(y\) over the same portion of the relationship \(y=x^2\).

This also illustrates why integration should not always be described as finding area. Here, the integral of \(\frac{dy}{dx}\) with respect to \(x\) gives the net change in \(y\). Depending on the integrand and context, a definite integral can represent signed area, net change, or another accumulated quantity.

## 7. Why the variable of integration must remain consistent

The key to interpreting expressions involving differentials is to preserve the relationship between the variables.

Starting with

\[
y=x^2,
\]

we differentiate both sides with respect to \(x\):

\[
\frac{dy}{dx}=2x.
\]

To reverse that differentiation, we integrate both sides with respect to \(x\):

\[
\int\frac{dy}{dx}\,dx=\int2x\,dx.
\]

This gives

\[
y=x^2+C.
\]

Only after establishing this expression should we introduce the differential shorthand:

\[
dy=2x\,dx,
\]

and therefore

\[
\int dy=\int2x\,dx.
\]

The differential notation does not change the variable used in the original differentiation-and-integration process. Rather, it compresses the expression \(\frac{dy}{dx}\,dx\) into \(dy\).

There are circumstances in which it is appropriate to integrate directly with respect to \(y\). For example, if the question is to find an antiderivative of \(2y\) with respect to \(y\), then \(\int 2y\,dy=y^2+C\) is appropriate. But that is a different calculation from reversing \(\frac{dy}{dx}=2x\).

For students learning this notation, the safest approach is to begin with the complete derivative, identify the variable with respect to which differentiation occurred, and explicitly integrate with respect to that same variable. Once that reasoning is clear, the shorter differential notation can be introduced as a convenient equivalent representation.