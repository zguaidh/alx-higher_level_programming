#!/usr/bin/node
const BSquare = require('./5-square');

class Square extends BSquare {
  constructor (size) {
    super(size, size);
    this.size = size;
  }

  charPrint (c) {
    if (c === undefined) {
      for (let i = 0; i < this.size; i++) {
        console.log('X'.repeat(this.size));
      }
    } else {
      for (let j = 0; j < this.size; j++) {
        console.log(c.repeat(this.size));
      }
    }
  }
}
module.exports = Square;
