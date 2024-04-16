#!/usr/bin/node
exports.esrever = function (list) {
  return list.map((_, a) => list[list.length - 1 - a]);
};
