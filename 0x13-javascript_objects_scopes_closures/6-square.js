#!/usr/bin/node

const Rectangle = require('./5-square');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      super.print();
    } else {
      for (let num = 0; num < this.height; num++) {
        console.log(c.repeat(this.width));
      }
    }
  }
}

module.exports = Square;
