#!/usr/bin/node
/* computes and prints a factorial */

function factorial (a) {
  if (a < 0) {
    return (-1);
  }
  if (a === 1 || a === 0) {
    return (1);
  }
  return (a * factorial(a - 1));
}

const inputN = Number(process.argv[2]);
let res;

if (!inputN) {
  res = 1;
} else {
  res = factorial(inputN);
}
console.log(res);
