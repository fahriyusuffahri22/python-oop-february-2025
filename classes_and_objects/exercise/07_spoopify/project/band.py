from typing import List
from project.album import Album


class Band:
    def __init__(self, name: str):
        self.name = name
        self.albums: List[Album] = []

    def add_album(self, album: Album) -> str:
        if album not in self.albums:
            self.albums.append(album)
            return f"Band {self.name} has added their newest album {album.name}."

        return f"Band {self.name} already has {album.name} in their library."

    def remove_album(self, album_name: str) -> str:
        for i in range(len(self.albums)):
            if self.albums[i].name == album_name:
                if self.albums[i].published:
                    return "Album has been published. It cannot be removed."

                self.albums.pop(i)
                return f"Album {album_name} has been removed."

        return f"Album {album_name} is not found."

    def details(self):
        return "\n".join([
            f"Band {self.name}",
            *(x.details() for x in self.albums)
        ])