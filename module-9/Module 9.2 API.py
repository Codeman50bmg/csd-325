#Steven Skinner
#Module 9.2

import requests

# URL of the API to get the astronauts in space
url = "http://api.open-notify.org/astros.json"

# Send a GET request to the API
response = requests.get(url)

# Check if the connection was successful (status code 200)
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()
    
    # Get the number of astronauts and their names
    num_astro = data['number']
    astronauts = data['people']
    
    print(f"There are {num_astro} astronauts currently in space.")
    print("Their names are:")
    
    for astronaut in astronauts:
        print(f"- {astronaut['name']}")
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")