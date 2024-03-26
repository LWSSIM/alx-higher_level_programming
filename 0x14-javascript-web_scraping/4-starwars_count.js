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

  else if (response.statusCode !== 200) console.log(response.statusMessage);

  else {
    const data = JSON.parse(body);
    let count = 0;
    data.results.forEach(film => {
      if (film.characters.includes(
        'https://swapi-api.alx-tools.com/api/people/18/')) {
        count++;
      }
    });
    console.log(`${count}`);
  }
});
