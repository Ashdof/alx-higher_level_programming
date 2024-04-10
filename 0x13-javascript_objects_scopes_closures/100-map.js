#!/usr/bin/node
// Import array and compute a new array
const list = require('./100-data').list;
console.log(list);
console.log(list.map((item, index) => item * index));
