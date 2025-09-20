from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..models.career_person_representational_statistics_model_age_group import (
    CareerPersonRepresentationalStatisticsModelAgeGroup,
)
from ..models.career_person_representational_statistics_model_discipline_type_1 import (
    CareerPersonRepresentationalStatisticsModelDisciplineType1,
)
from ..models.career_person_representational_statistics_model_discipline_type_2_type_1 import (
    CareerPersonRepresentationalStatisticsModelDisciplineType2Type1,
)
from ..models.career_person_representational_statistics_model_discipline_type_3_type_1 import (
    CareerPersonRepresentationalStatisticsModelDisciplineType3Type1,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.career_person_representational_statistics_model_organization import (
        CareerPersonRepresentationalStatisticsModelOrganization,
    )
    from ..models.career_person_representational_statistics_model_person import (
        CareerPersonRepresentationalStatisticsModelPerson,
    )
    from ..models.career_person_representational_statistics_model_statistics import (
        CareerPersonRepresentationalStatisticsModelStatistics,
    )


T = TypeVar("T", bound="CareerPersonRepresentationalStatisticsModel")


@_attrs_define
class CareerPersonRepresentationalStatisticsModel:
    """
    Attributes:
        person_id (Union[Unset, UUID]): The unique identifier of the person Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        person (Union[Unset, CareerPersonRepresentationalStatisticsModelPerson]): The person information
        organization_id (Union[Unset, str]): The unique identifier of the organization Example: 9.
        organization (Union[Unset, CareerPersonRepresentationalStatisticsModelOrganization]): The organization that this
            career person representational_statistics belongs to
        age_group (Union[Unset, CareerPersonRepresentationalStatisticsModelAgeGroup]): The age group of the season
            >- `JUNIOR` Junior
            >- `MASTERS` Masters
            >- `SENIOR` Senior
            >- `UNDER_15` Under 15
            >- `UNDER_16` Under 16
            >- `UNDER_17` Under 17
            >- `UNDER_18` Under 18
            >- `UNDER_19` Under 19
            >- `UNDER_20` Under 20
            >- `UNDER_21` Under 21
            >- `UNDER_22` Under 22
            >- `UNDER_23` Under 23
            >- `YOUTH` Youth
             Example: SENIOR.
        discipline (Union[CareerPersonRepresentationalStatisticsModelDisciplineType1,
            CareerPersonRepresentationalStatisticsModelDisciplineType2Type1,
            CareerPersonRepresentationalStatisticsModelDisciplineType3Type1, None, Unset]): match discipline
            >- None None
            >- `INDOOR` Indoor
            >- `OUTDOOR` Outdoor
             Example: INDOOR.
        representing (Union[None, Unset, str]): Who the person or team was representing Example: AUSTRALIA.
        statistics (Union[Unset, CareerPersonRepresentationalStatisticsModelStatistics]):
    """

    person_id: Union[Unset, UUID] = UNSET
    person: Union[Unset, "CareerPersonRepresentationalStatisticsModelPerson"] = UNSET
    organization_id: Union[Unset, str] = UNSET
    organization: Union[Unset, "CareerPersonRepresentationalStatisticsModelOrganization"] = UNSET
    age_group: Union[Unset, CareerPersonRepresentationalStatisticsModelAgeGroup] = UNSET
    discipline: Union[
        CareerPersonRepresentationalStatisticsModelDisciplineType1,
        CareerPersonRepresentationalStatisticsModelDisciplineType2Type1,
        CareerPersonRepresentationalStatisticsModelDisciplineType3Type1,
        None,
        Unset,
    ] = UNSET
    representing: Union[None, Unset, str] = UNSET
    statistics: Union[Unset, "CareerPersonRepresentationalStatisticsModelStatistics"] = UNSET

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

        age_group: Union[Unset, str] = UNSET
        if not isinstance(self.age_group, Unset):
            age_group = self.age_group.value

        discipline: Union[None, Unset, str]
        if isinstance(self.discipline, Unset):
            discipline = UNSET
        elif isinstance(self.discipline, CareerPersonRepresentationalStatisticsModelDisciplineType1):
            discipline = self.discipline.value
        elif isinstance(self.discipline, CareerPersonRepresentationalStatisticsModelDisciplineType2Type1):
            discipline = self.discipline.value
        elif isinstance(self.discipline, CareerPersonRepresentationalStatisticsModelDisciplineType3Type1):
            discipline = self.discipline.value
        else:
            discipline = self.discipline

        representing: Union[None, Unset, str]
        if isinstance(self.representing, Unset):
            representing = UNSET
        else:
            representing = self.representing

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
        if age_group is not UNSET:
            field_dict["ageGroup"] = age_group
        if discipline is not UNSET:
            field_dict["discipline"] = discipline
        if representing is not UNSET:
            field_dict["representing"] = representing
        if statistics is not UNSET:
            field_dict["statistics"] = statistics

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.career_person_representational_statistics_model_organization import (
            CareerPersonRepresentationalStatisticsModelOrganization,
        )
        from ..models.career_person_representational_statistics_model_person import (
            CareerPersonRepresentationalStatisticsModelPerson,
        )
        from ..models.career_person_representational_statistics_model_statistics import (
            CareerPersonRepresentationalStatisticsModelStatistics,
        )

        d = dict(src_dict)
        _person_id = d.pop("personId", UNSET)
        person_id: Union[Unset, UUID]
        if isinstance(_person_id, Unset):
            person_id = UNSET
        else:
            person_id = UUID(_person_id)

        _person = d.pop("person", UNSET)
        person: Union[Unset, CareerPersonRepresentationalStatisticsModelPerson]
        if isinstance(_person, Unset):
            person = UNSET
        else:
            person = CareerPersonRepresentationalStatisticsModelPerson.from_dict(_person)

        organization_id = d.pop("organizationId", UNSET)

        _organization = d.pop("organization", UNSET)
        organization: Union[Unset, CareerPersonRepresentationalStatisticsModelOrganization]
        if isinstance(_organization, Unset):
            organization = UNSET
        else:
            organization = CareerPersonRepresentationalStatisticsModelOrganization.from_dict(_organization)

        _age_group = d.pop("ageGroup", UNSET)
        age_group: Union[Unset, CareerPersonRepresentationalStatisticsModelAgeGroup]
        if isinstance(_age_group, Unset):
            age_group = UNSET
        else:
            age_group = CareerPersonRepresentationalStatisticsModelAgeGroup(_age_group)

        def _parse_discipline(
            data: object,
        ) -> Union[
            CareerPersonRepresentationalStatisticsModelDisciplineType1,
            CareerPersonRepresentationalStatisticsModelDisciplineType2Type1,
            CareerPersonRepresentationalStatisticsModelDisciplineType3Type1,
            None,
            Unset,
        ]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                discipline_type_1 = CareerPersonRepresentationalStatisticsModelDisciplineType1(data)

                return discipline_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                discipline_type_2_type_1 = CareerPersonRepresentationalStatisticsModelDisciplineType2Type1(data)

                return discipline_type_2_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                discipline_type_3_type_1 = CareerPersonRepresentationalStatisticsModelDisciplineType3Type1(data)

                return discipline_type_3_type_1
            except:  # noqa: E722
                pass
            return cast(
                Union[
                    CareerPersonRepresentationalStatisticsModelDisciplineType1,
                    CareerPersonRepresentationalStatisticsModelDisciplineType2Type1,
                    CareerPersonRepresentationalStatisticsModelDisciplineType3Type1,
                    None,
                    Unset,
                ],
                data,
            )

        discipline = _parse_discipline(d.pop("discipline", UNSET))

        def _parse_representing(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        representing = _parse_representing(d.pop("representing", UNSET))

        _statistics = d.pop("statistics", UNSET)
        statistics: Union[Unset, CareerPersonRepresentationalStatisticsModelStatistics]
        if isinstance(_statistics, Unset):
            statistics = UNSET
        else:
            statistics = CareerPersonRepresentationalStatisticsModelStatistics.from_dict(_statistics)

        career_person_representational_statistics_model = cls(
            person_id=person_id,
            person=person,
            organization_id=organization_id,
            organization=organization,
            age_group=age_group,
            discipline=discipline,
            representing=representing,
            statistics=statistics,
        )

        return career_person_representational_statistics_model
