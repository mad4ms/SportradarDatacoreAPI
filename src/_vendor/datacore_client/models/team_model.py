import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.team_model_age_group_type_1 import TeamModelAgeGroupType1
from ..models.team_model_age_group_type_2_type_1 import TeamModelAgeGroupType2Type1
from ..models.team_model_age_group_type_3_type_1 import TeamModelAgeGroupType3Type1
from ..models.team_model_discipline_type_1 import TeamModelDisciplineType1
from ..models.team_model_discipline_type_2_type_1 import TeamModelDisciplineType2Type1
from ..models.team_model_discipline_type_3_type_1 import TeamModelDisciplineType3Type1
from ..models.team_model_gender_type_1 import TeamModelGenderType1
from ..models.team_model_gender_type_2_type_1 import TeamModelGenderType2Type1
from ..models.team_model_gender_type_3_type_1 import TeamModelGenderType3Type1
from ..models.team_model_standard_type_1 import TeamModelStandardType1
from ..models.team_model_standard_type_2_type_1 import TeamModelStandardType2Type1
from ..models.team_model_standard_type_3_type_1 import TeamModelStandardType3Type1
from ..models.team_model_status import TeamModelStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.images_model import ImagesModel
    from ..models.team_model_additional_names import TeamModelAdditionalNames
    from ..models.team_model_colors import TeamModelColors
    from ..models.team_model_contact_details import TeamModelContactDetails
    from ..models.team_model_entity_additional_details import TeamModelEntityAdditionalDetails
    from ..models.team_model_entity_group import TeamModelEntityGroup
    from ..models.team_model_organization import TeamModelOrganization
    from ..models.team_model_social_media import TeamModelSocialMedia
    from ..models.team_model_team_address import TeamModelTeamAddress
    from ..models.team_model_team_historical_name import TeamModelTeamHistoricalName


T = TypeVar("T", bound="TeamModel")


