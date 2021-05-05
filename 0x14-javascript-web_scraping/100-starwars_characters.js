#!/usr/bin/node
const request = require('request');
const SWrequest = 'https://swapi-api.hbtn.io/api/films/'.concat(process.argv[2]);

request(SWrequest, function (error, respons, body) {
  if (error) {
    console.log(error);
  } else {
    const characters = JSON.parse(body).characters;

    for (let i = 0; i < characters.length; i++) {
      request(characters[i], function (charError, charRespons, charBody) {
        console.log(JSON.parse(charBody).name);
      });
    }
  }
});
