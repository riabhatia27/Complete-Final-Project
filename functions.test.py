import unittest

import data
import functions
from functions import search_movie


reduced_data = [data.Movie(
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
        data.Movie(
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
        data.Movie(
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
        data.Movie(
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


class Testing(unittest.TestCase):
    pass


# function 1

    def test_search_movie1(self):
        self.assertTrue(search_movie("Barbie", "titles.txt"))


    def test_search_movie2(self):
        self.assertFalse(search_movie("Harry Potter and the Goblet of Fire", "titles.txt"))

# function 2
    def test_movies_above_rating1(self):
        result = functions.movies_above_rating(reduced_data, 7.5)
        titles = [movie.title for movie in result]
        expected_titles = ["Shrek", "Superbad", "The Godfather"]
        self.assertCountEqual(titles, expected_titles)


    def test_movies_above_rating2(self):
        result = functions.movies_above_rating(reduced_data, 8.0)
        titles = [movie.title for movie in result]
        expected_titles = ["The Godfather"]
        self.assertCountEqual(titles, expected_titles)


# function 3

    def test_sort_alpha1(self):
        result = functions.sort_alpha(reduced_data)
        sorted_titles = [movie.title for movie in result]
        expected_titles = ["Barbie", "Shrek", "Superbad", "The Godfather"]
        self.assertEqual(sorted_titles, expected_titles)


    def test_sort_alpha2(self):
        result = functions.sort_alpha(reduced_data)
        sorted_titles = [movie.title for movie in result]
        expected_titles = ["Barbie", "Superbad", "Shrek", "The Godfather"]
        self.assertIsNot(sorted_titles, expected_titles)


# function 4

    def test_average_sales_by_region1(self):
        result = functions.average_sales_by_region(reduced_data, "North America")
        expected = (0.40 * 3900000000 +
                    0.65 * 170812834 +
                    0.98 * 1400000000 +
                    0.55 * 250342198) / 4
        self.assertEqual(result, expected)


    def test_average_sales_by_region2(self):
        result = functions.average_sales_by_region(reduced_data, "Antarctica")
        expected = (0)
        self.assertEqual(result, expected)

# function 5

    def test_children_movies(self):
       result = functions.children_movies(reduced_data)
       expected = ["Shrek"]
       self.assertEqual(expected, result)


    def test_children_movies1(self):
       result = len(functions.children_movies(reduced_data))
       expected = 1
       self.assertEqual(expected, result)

# function 6

    def test_young_adult_movies(self):
       result = functions.young_adult_movies(reduced_data)
       expected = ["Barbie", "Shrek"]
       self.assertEqual(expected, result)


    def test_young_adult_movies1(self):
       result = len(functions.young_adult_movies(reduced_data))
       expected = 2
       self.assertEqual(expected, result)

# function 7

    def test_sorted_by_genre(self):
       result = functions.sorted_by_genre(reduced_data, "Comedy")
       expected = ["Barbie", "Shrek", "Superbad" ]
       self.assertEqual(expected, result)


    def test_sorted_by_genre1(self):
       result = functions.sorted_by_genre(reduced_data, "Romance")
       expected = ["Shrek"]
       self.assertEqual(expected, result)

# function 8

    def test_run_time(self):
       result = functions.run_time_less_than(reduced_data, 115)
       expected = ["Shrek", "Barbie"]
       self.assertEqual(expected, result)


    def test_run_time1(self):
       result = functions.run_time_less_than(reduced_data, 190)
       expected = ["Shrek", "Superbad", "Barbie", "The Godfather"]
       self.assertEqual(expected, result)




if __name__ == '__main__':
    unittest.main()