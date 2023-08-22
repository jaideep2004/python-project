import json
import csv

# List of JSON file names
json_files = ['data1.json', 'data2.json', 'data3.json', 'data4.json', 'data5.json', 'data6.json', 'data7.json', 'data8.json', 'data9.json', 'data10.json',
              'data11.json', 'data12.json', 'data13.json', 'data14.json', 'data15.json', 'data16.json', 'data17.json', 'data18.json','data19.json','data20.json']  # Add your JSON file names here

# Initialize a list to store the combined data
combined_data = []

# Loop through each JSON file
for json_file in json_files:
    # Read the JSON file
    with open(json_file, 'r', encoding='utf-8') as file:
        json_content = file.read()

    # Load JSON content
    data_list = json.loads(json_content)

    # Add the data from this JSON file to the combined list
    combined_data.extend(data_list)

# Define CSV columns
csv_columns = ['link', 'title', 'rating', 'price', 'review']

# Write the combined data to a single CSV file
csv_filename = 'combined_data.csv'
with open(csv_filename, 'w', newline='', encoding='utf-8') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=csv_columns)
    writer.writeheader()
    for data in combined_data:
        writer.writerow({
            'link': data.get('link', ''),
            'title': data.get('title', ''),
            'rating': data.get('rating', ''),
            'price': data.get('price', ''),
            'review': data.get('review', '')
        })

print(f'Combined data from all JSON files converted to {csv_filename}')
