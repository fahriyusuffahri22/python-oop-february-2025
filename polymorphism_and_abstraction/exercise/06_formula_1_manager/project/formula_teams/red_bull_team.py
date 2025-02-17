from typing import Tuple, Dict

from project.formula_teams.formula_team import FormulaTeam


class RedBullTeam(FormulaTeam):
    @property
    def _expenses(self) -> int:
        return -250000

    @property
    def _sponsors(self) -> Tuple[Dict[int, int], ...]:
        return (
            {
                1: 1500000,
                2: 800000
            },
            {
                8: 20000,
                10: 10000
            }
        )