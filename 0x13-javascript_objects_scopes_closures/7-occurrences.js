#!/usr/bin/node
// Prints the number of occurrences in a list
exports.nbOccurences = function (list, searchElement) {
    return list.reduce((count, current) => current === searchElement ? count + 1 : count, 0);
};
