#!/usr/bin/node

const args = process.argv;
args.splice(0, 2);

if (args.length <= 1) {
  console.log('0');
} else {
  args.sort((a, b) => b - a);
  console.log(args[1]);
}
