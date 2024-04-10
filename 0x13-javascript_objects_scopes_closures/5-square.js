#!/usr/bin/node
// A class that models a square and extends the rectagle class
const Rectangle = require('./4-rectangle');

module.exports = class Square extends Rectangle {
  constructor(size) {
    super(size, size);
    this.size = size;
  }
}
