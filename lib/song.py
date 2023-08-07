class Song:
    
    song_catalog = []
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}
    
    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        self.add_to_catalog(self)
        self.add_to_genres(genre)
        self.add_song_to_count()
        self.add_to_artists(artist)
        self.count_song_genres(self)
        self.count_song_artists(self)

    @classmethod
    def add_song_to_count(cls, increment=1):
        cls.count += increment

    @classmethod
    def add_to_genres(cls, genre):
        if (genre not in cls.genres):
            cls.genres.append(genre)
        else:
            print(f'{genre} has already been added to the list of genres.')
    
    @classmethod
    def add_to_artists(cls, artist):
        if (artist not in cls.artists):
            cls.artists.append(artist)
        else:
            print(f'{artist} has already been added to the list of artists.')
    
    @classmethod
    def add_to_catalog(cls, song):
        cls.song_catalog.append(song)
    
    @classmethod
    def count_song_genres(cls, song):
        for genre in cls.genres:
            current_genre_count = 0
            for song in cls.song_catalog:
                if (genre == song.genre):
                    current_genre_count +=1
            update_val = {genre : current_genre_count}
            cls.genre_count.update(update_val)

    @classmethod
    def count_song_artists(cls, song):
        for artist in cls.artists:
            current_artist_count = 0
            for song in cls.song_catalog:
                if (artist == song.artist):
                    current_artist_count +=1
            update_val = {artist : current_artist_count}
            cls.artist_count.update(update_val)