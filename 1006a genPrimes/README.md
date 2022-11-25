# 1006a Exercise: genPrimes

Write a generator, `genPrimes`, that returns the sequence of [prime numbers](http://en.wikipedia.org/wiki/Prime_number) on successive calls to its `next()` method: 2, 3, 5, 7, 11, ...

### **Hints**

**Ideas about the problem**

Have the generator keep a list of the primes it's generated. A candidate number `x` is prime if `(x % p) != 0` for all earlier primes `p`.