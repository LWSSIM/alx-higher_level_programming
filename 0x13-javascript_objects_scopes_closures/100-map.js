#!/usr/bin/node
/* imports an array and computes a new array */
/* import list from the file 100-data.js */

const list = require('./100-data.js').list;
const listNew = list.map((item, index) => item * index);

console.log(list);
console.log(listNew);
