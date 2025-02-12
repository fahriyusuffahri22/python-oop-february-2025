from typing import List
from project.pokemon import Pokemon


class Trainer:
    def __init__(self, name: str):
        self.name = name
        self.pokemons: List[Pokemon] = []

    def add_pokemon(self, pokemon: Pokemon) -> str:
        if pokemon not in self.pokemons:
            self.pokemons.append(pokemon)
            return f"Caught {pokemon.pokemon_details()}"

        return "This pokemon is already caught"

    def release_pokemon(self, pokemon_name: str) -> str:
        for i in range(len(self.pokemons)):
            if self.pokemons[i].name == pokemon_name:
                return f"You have released {self.pokemons.pop(i).name}"

        return "Pokemon is not caught"

    def trainer_data(self) -> str:
        return "\n".join([
            f"Pokemon Trainer {self.name}",
            f"Pokemon count {len(self.pokemons)}",
            *(f"- {x.pokemon_details()}" for x in self.pokemons)
        ])