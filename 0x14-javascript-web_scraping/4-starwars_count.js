#!/usr/bin/node
const request = require('request');
const SWrequest = process.argv[2];
let cnt = 0;

request(SWrequest, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    body = JSON.parse(body).results;

    for (let i = 0; i < body.length; i++) {
      const characters = body[i].characters;

      for (let n = 0; n < characters.length; n++) {
        const character = characters[n];
        const characterID = character.split('/')[5];

        if (characterID === '18') {
          cnt += 1;
        }
      }
    }

    console.log(cnt);
  }
});
