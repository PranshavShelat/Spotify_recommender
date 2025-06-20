import streamlit as st
import pandas as pd

df_full = pd.read_csv("spotify_dataset_cleaned.csv")


def recommend(selected_song, df, n_recommendations):
    cluster_label = selected_song['cluster']
    similar_songs = df[(df['cluster'] == cluster_label) & (df['track_name'].str.lower() != selected_song['track_name'].lower())]
    recommended = similar_songs.sample(n=min(n_recommendations, len(similar_songs)))
    return recommended[['track_name', 'track_artist', 'playlist_genre', 'track_popularity']]


st.set_page_config(page_title="Spotify Song Recommender", layout="centered")
st.title("Spotify Genre-Based Song Recommender")

song_name = st.text_input("Enter a song name")
num_recs = st.number_input("Number of recommendations", min_value=1, max_value=20, value=5, step=1)

if song_name:
    matches = df_full[df_full['track_name'].str.lower().str.contains(song_name.lower(), na=False)]

    if matches.empty:
        st.warning(f"No matches found for '{song_name}'")
    else:
        options = matches[['track_name', 'track_artist']].drop_duplicates()
        options['label'] = options['track_name'] + " — " + options['track_artist']

        selected_label = st.selectbox("Select your song:", options['label'].tolist(), key="match_select")

        if st.button("Get Recommendations"):
         
            selected_row = matches[(matches['track_name'] + " — " + matches['track_artist']) == selected_label].iloc[0]
            st.session_state.selected_song = selected_row
            st.session_state.num_recs = int(num_recs)
            st.session_state.show_recs = True


if st.session_state.get("show_recs", False):
    st.subheader("Recommended Songs")
    recommendations = recommend(st.session_state.selected_song, df_full, st.session_state.num_recs)
    st.dataframe(recommendations.reset_index(drop=True))

