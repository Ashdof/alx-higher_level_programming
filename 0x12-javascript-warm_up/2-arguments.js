#!/usr/bin/node
// Prints a message depending on the number of arguments pass
const num = process.argv.length;
console.log(num === 2 ? 'No argument' : num === 3 ? 'Argument found' : 'Arguments found');
