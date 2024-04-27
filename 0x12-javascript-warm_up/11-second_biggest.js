#!/usr/bin/node
const { argv } = require('node:process');
function scMax (array) {
  if (array.length <= 1) {
    return 0;
  } else {
    let max = parseInt(array[0]);
    for (let i = 1; i < array.length; i++) {
      if (max < parseInt(array[i])) {
        max = parseInt(array[i]);
      }
    }
    let sc = Number.MIN_SAFE_INTEGER;
    for (let j = 0; j < array.length; j++) {
      if (parseInt(array[j]) < max && parseInt(array[j]) >= sc) {
        sc = parseInt(array[j]);
      }
    }
    return parseInt(sc);
  }
}
const array = argv.slice(2);
console.log(scMax(array));
