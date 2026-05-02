<div align='center'>
    <h1> Logical Connectors "if", "only if" and "if and only if" </h1>
</div>

In mathematics, precise language is essential because the meaning of a statement determines how it should be interpreted and proven. Logical connectors such as `if`, `only if`, and `if and only if` are used to describe relationships between mathematical statements. These phrases are not merely linguistic; they correspond directly to logical implications and define the structure of proofs.

In what follows, the letter $P$ will stand for some proposition and $Q$ for another. Each connective makes a different promise about the relationship between $P$ and $Q$ — and that promise travels in a specific direction.

<div align='center'>
    <h1> Implications </h1>
</div>

One of the most common misconceptions when first encountering logic is the belief that "implies" means "has the same value as". It does not. When we write $P \Rightarrow Q$, we are making a one-directional contract. The contract states **whenever** $P$ **is true,** $Q$ **must also be true**. That is the entire promise. The statement says **nothing whatsoever about what happens when** $P$ **is false**, in that case $Q$ can be true or false and the implication is not violated either way. It places no restriction on $Q$ when $P$ is false, so those cases are always considered true. Implications do not mean they share the same value. It is a one-way relationship, not a symmetric one.

A real world example can assist. Consider the statement "If it is raining, the ground is wet". This feels obviously true, and it is. But notice what it does and does not say. It guarantees that rain produces a wet ground. It does not say anything about what causes a wet ground in general, someone could have used a hose, a pipe could have burst or someone dropped a bucket of water. The ground being wet does not imply it is raining. But rain does imply a wet ground. The relationship is one direction only.

| Raining ($P$) | Ground wet ($Q$) | Raining $\Rightarrow$ Ground wet |
|:---:|:---:|:---:|
| T | T | T |
| T | F | **F** |
| F | T | T |
| F | F | T |

The only row that breaks the implication is the second one, where it is raining and the ground is somehow not wet. That is the broken promise. The third row, where the ground is wet but it is not raining, is perfectly fine. The implication was never violated because rain never occurred.

<div align='center'>
    <h1> Necessary and Sufficient </h1>
</div>

#### Necessary Condition

When we say $Q$ is **necessary** for $P$, this directly translates to 

```math
P \Rightarrow Q
```

This is a requirement statement.

It asserts whenever $P$ is true, $Q$ must also be true. That is the entire constraint. The statement does not claim that $Q$ causes or guarantees $P$, only that $P$ cannot occur without it.

Equivalently,

- If $Q$ is false, then $P$ must be false.
- $P$ is impossible without $Q$

The statement places a restriction on $P$, not on $Q$

#### Sufficient Condition

When we say $Q$ is **sufficient** for $P$, this directly translates to 

```math
Q \Rightarrow P
```

This is a guarantee statement. It asserts that whenever $Q$ is true, $P$ must also be true. That is the entire promise. The statement does not say that $Q$ is required for $P$, only that it is enough to ensure it.

Equivalently,

- If $Q$ is true, then $P$ must be true.
- $Q$ guarantees $P$.

The statement places a restriction on $Q$, not on $P$.

#### Necessary vs Sufficient

- A **necessary** condition is something that $P$ depends on.
- A **sufficient** condition is something that forces $P$.

These are opposite directions of implication

```math
\text{Necessary}:  P \Rightarrow Q \\
\text{Sufficient}:  Q \Rightarrow P
```

Therefore, when we say $Q$ is necessary **and** sufficient for $P$ it directly translates to $P \Leftrightarrow Q$. This combines both directions 

```math
P \Rightarrow Q \space \text{and} \space Q \Rightarrow P
```

This is no longer a one-way relationship. It is a two-way constraint.

<div align='center'>
    <h1> "if" - The Forward Implication </h1>
</div>

The phrase `if` introduces a sufficient condition. A statement of the form,

```math
P \space \text{if} \space Q
```

means that,

```math
Q \Rightarrow P
```

This indicates whenever $Q$ is true, $P$ must also be true. This is written formally as $Q \Rightarrow P$ which is read as "Q implies P". The implication flows from $Q$ to $P$.

The `if` direction is a one-way street. The implication runs in one direction only. When the hypothesis holds, the conclusion is guaranteed, but the conclusion holding says nothing about whether the hypothesis holds. Sufficiency is not reversible. $Q$ being true forces $P$ to be true, but $P$ being true places no constraint whatsoever on $Q$.

This is also called a *sufficient condition*, $Q$ is sufficient for $P$. Knowing $Q$ is all you need to conclude $P$. However, $P$ might be true even without $Q$, other routes to $P$ may exist.

