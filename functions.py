# This file has all the different functions we will be implementing for our project.
import data
from data import Movie
from data import reduced_data


# This function searches if a movie is on the platform (Ria)
# str argument is the string title representation of the movie
# The function returns true if the movie is present and false if it is not present
# incorporates exception handling and the statement "Movie Unavailable"

def search_movie(title: str, filename: str = "titles.txt") -> bool:
    try:
        with open(filename, "r") as file:
            for line in file:
                if title.strip().lower() == line.strip().lower():
                    return True
        return False
    except FileNotFoundError:
        return False


# This function evaluates if certain movies fall above a certain threshold and creates a new list of those movies who do (Ria)
# list argument is the list of various movie titles
# float argument is the threshold that is being compared
# This function returns a list of movies whose ratings fall above a certain threshold

def movies_above_rating(movies: list[Movie], threshold: float) -> list:
    result = []
    for movie in movies:
        if movie.rating >= threshold:
            result.append(movie)
    return result

# This function sorts movie titles alphabetically (Ria)
# list argument is the list of various movie titles
# This function returns a list of movies in alphabetical order

def sort_alpha(movies: list[Movie]) -> list:
    for i in range(0, len(movies) - 1):
        small_idx = i
        for j in range(i + 1, len(movies)):
            if movies[j].title.lower() < movies[small_idx].title.lower():
                small_idx = j
        if small_idx != i:
            movies[i], movies[small_idx] = movies[small_idx], movies[i]
    return movies


# This function evaluates the average ticket sales for a particular region (Ria).
# list argument is the list of various movie titles
# string argument is the name of the continent being compared
# This function returns the average sales a movie received in a continent

def average_sales_by_region(movies: list[Movie], region: str) -> float:
    total_sales = 0
    count = 0

    for movie in movies:
        if region in movie.region_sales:
            percent = movie.region_sales[region] / 100
            region_dollar_sales = movie.total_sales * percent
            total_sales += region_dollar_sales
            count += 1

    return total_sales / count if count > 0 else 0.0

# user input function


def check_movie_subtitles(movies: list):

    movie_title = input("Enter the movie title: ").strip()
    language = input("Enter the language to check for subtitles: ").strip()

    for movie in movies:
        if movie.title.lower() == movie_title.lower():
            has_subs = movie.subtitles.get(language, None)
            if has_subs is True:
                print(f" '{movie.title}' has subtitles in {language}.")
            elif has_subs is False:
                print(f" '{movie.title}' does NOT have subtitles in {language}.")
            else:
                print(f"️ '{language}' subtitles are not listed for '{movie.title}'.")
            return

    print(f"Movie titled '{movie_title}' not found.")

check_movie_subtitles(reduced_data)


