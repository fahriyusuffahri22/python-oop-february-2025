from __future__ import annotations
from typing import List
from math import ceil

class PhotoAlbum:
    PAGE_CAPACITY_DEFAULT: int = 4
    PAGE_SEPARATION: str = "-" * 11

    def __init__(self, pages: int):
        self.pages = pages
        self.photos: List[List[str]] = [[] for _ in range(pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int) -> PhotoAlbum:
        return cls(ceil(photos_count / cls.PAGE_CAPACITY_DEFAULT))

    def add_photo(self, label: str) -> str:
        for i in range(self.pages):
            if len(self.photos[i]) < PhotoAlbum.PAGE_CAPACITY_DEFAULT:
                self.photos[i].append(label)
                return f"{label} photo added successfully on page {i + 1} slot {len(self.photos[i])}"

        return "No more free slots"

    def display(self) -> str:
        return "\n".join([
            PhotoAlbum.PAGE_SEPARATION,
            *(f"{' '.join('[]' for _ in range(len(x)))}\n{PhotoAlbum.PAGE_SEPARATION}" for x in self.photos)
        ])