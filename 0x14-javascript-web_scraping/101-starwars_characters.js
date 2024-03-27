#!/usr/bin/node
/* prints all characters of a Star Wars movie
 * - The first argument is the Movie ID - example: 3 = “Return of the Jedi”
 * - Display one character name by line
 * - in the same order of the list “characters” in the /films/ response
 * - Using the Star wars API
 * NOTE: This is very slow
 *   */

const request = require('request');
const util = require('util');
const scriptName = process.argv[1].split('/').pop();

if (process.argv.length !== 3) {
  console.log(`Usage: ./${scriptName} <movie number>`);
  process.exit(1);
}

const id = process.argv[2];

const preRequest = util.promisify(request);

(async () => {
  try {
    const response = (await preRequest(`https://swapi-api.alx-tools.com/api/films/${id}`, { json: true })).body;
    for (const character of response.characters) {
      const response = (await preRequest(character, { json: true })).body;
      console.log(response.name);
    }
  } catch (err) {
    console.log(err.message);
  }
})();
