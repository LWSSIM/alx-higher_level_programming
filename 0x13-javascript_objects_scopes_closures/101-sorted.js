#!/usr/bin/node
/*  imports a dictionary of occurrences by user id and computes a dictionary of user ids by occurrence */

const dict = require('./101-data').dict;
const dictNew = {};

for (const userId in dict) {
  const occurrence = dict[userId];

  if (!dictNew[occurrence]) {
    dictNew[occurrence] = [];
  }

  dictNew[occurrence].push(userId);
}

console.log(dictNew);
