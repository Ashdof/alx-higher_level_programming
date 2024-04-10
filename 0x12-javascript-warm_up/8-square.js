#!/usr/bin/node
// Prints a square, according to the number passed as argument
const num = Number(process.argv[2]);

if (isNaN(num)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < num; i++) {
    let row = '';
    for (let j = 0; j < num; j++) {
      row += 'X';
    }

    console.log(row);
  }
}
