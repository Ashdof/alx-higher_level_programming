#!/usr/bin/node
const axios = require('axios');

// Function to fetch and print characters of a Star Wars movie
async function getMovieCharacters (movieId) {
  // Fetch the movie data using the movie ID
  const response = await axios.get(`https://swapi.dev/api/films/${movieId}/`);
  const movieData = response.data;

  // Get the list of character URLs
  const characterUrls = movieData.characters;

  // Fetch and print each character's name
  for (const url of characterUrls) {
    const characterResponse = await axios.get(url);
    console.log(characterResponse.data.name);
  }
}

// Get the movie ID from command line arguments
const movieId = process.argv[2];

if (!movieId) {
  console.log('Usage: node script.js <movie_id>');
  process.exit(1);
}

getMovieCharacters(movieId);
