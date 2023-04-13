#!/usr/bin/node
function factorial (n) {
  let answer = !n || isNaN(n) ? 1 : n * factorial(n - 1);
  return answer;
}
console.log(factorial(Number(process.argv[2])));
