#!/usr/bin/node

exports.esrever = function (list) {
  let lgt = list.length - 1;

  for (let num = 0; num <= list.length / 2; num++, lgt--) {
    list[num] = list[lgt];
    list[lgt] = list[num];
  }
  return (list);
};
