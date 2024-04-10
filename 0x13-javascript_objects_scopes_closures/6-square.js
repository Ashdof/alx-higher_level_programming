#!/usr/bin/node
// A class that models a square and extends the rectagle class
const Rectangle = require('./4-rectangle');

module.exports = class Square extends Rectangle {
  constructor(size) {
    super(size, size);
    this.size = size;
  }

  charPrint(c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let i = 0; i < this.height; i++) {
	console.log(c.repeat(this.width));
      }
    }
  }
}
