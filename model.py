import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import StandardScaler

# Load dataset
data = pd.read_csv("Spotify_Youtube.csv")

# Select features
features = ['Danceability','Energy','Tempo']

# Convert to numeric
for col in features:
    data[col] = pd.to_numeric(data[col], errors='coerce')

# Remove rows with missing values
data = data.dropna(subset=features)

# Prepare feature matrix
X = data[features]

# Scale values
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Calculate similarity
similarity = cosine_similarity(X_scaled)

def recommend(song):

    if song not in data['Track'].values:
        return []

    index = data[data['Track'] == song].index[0]

    distances = list(enumerate(similarity[index]))

    distances = sorted(distances, key=lambda x: x[1], reverse=True)[1:6]

    result = []

    for i in distances:
        row = data.iloc[i[0]]

        result.append({
            "song": row['Track'],
            "artist": row['Artist'],
            "youtube": row['Url_youtube']
        })

    return result