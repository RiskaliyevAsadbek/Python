# 1 Task: JSON Parsing
# write a Python script that reads the students.jon JSON file and prints details of each student.

import json 

with open('students.json', 'r') as file:
    data = json.load(file)
print(data)

# 2 Task: Weather API
# Use this url : https://openweathermap.org/
# Use the requests library to fetch weather data 
# for a specific city(ex. your hometown: Tashkent) and print relevant information (temperature, humidity, etc.).

import requests
import json
url = "https://api.openweathermap.org/data/2.5/weather?q=Tashkent&appid=cbd84157db6bc50346489393ab5a8e83&units=metric"
response = requests.get(url)
data = response.json()
temperature = data['main']['temp']
print(f'First assignment of Task 2 {response.text}')
print(temperature)

# 3 Task: JSON Modification
# Write a program that allows users to add new books,
# update existing book information, and delete books from the books.json JSON file.
import json
import os

FILE_NAME = "books.json"

def load_books():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    return []

def save_books(books):
    with open(FILE_NAME, "w") as f:
        json.dump(books, f, indent=4)

def add_book():
    title = input("Enter book title: ")
    author = input("Enter author: ")
    year = input("Enter year: ")

    books = load_books()
    books.append({"title": title, "author": author, "year": year})
    save_books(books)
    print(f" Book '{title}' added successfully!")

def update_book():
    title = input("Enter the title of the book to update: ")
    books = load_books()

    for book in books:
        if book["title"].lower() == title.lower():
            print("Book found! Leave blank to keep current value.")
            new_title = input(f"New title (current: {book['title']}): ") or book["title"]
            new_author = input(f"New author (current: {book['author']}): ") or book["author"]
            new_year = input(f"New year (current: {book['year']}): ") or book["year"]

            book.update({"title": new_title, "author": new_author, "year": new_year})
            save_books(books)
            print(" Book updated successfully!")
            return

    print(" Book not found.")

def delete_book():
    title = input("Enter the title of the book to delete: ")
    books = load_books()

    updated_books = [book for book in books if book["title"].lower() != title.lower()]

    if len(updated_books) < len(books):
        save_books(updated_books)
        print(f" Book '{title}' deleted successfully!")
    else:
        print(" Book not found.")

def main():
    while True:
        print("\n=== BOOK MANAGEMENT SYSTEM ===")
        print("1. Add Book")
        print("2. Update Book")
        print("3. Delete Book")
        print("4. View All Books")
        print("5. Exit")

        choice = input("Choose an option (1–5): ")

        if choice == "1":
            add_book()
        elif choice == "2":
            update_book()
        elif choice == "3":
            delete_book()
        elif choice == "4":
            books = load_books()
            if books:
                print("\nCurrent Books:")
                for book in books:
                    print(f"- {book['title']} by {book['author']} ({book['year']})")
            else:
                print("No books found.")
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

# 4 Task: Movie Recommendation System
# Use this url http://www.omdbapi.com/ to fetch information about movies.
# Create a program that asks users for a movie genre and recommends a random movie from that genre.
import requests
import random

# Replace with your OMDb API key
API_KEY = "e9cc284"
BASE_URL = "http://www.omdbapi.com/"

# Some common genres to choose from
genres = ["Action", "Comedy", "Drama", "Horror", "Romance", "Sci-Fi", "Thriller"]

print("Available genres:", ", ".join(genres))
user_genre = input("Enter a movie genre: ").capitalize()

if user_genre not in genres:
    print("Sorry, that genre is not available.")
else:
    # A list of sample popular titles to search (since OMDb API does not directly filter by genre)
    sample_titles = [
        "Inception", "Titanic", "Avengers", "The Matrix", "The Notebook",
        "The Dark Knight", "Get Out", "Interstellar", "Parasite", "Joker",
        "Forrest Gump", "Gladiator", "Pulp Fiction", "The Godfather"
    ]
    
    random.shuffle(sample_titles)
    found_movies = []

    # Search through random titles and pick those matching the genre
    for title in sample_titles:
        params = {"t": title, "apikey": API_KEY}
        response = requests.get(BASE_URL, params=params)
        data = response.json()
        
        if data.get("Response") == "True" and user_genre in data.get("Genre", ""):
            found_movies.append({
                "Title": data["Title"],
                "Year": data["Year"],
                "Genre": data["Genre"],
                "Plot": data["Plot"]
            })

    if found_movies:
        movie = random.choice(found_movies)
        print("\n🎥 Recommended Movie:")
        print(f"Title: {movie['Title']}")
        print(f"Year: {movie['Year']}")
        print(f"Genre: {movie['Genre']}")
        print(f"Plot: {movie['Plot']}")
    else:
        print("No movies found for that genre. Try another one!")
