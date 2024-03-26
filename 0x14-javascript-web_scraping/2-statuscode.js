#!/usr/bin/node
/* display the status code of a GET request
Format code: < status code > */

const request = require('request');
const scriptName = process.argv[1].split('/').pop();

if (process.argv.length !== 3) {
  console.log(`Usage: ./${scriptName} <URL>`)
  process.exit(1)
}

const url = process.argv[2]

request(url, (err, response) => {
  if (err) console.log(err.message);

  else if (!response) console.log('Empty response');

  else console.log(`code: ${response.statusCode}`);
});
