#!/usr/bin/node
// Prints the second largest of a list of arguments
if (process.argv.length <= 3) {
  console.log(0);
} else {
  const args = process.argv.map(Number)
    .slice(2, process.argv.length)
    .sort((a, b) => a - b);
  console.log(args[args.length - 2]);
}
