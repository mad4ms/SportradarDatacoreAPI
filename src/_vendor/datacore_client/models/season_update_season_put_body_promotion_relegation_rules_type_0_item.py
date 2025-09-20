from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.season_update_season_put_body_promotion_relegation_rules_type_0_item_rule_type import (
    SeasonUpdateSeasonPutBodyPromotionRelegationRulesType0ItemRuleType,
)

T = TypeVar("T", bound="SeasonUpdateSeasonPutBodyPromotionRelegationRulesType0Item")


@_attrs_define
class SeasonUpdateSeasonPutBodyPromotionRelegationRulesType0Item:
    """
    Attributes:
        rule_type (SeasonUpdateSeasonPutBodyPromotionRelegationRulesType0ItemRuleType): Rule Type
        position (float): Standings Position
        value (str): Value to apply to Promotion or Relegation Example: DIV1.
    """

    rule_type: SeasonUpdateSeasonPutBodyPromotionRelegationRulesType0ItemRuleType
    position: float
    value: str

    def to_dict(self) -> dict[str, Any]:
        rule_type = self.rule_type.value

        position = self.position

        value = self.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "ruleType": rule_type,
                "position": position,
                "value": value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        rule_type = SeasonUpdateSeasonPutBodyPromotionRelegationRulesType0ItemRuleType(
            d.pop("ruleType")
        )

        position = d.pop("position")

        value = d.pop("value")

        season_update_season_put_body_promotion_relegation_rules_type_0_item = cls(
            rule_type=rule_type,
            position=position,
            value=value,
        )

        return season_update_season_put_body_promotion_relegation_rules_type_0_item
