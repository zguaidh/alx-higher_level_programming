#!/usr/bin/node
exports.esrever = function (list) {
  const ls = [];
  for (let i = 1; i <= list.length; i++) {
    ls.push(list[list.length - i]);
  }
  return ls;
};
