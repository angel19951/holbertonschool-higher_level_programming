#!/usr/bin/node

const toInt = process.argv[2];
const check = parseInt(toInt);

if (toInt === undefined) {
  console.log('Not a number');
} else if (isNaN(check)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + check);
}
