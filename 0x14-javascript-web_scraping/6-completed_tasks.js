#!/usr/bin/node
/* compute the number of completed tasks by user id */

const request = require('request');
const scriptName = process.argv[1].split('/').pop();

if (process.argv.length !== 3) {
  console.log(`Usage: ./${scriptName} <url>`);
  process.exit(1);
}

const url = process.argv[2];

request(url, { json: true }, (err, res, body) => {
  if (err) {
    console.log(err);
    process.exit(1);
  }
  if (res.statusCode !== 200) {
    console.log(res.statusMessage);
    process.exit(1);
  }

  const completedTasks = {};
  body.forEach(task => {
    if (task.completed === true) {
      if (!completedTasks[task.userId]) {
        completedTasks[task.userId] = 1;
      } else {
        completedTasks[task.userId]++;
      }
    }
  });
  console.log(completedTasks);
});
