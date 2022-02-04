from DbStreamer.main import *
from data import *
import csv

obj = DbStreamer(host="localhost", user="root",
                 password="0000", database="mydb")

# Inserting into Tables
file = open('./data/movies.csv')
for row in list(csv.reader(file))[1:]:
    name = row[0]
    genre = row[1]
    studio = row[2]
    audience_score = row[3]
    profitability = row[4]
    rotten_tomatoes = row[5]
    worldwide_gross = row[6][1:-1]
    year = row[7]
    obj.insert_into_movies(
        name, genre, studio, audience_score, profitability,
        rotten_tomatoes, worldwide_gross, year
    )

# Deleting an entry from a movie
obj.delete_in_movies(1)
