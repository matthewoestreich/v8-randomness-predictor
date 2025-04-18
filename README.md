# v8-randomness-predictor

Using [z3](https://github.com/Z3Prover/z3) to predict `Math.random` in [v8](https://v8.dev)

## YouTube video

<p>
  <a href='https://www.youtube.com/watch?v=-h_rj2-HP2E'>
    <img src="https://user-images.githubusercontent.com/19750782/178938498-371e69b9-1182-427a-86c3-dca3e769e7ef.png" alt="PwnFunction YouTube Video" width="600">
  </a>
</p>

Watch the [✨ YouTube Video](https://www.youtube.com/watch?v=-h_rj2-HP2E)

## Run Instructions

Get a few Random numbers from v8, run to following code in [d8](https://v8.dev/docs/d8), [nodejs](https://nodejs.org/) or [chrome](https://www.google.com/chrome/).

```js
Array.from(Array(5), Math.random)
```

Optionally you can set the random seed in nodejs so you'd get the same numbers as shown below.
```js
/*
* Run nodejs with `--random_seed` flag like
* node --random_seed=1337
*/
Array.from(Array(5), Math.random)
/*
[
  0.0026343227180927187,
  0.2751195310657766,
  0.14987294404396945,
  0.6754760504043595,
  0.4807256393350896
]
*/
```

You can use `main.py` at the root of this repo as a demo.

- Create a Python script
- Import `V8RandomnessPredictor`
- Create a variable to store generated random numbers from above
- Create `V8RandomnessPredictor` instance
- Call `predict_next()`
- Verify output is correct

```python
from V8RandomnessPredictor import V8RandomnessPredictor

sequence = [
  0.0026343227180927187,
  0.2751195310657766,
  0.14987294404396945,
  0.6754760504043595,
  0.4807256393350896
]

predictor = V8RandomnessPredictor(sequence)
next = predictor.predict_next()
print(next)
```

You can call `predict_next()` as many times as you would like, or until the generated cache of random numbers, that V8 creates internally, is exhausted.

Once that pool is exhausted the cache is refreshed with a different seed.

```python
next_ten_predictions = [predictor.predict_next() for _ in range(10)]
```

## Resources
- [Learn z3 by solving simple challenges](https://github.com/PwnFunction/learn-z3)
- [There’s Math.random(), and then there’s Math.random()](https://v8.dev/blog/math-random)
- [Further scramblings of Marsaglia’s xorshift generators](https://vigna.di.unimi.it/ftp/papers/xorshiftplus.pdf)
- [(V8 Deep Dives) Random Thoughts on Math.random()](https://apechkurov.medium.com/v8-deep-dives-random-thoughts-on-math-random-fb155075e9e5)
- [Hacking the JavaScript Lottery](https://blog.securityevaluators.com/hacking-the-javascript-lottery-80cc437e3b7f)
