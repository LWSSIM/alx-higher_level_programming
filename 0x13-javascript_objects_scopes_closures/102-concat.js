#!/usr/bin/node
/* concats 2 files. */

const fs = require('fs');

const f1 = process.argv[2];
const f2 = process.argv[3];
const fD = process.argv[4];

fs.readFile(f1, 'utf8', (err, data1) => {
  if (err) {
    console.log(err);
    return;
  }

  fs.readFile(f2, 'utf8', (err, data2) => {
    if (err) {
      console.log(err);
      return;
    }

    const concatData = data1 + data2;
    
    fs.writeFile(fD, concatData, (err) => {
    if (err) {
      console.log(err);
      return;
    }
    });
  });
});
