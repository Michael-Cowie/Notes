<div align='center'>
    <h1> Introduction of Units </h1>
</div>

A unit, in mathematical and scientific contexts is a standardized quantity used as a refernce for measuring a particular physical or abstract property. It assigns meaning to a numerical value by **specifying the dimension it represents**. For instance, the number "6" alone is dimensionless and ambiguous, however, when paired with a unit such as \( 6 \ \frac{\mathrm{km}}{\mathrm{h}} \), it becomes velocity, indicating a rate of change in position over time. Formally, units are part of dimensional analysis, a branch of mathematics that **ensures consistency in equations** by tracking dimensions associated with quantites. A unit is a constraint on how a numerical value participates in equations. Units are algebraic labels that enforce correct combination of quantities. **Only equations give physical meaning, units alone never do**. Units must be fixed and cannot contain numerical information.

A quantity is defined as an ordered pair consisting of a scalar and a unit. Equivalently, it may be written as the product.

\[
Q = xu
\]

Where,

- \( x ∈ \mathbb{R} \) is a numerical magnitude.
- \( u \) is a unit representing a reference standard.

The unit \( 𝑢 \) specifies the dimension of the quantity and provides semantic meaning to the scalar \( 𝑥 \). Without \( 𝑢 \), the numerical value \( 𝑥 \) alone is dimensionally indeterminate. The expression \( xu \) is interpreted as "\(x \) times the reference quantiy defined by \( u \)"

A unit defines **the dimension** of a quantity, and the **scalar multiplies** that unit to determine its magnitude. Consider the example \( 6 \frac{\mathrm{km}}{\mathrm{h}} \), "km" denotes kilometres and "h" denotes hours. The "/" symbol indicates divison, hence \( 6 \ \frac{\mathrm{km}}{\mathrm{h}} \) is read as "kilometres per hour". Meaning, the distance travelled in kilometres divided by the time elapsed in hours. This interpretation allows us to understand the quantity as a rate, for every hour, 6 kilometres are covered.

- **Length** - \( 5m \) (metres), read as "five metres". Here, the unit "m" specifies linear extent.
- **Area** - \( 4m^2 \) (square metres), read as "four square metres", indicating length squared.
- **Volume** - \( 3m^3 \) (cubic metres), read as "three cubic metres", from length cubed.
- **Density** - \( 2 \ \frac{\mathrm{kg}}{\mathrm{m^3}} \), read as "two kilogrames per cubic metre", a mass per unit volume.

<div align='center'>
<h1> Meaning and Creation </h1>

</div>

A unit derives its meaning from its ability to quantify measurable quantities in a consistent and reproducible manner. Units are created through standardization bodies like the International System of Units (SI), which defines seven base units.

1. **Meter (m)** - For length, is defined from the speed of light
2. **Kilogram (kg)** - For mass.
3. **Second (s)** - For time, it is defined by a specific atomic transition.
4. **Ampere (A)** - For electric current.
5. **Kelvin (K)** - For temperature.
6. **Mole (mol)** - For amount of substance.
7. **Candela (cd)** - For luminous intensity.

Derived units are formed by algebraic combinations of these base units via multiplication, division or exponentiation.

For example,

- **Velocity \( \frac{\mathrm{m}}{\mathrm{s}} \)** = \( \frac{\mathrm{Length}}{\mathrm{Time}} \), created by dividing length by time.

- **Acceleration \( \frac{\mathrm{m}}{\mathrm{s^2}} \)** = \( \frac{\mathrm{Length}}{\mathrm{Time^2}} \), from velocity divided by time.

- **Force (Newton) \( \frac{\mathrm{kg \ \cdot \ m }}{\mathrm{s^2}} \)**, from mass times acceleration.

Base units like "metre" are not ratios, they are fundamental references. However, many derived units, especially rates are ratios, such as speed \( \frac{\mathrm{distance}}{\mathrm{time}} \). Even non-ratio units can be expressed dimensionally, for instance energy (joule) is \( \frac{\mathrm{kg \ \cdot \ m^2 }}{\mathrm{s^2}} \), which is not purely a ratio but a product of ratios. Units can also be dimensionless, such as angles (\( \mathrm{rad} \)) or ratios like efficiency, e.g. 0.8 meaning 80%.

Creation of a unit involves,

1. **Selection of base units** - Choose appropriate standards, e.g. SI vs Imperial.
2. **Algebraic operations** - Multiply for products (e.g. \( Area = Length \cdot Length \)), divide for rates (e.g. \( density = \frac{mass}{volume} \)) or raise to powers (e.g. \( pressure = \frac{force}{area} = \frac{N}{m^2} \))
3. **Prefixes for scaling** - Use SI prefixes like kilo (\( 10^{3} \)) to adjust magnitude without changing the dimension.

