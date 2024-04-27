#!/usr/bin/node
const { argv } = require('node:process');
function max(array) {
  if (array.length === 1) {
    return 0;
  } else {
    let max = array[0];
    for (let i = 1; i <= array.length - 1; i++) {
      if (max < array[i]) {
        max = array[i];
      }
    }
    return parseInt(max);
  }
}
const array = argv.slice(2);
console.log(max (array));
