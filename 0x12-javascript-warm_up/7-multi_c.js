#!/usr/bin/node
/*  prints x times “C is fun” */

const msg = 'C is fun';
const msg1 = 'Missing number of occurrences';
const x = Number(process.argv[2]);

if (!x) {
  console.log(msg1);
}
for (let i = 0; i < x; i++) {
  console.log(msg);
}
