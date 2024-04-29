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
}
module.exports = Rectangle;
