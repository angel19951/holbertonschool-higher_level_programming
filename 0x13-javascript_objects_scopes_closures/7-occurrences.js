#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let cnt = 0;

  for (let num = 0; num < list.length; num++) {
    if (list[num] === searchElement) {
      cnt++;
    }
  }
  return (cnt);
};
