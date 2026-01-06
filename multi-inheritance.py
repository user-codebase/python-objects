import random
from datetime import datetime

class Video:
    def __init__(self, title, year, genre):
        self.title = title
        self.year = year
        self.genre = genre
        self.views = 0

    def play(self):
        self.views += 1

    def __lt__(self, other):
        return self.title < other.title


class Movie(Video):
    def __str__(self):
        return f"{self.title} ({self.year})"


class Series(Video):
    def __init__(self, title, year, genre, season, episode):
        super().__init__(title, year, genre)
        self.season = season
        self.episode = episode

    def __str__(self):
        return f"{self.title} S{self.season:02d}E{self.episode:02d}"


def get_movies(video_library):
    return sorted([item for item in video_library if isinstance(item, Movie)]) # sorted uzywa def __lt__(self, other)


def get_series(video_library):
    return sorted([item for item in video_library if isinstance(item, Series)]) # sorted uzywa def __lt__(self, other)



def search(video_library, title):
    return [item for item in video_library if title in item.title]


def generate_views(video_library):
    random_index = random.randint(0, len(video_library) - 1)
    video_library[random_index].views += random.randint(1, 100)


def generate_views_10_times(video_library):
    for i in range(10):
        generate_views(video_library)

def get_views(item):
    return item.views

def top_titles(video_library, amount, content_type):
    if content_type == "movie":
        items = get_movies(video_library)
    elif content_type == "series":
        items = get_series(video_library)
    else:
        items = video_library

    list_with_videos = sorted(items, key=get_views, reverse=True) # sorted uzywa def get_views do porownania
    return list_with_videos[:amount]


def add_full_season(video_library, title, year, genre, season, episodes):
    for episode_number in range(episodes):
        video_library.append(Series(title, year, genre, season, episode_number + 1))

def count_episodes(video_library, title):
    return len([item for item in video_library if isinstance(item, Series) and item.title == title])

if __name__ == '__main__':

    print("Biblioteka filmów")

    video_library = []

    movie_1 = Movie("Movie_1", 1990, "Action")
    movie_2 = Movie("Movie_2", 2010, "Crime")
    movie_3 = Movie("Movie_3", 2000, "Sci-Fi")

    video_library.append(movie_1)
    video_library.append(movie_2)
    video_library.append(movie_3)

    add_full_season(video_library, "Series_1", 1999, "Fun", 1, 8)
    add_full_season(video_library, "Series_2", 2000, "Drama", 1, 3)
    add_full_season(video_library, "Series_3", 2000, "Action", 1, 4)

    generate_views_10_times(video_library)

    print("Wszystkie video w bibliotece:")
    for video in video_library:
        print(video)

    print(f"Najpopularniejsze filmy i seriale dnia {datetime.now().strftime('%d.%m.%Y')}")

    print("Top 3 Seriale w bibliotece:")
    for item in top_titles(video_library, amount=3, content_type="series"):
        print(f"{item} – {item.views} odtworzeń")

    print("Top 3 Filmy w bibliotece:")
    for item in top_titles(video_library, amount=3, content_type="movie"):
        print(f"{item} – {item.views} odtworzeń")
