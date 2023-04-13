#!/usr/bin/node
let list = process.argv;
if (list.length <= 3) {
  console.log(0);
} else {
  list.splice(0, 2);
  const large = Math.max(...list);
  const newArray = list.filter(item => item !== large.toString());
  const second_large = Math.max(...newArray);
  console.log(second_large);
}
