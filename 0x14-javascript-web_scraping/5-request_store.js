#!/usr/bin/node
/* gets the contents of a webpage and stores it in a file. */

const request = require('request');
const fs = require('fs');

const scriptName = process.argv[1].split('/').pop();

if (process.argv.length !== 4) {
  console.log(`Usage: ./${scriptName} <url>`);
  process.exit(1);
}

const url = process.argv[2];
const fileDest = process.argv[3];

request(url, (err, res, body) => {
  if (err) {
    console.log(err);
    process.exit(1);
  }

  body = body.toString();
  const data = body;

  fs.writeFile(fileDest, data, (err) => {
    if (err) {
      console.log(err);
      process.exit(1);
    }
  });
});
