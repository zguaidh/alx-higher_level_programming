#!/usr/bin/node
const { argv } = require('node:process');
if (isNaN(parseInt(argv[2]))) {
  console.log('Missing number of occurrences');
}
let i = 0;
while (i < argv[2]) {
  console.log('C is fun');
  i++;
}
