import data
from data import reduced_data

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