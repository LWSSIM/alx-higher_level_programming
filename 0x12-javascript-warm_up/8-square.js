#!/usr/bin/node
/* prints a square */

const msg1 = 'Missing size';
const x = Number(process.argv[2]);

if (!x) {
  console.log(msg1);
}
for (let i = 0; i < x; i++) {
  console.log('X'.repeat(x));
}
