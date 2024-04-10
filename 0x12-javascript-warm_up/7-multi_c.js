#!/usr/bin/node
// Prints a statement a number of times
const num = Number(process.argv[2]);
if (isNaN(num)) {
  console.log('Missing number of occurrences');
} else {
  let i = 0;
  while (i < num) {
    console.log('C is fun');
    i++;
  }
}
