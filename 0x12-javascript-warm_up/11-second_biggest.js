#!/usr/bin/node
/* searches the second biggest integer in the list of arguments  */

const argvIntegers = process.argv.slice(2).map(element => parseInt(element));

argvIntegers.sort((a, b) => a - b);

const res = argvIntegers[argvIntegers.length - 2];
if (!res) {
  console.log(0);
} else {
  console.log(res);
}
