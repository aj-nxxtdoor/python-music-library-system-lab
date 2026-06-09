#!/usr/bin/env python3

class classproperty:
    """Descriptor to allow class-level properties."""
    def __init__(self, func):
        self.func = func
    def __get__(self, obj, owner):
        return self.func(owner)

class Song:
    """Represents a song in a music library system."""

    count = 0
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        """Initialize a Song with a name, artist, and genre."""
        self.name = name
        self.artist = artist
        self.genre = genre

        Song.count += 1

        if genre in Song.genre_count:
            Song.genre_count[genre] += 1
        else:
            Song.genre_count[genre] = 1

        if artist in Song.artist_count:
            Song.artist_count[artist] += 1
        else:
            Song.artist_count[artist] = 1

    @classproperty
    def genres(cls):
        """Return a list of all unique genres."""
        return list(cls.genre_count.keys())

    @classproperty
    def artists(cls):
        """Return a list of all unique artists."""
        return list(cls.artist_count.keys())
