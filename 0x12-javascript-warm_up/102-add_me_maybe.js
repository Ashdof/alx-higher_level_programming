#!/usr/bin/node
// Increment and call a function
exports.addMeMaybe = function (number, theFunction) {
  theFunction(++number);
};
