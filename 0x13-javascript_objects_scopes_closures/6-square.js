#!/us/bin/node

const Rectangle = require('./4-rectangle');

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
