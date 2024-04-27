#!/usr/bin/node
const { argv } = require('node:process');
function fac (a) {
  if (isNaN(a) || a === 0) {
    return 1;
  } else {
    return a * fac(a - 1);
  }
}
const num = parseInt(argv[2]);
console.log(fac(num));
