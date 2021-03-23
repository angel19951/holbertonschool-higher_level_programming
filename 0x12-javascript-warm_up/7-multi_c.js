#!/usr/bin/node

const myArgs = process.argv[2];
const check = parseInt(myArgs);

if (myArgs === undefined) {
  console.log('Missing number of occurrences');
} else if (check > 0) {
  for (let num = 0; num < check; num++) {
    console.log('C is fun');
  }
}
