#!/usr/bin/node

const fac = parseInt(process.argv[2]);

function factorial (a) {
  if (a === undefined || isNaN(a)) {
    return 1;
  } else if (a === 0) {
    return 1;
  }
  return a * factorial(a - 1);
}

console.log(factorial(fac));
