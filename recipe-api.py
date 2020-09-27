from recipe_scrapers import scrape_me
import csv
import json

csv_file = 'recipe_urls.csv'
category = 'recipes'
json_file = 'recipes.json'

with open(csv_file, 'r') as fd:
    reader = csv.reader(fd)

    data = {}
    data[category] = []

    for row in reader:
        # Gives the url as a string from csv file
        scraper = scrape_me(row[0])

        data['recipes'].append({
            'title' : scraper.title(),
            # 'total_time' : scraper.total_time(),
            'yields' : scraper.yields(),
            'ingredients' : scraper.ingredients(),
            'instructions' : scraper.instructions(),
            'image' : scraper.image(),
        })

    # Serializing json
    json_object = json.dumps(data, indent = 5)

    # Writing to recipes.json
    with open(json_file, "w") as outfile:
        outfile.write(json_object)

