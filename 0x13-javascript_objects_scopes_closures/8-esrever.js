#!/usr/bin/node
exports.esrever = function (list) {
  const [array, length] = [[], list.length];
  for (let x = 0; x < length; x++) {
    array.push(list.pop());
  }
  return array;
};
