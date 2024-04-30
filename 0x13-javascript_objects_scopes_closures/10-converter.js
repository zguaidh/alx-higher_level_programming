#!/usr/bin/node
exports.converter = function (base) {
  const converter = function (num) {
    return num.toString(base);
  };
  return converter;
};
