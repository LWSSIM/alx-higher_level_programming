#!/usr/bin/node
/* Class that defines a rectangle */
/* Add and init 2 attrs (w & h) */
/* Add attr validation */
/* Add print instance method */
/* Add double instance method */
/* Add rotate instance method */

class Rectangle {
  constructor (w, h) {
    if (!w || !h || w <= 0 || h <= 0) {
      return;
    }
    this.width = w;
    this.height = h;
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let arr = '';
      for (let j = 0; j < this.width; j++) {
        arr += 'X';
      }
      console.log(arr);
    }
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }

  rotate () {
    const tmp = this.width;
    this.width = this.height;
    this.height = tmp;
  }
}

module.exports = Rectangle;
