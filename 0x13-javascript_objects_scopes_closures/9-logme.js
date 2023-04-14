#!/usr/bin/node

let occurence = 0;
exports.logMe = function logMe (item) {
  console.log(`${occurence}: ${item}`);
  occurence++;
};
