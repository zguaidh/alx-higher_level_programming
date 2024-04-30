#!/usr/bin/node
const BSquare = require('./5-square');

class Square extends BSquare {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      for (let i = 0; i < this.width; i++) {
        console.log('X'.repeat(this.width));
      }
    } else {
      for (let i = 0; i < this.width; i++) {
        console.log(c.repeat(this.width));
      }
    }
  }
}
module.exports = Square;
