#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log(0);
} else {
  process.argv.pop(Math.max(...process.argv));
  console.log(process.argv.pop(Math.max(...process.argv)));
}
