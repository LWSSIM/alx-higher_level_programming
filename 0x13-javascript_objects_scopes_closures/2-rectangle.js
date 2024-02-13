#!/usr/bin/node
/* Class that defines a rectangle */
/* Add and init 2 attrs (w & h) */

class Rectangle {
  constructor (w, h) {
    if (!w || !h || w <= 0 || h <= 0) {
      return;
    }
    this.width = w;
    this.height = h;
  }
}

module.exports = Rectangle;
