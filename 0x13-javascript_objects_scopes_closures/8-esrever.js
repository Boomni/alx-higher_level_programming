#!/usr/bin/node

exports.esrever = function esrever (list) {
  const reversedList = [];
  for (let i = list.length; i > 0; i--) {
    reversedList.push(i);
  }
  return reversedList;
};
