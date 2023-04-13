#!/usr/bin/node

class Rectangle {
  constructor (parseInt(w), parseInt(h)) {
    if (w <= 1 || h <= 1) {
      return {};
    } else {
      this.width = w;
      this.height = h;
    }
  }
}
module.exports = Rectangle;
