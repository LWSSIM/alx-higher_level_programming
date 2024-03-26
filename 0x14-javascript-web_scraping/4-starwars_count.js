#!/usr/bin/node
/* prints the number of movies where the character
 * “Wedge Antilles” is present */

const request = require('request');
const scriptName = process.argv[1].split('/').pop();

if (process.argv.length !== 3) {
  console.log(`Usage: ./${scriptName} <url>`);
  process.exit(1);
}

const url = process.argv[2];

request(url, (err, response, body) => {
  if (err) console.log(err.message);

  const count = body.split('/people/18/').length - 1;
  console.log(count);
});
