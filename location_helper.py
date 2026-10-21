import pandas as pd
from geopy.distance import geodesic

def filter_spaces(csv_path, user_lat, user_lon, max_distance_km, noise_filter="All"):
    # Load dataset
    df = pd.read_csv(csv_path)
    
    # Calculate distance for each location
    distances = []
    for idx, row in df.iterrows():
        space_location = (row['latitude'], row['longitude'])
        user_location = (user_lat, user_lon)
        dist_km = geodesic(user_location, space_location).km
        distances.append(round(dist_km, 2))
    
    df['distance_km'] = distances
    
    # Range filtering
    filtered_df = df[df['distance_km'] <= max_distance_km]
    
    # Noise level filter (Optional)
    if noise_filter != "All":
        filtered_df = filtered_df[filtered_df['noise_level'] == noise_filter]
        
    return filtered_df.sort_values(by='distance_km')