@_attrs_define
class TeamModel:
    """
    Attributes:
        entity_id (Union[Unset, UUID]): The unique identifier of the team Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        organization_id (Union[Unset, str]): The unique identifier of the organization Example: 9.
        organization (Union[Unset, TeamModelOrganization]): The organization that this team belongs to
        entity_group_id (Union[None, UUID, Unset]): The club that this team belongs to Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        entity_group (Union[Unset, TeamModelEntityGroup]): The club that this team belongs to
        international_reference (Union[None, Unset, str]): The international reference for this team given by the sport
            governing body Example: CA3243-3.
        status (Union[Unset, TeamModelStatus]): Status
            >- `ACTIVE` Active
            >- `INACTIVE` Inactive
            >- `PENDING` Pending
             Example: ACTIVE.
        name_full_local (Union[Unset, str]): The full name of the team in the [local](#section/Introduction/Character-
            Sets-and-Names) language Example: Los Angeles Armadillos.
        additional_names (Union[Unset, TeamModelAdditionalNames]):
        name_full_latin (Union[None, Unset, str]): The full name of the team in [latin](#section/Introduction/Character-
            Sets-and-Names) characters Example: Los Angeles Armadillos.
        code_local (Union[None, Unset, str]): The code of the team in the [local](#section/Introduction/Character-Sets-
            and-Names) language Example: TEST.
        code_latin (Union[None, Unset, str]): The code of the team in [latin](#section/Introduction/Character-Sets-and-
            Names) characters Example: TEST.
        address (Union['TeamModelTeamAddress', None, Unset]): Street Address for the team
        social (Union['TeamModelSocialMedia', None, Unset]): Social Media contacts
        contacts (Union['TeamModelContactDetails', None, Unset]): Public contact fields
        details (Union['TeamModelEntityAdditionalDetails', None, Unset]): Additional detail fields
        colors (Union[Unset, TeamModelColors]):
        historical_names (Union[None, Unset, list['TeamModelTeamHistoricalName']]): Array of team historical names
        external_id (Union[None, Unset, str]): The Id of the data as set by the provider of the data Example: A123.
        age_group (Union[None, TeamModelAgeGroupType1, TeamModelAgeGroupType2Type1, TeamModelAgeGroupType3Type1,
            Unset]): The age group of the team
            >- None None
            >- `JUNIOR` Junior
            >- `MASTERS` Masters
            >- `SENIOR` Senior
            >- `UNDER_10` Under 10
            >- `UNDER_11` Under 11
            >- `UNDER_12` Under 12
            >- `UNDER_13` Under 13
            >- `UNDER_14` Under 14
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
        gender (Union[None, TeamModelGenderType1, TeamModelGenderType2Type1, TeamModelGenderType3Type1, Unset]): The
            gender of the participants in the team
            >- None None
            >- `FEMALE` Female
            >- `MALE` Male
            >- `MIXED` Mixed
            >- `UNKNOWN` Unknown
             Example: MALE.
        standard (Union[None, TeamModelStandardType1, TeamModelStandardType2Type1, TeamModelStandardType3Type1, Unset]):
            The playing standard of the team
            >- None None
            >- `ELITE` Professional/elite organisation
            >- `FRIENDLY` International Friendly
            >- `GRASS_ROOT` Normal
            >- `INTERNATIONAL` International
            >- `NONCONTINENTAL_CHAMPIONSHIP` Non-continental Championship
            >- `OLYMPIC` Olympics
            >- `REGION` Regional
            >- `TIER2` lesser standard than elite
            >- `TIER3` lesser standard than tier 2
            >- `WORLD_CHAMPIONSHIP` World Championship
            >- `ZONE_CHAMPIONSHIP` International Zone Championship
             Example: ELITE.
        grade (Union[None, Unset, str]): The playing grade of the matches for this team Example: A.
        representing (Union[None, Unset, str]): Who the team was representing Example: AUSTRALIA.
        discipline (Union[None, TeamModelDisciplineType1, TeamModelDisciplineType2Type1, TeamModelDisciplineType3Type1,
            Unset]): Discipline' the team participates in
            >- None None
            >- `INDOOR` Indoor
            >- `OUTDOOR` Outdoor
             Example: INDOOR.
        updated (Union[Unset, datetime.datetime]): Date/time last modified. In UTC
        added (Union[Unset, datetime.datetime]): Date/time added. In UTC
        default_venue_id (Union[None, UUID, Unset]): The unique identifier of the default venue Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        alternate_venue_ids (Union[Unset, list[UUID]]):
        images (Union[Unset, list['ImagesModel']]):
    """

    entity_id: Union[Unset, UUID] = UNSET
    organization_id: Union[Unset, str] = UNSET
    organization: Union[Unset, "TeamModelOrganization"] = UNSET
    entity_group_id: Union[None, UUID, Unset] = UNSET
    entity_group: Union[Unset, "TeamModelEntityGroup"] = UNSET
    international_reference: Union[None, Unset, str] = UNSET
    status: Union[Unset, TeamModelStatus] = UNSET
    name_full_local: Union[Unset, str] = UNSET
    additional_names: Union[Unset, "TeamModelAdditionalNames"] = UNSET
    name_full_latin: Union[None, Unset, str] = UNSET
    code_local: Union[None, Unset, str] = UNSET
    code_latin: Union[None, Unset, str] = UNSET
    address: Union["TeamModelTeamAddress", None, Unset] = UNSET
    social: Union["TeamModelSocialMedia", None, Unset] = UNSET
    contacts: Union["TeamModelContactDetails", None, Unset] = UNSET
    details: Union["TeamModelEntityAdditionalDetails", None, Unset] = UNSET
    colors: Union[Unset, "TeamModelColors"] = UNSET
    historical_names: Union[None, Unset, list["TeamModelTeamHistoricalName"]] = UNSET
    external_id: Union[None, Unset, str] = UNSET
    age_group: Union[None, TeamModelAgeGroupType1, TeamModelAgeGroupType2Type1, TeamModelAgeGroupType3Type1, Unset] = (
        UNSET
    )
    gender: Union[None, TeamModelGenderType1, TeamModelGenderType2Type1, TeamModelGenderType3Type1, Unset] = UNSET
    standard: Union[None, TeamModelStandardType1, TeamModelStandardType2Type1, TeamModelStandardType3Type1, Unset] = (
        UNSET
    )
    grade: Union[None, Unset, str] = UNSET
    representing: Union[None, Unset, str] = UNSET
    discipline: Union[
        None, TeamModelDisciplineType1, TeamModelDisciplineType2Type1, TeamModelDisciplineType3Type1, Unset
    ] = UNSET
    updated: Union[Unset, datetime.datetime] = UNSET
    added: Union[Unset, datetime.datetime] = UNSET
    default_venue_id: Union[None, UUID, Unset] = UNSET
    alternate_venue_ids: Union[Unset, list[UUID]] = UNSET
    images: Union[Unset, list["ImagesModel"]] = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.team_model_contact_details import TeamModelContactDetails
        from ..models.team_model_entity_additional_details import TeamModelEntityAdditionalDetails
        from ..models.team_model_social_media import TeamModelSocialMedia
        from ..models.team_model_team_address import TeamModelTeamAddress

        entity_id: Union[Unset, str] = UNSET
        if not isinstance(self.entity_id, Unset):
            entity_id = str(self.entity_id)

        organization_id = self.organization_id

        organization: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.organization, Unset):
            organization = self.organization.to_dict()

        entity_group_id: Union[None, Unset, str]
        if isinstance(self.entity_group_id, Unset):
            entity_group_id = UNSET
        elif isinstance(self.entity_group_id, UUID):
            entity_group_id = str(self.entity_group_id)
        else:
            entity_group_id = self.entity_group_id

        entity_group: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.entity_group, Unset):
            entity_group = self.entity_group.to_dict()

        international_reference: Union[None, Unset, str]
        if isinstance(self.international_reference, Unset):
            international_reference = UNSET
        else:
            international_reference = self.international_reference

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        name_full_local = self.name_full_local

        additional_names: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.additional_names, Unset):
            additional_names = self.additional_names.to_dict()

        name_full_latin: Union[None, Unset, str]
        if isinstance(self.name_full_latin, Unset):
            name_full_latin = UNSET
        else:
            name_full_latin = self.name_full_latin

        code_local: Union[None, Unset, str]
        if isinstance(self.code_local, Unset):
            code_local = UNSET
        else:
            code_local = self.code_local

        code_latin: Union[None, Unset, str]
        if isinstance(self.code_latin, Unset):
            code_latin = UNSET
        else:
            code_latin = self.code_latin

        address: Union[None, Unset, dict[str, Any]]
        if isinstance(self.address, Unset):
            address = UNSET
        elif isinstance(self.address, TeamModelTeamAddress):
            address = self.address.to_dict()
        else:
            address = self.address

        social: Union[None, Unset, dict[str, Any]]
        if isinstance(self.social, Unset):
            social = UNSET
        elif isinstance(self.social, TeamModelSocialMedia):
            social = self.social.to_dict()
        else:
            social = self.social

        contacts: Union[None, Unset, dict[str, Any]]
        if isinstance(self.contacts, Unset):
            contacts = UNSET
        elif isinstance(self.contacts, TeamModelContactDetails):
            contacts = self.contacts.to_dict()
        else:
            contacts = self.contacts

        details: Union[None, Unset, dict[str, Any]]
        if isinstance(self.details, Unset):
            details = UNSET
        elif isinstance(self.details, TeamModelEntityAdditionalDetails):
            details = self.details.to_dict()
        else:
            details = self.details

        colors: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.colors, Unset):
            colors = self.colors.to_dict()

        historical_names: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.historical_names, Unset):
            historical_names = UNSET
        elif isinstance(self.historical_names, list):
            historical_names = []
            for historical_names_type_0_item_data in self.historical_names:
                historical_names_type_0_item = historical_names_type_0_item_data.to_dict()
                historical_names.append(historical_names_type_0_item)

        else:
            historical_names = self.historical_names

        external_id: Union[None, Unset, str]
        if isinstance(self.external_id, Unset):
            external_id = UNSET
        else:
            external_id = self.external_id

        age_group: Union[None, Unset, str]
        if isinstance(self.age_group, Unset):
            age_group = UNSET
        elif isinstance(self.age_group, TeamModelAgeGroupType1):
            age_group = self.age_group.value
        elif isinstance(self.age_group, TeamModelAgeGroupType2Type1):
            age_group = self.age_group.value
        elif isinstance(self.age_group, TeamModelAgeGroupType3Type1):
            age_group = self.age_group.value
        else:
            age_group = self.age_group

        gender: Union[None, Unset, str]
        if isinstance(self.gender, Unset):
            gender = UNSET
        elif isinstance(self.gender, TeamModelGenderType1):
            gender = self.gender.value
        elif isinstance(self.gender, TeamModelGenderType2Type1):
            gender = self.gender.value
        elif isinstance(self.gender, TeamModelGenderType3Type1):
            gender = self.gender.value
        else:
            gender = self.gender

        standard: Union[None, Unset, str]
        if isinstance(self.standard, Unset):
            standard = UNSET
        elif isinstance(self.standard, TeamModelStandardType1):
            standard = self.standard.value
        elif isinstance(self.standard, TeamModelStandardType2Type1):
            standard = self.standard.value
        elif isinstance(self.standard, TeamModelStandardType3Type1):
            standard = self.standard.value
        else:
            standard = self.standard

        grade: Union[None, Unset, str]
        if isinstance(self.grade, Unset):
            grade = UNSET
        else:
            grade = self.grade

        representing: Union[None, Unset, str]
        if isinstance(self.representing, Unset):
            representing = UNSET
        else:
            representing = self.representing

        discipline: Union[None, Unset, str]
        if isinstance(self.discipline, Unset):
            discipline = UNSET
        elif isinstance(self.discipline, TeamModelDisciplineType1):
            discipline = self.discipline.value
        elif isinstance(self.discipline, TeamModelDisciplineType2Type1):
            discipline = self.discipline.value
        elif isinstance(self.discipline, TeamModelDisciplineType3Type1):
            discipline = self.discipline.value
        else:
            discipline = self.discipline

        updated: Union[Unset, str] = UNSET
        if not isinstance(self.updated, Unset):
            updated = self.updated.isoformat()

        added: Union[Unset, str] = UNSET
        if not isinstance(self.added, Unset):
            added = self.added.isoformat()

        default_venue_id: Union[None, Unset, str]
        if isinstance(self.default_venue_id, Unset):
            default_venue_id = UNSET
        elif isinstance(self.default_venue_id, UUID):
            default_venue_id = str(self.default_venue_id)
        else:
            default_venue_id = self.default_venue_id

        alternate_venue_ids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.alternate_venue_ids, Unset):
            alternate_venue_ids = []
            for alternate_venue_ids_item_data in self.alternate_venue_ids:
                alternate_venue_ids_item = str(alternate_venue_ids_item_data)
                alternate_venue_ids.append(alternate_venue_ids_item)

        images: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.images, Unset):
            images = []
            for images_item_data in self.images:
                images_item = images_item_data.to_dict()
                images.append(images_item)

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if entity_id is not UNSET:
            field_dict["entityId"] = entity_id
        if organization_id is not UNSET:
            field_dict["organizationId"] = organization_id
        if organization is not UNSET:
            field_dict["organization"] = organization
        if entity_group_id is not UNSET:
            field_dict["entityGroupId"] = entity_group_id
        if entity_group is not UNSET:
            field_dict["entityGroup"] = entity_group
        if international_reference is not UNSET:
            field_dict["internationalReference"] = international_reference
        if status is not UNSET:
            field_dict["status"] = status
        if name_full_local is not UNSET:
            field_dict["nameFullLocal"] = name_full_local
        if additional_names is not UNSET:
            field_dict["additionalNames"] = additional_names
        if name_full_latin is not UNSET:
            field_dict["nameFullLatin"] = name_full_latin
        if code_local is not UNSET:
            field_dict["codeLocal"] = code_local
        if code_latin is not UNSET:
            field_dict["codeLatin"] = code_latin
        if address is not UNSET:
            field_dict["address"] = address
        if social is not UNSET:
            field_dict["social"] = social
        if contacts is not UNSET:
            field_dict["contacts"] = contacts
        if details is not UNSET:
            field_dict["details"] = details
        if colors is not UNSET:
            field_dict["colors"] = colors
        if historical_names is not UNSET:
            field_dict["historicalNames"] = historical_names
        if external_id is not UNSET:
            field_dict["externalId"] = external_id
        if age_group is not UNSET:
            field_dict["ageGroup"] = age_group
        if gender is not UNSET:
            field_dict["gender"] = gender
        if standard is not UNSET:
            field_dict["standard"] = standard
        if grade is not UNSET:
            field_dict["grade"] = grade
        if representing is not UNSET:
            field_dict["representing"] = representing
        if discipline is not UNSET:
            field_dict["discipline"] = discipline
        if updated is not UNSET:
            field_dict["updated"] = updated
        if added is not UNSET:
            field_dict["added"] = added
        if default_venue_id is not UNSET:
            field_dict["defaultVenueId"] = default_venue_id
        if alternate_venue_ids is not UNSET:
            field_dict["alternateVenueIds"] = alternate_venue_ids
        if images is not UNSET:
            field_dict["images"] = images

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.images_model import ImagesModel
        from ..models.team_model_additional_names import TeamModelAdditionalNames
        from ..models.team_model_colors import TeamModelColors
        from ..models.team_model_contact_details import TeamModelContactDetails
        from ..models.team_model_entity_additional_details import TeamModelEntityAdditionalDetails
        from ..models.team_model_entity_group import TeamModelEntityGroup
        from ..models.team_model_organization import TeamModelOrganization
        from ..models.team_model_social_media import TeamModelSocialMedia
        from ..models.team_model_team_address import TeamModelTeamAddress
        from ..models.team_model_team_historical_name import TeamModelTeamHistoricalName

        d = dict(src_dict)
        _entity_id = d.pop("entityId", UNSET)
        entity_id: Union[Unset, UUID]
        if isinstance(_entity_id, Unset):
            entity_id = UNSET
        else:
            entity_id = UUID(_entity_id)

        organization_id = d.pop("organizationId", UNSET)

        _organization = d.pop("organization", UNSET)
        organization: Union[Unset, TeamModelOrganization]
        if isinstance(_organization, Unset):
            organization = UNSET
        else:
            organization = TeamModelOrganization.from_dict(_organization)

        def _parse_entity_group_id(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                entity_group_id_type_0 = UUID(data)

                return entity_group_id_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        entity_group_id = _parse_entity_group_id(d.pop("entityGroupId", UNSET))

        _entity_group = d.pop("entityGroup", UNSET)
        entity_group: Union[Unset, TeamModelEntityGroup]
        if isinstance(_entity_group, Unset):
            entity_group = UNSET
        else:
            entity_group = TeamModelEntityGroup.from_dict(_entity_group)

        def _parse_international_reference(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        international_reference = _parse_international_reference(d.pop("internationalReference", UNSET))

        _status = d.pop("status", UNSET)
        status: Union[Unset, TeamModelStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = TeamModelStatus(_status)

        name_full_local = d.pop("nameFullLocal", UNSET)

        _additional_names = d.pop("additionalNames", UNSET)
        additional_names: Union[Unset, TeamModelAdditionalNames]
        if isinstance(_additional_names, Unset):
            additional_names = UNSET
        else:
            additional_names = TeamModelAdditionalNames.from_dict(_additional_names)

        def _parse_name_full_latin(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name_full_latin = _parse_name_full_latin(d.pop("nameFullLatin", UNSET))

        def _parse_code_local(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        code_local = _parse_code_local(d.pop("codeLocal", UNSET))

        def _parse_code_latin(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        code_latin = _parse_code_latin(d.pop("codeLatin", UNSET))

        def _parse_address(data: object) -> Union["TeamModelTeamAddress", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                address_type_0 = TeamModelTeamAddress.from_dict(data)

                return address_type_0
            except:  # noqa: E722
                pass
            return cast(Union["TeamModelTeamAddress", None, Unset], data)

        address = _parse_address(d.pop("address", UNSET))

        def _parse_social(data: object) -> Union["TeamModelSocialMedia", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                social_type_0 = TeamModelSocialMedia.from_dict(data)

                return social_type_0
            except:  # noqa: E722
                pass
            return cast(Union["TeamModelSocialMedia", None, Unset], data)

        social = _parse_social(d.pop("social", UNSET))

        def _parse_contacts(data: object) -> Union["TeamModelContactDetails", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                contacts_type_0 = TeamModelContactDetails.from_dict(data)

                return contacts_type_0
            except:  # noqa: E722
                pass
            return cast(Union["TeamModelContactDetails", None, Unset], data)

        contacts = _parse_contacts(d.pop("contacts", UNSET))

        def _parse_details(data: object) -> Union["TeamModelEntityAdditionalDetails", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                details_type_0 = TeamModelEntityAdditionalDetails.from_dict(data)

                return details_type_0
            except:  # noqa: E722
                pass
            return cast(Union["TeamModelEntityAdditionalDetails", None, Unset], data)

        details = _parse_details(d.pop("details", UNSET))

        _colors = d.pop("colors", UNSET)
        colors: Union[Unset, TeamModelColors]
        if isinstance(_colors, Unset):
            colors = UNSET
        else:
            colors = TeamModelColors.from_dict(_colors)

        def _parse_historical_names(data: object) -> Union[None, Unset, list["TeamModelTeamHistoricalName"]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                historical_names_type_0 = []
                _historical_names_type_0 = data
                for historical_names_type_0_item_data in _historical_names_type_0:
                    historical_names_type_0_item = TeamModelTeamHistoricalName.from_dict(
                        historical_names_type_0_item_data
                    )

                    historical_names_type_0.append(historical_names_type_0_item)

                return historical_names_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["TeamModelTeamHistoricalName"]], data)

        historical_names = _parse_historical_names(d.pop("historicalNames", UNSET))

        def _parse_external_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        external_id = _parse_external_id(d.pop("externalId", UNSET))

        def _parse_age_group(
            data: object,
        ) -> Union[None, TeamModelAgeGroupType1, TeamModelAgeGroupType2Type1, TeamModelAgeGroupType3Type1, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                age_group_type_1 = TeamModelAgeGroupType1(data)

                return age_group_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                age_group_type_2_type_1 = TeamModelAgeGroupType2Type1(data)

                return age_group_type_2_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                age_group_type_3_type_1 = TeamModelAgeGroupType3Type1(data)

                return age_group_type_3_type_1
            except:  # noqa: E722
                pass
            return cast(
                Union[None, TeamModelAgeGroupType1, TeamModelAgeGroupType2Type1, TeamModelAgeGroupType3Type1, Unset],
                data,
            )

        age_group = _parse_age_group(d.pop("ageGroup", UNSET))

        def _parse_gender(
            data: object,
        ) -> Union[None, TeamModelGenderType1, TeamModelGenderType2Type1, TeamModelGenderType3Type1, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                gender_type_1 = TeamModelGenderType1(data)

                return gender_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                gender_type_2_type_1 = TeamModelGenderType2Type1(data)

                return gender_type_2_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                gender_type_3_type_1 = TeamModelGenderType3Type1(data)

                return gender_type_3_type_1
            except:  # noqa: E722
                pass
            return cast(
                Union[None, TeamModelGenderType1, TeamModelGenderType2Type1, TeamModelGenderType3Type1, Unset], data
            )

        gender = _parse_gender(d.pop("gender", UNSET))

        def _parse_standard(
            data: object,
        ) -> Union[None, TeamModelStandardType1, TeamModelStandardType2Type1, TeamModelStandardType3Type1, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                standard_type_1 = TeamModelStandardType1(data)

                return standard_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                standard_type_2_type_1 = TeamModelStandardType2Type1(data)

                return standard_type_2_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                standard_type_3_type_1 = TeamModelStandardType3Type1(data)

                return standard_type_3_type_1
            except:  # noqa: E722
                pass
            return cast(
                Union[None, TeamModelStandardType1, TeamModelStandardType2Type1, TeamModelStandardType3Type1, Unset],
                data,
            )

        standard = _parse_standard(d.pop("standard", UNSET))

        def _parse_grade(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        grade = _parse_grade(d.pop("grade", UNSET))

        def _parse_representing(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        representing = _parse_representing(d.pop("representing", UNSET))

        def _parse_discipline(
            data: object,
        ) -> Union[None, TeamModelDisciplineType1, TeamModelDisciplineType2Type1, TeamModelDisciplineType3Type1, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                discipline_type_1 = TeamModelDisciplineType1(data)

                return discipline_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                discipline_type_2_type_1 = TeamModelDisciplineType2Type1(data)

                return discipline_type_2_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                discipline_type_3_type_1 = TeamModelDisciplineType3Type1(data)

                return discipline_type_3_type_1
            except:  # noqa: E722
                pass
            return cast(
                Union[
                    None, TeamModelDisciplineType1, TeamModelDisciplineType2Type1, TeamModelDisciplineType3Type1, Unset
                ],
                data,
            )

        discipline = _parse_discipline(d.pop("discipline", UNSET))

        _updated = d.pop("updated", UNSET)
        updated: Union[Unset, datetime.datetime]
        if isinstance(_updated, Unset):
            updated = UNSET
        else:
            updated = isoparse(_updated)

        _added = d.pop("added", UNSET)
        added: Union[Unset, datetime.datetime]
        if isinstance(_added, Unset):
            added = UNSET
        else:
            added = isoparse(_added)

        def _parse_default_venue_id(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                default_venue_id_type_0 = UUID(data)

                return default_venue_id_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        default_venue_id = _parse_default_venue_id(d.pop("defaultVenueId", UNSET))

        alternate_venue_ids = []
        _alternate_venue_ids = d.pop("alternateVenueIds", UNSET)
        for alternate_venue_ids_item_data in _alternate_venue_ids or []:
            alternate_venue_ids_item = UUID(alternate_venue_ids_item_data)

            alternate_venue_ids.append(alternate_venue_ids_item)

        images = []
        _images = d.pop("images", UNSET)
        for images_item_data in _images or []:
            images_item = ImagesModel.from_dict(images_item_data)

            images.append(images_item)

        team_model = cls(
            entity_id=entity_id,
            organization_id=organization_id,
            organization=organization,
            entity_group_id=entity_group_id,
            entity_group=entity_group,
            international_reference=international_reference,
            status=status,
            name_full_local=name_full_local,
            additional_names=additional_names,
            name_full_latin=name_full_latin,
            code_local=code_local,
            code_latin=code_latin,
            address=address,
            social=social,
            contacts=contacts,
            details=details,
            colors=colors,
            historical_names=historical_names,
            external_id=external_id,
            age_group=age_group,
            gender=gender,
            standard=standard,
            grade=grade,
            representing=representing,
            discipline=discipline,
            updated=updated,
            added=added,
            default_venue_id=default_venue_id,
            alternate_venue_ids=alternate_venue_ids,
            images=images,
        )

        return team_model
