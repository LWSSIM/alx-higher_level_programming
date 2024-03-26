#!/usr/bin/node
/* prints all characters of a Star Wars movie
 * - The first argument is the Movie ID - example: 3 = “Return of the Jedi”
 * - Display one character name by line
 * - Using the Star wars API */

const request = require('request');
const scriptName = process.argv[1].split('/').pop();

if (process.argv.length !== 3) {
  console.log(`Usage: ./${scriptName} <movie number>`);
  process.exit(1);
}

const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

request(url, { json: true }, (err, response, body) => {
  if (err) console.log(err.message);

  else if (response.statusCode !== 200) console.log(response.statusMessage);

  else {
    const characters = body.characters;
    characters.forEach(character => {
      request(character, (err, res, body) => {
        if (err) console.log(err.message);
        else if (res.statusCode !== 200) console.log(res.statusMessage);
        else {
          const data = JSON.parse(body);
          console.log(data.name);
        }
      });
    });
  }
});
