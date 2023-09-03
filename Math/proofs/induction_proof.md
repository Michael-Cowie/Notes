# Proof by Induction

The simpliest and most common form of mathematical induction refers that a statement involving a natural number $n$ holds for all values of $n$. <br>

The proof consists of two steps;

1. **The Base Case** <br>
    Prove that the statement holds for the first natural number $n$, usually $n = 0$ or $n = 1$. Rarely but sometimes convenientely the base value of $n$ may be taken as a larger number or even as a negative number. The statement only holds true for that value and above the threshold.

2. **The step case or inductive step** <br>
   Assume the statement holds for some natural number $n$, and prove that then the statement holds for $n+1$.

The hypothesis in the inductive step, that the statement holds for $n$ is called the induction hypothesis. To prove the inductive step, one assumes the induction hypothesis and then uses this assumption, involving $n$, to prove the statement for $n + 1$.

## Example

Mathematical induction can be used to prove, that the following statement $P(n)$ holds for all natural numbers $n$, <br>

$0 + 1 + 2 + ... + n = \frac{n \ * \ (n + 1)}{2}$


**Base Case:** Show that the statement holds for $n = 0$ <br>

1. $P(0)$ is easily seen to be true, <br>

   $0 = \frac{0 \ * \ (0 + 1)}{2}$ $\checkmark$

**Inductive step:** Show that if $P(k)$ holds, then also $P(k+1)$ holds. Assume $P(k)$ holds (for some unspecified value of $k$). It must then be shown that $P(k + 1)$ holds, that is: <br>

$(0 + 1 + 2 + ... + k) + (k + 1) = \frac{(k \ + \ 1) \ * \ ((k \ + \ 1) \ + \ 1)}{2}$ 
   
Using the induction assumption that $P(k)$ holds, the left-side can be written to,

$\frac{k \ * \ (k \ + \ 1)}{2} + (k + 1)$, hence <br>
$\frac{k \ * \ (k \ + \ 1)}{2} + (k + 1) = \frac{k \ * \ (k \ + \ 1) \ + \ 2(k \ + \ 1) }{2}$ <br>
$\frac{k \ * \ (k \ + \ 1)}{2} + (k + 1) = \frac{(k \ + \ 1)(k \ + \ 2)}{2}$ <br>
$\frac{k \ * \ (k \ + \ 1)}{2} + (k + 1) = \frac{(k \ + \ 1)((k \ + \ 1) \ + \ 1)}{2}$ <br>

Therefore, showing that indeed $P(k + 1)$ holds. Since both the base case and the inductive step have been performed, we can show that the statement $P(n)$ holds for all natural numbers $n$.
