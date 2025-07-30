import streamlit as st
from Movies_Api import *

# Streamlit page configuration
st.set_page_config(page_title="🎬 Movie Search", layout="wide", page_icon="🎥")

# Custom CSS for styling the app
st.markdown("""
    <style>
    .main {
        background-color: #f7f9fc;
    }
    h1 {
        color: #2c3e50;
        text-align: center;
    }
    .movie-card {
        background-color: white;
        padding: 15px;
        border-radius: 12px;
        box-shadow: 0px 4px 8px rgba(0,0,0,0.1);
        margin-bottom: 20px;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)
#  Main app title 
st.title("🎬 Movies Search App")

# Sidebar with search input and button
with st.sidebar:
    st.header("🔍 Search for a Movie")
    search = st.text_input("Enter the movie name")
    search_button = st.button("Search")

# Handle search button click
if search_button:
    # Check if the input is empty
    if not search.strip():  
        st.error("❌ Please enter a movie name to search.")
    else:  #Fetch data from your custom API functions
        movies_data = get_movie_data(search)
        dataframe = build_dataframe(movies_data)
        # Placeholder image for movies without posters
        PLACEHOLDER_POSTER = "https://upload.wikimedia.org/wikipedia/commons/thumb/6/65/No-Image-Placeholder.svg/330px-No-Image-Placeholder.svg.png?20200912122019"

        if len(dataframe) != 0:
            st.subheader(f"✅ {len(dataframe)} Results Found for **{search}**")
            cols = st.columns(3)  # Display in 3 columns

            # Loop through the DataFrame rows
            for i, row in dataframe.iterrows():
                poster_url = row["Poster"] if row["Poster"] and row["Poster"] != "N/A" else PLACEHOLDER_POSTER
                col = cols[i % 3] # Distribute cards across 3 columns

                with col: # Movie card with poster, title, and year
                   st.markdown('<div class="movie-card">', unsafe_allow_html=True)
                   st.image(poster_url, use_container_width=True)  # Display the movie poster
                   st.markdown(f"### 🎞️ {row['Title']}")
                   st.markdown(f"⭐ **Year:** {row['Year']}")
                   st.markdown("</div>", unsafe_allow_html=True)

        else: #Show a warning if no movies are found
          st.warning("⚠️ No movie found. Please check the movie name.")


