import json
import pandas as pd

raw_file = "data/raw/global_power_plant_database.csv"
output_file = "data/processed/powerplants.geojson"

plants = pd.read_csv(raw_file, low_memory=False)

plants = plants.dropna(subset=["latitude", "longitude"])

features = []

for _, plant in plants.iterrows():
    feature = {
        "type": "Feature",
        "geometry": {
            "type": "Point",
            "coordinates": [plant["longitude"], plant["latitude"]],
        },
        "properties": {
            "name": plant["name"],
            "country": plant["country_long"],
            "fuel": plant["primary_fuel"],
            "capacity_mw": plant["capacity_mw"],
        },
    }

    features.append(feature)

geojson = {
    "type": "FeatureCollection",
    "features": features,
}

with open(output_file, "w", encoding="utf-8") as f:
    json.dump(geojson, f)

print(f"Exported {len(features)} power plants to {output_file}")