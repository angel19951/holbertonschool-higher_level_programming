#!/usr/bin/node
const request = require('request');
const SWrequest = 'https://swapi-api.hbtn.io/api/films/'.concat(process.argv[2]);

request(SWrequest, function (error, response, body) {
  body = JSON.parse(body);
  console.log(body.title);
});
