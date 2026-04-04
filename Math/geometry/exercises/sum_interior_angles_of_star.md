<div align='center'>
    <h1> 5 Vertex Star <h1>
</div>

Before moving into larger vertex shapes, we will begin by demonstrating the base case where oth

<div align='center'>
    <img src='./images/1.png' width='400'/>
</div> 

#### Solution 1 - Using Exterior Angle Theorem

We first identify a triangle using two of the interior angles and use the the exterior angle theorem to use the identification below.

<div align='center'>
    <img src='./images/2.png' width='400'/>
</div> 

We then apply this again.

<div align='center'>
    <img src='./images/3.png' width='400'/>
</div>

Now, due to the definition of the sum of interior angles equalling 180 we know that the sum of the interior angles must all therefore equal 180.

<div align='center'>
    <img src='./images/4.png' width='400'/>
</div> 


#### Solution 2 - Using Interior Angles

While we have two possible approaches here, we will first be taking the approach where the star is regular. Regular meaning, all angles would be the same.

<div align='center'>
    <img src='./images/5.png' width='400'/>
</div> 

Inside the star, we can identify the pentagon that is illustrated by the blue lines. Additionally, we know that the interior angles on the convex polygon is $180 \cdot (n - 2)$. Therefore with $n = 5$ we can identify the purple angle with,

$$
180 \cdot (5 - 2) = 540 
$$

This is the sum of all angles, given that this is regular and they're all equal it means that the purple angle is 

$$\frac{540}{5} = 108$$

We can identify the triangle with purple lines and given that this is a regular star it is therefore an isoceles triangle with both green angles being the same. This leads to,

$$
\begin{aligned}
2 \cdot \text{green} + 108 &= 180 \\
2 \cdot \text{green} &= 72 \\
\angle \text{green} &= 36
\end{aligned}
$$

This is the single angle and therefore the sum of all angles is $$36 \cdot 5 = 180$$.

<div align='center'>
    <h1> 7 Vertex Star <h1>
</div>

#### Solution 1 - Using Exterior Angle Theorem

The exterior angle theorem will still apply, however it is going to take more steps.

<div align='center'>
    <img src='./images/6.png' width='600'/>
</div>

<div align='center'>
    <img src='./images/7.png' width='600'/>
</div>

<div align='center'>
    <img src='./images/8.png' width='600'/>
</div>

<div align='center'>
    <img src='./images/9.png' width='600'/>
</div> 

<div align='center'>
    <img src='./images/10.png' width='600'/>
</div> 

<div align='center'>
    <img src='./images/11.png' width='600'/>
</div>

This finally allows us to identify the final triangle and identify that,

$$
A + B + C + D + E + F + G = 180
$$

#### Solution 2 - Using Interior Angles for a Regular Convex Polygon

We will solve the sum of all interior angles of the star by first performing the arithmatic on a regular sized heptagonal star. As illustrated below, all angles will be the same and will be named $a$. Additionally, we have identified the triangle which will have the sum interior angles of $2a + b$.

<div align='center'>
    <img src='./images/12.png' width='600'/>
</div>

We can calculate the angle $b$ by first identifying a seven sided shape in the centre. We know that the interior angles on the convex polygon is $180 \cdot (n - 2)$. Therefore with $n = 7$ we can identify the angle $b$ with,

<div align='center'>
    <img src='./images/13.png' width='600'/>
</div>


$$
180 \cdot (7 - 2) = 900 
$$

This is the sum of all angles, given that this is regular and they're all equal it means that the purple angle is 

$$b = \frac{900}{7} = 128.57$$

We can now solve for $a$,

$$
\begin{aligned}
2a + b &= 180 \\
2b &= 51.43   \\
\angle b &= 25.715
\end{aligned}
$$

Therefore, the sum of all interior angles will be $$7b$$ and therefore give us $$7 \cdot 25.715 = 180$$

#### Solution 3 - Using Interior Angles for a Iregular Convex Polygon


Now, we will solve the same problem with an irregular shape. By being irregular we cannot calculate one angle and multiply it by $7$ to get the totla interior angle as they're not equivalent.

<div align='center'>
    <img src='./images/14.png' width='600'/>
</div>

We begin by identifying the 7 angles and label each one with a different variable.

<div align='center'>
    <img src='./images/15.png' width='600'/>
</div>

Then, we identify the interior polygon and name the angles too.

<div align='center'>
    <img src='./images/16.png' width='600'/>
</div>

Once all have been labelled we begin the list the geometric relationships. Below is an example of a geometric relationship for one angle of the interior polygon using $t$

<div align='center'>
    <img src='./images/17.png' width='600'/>
</div>

Finally, construct and identify each triangle using each interior angle of the internal polygon.

<div align='center'>
    <img src='./images/18.png' width='200'/>
</div>

Recall that the goal of this proof is to find $a + b + c + d + e + g$.

<div align='center'>
    <img src='./images/19.png' width='800'/>
</div>

<div align='center'>
    <img src='./images/20.png' width='800' />
</div>

<div align='center'>
    <img src='./images/21.png' width='800' height='60'/>
</div>

<div align='center'>
    <img src='./images/22.png' width='800' height='60'/>
</div>

This finally gives us,

$$
\boxed{a + b + c + d + e + f + g = 180}
$$