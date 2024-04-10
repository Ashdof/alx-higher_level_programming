#!/usr/bin/node
// Convert a number from base 10 to another, passed as argument
exports.converter = function (base) {
  return num => num.toString(base);
};
