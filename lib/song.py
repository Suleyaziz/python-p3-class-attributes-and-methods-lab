#!/usr/bin/env python3

class Song:
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}
    
    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        
        # Update all class attributes
        self.__class__.count += 1
        self.__class__.add_to_genre(genre)
        self.__class__.add_to_artist(artist)
        self.__class__.add_to_genre_count(genre)
        self.__class__.add_to_artist_count(artist)
    
    @classmethod
    def add_to_genre(cls, genre):
        if genre not in cls.genres:
            cls.genres.append(genre)
    
    @classmethod
    def add_to_artist(cls, artist):
        if artist not in cls.artists:
            cls.artists.append(artist)
    
    @classmethod
    def add_to_genre_count(cls, genre):
        cls.genre_count[genre] = cls.genre_count.get(genre, 0) + 1
    
    @classmethod
    def add_to_artist_count(cls, artist):
        cls.artist_count[artist] = cls.artist_count.get(artist, 0) + 1