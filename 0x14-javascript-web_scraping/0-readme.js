#!/usr/bin/node
/* Reads and prints the content of a file */

const fs = require('fs');

// Read the file
fs.readFile(process.argv[2], 'utf8', (err, data) => {
  if (err) {
    console.log(err);
    return;
  }
  console.log(data);
});
