#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (isNaN(w) || w <= 0 || isNaN(h) || h <= 0) {
      return null;
    } else {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }

  rotate () {
    let z = this.width;
    this.width = this.height;
    this.height = z;
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
}
module.exports = Rectangle;
