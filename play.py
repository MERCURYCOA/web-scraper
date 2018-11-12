import csv
import validators
with open("results.csv", 'r') as f:
    for row in f:
        url = row.split(',')[1]
        if(validators.url(url)):
            print(url)
            #one_link_posts("open2.csv", url)
        else:
            continue

