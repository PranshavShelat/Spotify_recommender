import streamlit as st
import pandas as pd


df_full = pd.read_csv("spotify_dataset_cleaned.csv")


def recommend(song_name, df, n_recommendations):
    matches = df[df['track_name'].str.lower().str.contains(song_name.lower(), na=False)]
    if matches.empty:
        return pd.DataFrame([{"Error": f"Song '{song_name}' not found"}])

    if len(matches) > 1:
   
        options = matches[['track_name', 'track_artist']].drop_duplicates()
        options['label'] = options['track_name'] + " — " + options['track_artist']
        selection = st.selectbox("Multiple matches found. Please pick one:", options['label'].tolist())
        song = matches[(matches['track_name'] + " — " + matches['track_artist']) == selection].iloc[0]
    else:
        song = matches.iloc[0]

    cluster_label = song['cluster']
    similar_songs = df[(df['cluster'] == cluster_label) & (df['track_name'].str.lower() != song_name.lower())]
    recommended = similar_songs.sample(n=min(n_recommendations, len(similar_songs)))
    return recommended[['track_name', 'track_artist', 'playlist_genre', 'track_popularity']]


st.set_page_config(page_title="Spotify Song Recommender", layout="centered")
st.title("Spotify Genre-Based Song Recommender")
st.write("Enter a song name and how many similar songs you'd like.")


song_name = st.text_input("Enter a song name")
num_recs = st.number_input("Number of recommendations", min_value=1, max_value=20, value=5, step=1)


if st.button("Get Recommendations"):
    with st.spinner("Finding similar songs..."):
        results = recommend(song_name, df_full, int(num_recs))
        st.write(results)
