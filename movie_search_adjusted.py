#The goal of this code is to find movies for evening view based on genre and release year using TMDB database.

import requests
import json

#API key
tmdb_api_key = "34d33e5cc8ca469a32e22b084bb7b2fd"

#Search parameters
genre = input("Enter genre: ")
release_year = input("Enter release year (yyyy): ")

#TMDB API search endpoint
tmdb_url = f"https://api.themoviedb.org/3/discover/movie?api_key={tmdb_api_key}&sort_by=vote_average.desc&vote_count.gte=100&with_genres={genre}&primary_release_year={release_year}"

#Send GET request to TMDB API
tmdb_response = requests.get(tmdb_url)

#Parse JSON response
tmdb_data = json.loads(tmdb_response.content)

#Extract top 10 movies based on user rating
if tmdb_data["total_results"] > 0:
    results = tmdb_data["results"][:10]
    for result in results:
        print(f"Title: {result['title']}\nRelease date: {result['release_date']}\nOverview: {result['overview']}\n")
else:
    print("No results found")