#!/usr/bin/node
let numPrinted = 0;
exports.logMe = function (item) { console.log(`${numPrinted++}: ${item}`); }
