#!/usr/bin/node
/* Class that defines a square inherit from rectangle */
/* uses extends + super() */

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
}

module.exports = Square;
