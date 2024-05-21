#!/usr/bin/node
const request = require('request');

// Function to fetch and print characters of a Star Wars movie
function getMovieCharacters (movieId) {
  const url = `https://swapi.dev/api/films/${movieId}/`;

  request(url, { json: true }, (err, res, body) => {
    if (err) {
      return console.error(`Error: Unable to fetch data for movie ID ${movieId}`, err.message);
    }

    if (res.statusCode !== 200) {
      return console.error(`Error: Received status code ${res.statusCode}`);
    }

    const characterUrls = body.characters;

    characterUrls.forEach(characterUrl => {
      request(characterUrl, { json: true }, (err, res, body) => {
        if (err) {
          return console.error(`Error fetching character data from ${characterUrl}`, err.message);
        }

        if (res.statusCode !== 200) {
          return console.error(`Error: Received status code ${res.statusCode} for ${characterUrl}`);
        }

        console.log(body.name);
      });
    });
  });
}

// Get the movie ID from command line arguments
const movieId = process.argv[2];

if (!movieId) {
  console.log('Usage: node script.js <movie_id>');
  process.exit(1);
}

getMovieCharacters(movieId);
