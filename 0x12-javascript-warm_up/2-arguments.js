#!/usr/bin/node
/*  prints a message depending of the number of arguments passed */

let argc = process.argv.length - 2;

let msg1 = 'No argument', msg2 = 'Argument found', msg3 = 'Arguments found';

if (argc == 0)
  console.log(msg1);
else if (argc == 1)
  console.log(msg2);
else
  console.log(msg3);
