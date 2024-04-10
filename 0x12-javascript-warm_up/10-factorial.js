#!/usr/bin/node
// Prints the factorial of a number passed via argument
function factorial (val) {
  return val === 0 || isNaN(val) ? 1 : val * factorial(val - 1);
}

console.log(factorial(Number(process.argv[2])));
