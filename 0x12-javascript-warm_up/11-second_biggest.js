#!/usr/bin/node
const { argv } = require('node:process');
function max(array) {
  if (array.length === 1 || array.length === 0) {
    return 0;
  } else {
    let max = array[0];
    for (let i = 1; i <= array.length - 1; i++) {
      if (max < array[i]) {
        max = array[i];
      }
    }
    let sc = 0;
    for (let j = 0; j <= array.length - 1; j++) {
      if ( array[i] < max && array[i] > sc) {
        sc = array[i];
      }
    return parseInt(sc);
    }
  }
}
const arg = argv.slice(2);
console.log(max (arg));
