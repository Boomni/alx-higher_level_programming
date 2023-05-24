#!/usr/bin/node

const request = require('request');
const url = process.args[2];

request(url, function (error, response, body) {
  if (error) console.log('error:', error);
  else {
    const todos = JSON.parse(body);
    const dash = {};
    for (let i = 0; i < todos.length; i++) {
      const status = (todos[i].completed);
      const key = todos[i].userId.toString();
      if (status) {
        if (dash[key]) {
          dash[key]++;
        } else {
          dash[key] = 1;
        }
      }
    }
    console.log(dash);
  }
});
