#!/usr/bin/node

const request = require('requests');

const url = process.argv[2];

request.get(url).on('response', function (response) {
  console.log('code:', response.statusCode);
});