In practice, units ensure that each term in an equation is consistent, compatible and in the same dimension. For example, in the kinematics equation \( v = u + at\), all terms must have units of velocity for the equation to hold.

A term in this context is any individual piece of an equation seperated by a plus or minus sign. Key points about terms i,

- **Simple or compound** - A term can be a single variable (e.g. \( u\)) or a combination of variables (e.g. \( at \))

- **Independent contribution** - Each term contributes independently to the total value of the expression.

- **Unit consistency** - Terms that are added or subtracted must have the same units, otherwise the equation is physically meaningless.

In the equation \( v = u + at \)

- \( u \) has the unit of velocity, \( \frac{m}{s} \)
- \( at \) has the unit of velocity \( \frac{m}{s} \) because \( a \ (\frac{m}{s^2}) \cdot t \ (s) = \frac{m}{s} \)

Therefore, the equation is valid and the plus and minus of each term can occur because all terms share compatible units.

#### Units as Operational Constraints, Not Representations

In Physics and mathematics, a **unit does not describe what a quantity looks like** and does not encode a physical mechanism. Instead, a unit functions as an **operational constraint**. It specifies how a numerical value is permitted to participate in equations, comparisons and algebraic operations.

Formally, a physical quantity consists of a numeric value together with a unit. The unit acts as a **comparison standard**, defining what "1" means for that kind of measurement and determining which quantities may be meaningfully added, subtracted, multiplied or divided. For example, lengths may be added to lengths, but not to times. Forces may be multiplied by distances, but not added to them. In this sense, units play a role analogous to types in a programming language, they prevent invalid operations and enforce structural consistency.

#### Division vs Multiplication of Units

When units are divided, the result is a **rate**. A unit such as \(\frac{m}{s}\) **answers a "per" question**. How much length corresponds to one unit of time. Rate units are often intuitive because they align with everyday experience and sequential reasoning.

Multiplication of units, by contrast does not produce a rate and does not imply spatial extension, motion or geometry. A product such as \( N \cdot m \) signifies joint dependence. The resulting quantity depends linearly on both contributing quantities simultaneously. This dependence is purely algebraic. If either factor is scaled, the resulting quantity scales proportionally. If both are scaled, the effect compounds. No additional interpretation is implied by the multiplication itself.

#### Why Compound Units Resist Visualization

Certain compound units, mostly notably area (\(m^2\)), has a geometric visualization. This is a special case arising from the structure of physical space, not a general feature of unit multiplication. Most compound units such as \(N \cdot m\), \( \frac{kg \cdot m}{s}\), or \( J \cdot s\) **do not correspond to shapes, regions or spatial distributions**. Attempting to visualize them leads to confusion because such units **were never intended** to represent physical objects or configurations.

Questions such as "Where is the meter" or "What shape does \(N \cdot m\) make" are therefore category errors. They assume that a unit must encode spatial or mechanical structure, when it infacts **it encodes algebraic compatibility**.

#### Meaning Comes from Equations, Not Units

**A unit itself carries no physical meaning** beyond its algebraic role. The same unit may appear in distinct physical contexts with different interpretations. For example, \( N \cdot m\) appears in both work and torque, yet these quantites differ fundamentally in behaviour and interpretation. The distinction arises from the **equations in which the unit appears, not from the unit itself**.

Therefore, physical meaning is assigned by equations and laws, while units serve to ensure that those equations are internally consistent and dimensionally valid. Units enforce how quantities combine, equations determine what those combinations represent.

Units should be understood as **algebraic labels that constrain numeric values**, not as representations of physical objects, motions or geometries. Multiplying units create a new label that records simultaneous dependence on multiple base quantities. Visualization is optional and often unavailable, area is an exception rather than a model.

**Units enforce consistency, equations assign meaning**. Once this distinction is accepted, compound units such as \(N \cdot m\) cease to be mysterious and instead become predictable elements of a coherent algebraic system.

<div align='center'>
    <h1> Different Types of Units </h1>
</div>

#### Base Units

These are the fundamental, irreducible units defined independently. As mentioned, SI base units include m, kg, s, etc. They are not derived from others and serve as building blocks. Interpretation is straightforward, "1kg" is read as "one kilogram", representing mass without ratios.

#### Derived Units

A derived unit,

