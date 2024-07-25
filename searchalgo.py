# Step 1: Define a local database of movies (Netflix database)
local_database = [
    {"title": "Inception", "genre": "Sci-Fi", "director": "Christopher Nolan", "actors": ["Leonardo DiCaprio"], "country": "USA"},
    {"title": "The Dark Knight", "genre": "Action", "director": "Christopher Nolan", "actors": ["Christian Bale"], "country": "USA"},
    {"title": "Parasite", "genre": "Thriller", "director": "Bong Joon-ho", "actors": ["Kang-ho Song"], "country": "South Korea"},
    {"title": "Interstellar", "genre": "Sci-Fi", "director": "Christopher Nolan", "actors": ["Matthew McConaughey"], "country": "USA"},
    {"title": "La La Land", "genre": "Romance", "director": "Damien Chazelle", "actors": ["Ryan Gosling", "Emma Stone"], "country": "USA"},
]

# Step 2: Define a larger external database of movies (simulating a comprehensive movie database)
external_database = [
    {"title": "Inception", "genre": "Sci-Fi", "director": "Christopher Nolan", "actors": ["Leonardo DiCaprio"], "country": "USA"},
    {"title": "The Dark Knight", "genre": "Action", "director": "Christopher Nolan", "actors": ["Christian Bale"], "country": "USA"},
    {"title": "Parasite", "genre": "Thriller", "director": "Bong Joon-ho", "actors": ["Kang-ho Song"], "country": "South Korea"},
    {"title": "Interstellar", "genre": "Sci-Fi", "director": "Christopher Nolan", "actors": ["Matthew McConaughey"], "country": "USA"},

    {"title": "Inception", "genre": "Sci-Fi", "director": "Christopher Nolan", "actors": ["Leonardo DiCaprio"], "country": "USA"},
    {"title": "The Matrix", "genre": "Sci-Fi", "director": "Wachowskis", "actors": ["Keanu Reeves"], "country": "USA"},
    {"title": "Avatar", "genre": "Sci-Fi", "director": "James Cameron", "actors": ["Sam Worthington"], "country": "USA"},
    {"title": "Titanic", "genre": "Romance", "director": "James Cameron", "actors": ["Leonardo DiCaprio"], "country": "USA"},
    {"title": "Gladiator", "genre": "Action", "director": "Ridley Scott", "actors": ["Russell Crowe"], "country": "USA"},
    {"title": "Joker", "genre": "Thriller", "director": "Todd Phillips", "actors": ["Joaquin Phoenix"], "country": "USA"},
    {"title": "Mad Max: Fury Road", "genre": "Action", "director": "George Miller", "actors": ["Tom Hardy"], "country": "Australia"},
    {"title": "Gravity", "genre": "Sci-Fi", "director": "Alfonso Cuarón", "actors": ["Sandra Bullock"], "country": "USA"},
]

# Step 3: Define a function to search the local database
def search_local_database(query):
    for movie in local_database:
        if query.lower() in movie["title"].lower():
            return movie
    return None

# Step 4: Define a function to search the external database
def search_external_database(query):
    for movie in external_database:
        if query.lower() in movie["title"].lower():
            return movie
    return None

# Step 5: Define a function to find similar movies in the local database
def find_similar_movies(external_info):
    similar_movies = []
    for movie in local_database:
        score = calculate_similarity(movie, external_info)
        if score > 0:  # Threshold for similarity
            similar_movies.append(movie)
    return similar_movies

# Step 6: Define a function to calculate similarity (simple example)
def calculate_similarity(movie, external_info):
    score = 0
    if movie["genre"] == external_info["genre"]:
        score += 1
    if movie["director"] == external_info["director"]:
        score += 1
    return score

# Step 7: Main search function
def search_movie():
    user_query = input("Enter the movie name: ")

    # Search in local database
    local_result = search_local_database(user_query)
    if local_result:
        print(f"Found in local database: {local_result}")
        return
    
    # Search in external database
    external_info = search_external_database(user_query)
    if external_info:
        similar_movies = find_similar_movies(external_info)
        if similar_movies:
            print(f"No exact match in local database. Similar movies from local database: {similar_movies}")
        else:
            print("No similar movies found in local database.")
        return
    
    print("No results found in either local or external database.")

# Example usage
search_movie()
