#!/usr/bin/node
const { argv } = require('node:process');
const a = parseInt(argv[2]);
const b = parseInt(argv[3]);
function add (a, b) {
  const c = a + b;
  console.log(c);
  return c;
}
add(a, b);