- Is a product of base units.
- Is treated **as a single compound unit**.
- Scales exactly like any other unit.

So,

\[
c \left(\frac{m}{s} \right) = c \cdot m \cdot s^{-1}
\]

Is just a scalar multiplication of a symbolic unit expression. A derived unit like \(\frac{m}{s}\) **is not a number fraction**, it is a compound unit \(ms^{-1}\) and multiplying by a scalar scales the entire compound unit exactly the same way as multiplying \( 6 \cdot m\) scales metres.

A derived unit is just algebra on base units. For example,

\[
\frac{m}{s} = m \cdot s^{-1}
\]

That's it. It is **not a numerical fraction**. It is a product of unit symbols with exponents.

\[
1\frac{m}{s} = 1 \cdot m \cdot s^{-1}
\]

Where, the "1" is the scalar. The unit part is \(m \cdot s^{-1}\). The "per 1 second" is not something being divided numerically, it is built into the unit definition.

Take,

\[
\frac{6}{5} \frac{m}{s}
\]

This means,

\[
\frac{6}{5} \cdot m \cdot s^{-1}
\]

That is the complete structure. There is,

- One scalar, \( \frac{6}{5} \)
- One unit expression, \( ms^{-1} \)

Nothing inside the unit is independently scaled.

If you rewrite,

\[
\frac{6}{5} \cdot m \cdot s^{-1}
\]

as a fraction, you get

\[
\frac{6m}{5s}
\]

Now it looks like 6 went to metres and 5 went to seconds, but that is just algebraic rearrangement. This did not scale metres and not seconds, **the entire unit expression was scaled** and then rewrote it. Units behave like algebraic symbols. Just like,

\[
\frac{6}{5}xy^{-1}
\]

The scalar multiplies the whole product. You're never scaling the numerator and denominator separately.

Units are **always defined relative to 1 of that unit**.

So when we say,

\[
1.2\frac{m}{s}
\]

We mean, 1.2 × (1 metre per 1 second). We always normalize back to "per 1 second" because that is the unit definition. That does not mean the denominator stayed unchanged during multiplication. It means we express the final value relative to the standard unit.

Even though,

\[
\frac{6}{5} \frac{m}{s} = \frac{6m}{5s}
\]

both are mathematically the same, **we always express it relative to the standard unit**, which is "per 1 second" in \( \frac{m}{s} \).

So,

\[
\frac{6m}{5s} = \frac{6}{5} \frac{m}{s} = 1.2 \frac{m}{s}
\]

#### Scaling Units - Dimensionless and Prefixed

Scaling refers to units that adjust magnitude without altering dimension. There are five common scaling units.

- **Prefixes** - These are multiplicative factors, e.g. micro (\( μ = 10^{-6} \)) in \(μm\) (micrometre). Reading "\( 5 μm\)" as "five micromtres", equivalent to \( 5 × 10^{-6} m \)
  - Kilo (k) - Multiplies the base unit by \( 10^{3} \), as in kilometre (1000 metres) or kilogram (1000 grams).
  - Mega (M) - Multiplies the base unit by \( 10^{6} \)
  - Giga (G) - Multiplies the base unit by \( 10^{9} \)
  - Milli (m) - Divides the base unit by 1000 or multiplying by \( 10^{-3} \)
  - Micro (μ) - Divides the base unit by 1,000,000 or multiplying by \( 10^{-6} \)

- **Dimensionless units** - These have no physical dimension, often arising from ratios of like quantites. These quantities have no physical dimension and arise from ratios of the same type of quantity, so the units cancel out. They act purely as scaling factors, changing only magnitude. If an objects mass changes from 5kg to 10kg, the ratio is \( \frac{10}{5} = 2\), which is unitless. This means the mass has doubled, often read as "twice as large".

Versus other types, scaling units differ from dimensional units in that they do not introduce new dimensions, they merely resize. In contrast, derived units like \( \frac{km}{h}\) introduce a rate dimension.

#### Specialized Units

In fields like thermodynamics (e.g. entrophy \( \frac{J}{K} \)) or electromagnetism (e.g. \( Tesla = \frac{kg}{s^2 \ \cdot \ A} \)). These are derived but tailored to specific domains.

<div align='center'>
    <h1> Working with Units </h1>
</div>

## Multiplying

A physical quantity is defined as the product of a scalar number and a unit.

\[
Q = n \cdot u
\]

where \( n \) is a real number and \( U \) is a unit symbol. **This unit is not embedded in the number, it is an independent algebraic factor**. This separation is foundational. Numerical operations act on numbers, while units combine according to algebraic rules.

