#!/usr/bin/node

const myArgs = process.argv.slice(2);

if (process.argv.length <= 3) {
  console.log(0);
} else {
  myArgs.sort((a, b) => b - a);
  console.log(myArgs[1]);
}
