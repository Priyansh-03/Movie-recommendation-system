import streamlit as st
import pickle

movies = pickle.load(open("movies.pkl", "rb"))
similarity = pickle.load(open("similarity.pkl", "rb"))

movies_list = movies["title"].values

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(enumerate(distances), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = []
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies

st.title("Movie Recommendation System")

selected_option = st.selectbox(
    'What would you like to watch?',
    movies_list
)

if st.button('Recommend'):
    recommendations = recommend(selected_option)
    # for i in recommendations:
    #     st.write(i)

    # Display recommendations in columns
    columns = st.columns(5)
    for i, col in enumerate(columns):
        col.write(recommendations[i])

#3 to run --> streamlit app.py 