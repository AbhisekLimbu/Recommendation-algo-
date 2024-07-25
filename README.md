# Recommendation-algo

# Recommendation Algorithm Prototype

This project is a prototype of a recommendation algorithm. It aims to search a local database for a product based on user input. If the product is found in the local database, it is displayed to the user. If the product is not found locally, the algorithm searches a larger information center (like Google) to identify the product and its details. Subsequently, the algorithm compares the product details with those in the local database to find similar items and make recommendations to the user based on this similarity.

## Features

- **Local Database Search**: Quickly searches a local database of products.
- **External Database Search**: Searches a comprehensive external database if no local match is found.
- **Similarity-Based Recommendations**: Suggests similar products from the local database based on key attributes such as genre and director.

## Workflow

1. **User Query**: The user inputs the name of the product they are searching for.
2. **Local Search**: The algorithm first searches for the product in the local database.
   - If an exact match is found, the product details are displayed.
   - If no exact match is found, the algorithm proceeds to the external search.
3. **External Search**: The algorithm searches a larger external database for the product.
   - If the product is found, its details are retrieved.
   - If the product is not found, the user is informed that no results were found.
4. **Similarity Comparison**: The algorithm compares the external product details with the local database to find similar products.
   - Similar products are identified based on attributes such as genre, director, or other relevant features.
5. **Recommendations**: The algorithm suggests similar products from the local database to the user.

## Example Usage

1. **User Input**: The user inputs the product name.
2. **Search Results**:
   - If found in the local database, the product details are displayed.
   - If not found locally, the external database is searched and similar products are recommended.

