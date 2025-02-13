from typing import List
from project.player import Player


class Guild:
    def __init__(self, name: str):
        self.name = name
        self.players: List[Player] = []


    def assign_player(self, player: Player) -> str:
        if player.guild == Player.DEFAULT_GUILD:
            self.players.append(player)
            player.guild = self.name
            return f"Welcome player {player.name} to the guild {self.name}"

        if player.guild == self.name:
            return f"Player {player.name} is already in the guild."

        return f"Player {player.name} is in another guild."

    def kick_player(self, player_name: str) -> str:
        for i in range(len(self.players)):
            if self.players[i].name == player_name:
                self.players[i].guild = Player.DEFAULT_GUILD
                self.players.pop(i)
                return f"Player {player_name} has been removed from the guild."

        return f"Player {player_name} is not in the guild."

    def guild_info(self) -> str:
        return  "\n".join([
            f"Guild: {self.name}",
            *(x.player_info() for x in self.players)
        ])