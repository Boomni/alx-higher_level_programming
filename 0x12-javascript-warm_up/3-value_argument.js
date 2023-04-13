#!/usr/bin/node

const args = process.argv.slice(2);

if (process.argv[2]) {
  console.log(args[0]);
} else {
  console.log('No argument');
}
