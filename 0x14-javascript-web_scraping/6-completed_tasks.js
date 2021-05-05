#!/usr/bin/node
const request = require('request');

request(process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const completedTasksByUser = {};
    body = JSON.parse(body);

    for (let i = 0; i < body.length; ++i) {
      const userId = body[i].userId;
      const completed = body[i].completed;

      if (completed && !completedTasksByUser[userId]) {
        completedTasksByUser[userId] = 0;
      }
      if (completed) ++completedTasksByUser[userId];
    }

    console.log(completedTasksByUser);
  }
});
