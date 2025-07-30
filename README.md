o
# 🎬 Movies Search App (OMDb API)

This project is a simple movie search application built with **Streamlit** and the **OMDb API**.  
It allows users to search for movies by title and view their posters, release year, and basic details.

---

## 🚀 Features
- Search for movies using the OMDb API.
- Display results in a clean grid layout with posters and details.
- Uses a placeholder image when no poster is available.
- Environment variables for secure API key management.
- Clean and modular code with separate API and UI scripts.

##📜 How It Works

### Movies_Api.py:

Uses the OMDb API to fetch movie data.

Converts JSON results into a Pandas DataFrame.

### app.py:

Builds the UI with Streamlit.

Allows users to search for movies and display results in a styled grid.

##📌  Example Usage
Open the Streamlit app.

Enter a movie title (e.g., Inception).

Click Search.

View movie posters and details directly in the browser.
