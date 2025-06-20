import streamlit as st
import pandas as pd


df_full = pd.read_csv("spotify_dataset_cleaned.csv")


def recommend(song_name,df,n_recommendations):
  matches = df[df['track_name'].str.lower().str.contains(song_name.lower(), na=False)]
  if matches.empty:
    return f"Song '{song_name}' not found"
  if(len(matches)>1):
    print("Multiple matches found, please pick one: ")
    for i,row in matches[['track_name','track_artist']].reset_index(drop=True).iterrows():
      print(f"{i+1}. {row['track_name']}-{row['track_artist']}")
    choice=int(input("Enter your choice: "))
    if(choice<0 or choice>len(matches)):
      return "Invalid choice"
    song=matches.iloc[choice-1]
    print(f"your choice: {song['track_name']} - {song['track_artist']}")
  else:
    song=matches.iloc[0]
    print(f"your choice: {song['track_name']} - {song['track_artist']}")
  cluster_label=song['cluster']
  similar_songs=df[(df['cluster']==cluster_label)&(df['track_name'].str.lower()!=song_name.lower())]
  recommended=similar_songs.sample(n=min(n_recommendations,len(similar_songs)))
  return recommended[['track_name', 'track_artist', 'playlist_genre', 'track_popularity']]
st.set_page_config(page_title="Spotify Song Recommender", layout="centered")
st.title("Spotify Genre-Based Song Recommender")
st.write("Enter a song name and how many similar recommendations you'd like.")


song_name = st.text_input("Enter a song name")
num_recs = st.number_input("Number of recommendations", min_value=1, max_value=20, value=5, step=1)


if st.button("Get Recommendations"):
    with st.spinner("Finding similar songs..."):
        results = recommend(song_name, df_full, int(num_recs))
        st.write(results)
