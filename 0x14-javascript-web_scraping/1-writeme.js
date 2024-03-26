#!/usr/bin/node
/* Write a string to a file */

const fs = require('fs');

// Write input to file
fs.writeFile(process.argv[2], process.argv[3], 'utf-8', (err) => {
  if (err) {
    console.log(err);
  }
});
