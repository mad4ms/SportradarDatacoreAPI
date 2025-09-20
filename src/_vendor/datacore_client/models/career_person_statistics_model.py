from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.career_person_statistics_model_organization import CareerPersonStatisticsModelOrganization
    from ..models.career_person_statistics_model_person import CareerPersonStatisticsModelPerson
    from ..models.career_person_statistics_model_statistics import CareerPersonStatisticsModelStatistics


T = TypeVar("T", bound="CareerPersonStatisticsModel")


@_attrs_define
class CareerPersonStatisticsModel:
    """
    Attributes:
        person_id (Union[Unset, UUID]): The unique identifier of the person Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        person (Union[Unset, CareerPersonStatisticsModelPerson]): The person information
        organization_id (Union[Unset, str]): The unique identifier of the organization Example: 9.
        organization (Union[Unset, CareerPersonStatisticsModelOrganization]): The organization that this career person
            statistics belongs to
        statistics (Union[Unset, CareerPersonStatisticsModelStatistics]):
    """

    person_id: Union[Unset, UUID] = UNSET
    person: Union[Unset, "CareerPersonStatisticsModelPerson"] = UNSET
    organization_id: Union[Unset, str] = UNSET
    organization: Union[Unset, "CareerPersonStatisticsModelOrganization"] = UNSET
    statistics: Union[Unset, "CareerPersonStatisticsModelStatistics"] = UNSET

    def to_dict(self) -> dict[str, Any]:
        person_id: Union[Unset, str] = UNSET
        if not isinstance(self.person_id, Unset):
            person_id = str(self.person_id)

        person: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.person, Unset):
            person = self.person.to_dict()

        organization_id = self.organization_id

        organization: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.organization, Unset):
            organization = self.organization.to_dict()

        statistics: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.statistics, Unset):
            statistics = self.statistics.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if person_id is not UNSET:
            field_dict["personId"] = person_id
        if person is not UNSET:
            field_dict["person"] = person
        if organization_id is not UNSET:
            field_dict["organizationId"] = organization_id
        if organization is not UNSET:
            field_dict["organization"] = organization
        if statistics is not UNSET:
            field_dict["statistics"] = statistics

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.career_person_statistics_model_organization import CareerPersonStatisticsModelOrganization
        from ..models.career_person_statistics_model_person import CareerPersonStatisticsModelPerson
        from ..models.career_person_statistics_model_statistics import CareerPersonStatisticsModelStatistics

        d = dict(src_dict)
        _person_id = d.pop("personId", UNSET)
        person_id: Union[Unset, UUID]
        if isinstance(_person_id, Unset):
            person_id = UNSET
        else:
            person_id = UUID(_person_id)

        _person = d.pop("person", UNSET)
        person: Union[Unset, CareerPersonStatisticsModelPerson]
        if isinstance(_person, Unset):
            person = UNSET
        else:
            person = CareerPersonStatisticsModelPerson.from_dict(_person)

        organization_id = d.pop("organizationId", UNSET)

        _organization = d.pop("organization", UNSET)
        organization: Union[Unset, CareerPersonStatisticsModelOrganization]
        if isinstance(_organization, Unset):
            organization = UNSET
        else:
            organization = CareerPersonStatisticsModelOrganization.from_dict(_organization)

        _statistics = d.pop("statistics", UNSET)
        statistics: Union[Unset, CareerPersonStatisticsModelStatistics]
        if isinstance(_statistics, Unset):
            statistics = UNSET
        else:
            statistics = CareerPersonStatisticsModelStatistics.from_dict(_statistics)

        career_person_statistics_model = cls(
            person_id=person_id,
            person=person,
            organization_id=organization_id,
            organization=organization,
            statistics=statistics,
        )

        return career_person_statistics_model
