#!/usr/bin/node
/* Class that defines a square inherit from rectangle */
/* uses extends + super() */

const S = require('./5-square');

class Square extends S {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (!c) {
      c = 'X';
    }
    for (let index = 0; index < this.height; index++) {
      console.log(c.repeat(this.width));
    }
  }
}

module.exports = Square;
