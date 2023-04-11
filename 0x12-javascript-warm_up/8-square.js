//#!/usr/bin/node
let number = Number(process.argv[2]);
if (isNaN(number)) {
    console.log('Missing size');
} else {
    for (let i = 1; i <= number; i++) {
        let line = '';
        for (let i = 1; i <= number; i++) {
            line += 'X'
        }
        console.log(line);
    }
}