When two quantities are multiplied, the multiplication processes **independently on numbers and units**.

\[
(aU)×(bV)=(a×b)(U×V)
\]

This rule is exact and universal. No interpretation is applied at this stage, the operation is purely algebraic. Multiplying quantities does not describe a physical process, nor does it imply motion, shape or distribution.

**Example** - Separate into two operations. One for the numbers and one for the units.
\[
\frac{8}{3} \frac{L}{s} \times 8000L
\]

**Numbers**
\[
\frac{8}{3} \times 8000 = \frac{64000}{3}
\]

**Units**
\[
\frac{L}{s} \times L = \frac{L^2}{s}
\]

**Combine**
\[
\frac{64000}{3} \frac{L^2}{s}
\]

Units behave like algebraic symbols.

- They multiply
- They divide
- They cancel
- They exponentiate

They do **not** mix with numbers. You **never multiply a number ino a unit**. You only attach the unit after the numeric operation. **Units only change when you multiply by something that itself has units**.

- **Multiply by \(3\)** - Only the **number** changes.
- **Multiply by \( \frac{3}{3} \)** - Nothing changes.
- **Multiply by \( \frac{3s}{3s} \)** - Still nothing changes.
- **Multiply by \( 3s \)** - **Units** change.

So if you want a factor of \(3\) to appear in the unit, it must come from an expression that already contains that unit.

- Dimensionless factors only change numbers.
- Unit-bearing factors change units.

Additionally, **you do not need the same quantity to cancel units**. You need the same unit, not the same quantity.

**Example**
\[
\frac{5}{3} \frac{km}{s} \times 2s
\]

**Step 1 - Write in scalar-unit form**
\[
\frac{5}{3} \frac{km}{s} = \left( \frac{5}{3} \right) \frac{km}{s}
\]
\[
2s = 2 \times s
\]

**Step 2 - Multiply scalars and units separately**
\[
\left(\frac{5}{3} \times 2 \right) \left( \frac{km}{s} \times s\right)
\]

**Step 3 - Cancel units, not numbers**

You do not cancel \( 3s \) with \( 2s \), you only cancel the unit \( s \).

\[
\frac{km}{\cancel{s}} \times \cancel{s} = km
\]

**Result**
\[
\frac{10}{3} km
\]

## Inverting

A measured quantity is,

\[
Q = c \cdot U
\]

Where,

- \( c \) = scalar
- \( U \) = unit expression

They are distinct types of objects, but they are multiplied together into one algebraic object.

If you invert a quantity, you invert the entire product.

\[
Q^{-1} = \left( c \cdot U \right)^{-1}
\]

Now use the algebra rule
\[
(ab)^{-1} = a^{-1}b^{-1}
\]

Therefore

\[
(c \cdot U)^{-1} = c^{-1} \cdot U^{-1}
\]

Hence if we had the example,

\[
\frac{5}{3} \frac{m}{s} = \frac{5}{3} \cdot ms^{-1}
\]

Invert entire quantity

\[
= \left( \frac{5}{3} \right)^{-1} \cdot (ms^{-1})^{-1}
\]

\[
= \frac{3}{5} \cdot sm^{-1} = \frac{3}{5} \frac{s}{m}
\]

This has resulted the scalar being inverted and the unit exponents inverted. Multiplication and inversion apply to the entire product structure. The scalar and unit don't mix, they transform in parallel.

## Changing Between Units

To change units, we multiply conversion factors that equal 1.

We know,

\[
1km = 1000m \\
3600s = 1hr
\]

So,

\[
\frac{1km}{1000m} = \frac{\cancel{1000m}}{\cancel{1000m}} = 1
\]

\[
\frac{3600s}{1h} = \frac{\cancel{1h}}{\cancel{1h}} = 1
\]

So, what we want to do is multiply by 1 in disguise. Hence if we wish to change from \(\frac{m}{s}\) to \(\frac{km}{h} \)

\[
\frac{6}{5} \frac{m}{s} \cdot \frac{1km}{1000m} \cdot \frac{3600s}{1hr}
\]

Now, group and scalars.

**Scalars**
\[
\frac{6}{5} \cdot \frac{1}{1000} \cdot 3600 = \frac{6}{5} \cdot \frac{3600}{1000} = 4.32
\]

**Units**
\[
\frac{\cancel{m}}{\cancel{s}} \cdot \frac{km}{\cancel{m}} \cdot \frac{\cancel{s}}{hr} = \frac{km}{hr}
\]

**Result**
\[
4.32 \frac{km}{hr}
\]

