# Spotify Genre-Based Song Recommender

A genre based song recommendation system that uses Spotify audio features to recommend songs similar in sound and style. Built using machine learning and deployed with Streamlit.

---

## Live Demo

Try the app: [spotifyrecommender1.streamlit.app](https://spotifyrecommender1.streamlit.app)

---

## Project Structure



app.py                        - Main Streamlit app  
spotify_dataset_cleaned.csv  - Cleaned dataset with cluster labels  
requirements.txt             - Python dependencies for Streamlit  
Song_recommendation.ipynb    - Jupyter notebook for EDA & clustering  
README.md                    - Project documentation  



---

## How It Works

1. Loads a cleaned dataset of Spotify songs with audio features.
2. Uses **KMeans clustering** to group songs by similar musical properties.
3. You enter a song name and how many similar songs you want.
4. The app finds your song’s cluster and recommends others from the same group.

---

## Features

- Fuzzy search: match even if song name isn’t exact
- Cluster-based recommendations using KMeans
- User-defined number of recommendations
- Clean table output of results
- Fully deployed on [Streamlit Cloud](https://streamlit.io/cloud)

---

## Run Locally

```bash
git clone https://github.com/yourusername/spotify-recommender.git
cd spotify-recommender
pip install -r requirements.txt
streamlit run app.py
