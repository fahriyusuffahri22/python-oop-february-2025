from project.formula_teams.formula_team import FormulaTeam
from typing import Tuple, Dict


class MercedesTeam(FormulaTeam):
    @property
    def _expenses(self) -> int:
        return -200000

    @property
    def _sponsors(self) -> Tuple[Dict[int, int], ...]:
        return (
            {
                1: 1000000,
                3: 500000
            },
            {
                5: 100000,
                7: 50000
            }
        )