#!/usr/bin/node

let int = parseInt(process.argv[2]);
if (isNaN(int) || process.argv[2] === undefined) {
  console.log('Missing number of occurences');
} else {
  while (int > 0) {
    console.log('C is fun');
    int--;
  }
}
