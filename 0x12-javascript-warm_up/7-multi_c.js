#!/usr/bin/node
let x = Math.floor(Number(process.argv[2]));
if (isNaN(x)) {
    console.log('Missing number of occurrences');
} else {
    for (let i = 1; i <= x; i++) {
        console.log('C is fun');
    }
}
