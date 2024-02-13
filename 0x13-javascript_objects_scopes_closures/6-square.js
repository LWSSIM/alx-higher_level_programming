#!/usr/bin/node
/* Class that defines a square inherit from rectangle */
/* uses extends + super() */

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
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
