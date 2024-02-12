#!/usr/bin/node
/*  prints My number: <first argument converted in integer>
 *    if the first argument can be converted to an integer */

const newINT = Number(process.argv[2]);

if (newINT) {
  console.log(`My number: ${newINT}`);
} else {
  console.log('Not a number');
}
