#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let num = 0; num < this.height; num++) {
      console.log('X'.repeat(this.width));
    }
  }
}

module.exports = Rectangle;