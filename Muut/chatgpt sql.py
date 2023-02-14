import mysql.connector
import random
import folium

# Connect to the database
conn = mysql.connector.connect(
    host="localhost",
    user="user1",
    password="sala1",
    database="flight_game"
)

# Create a cursor object to execute queries
cursor = conn.cursor()

# Execute the SELECT query
query = "SELECT name, continent, longitude_deg, latitude_deg, ident FROM airport WHERE continent = 'EU' OR continent = 'AF'"
cursor.execute(query)

# Fetch all the rows of the query result
result = cursor.fetchall()

# Select 50 random rows from the result
filtered_airports = random.sample(result, 50)

# Create a map centered on the average latitude and longitude of the airports
latitudes = [airport[3] for airport in filtered_airports]
longitudes = [airport[2] for airport in filtered_airports]
avg_latitude = sum(latitudes) / len(latitudes)
avg_longitude = sum(longitudes) / len(longitudes)
map = folium.Map(location=[avg_latitude, avg_longitude], zoom_start=3)

# Add markers for each airport on the map
for airport in filtered_airports:
    name, continent, longitude, latitude, ident = airport
    folium.Marker(location=[latitude, longitude], popup=name).add_to(map)

# Display the map
map.save("filtered_airports.html")