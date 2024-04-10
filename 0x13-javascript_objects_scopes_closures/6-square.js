#!/usr/bin/node
// A class that models a square and extends the rectagle class
const Rectangle = require('./5-square');

module.exports = class Square extends Rectangle {
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
