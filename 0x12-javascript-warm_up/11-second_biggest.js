#!/usr/bin/node
const { argv } = require('node:process');
const array = argv.slice(2);
if (array.length === 0) {
  console.log(0);
} else {
  let max = array[0];
  for (let i = 1; i <= array.length - 1; i++) {
    if (max < array[i]) {
      max = array[i];
    }
  }
  console.log(max);
}
