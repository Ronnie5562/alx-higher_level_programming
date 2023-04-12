#!/usr/bin/node
let num_printed = 0;
exports.logMe = function (item) { console.log(`${num_printed++}: ${item}`); };
