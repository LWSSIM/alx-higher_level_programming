#!/usr/bin/node
/* returns the reversed version of a list */

exports.esrever = function (list) {
  const tmp = list.slice();
  const listR = [];

  while (tmp.length) {
    listR.push(tmp.pop());
  }
  return listR;
};
