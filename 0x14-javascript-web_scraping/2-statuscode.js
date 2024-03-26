#!/usr/bin/node
/* display the status code of a GET request
 * Format=> code: <status code>*/

const request = require('request')

request(process.argv[2], (response) => {
  console.log(`code: ${response.statusCode}`)
})
