#!/usr/bin/node

function factorial (number) {
  let factorial = 1;
  if (isNaN(number) && (number < 1)) {
    console.log(1);
  } else {
    for (let i = 1; i <= number; i++) {
      factorial = factorial * i;
    }
    console.log(factorial);
  }
}
const number = parseInt(process.argv[2]);
factorial(number);
