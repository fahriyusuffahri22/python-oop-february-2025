from typing import List
from project.song import Song

class Album:
    def __init__(self, name: str, *songs: Song):
        self.name = name
        self.published: bool = False
        self.songs: List[Song] = list(songs)

    def add_song(self, song: Song) -> str:
        if song.single:
            return f"Cannot add {song.name}. It's a single"

        if self.published:
            return f"Cannot add songs. Album is published."

        if song not in self.songs:
            self.songs.append(song)
            return f"Song {song.name} has been added to the album {self.name}."

        return "Song is already in the album."

    def remove_song(self, song_name: str) -> str:
        if self.published:
            return "Cannot remove songs. Album is published."

        for i in range(len(self.songs)):
            if self.songs[i].name == song_name:
                self.songs.pop(i)
                return f"Removed song {song_name} from album {self.name}."

        return "Song is not in the album."

    def publish(self) -> str:
        if not self.published:
            self.published = True
            return f"Album {self.name} has been published."

        return "Album {name} is already published."

    def details(self) -> str:
        return  "\n".join([
            f"Album {self.name}",
            *(f'== {x.get_info()}' for x in self.songs)
        ])