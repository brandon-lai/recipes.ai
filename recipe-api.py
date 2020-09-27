from recipe_scrapers import scrape_me
import csv
import json

category = 'recipes'

with open('recipe_urls.csv', 'r') as fd:
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
    with open('recipes.json', "w") as outfile:
        outfile.write(json_object)

