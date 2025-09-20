from enum import Enum


class SeasonInsertSeasonPostBodyPromotionRelegationRulesType0ItemRuleType(str, Enum):
    PROMOTION = "PROMOTION"
    RELEGATION = "RELEGATION"

    def __str__(self) -> str:
        return str(self.value)
