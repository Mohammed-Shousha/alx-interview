#!/usr/bin/node
const request = require("request-promise-native");
const API_URL = "https://swapi-api.hbtn.io/api";

if (process.argv.length > 2) {
  (async () => {
    try {
      const body = await request(`${API_URL}/films/${process.argv[2]}/`);
      const charactersURL = JSON.parse(body).characters;
      const charactersName = await Promise.all(
        charactersURL.map(async (url) => {
          const charactersReqBody = await request(url);
          return JSON.parse(charactersReqBody).name;
        })
      );
      console.log(charactersName.join("\n"));
    } catch (err) {
      console.log(err);
    }
  })();
}
