import requests
import json

# mist lab
mist_token = '8GMpPF7QaCOY2cwykSVYdrZ5Fd1Dlq1GWGf0fDhHcDuchK3ZMU5cesBeUUCR5VhiEqkAhg6c1nQcRfexbfoAiLEOBfcq4MbS'
organization_id = 'f9d9f882-7e5f-4407-b1f4-75dbe221c52e'

# mist mwt read only
mwt_id = 'f9d9f882-7e5f-4407-b1f4-75dbe221c52e'
mwt_token = 'mYmS8b4aDZ9NljaVcWfkGpsPS3MtbgQQrIjYKoh7TnQd7kLkRA8Soaz4GXgXAHBZ2aFSK3QeiQGU0dJtvr0mA9yPxW7jJLgK'# read only


# mist stores read only 
stores_id = '9a9d648b-610b-40fb-bf16-1231f682ff51'
stores_token = 'Nm6h9ihcRFvfujxudn6PB243dao0u6dR8jCiqctDfdXUU00CXplRr4tPChnY6A9KZlMAbTfYlVoMnDLGRec82yNzmWYjE9Mi'# read only

# filenames for each inventory
output_mwt_filename = 'mwt_inventory.txt'
output_stores_filename = 'stores_inventory.txt'

# API endpoints
api_mwt_url = f'https://api.mist.com/api/v1/orgs/{mwt_id}/inventory'
api_stores_url = f'https://api.mist.com/api/v1/orgs/{stores_id}/inventory'

# Set headers with right token
mwt_headers = {
    'Authorization': f'Token {mwt_token}',
    'Content-Type': 'application/json'
}
# Set headers with right token
stores_headers = {
    'Authorization': f'Token {stores_token}',
    'Content-Type': 'application/json'
}

# Send the GET request to retrieve the device inventory
response_mwt = requests.get(api_mwt_url, headers=mwt_headers)
response_stores = requests.get(api_stores_url, headers=stores_headers)

# Check if the request was successful
if response_mwt.status_code == 200:
    # Format the JSON response with indentation for readability
    formatted_json = json.dumps(response_mwt.json(), indent=4)

    # Save the formatted JSON to a text file
    with open(output_mwt_filename, 'w') as file:
        file.write(formatted_json)

    print(f"Device inventory saved to {output_mwt_filename} successfully.")
else:
    print(f"Failed to retrieve device inventory. Error: {response_mwt.text}")

# Check if the request was successful
if response_stores.status_code == 200:
    # Format the JSON response with indentation for readability
    formatted_stores_json = json.dumps(response_stores.json(), indent=4)

    # Save the formatted JSON to a text file
    with open(output_stores_filename, 'w') as file:
        file.write(formatted_json)

    print(f"Device inventory saved to {output_stores_filename} successfully.")
else:
    print(f"Failed to retrieve device inventory. Error: {response_stores.text}")    