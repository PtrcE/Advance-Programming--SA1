#Exercise 10

#dictionary for film details
film_details = {
    "Title": "Inception",
    "Director": "Christopher Nolan",
    "Year": 2010,
    "Genre": "Science Fiction",
    "Rating": 8.8
}

#film details using a loop
print("Film Details:")
for key, value in film_details.items():
    print(f"{key}: {value}")
