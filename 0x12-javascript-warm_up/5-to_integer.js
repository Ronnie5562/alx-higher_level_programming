#!/usr/bin/node
console.log(Math.floor(process.argv[2]) ? `My number: ${Math.floor(process.argv[2])}` : 'Not a number');
