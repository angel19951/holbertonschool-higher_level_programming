#!/usr/bin/node
const dict = require('./101-data').dict;
const dictionary = {};
for (const k in dict) {
  if (dictionary[dict[k]] === undefined) {
    dictionary[dict[k]] = [k];
  } else {
    dictionary[dict[k]].push(k);
  }
}
console.log(dictionary);
