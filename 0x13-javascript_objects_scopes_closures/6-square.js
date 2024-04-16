#!/usr/bin/node

const Square5 = require('./5-square');

class Square extends Square5 {
  charPrint (c = 'X') {
    for (let a = 0; a < this.height; a++) {
      console.log(c.repeat(this.width));
    }
  }
}

module.exports = Square;
