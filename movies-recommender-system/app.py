import streamlit as st
import pickle
import pandas as pd

st.title('Movie Recommender System')

# Load data
movie_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movie_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Movie recommendation function
def recommend_movies(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = []
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies

# User input
selected_movie_name = st.selectbox(
    'Select a movie:',
    movies['title'].values)

# Recommend button
if st.button('Recommend'):
    recommendations = recommend_movies(selected_movie_name)
    st.write("Top 5 recommendations:")
    for name in recommendations:
        st.write(name)
