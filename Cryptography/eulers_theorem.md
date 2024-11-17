<div align="center">
  <h1> Euclidean Theorem </h1>
</div>

In number theory, Euler's Theorem states that, if $a$ and $n$ and coprime positive integers, and φ(n) is Euler's totient function, then $a^{φ(n)}$ is congruent to $1$ modulo $n$, that is <br>

$a^{φ(n)} \equiv 1 \ (mod \ n)$

Recall that $φ(n)$ tells us the number of positive integers up to $n$ that are coprime to $n$. Also that integers $a$ and $b$ are coprime, relatively prime or mutually prime if the only positive integer that is a divisor of both of them is 1. It can be defined as $\  k, 1 \le k \le  n$ for which $\  gcd(k, n) = 1$

## Example

The theorem may be used to easily reduce large powers modulo $n$. <br>
Consider finding $7^{222} \ (mod \ 10)$. The integers $7$ and $10$ are coprime and $φ(n) = 4$. Hence Euler's theorem yields $7^{4} \equiv 1 \ (mod \ 10)$ and we get, <br>

$7^{222} \equiv 7^{4 \ * \ 55 \ + \ 2} \equiv (7^{4})^{55} * 7^2 \equiv 1^{55} * 7^2 \equiv 49 \equiv 9 \ (mod \ 10)$