from bs4 import BeautifulSoup
import json

# List of HTML file names and corresponding JSON file names
html_files = ['index.html','page2.html','page3.html', 'page4.html', 'page5.html', 'page6.html', 'page7.html', 'page8.html', 'page9.html', 'page10.html', 'page11.html', 'page12.html',
              'page13.html', 'page14.html', 'page15.html', 'page16.html', 'page17.html', 'page18.html', 'page19.html', 'page20.html']  # Add your file names here
json_files = ['data1.json','data2.json''data3.json', 'data4.json', 'data5.json', 'data6.json', 'data7.json', 'data8.json', 'data9.json', 'data10.json', 'data11.json', 'data12.json',
              'data13.json', 'data14.json', 'data15.json', 'data16.json', 'data17.json', 'data18.json', 'data19.json', 'data20.json']  # Add desired JSON file names

# Loop through each pair of HTML and JSON file names
for html_file, json_file in zip(html_files, json_files):
    # Read the HTML file
    with open(html_file, 'r', encoding='utf-8') as file:
        html_content = file.read()

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find all divs with the specified class
    divs = soup.find_all(
        'div', class_='sg-col sg-col-4-of-12 sg-col-8-of-16 sg-col-12-of-20 sg-col-12-of-24 s-list-col-right')

    # Initialize a list to store the extracted data from this HTML page
    data_list = []

    # Loop through each div
    for div in divs:
        img = div.find('img', class_='s-image')
        link = img['src'] if img else ''

        span_title = div.find(
            'span', class_='a-size-medium a-color-base a-text-normal')
        title = span_title.get_text() if span_title else ''

        span_rating = div.find(
            'span', class_='a-size-base puis-normal-weight-text')
        rating = span_rating.get_text() if span_rating else ''

        span_price = div.find('span', class_='a-price-whole')
        price = span_price.get_text() if span_price else ''

        span_review = div.find('span', class_='a-size-base s-underline-text')
        review = span_review.get_text() if span_review else ''

        data_list.append({
            'link': link,
            'title': title,
            'rating': rating,
            'price': price,
            'review': review
        })

    # Write the extracted data to the corresponding JSON file
    with open(json_file, 'w', encoding='utf-8') as json_file:
        json.dump(data_list, json_file, ensure_ascii=False, indent=4)

    print(f'Data extracted and written to {json_file}')
