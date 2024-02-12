#!/usr/bin/node
/*  prints a message depending of the number of arguments passed */

const argc = process.argv.length - 2;

const msg1 = 'No argument'; const msg2 = 'Argument found'; const msg3 = 'Arguments found';

if (argc === 0) { console.log(msg1); } else if (argc === 1) { console.log(msg2); } else { console.log(msg3); }
