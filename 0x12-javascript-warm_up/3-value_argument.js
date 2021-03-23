#!/usr/bin/node

const myArgs = process.argv.slice(2);
const fArg = myArgs[0];

if (fArg === undefined) {
  console.log('No argument');
} else {
  console.log(fArg);
}
