#!/usr/bin/node
/*  returns the number of occurrences in a list */

exports.nbOccurences = function (list, searchElement) {
  let res = 0;
  for (const i of list) {
    if (i === searchElement) {
      res++;
    }
  }
  return (res);
};