| $Q$ | $P$ | $Q \Rightarrow P$ ($P$ if $Q$) |
|:---:|:---:|:---:|
| T | T | T |
| T | F | **F** |
| F | T | T |
| F | F | T |

The only way this implication fails is when $Q$ is true but $P$ is false. All other combinations are considered genuinely true. However, a truth table lists all possible combinations, whether they're practically possible or forbidden.

Suppose we have an example, "The ground is wet **if** it is raining". Let $Q$ = "It is raining" and $P$ = The ground is wet". This means, $Q$ is sufficient for $P$. Whenever $Q$ is true, $P$ must also be true. Here, $Q \Rightarrow P$.

| $Q$ (Raining) | $P$ (Ground wet) | $Q \Rightarrow P$ |
|:---:|:---:|:---:|
| T | T | T — Raining and ground is wet. Expected. |
| T | F | **F** — Raining but ground is not wet. Impossible. |
| F | T | T — Not raining but ground is wet. Someone spilled a bucket of water. Fine. |
| F | F | T — Not raining and ground is dry. Fine. |

The ground being wet from a bucket does not break this, the implication only promised what happens **when $Q$ is true**. It says nothing about what else might make $P$ true.

<div align='center'>
    <h1> "Only if" - The Reverse Implication </h1>
</div>

The phrase `only if` introduces a necessary condition. A statement of the form,

```math
P \space \text{only if} \space Q
```

means that,

```math
P \Rightarrow Q
```

This indicates that $Q$ must be true whenever $P$ is true. In other words, $P$ cannot occur without $Q$. This time the arrow flows *from* $P$ *toward* $Q$. $Q$ is now a *necessary condition* for $P$. Without $Q$, $P$ is impossible. But $Q$ alone is not enough to guarantee $P$, it is merely required.

`Only if` sets the minimum requirement. It eliminates cases where $P$ holds without $Q$, but it does not promise that satisfying $Q$ is enough.

$P \Rightarrow Q$ tells you the following,

1. $Q$ is necessary for $P$
2. $P$ implies $Q$
3. $Q$ being true does not force $P$ to be true. 

| $P$ | $Q$ | $P \Rightarrow Q$ ($P$ only if $Q$) |
|:---:|:---:|:---:|
| T | T | T |
| T | F | **F** |
| F | T | T |
| F | F | T |

Previously, we had the example "The ground is wet if it is raining". Now, we will demonstrate that occurrs if we rephrase it to "The ground is wet **only if** it is raining".

Let $P$ = "The ground is wet" and $Q$ = "It is raining".

This means, $Q$ is necessary for $P$. $P$ cannot be true unless $Q$ is also true.

| $P$ (Ground wet) | $Q$ (Raining) | $P \Rightarrow Q$ |
|:---:|:---:|:---:|
| T | T | T — Ground is wet and it is raining. Fine. |
| T | F | **F** — Ground is wet but it is not raining. This breaks it as it can occurr in reality. |
| F | T | T — It is raining but ground is not wet. Fine. |
| F | F | T — Ground is dry and it is not raining. Fine. |

This is **false** because $P$ can be true while $Q$ is false, such as someone spilling a bucket of water. The ground is wet, but it is not raining. That lands us directly in row 2, and one counterexample is enough to break the implication. This is to illustrate that having "only if" in replacement of "if" redirects the implication and can make a once truthful statement, untruthful.

So, instead we will illustrate "only if" with a different statement. Let the statement be "It is raining **only if** there are clouds".

Let $P$ = "It is raining" and $Q$ = "There are clouds".

This means, $Q$ is necessary for $P$. It cannot be raining unless clouds are present.

| $P$ (Raining) | $Q$ (Clouds) | $P \Rightarrow Q$ |
|:---:|:---:|:---:|
| T | T | T — Raining and there are clouds. Expected. |
| T | F | **F** — Raining but no clouds. Impossible in reality, so not an acceptable cause of failure. |
| F | T | T — No rain but there are clouds. A dry overcast day. Fine. |
| F | F | T — No rain and no clouds. A clear sunny day. Fine. |

This is **true** because there is no scenario in reality where $P$ is true and $Q$ is false, it cannot rain without clouds. A dry overcast day lands in row 3, where $P$ is false, so the implication is never tested and never broken.

The truth table is not a description of reality, it is a checklist of all possible combinations of true and false. The implication $P \Rightarrow Q$ is only broken when you can find a real, possible scenario where $P$ is true and $Q$ is false.

- For "The ground is wet **only if** it is raining", row 2 is reachable in reality. A bucket of water makes $P$ true and $Q$ false. The implication is broken.

