#!/usr/bin/node

const myArgs = process.argv[2];
const check = parseInt(myArgs);

if (myArgs === undefined) {
  console.log('Missing size');
} else if (isNaN(check)) {
  console.log('Missing size');
} else if (check > 0) {
  for (let x = 0; x < check; x++) {
    console.log('X'.repeat(check));
  }
}
