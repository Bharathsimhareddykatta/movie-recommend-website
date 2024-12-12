import pickle
import streamlit as st
import requests
import pandas as pd

def fetch_poster(movie_id):
    """Fetch movie poster using TMDB API."""
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US"
    response = requests.get(url)

    if response.status_code == 200:  # Check if the API call was successful
        data = response.json()
        poster_path = data.get('poster_path')  # Use .get() to avoid KeyError
        if poster_path:  # Check if poster_path exists
            return f"https://image.tmdb.org/t/p/w500/{poster_path}"
        else:
            return "https://via.placeholder.com/500x750?text=No+Poster"  # Fallback poster
    else:
        # Log error and return a placeholder image
        st.error(f"Failed to fetch poster. Error: {response.status_code}")
        return "https://via.placeholder.com/500x750?text=Error"


def recommend(movie):
    """Recommend movies based on similarity."""
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:6]:  # Get top 5 recommendations
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names, recommended_movie_posters


# Streamlit App
st.header('Movie Recommender System')

# Load models
movies_dict=pickle.load(open('movie_dict.pkl','rb'))
movies=pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))

# Dropdown for selecting movies
movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

# Recommendation button
if st.button('Show Recommendation'):
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie)

    # Display recommended movies in columns
    cols = st.columns(5)  # Create 5 columns dynamically
    for col, name, poster in zip(cols, recommended_movie_names, recommended_movie_posters):
        with col:
            st.text(name)
            st.image(poster, use_container_width=True)