- For "It is raining **only if** there are clouds", row 2 is not reachable in reality. There is no scenario where it rains without clouds. So the implication is never violated and holds as true.

<div align='center'>
    <h1> "If and only if" - The biconditional </h1>
</div>

The statement $P$ if **and** only if $Q$, often abbreviated `iff` or written $P \Leftrightarrow Q$ is the conjunction of both implications. It asserts simultaneously that $Q \Rightarrow P$ (the `if`) and that $P \Rightarrow Q$ (the `only if`). **Both arrows must hold.**

This makes $Q$ both necessary and sufficient for $P$. The two propositions rise and fall together. **Whenever one is true, the other is true**. Whenever one is false, the other is false.

| $P$ | $Q$ | $P \Leftrightarrow Q$ |
|:---:|:---:|:---:|
| T | T | T |
| T | F | **F** |
| F | T | **F** |
| F | F | T |

An `iff` statement fails the moment the two propositions disagree. To *prove* a biconditional, you must prove both halves independently, first the forward direction, then the backward direction.

<div align='center'>
    <h1> Examples </h1>
</div>

### Example 1 - A nightclub door policy

**The statement -** "You can enter the club **only if** you have ID."

Let,

```math
\begin{aligned}
P &\text{ = "You are inside the club"} \\
Q &\text{ = "You have ID"}
\end{aligned}
```

The claim asserts $P \Rightarrow Q$.

**Only if** $(P \Rightarrow Q)$: ✓ *True.*
Having ID is a **necessary condition for entry**. If you are inside the club, you must have produced ID. No counterexample exists.

**If** $(Q \Rightarrow P)$: ✗ *False.*
Having ID **does not guarantee entry**. The bouncer may still refuse you, wrong dress code, overcapacity, or other conditions. $Q \Rightarrow P$ does not hold.

**If and only if** $(P \Leftrightarrow Q)$: ✗ *False.*
Because the `if` direction fails, the biconditional fails. ID is necessary but not sufficient.

The `only if` direction lets you deduce *backward*. Seeing someone inside, you know they have ID. But you cannot deduce *forward*. Knowing someone has ID, you cannot guarantee they're inside.

### Example 2 - Multiples of 4 and 2

**The statement -** "A number is a multiple of 4 **if and only if** it is a multiple of 2."

Let,

```math
\begin{aligned}
P &= \text{"n is a multiple of 4"} \\
Q &= \text{"n is a multiple of 2"}
\end{aligned}
```

The claim asserts $P \Leftrightarrow Q$. We need both $Q \Rightarrow P$ and $P \Rightarrow Q$ to hold.

**Only if** $(P \Rightarrow Q)$: ✓ *True.*
Every multiple of 4 is automatically a multiple of 2, because $4 = 2 \times 2$. If $n = 4k$ for some integer $k$, then $n = 2(2k)$, which is divisible by 2. No counterexample exists.

**If** $(Q \Rightarrow P)$: ✗ *False.*
Consider $n = 6$. It is a multiple of 2, but not a multiple of 4. So $n$ is a multiple of 4 **if** it is a multiple of 2 fails. One counterexample is all it takes.

**If and only if** $(P \Leftrightarrow Q)$: ✗ *False.*
Since the `if` direction fails, the biconditional fails. Being a multiple of 2 is necessary but not sufficient for being a multiple of 4.

### Example 3 - Even integers

**The statement -** $n^2$ is even if **and** only if $n$ is even.

Let,

```math
\begin{aligned}
P &= "n^2 \ \text{is even"} \\
Q &= \text{"$n$ is even"}
\end{aligned}
```

The claim asserts $P \Leftrightarrow Q$.

**If** $(Q \Rightarrow P)$: ✓ *True.*
If $n$ is even, write $n = 2k$. Then

```math
n^2 = (2k)^2 = 4k^2
```

which is even. ✓

**Only if** $(P \Rightarrow Q)$: ✓ *True.*
Proved by contrapositive. If $n$ is *odd*, write $n = 2k + 1$. Then

```math
n^2 = (2k+1)^2 = 4k^2 + 4k + 1
```

which is odd. So if $n$ is not even, $n^2$ is not even. The contrapositive of $P \Rightarrow Q$ is equivalent to it. ✓

**If and only if** $(P \Leftrightarrow Q)$: ✓ *True.*
Both directions hold. "Even" for $n$ and "even" for $n^2$ are equivalent conditions, one never occurs without the other.

This is the template for a correct biconditional proof. Prove each direction separately and explicitly. The structure of the write-up mirrors the structure of the claim forward, then backward.