<div align='center'>
    <h1> Exercises </h1>
</div>

**Question 1** - A \(1000L\) tank is filled at a rate of \( 25 \frac{L}{S}\). How long does it take to fill the tank?

Start with constructing the equation to solve for \( x \)
\[
25\frac{L}{s} \cdot x s = 1000L
\]

Cancel the seconds unit.
\[
25\frac{L}{\cancel{s}} \cdot x \cancel{s} = 1000L
\]

Condense the equation.
\[
25Lx = 1000L
\]

Cancel the Length unit.
\[
25\cancel{L}x = 1000\cancel{L}
\]

Now solve for \( x \)
\[
x = \frac{1000}{25} \\
x = 40
\]

Therefore, it will take 40 seconds to fill the tank.

**Question 2** - A car travels at a velocity of \(12\frac{m}{s}\) for \( 15s \). How far did the car travel?

Start with constructing the equation to solve for \( x \)
\[
12\frac{m}{s} \cdot 15s = xm
\]

Separate the scalar and units. Then condense the equation.
\[
\left( 12 \cdot 15\right) \left( \frac{m}{\cancel{s}} \cdot \cancel{s} \right) = xm
\]

Cancel out the metre units.
\[
180\cancel{m} = x\cancel{m}
\]

Solve for x.
\[
180 = x
\]

Therefore, the car will travel 180 metres.

**Question 3** - Convert \(8\frac{m}{s}\) to \(\frac{km}{hr}\)

Start by identifying the current units \( \frac{m}{s} \) and the units we need to change it to \( \frac{km}{h} \). Remember the golden rule, it's completely fine to multiplying by \( 1 \).

First, identify the conversion between \(m\) and \(km\)
\[
1km = 1000m \\
\frac{1km}{1000m} = 1
\]

Secondly, identify the conversion between \(s\) and \(hr\)

\[
3600s = 1hr \\
\frac{3600s}{1hr} = 1
\]

Now, we use this to convert between units by multiplying by 1 in disguise.

\[
8\frac{m}{s} \cdot \frac{1km}{1000m} \cdot \frac{3600s}{1hr}
\]

Now multiply separately between the scalar and the units.

\[
\left( 8 \cdot \frac{1}{1000} \cdot \frac{3600}{1} \right) \left( \frac{\cancel{m}}{\cancel{s}} \cdot \frac{km}{\cancel{m}} \cdot \frac{\cancel{s}}{hr} \right) = 8 \cdot \frac{3600}{1000} \frac{km}{hr} = 28.8 \frac{km}{hr}
\]

Therefore, \( 8\frac{m}{s} \) is equivalent to \( 28.8 \frac{km}{hr} \)

**Question 4** - A runner is moving at a velocity of 5\( \frac{m}{s} \). What is this rate in \( \frac{s}{m} \)?

Start with,

\[
5 \frac{m}{s}
\]

We want the recriprical. Therefore, we separate the scalar and unit and both put them to the power of \( - 1 \)

\[
\left( 5 \frac{m}{s}\right)^{-1} = \left(5^{-1}\right) \left(\frac{m}{s} \right)^{-1} = \frac{1}{5} \frac{s}{m}
\]

**Question 5** - With the density of liquid being \(800\frac{kg}{m^3}\) and having \( 4m^3\), what mass do you have?

First understand the question carefully to understand the unit we're solving for. We are asked to solve for how much mass we will have. Therefore, we need to solve the unknown \( x \) for the mass unit \( kg \).

\[
800\frac{kg}{m^3} \cdot 4m^3 = xkg
\]

\[
800\frac{kg}{\cancel{m^3}} \cdot 4\cancel{m^3} = xkg
\]

\[
800 \cdot 4 kg = xkg
\]

\[
3200 kg = xkg
\]

\[
3200 \cancel{kg} = x \cancel{kg}
\]

\[
3200 = x
\]

Now, solving for x we know that we will have \( 3200kg \)

**Question 6** - A rocket ejects gas at a rate of of \( 4\frac{kg}{s} \) with a velocity of \( 300 \frac{m}{s} \). What force is produced?

First, start with.

\[
4\frac{kg}{s} \cdot 300 \frac{m}{s}
\]

Group scalars and units.

\[
4 \cdot 300 \cdot \frac{kg}{s} \cdot \frac{m}{s}
\]

\[
1200 \frac{kg \cdot m}{s^2}  
\]

Now recognize,

\[
\frac{kg \cdot m}{s^2} = N
\]

Therefore,

\[
= 1200N
\]
