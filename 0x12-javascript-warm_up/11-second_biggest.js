#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log(0);
} else {
  let list = process.argv;
  list.pop(Math.max(...list));
  console.log(list.pop(Math.max(...list)));
}
