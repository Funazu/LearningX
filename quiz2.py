from pymongo import MongoClient
client = MongoClient('mongodb+srv://fauzunnaja:kamukepodeh@cluster0.kwi1dlp.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

# Mencari book dengan rating yang sama dengan The Godfather
target_movie = db.movies.find_one({'movie': "The Godfather"})
target_rating = target_movie['rating']

movies = list(db.movies.find({'rating': target_rating}))

for movie in movies:
    print(movie['movie'])



# db.movies.update_one(
#     {'movie': 'The Godfather'},
#     {'$set': {'rating': '0'}}
# )

# movie = db.movies.find_one({'movie': 'The Godfather'})
# print(movie['rating'])