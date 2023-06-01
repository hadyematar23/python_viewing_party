import requests 

def QueryMovie(query):
    api_key = "a2180673661db74377cb3704b314bd7a"
    url = f"https://api.themoviedb.org/3/search/movie?include_adult=false&language=en-US&page=1&query={query}"
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJhMjE4MDY3MzY2MWRiNzQzNzdjYjM3MDRiMzE0YmQ3YSIsInN1YiI6IjY0MWEzNjIyZjkxODNhMDFhMWNlNjdjYyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.ISKyw7rU82QKhmoaz8Y-PtohK-rztH4f8FlvkD0puRQ"
    }

    response = requests.get(url, headers=headers)

    return response.json()

