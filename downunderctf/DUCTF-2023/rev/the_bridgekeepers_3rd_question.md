# the bridgekeepers 3rd question (beginner)
What is your name? What is your quest? What is your favourite colour?

Author: hashkitten

https://rev-the-bridgekeepers-3rd-question-79d163ac441e.2023.ductf.dev

## Solution
On the website we are quested three questions per prompt, and after it we get a response. If we take a look at the source code of the website we see the following javascript:
```js
function cross() {
  prompt("What is your name?");
  prompt("What is your quest?");
  answer = prompt("What is your favourite colour?");
  if (answer == "blue") {
    document.getElementById('word').innerText = "flag is DUCTF{" + answer + "}";
    cross = escape;
  }
  else {
    document.getElementById('word').innerText = "you have been cast into the gorge";
    cross = unescape;
  }
}
```
So the site validates only the last answer of the three prompts.

But in the script section is also another js file loaded:
```html
  <script id="challenge" src="text/javascript">
    [...]
  </script>
```

Taking a look at this, we can see that the function _prompt()_ is overwritten:
```js
prompt = function (fun, x) {
  let answer = fun(x);

  if (!/^[a-z]{13}$/.exec(answer)) return "";

  let a = [], b = [], c = [], d = [], e = [], f = [], g = [], h = [], i = [], j = [], k = [], l = [], m = [];
  let n = "blue";
  a.push(a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, b, a, a, a, a, a, a, a, a);
  b.push(b, b, b, b, c, b, a, a, b, b, a, b, a, b, a, a, b, a, b, a, a, b, a, b, a, b);
  c.push(a, d, b, c, a, a, a, c, b, b, b, a, b, c, a, b, b, a, c, c, b, a, b, a, c, c);
  d.push(c, d, c, c, e, d, d, c, c, c, c, b, c, c, d, c, b, d, a, d, c, c, c, a, d, c);
  e.push(a, e, f, c, d, e, a, e, c, d, c, c, c, d, a, e, b, b, a, d, c, e, b, b, a, a);
  f.push(f, d, g, e, d, e, d, c, b, f, f, f, a, f, e, f, f, d, a, b, b, b, f, f, a, f);
  g.push(h, a, c, c, g, c, b, a, g, e, e, c, g, e, g, g, b, d, b, b, c, c, d, e, b, f);
  h.push(c, d, a, e, c, b, f, c, a, e, a, b, a, g, e, i, g, e, g, h, d, b, a, e, c, b);
  i.push(h, a, d, b, d, c, d, b, f, a, b, b, i, d, g, a, a, a, h, i, j, c, e, f, d, d);
  j.push(b, f, c, f, i, c, b, b, c, j, i, e, e, j, g, j, c, k, c, i, h, g, g, g, a, d);
  k.push(i, k, c, h, h, j, c, e, a, f, f, h, e, g, c, l, c, a, e, f, d, c, f, f, a, h);
  l.push(j, k, j, a, a, i, i, c, d, c, a, m, a, g, f, j, j, k, d, g, l, f, i, b, f, l);
  m.push(c, c, e, g, n, a, g, k, m, a, h, h, l, d, d, g, b, h, d, h, e, l, k, h, k, f);

  walk = a;

  for (let c of answer) {
    walk = walk[c.charCodeAt() - 97];
  }

  if (walk != "blue") return "";

  return {toString: () => _ = window._ ? answer : "blue"};

}.bind(null, prompt);

eval(document.getElementById('challenge').innerText);
```

At first the program checks if the input is 13 lowercase characters long. After that it creates a nested array with a depth of 13. In the last inner array `m` is the searched answer 'blue' (`n`) stored.

The other arrays has always only one reference to the next array. So the 17th place of `a` refers to `b`, the 4th place of `b` refers to `c` and so on. If we write down the places we find the following numbers:
```js
//     0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25
a.push(a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, b, a, a, a, a, a, a, a, a); // 17
b.push(b, b, b, b, c, b, a, a, b, b, a, b, a, b, a, a, b, a, b, a, a, b, a, b, a, b); // 4
c.push(a, d, b, c, a, a, a, c, b, b, b, a, b, c, a, b, b, a, c, c, b, a, b, a, c, c); // 1
d.push(c, d, c, c, e, d, d, c, c, c, c, b, c, c, d, c, b, d, a, d, c, c, c, a, d, c); // 4
e.push(a, e, f, c, d, e, a, e, c, d, c, c, c, d, a, e, b, b, a, d, c, e, b, b, a, a); // 2
f.push(f, d, g, e, d, e, d, c, b, f, f, f, a, f, e, f, f, d, a, b, b, b, f, f, a, f); // 2
g.push(h, a, c, c, g, c, b, a, g, e, e, c, g, e, g, g, b, d, b, b, c, c, d, e, b, f); // 0
h.push(c, d, a, e, c, b, f, c, a, e, a, b, a, g, e, i, g, e, g, h, d, b, a, e, c, b); // 15
i.push(h, a, d, b, d, c, d, b, f, a, b, b, i, d, g, a, a, a, h, i, j, c, e, f, d, d); // 20
j.push(b, f, c, f, i, c, b, b, c, j, i, e, e, j, g, j, c, k, c, i, h, g, g, g, a, d); // 17
k.push(i, k, c, h, h, j, c, e, a, f, f, h, e, g, c, l, c, a, e, f, d, c, f, f, a, h); // 15
l.push(j, k, j, a, a, i, i, c, d, c, a, m, a, g, f, j, j, k, d, g, l, f, i, b, f, l); // 11
m.push(c, c, e, g, n, a, g, k, m, a, h, h, l, d, d, g, b, h, d, h, e, l, k, h, k, f); // 4

let numbers = [17,4,1,4,2,2,0,15,20,17,15,11,4];
```

Going further in the js file, the program iterates in the next step over our input and substracts 97 from every integer representation of the characters and saves the array at this number of our initial nested array.

At the last step the program checks if the saved value is the answer 'blue'.

What we have to do now, is to input characters that represent the correct place of the next nested array after the substraction of 97.

To find this character we can simply add 97 to our numbers and check for ASCII representation. We can write a short script for that:
```js
let numbers = [17,4,1,4,2,2,0,15,20,17,15,11,4];

for (const num of numbers) {
  console.log(String.fromCharCode(num + 97));
}
```
As answer we get the following string: `rebeccapurple`

Entering that to the third question of the websites generates our flag: `DUCTF{rebeccapurple}`
