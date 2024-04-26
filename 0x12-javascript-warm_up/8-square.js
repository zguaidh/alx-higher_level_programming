#!/usr/bin/node
const { argv } = require('node:process');
const size = parseInt(argv[2]);
if (isNaN(size)) {
  console.log('Missing size');
}
let i = 0;
while (i < argv[2]) {
  console.log('X'.repeat(size));
  i++;
}
