#!/usr/bin/node

exports.nbOccurences = function nbOccurences (list, searchElement) {
  let count = 0;
  for (let i = 0; i < list.length; i++) {
    if (searchElement === list[i]) {
      count = count + 1;
    }
  }
  return count;
};
