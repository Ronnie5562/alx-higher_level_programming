#!/usr/bin/node
const argv_length = process.argv.length;
console.log(argv_length === 2 ? 'No argument' : argv_length === 3 ? 'Argument found' : 'Arguments found');
