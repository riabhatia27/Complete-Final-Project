class Movie:
    # Initialize a new Movie object.
    # input: the movie's title as a string
    # input: the movie's genre as a string
    # input: the movie's duration as a float
    # input: the movie's rating as a float
    # input: the movie's leading actors as a list of strings
    # input: the movie's director as a string
    # input: the movie's racial demographics as a dictionary
    # input: the movie's language as a string
    # input: the movie's release year as an integer
    # input: the movie's sales by continent as a dictionary
    # input: the movie's appropriateness rating as a string
    # input: the movie's accessibility to deaf viewers. outputs true or false

    def __init__(self,
                 title: str,
                 genre: list[str],
                 duration: float,
                 rating: float,
                 actors: list[str],
                 director: str,
                 cast_racial_demographics: dict[str, int],
                 language: str,
                 release_year: int,
                 total_sales: int,
                 region_sales:dict[str, int],
                 maturity: str,
                 subtitles: dict[str, bool]):

        self.title = title
        self.genre = genre
        self.duration = duration
        self.rating = rating
        self.actors = actors
        self.director = director
        self.cast_racial_demographics = cast_racial_demographics
        self.language = language
        self.release_year = release_year
        self.total_sales = total_sales
        self.region_sales = region_sales
        self.maturity = maturity
        self.subtitles = subtitles

    # Provide a developer-friendly string representation of the object.
    # input: Movie for which a string representation is desired.
    # output: string representation
    def __repr__(self):
        return 'Movie({}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {})'.format(
                self.title,
                self.genre,
                self.duration,
                self.rating,
                self.actors,
                self.director,
                self.cast_racial_demographics,
                self.language,
                self.release_year,
                self.total_sales,
                self.region_sales,
                self.maturity,
                self.subtitles)


    def __lt__(self, other):
        return self.title.lower() < other.title.lower()


    def __eq__(self, other):
        return isinstance(other, Movie) and self.title == other.title

reduced_data = [Movie(
            "Shrek",
            ["Comedy", "Romance", "Kids"],
            89,
            7.9,
            ["Mike Myers, Eddie Murphy, Cameron Diaz"],
            "Andrew Adamson",
            {"White": 75, "Black": 25},
            "English",
            2001,
            3900000000,
            {"North America": 40, "Europe": 35, "Asia": 10, "South America": 8, "Africa": 5, "Oceania": 2},
            "PG",
            {"English": True, "Spanish": True, "French": False, "German": False}
        ),
        Movie(
            "Superbad",
            ["Comedy", "Adventure"],
            119,
            7.6,
            ["Jonah Hill, Seth Rogen, Michael Cera"],
            "Greg Mottola",
            {"White": 90, "Black": 10},
            "English",
            2007,
            170812834,
            {"North America": 65, "Europe": 20, "Asia": 5, "South America": 5, "Africa": 2, "Oceania": 3},
            "R",
            {"English": True, "Spanish": True, "French": True, "German": True}
        ),
        Movie(
            "Barbie",
            ["Comedy"],
            113,
            6.8,
            ["Margot Robbie, Ryan Gosling, Will Ferrell"],
            "Greta Gerwig",
            {"White": 60, "Black": 15, "Asian": 10, "Latino": 10, "Other": 5},
            "English",
            2023,
            1400000000,
            {"North America": 98, "Europe": 0, "Asia": 15, "South America": 7, "Africa": 3, "Oceania": 0},
            "PG-13",
            {"English": True, "Spanish": True, "French": True, "German": True}
        ),
        Movie(
            "The Godfather",
            ["Crime", "Drama"],
            175,
            9.2,
            ["Al Pacino, Marlon Brando, James Caan"],
            "Francis Ford Coppola",
            {"White": 98, "Black": 0, "Asian": 0, "Latino": 0, "Other": 2},
            "English",
            1972,
            250342198,
            {"North America": 55, "Europe": 30, "Asia": 5, "South America": 5, "Africa": 2, "Oceania": 3},
            "R",
            {"English": True, "Spanish": True, "French": True, "German": True}
        )
    ]
