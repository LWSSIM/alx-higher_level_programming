#!/usr/bin/node
/*  prints the title of a Star Wars movie
 *  where the episode number matches a given integer */

const request = require('request');
const scriptName = process.argv[1].split('/').pop();

if (process.argv.length !== 3) {
  console.log(`Usage: ./${scriptName} <movie number>`);
  process.exit(1);
}

const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

request(url, (err, response, body) => {
  if (err) console.log(err.message);

  else if (response.statusCode !== 200) console.log(response.statusMessage);

  else {
    const data = JSON.parse(body);
    const movieName = data.title;
    console.log(movieName);
  }
});
