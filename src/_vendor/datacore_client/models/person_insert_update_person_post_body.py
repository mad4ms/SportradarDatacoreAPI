import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.person_insert_update_person_post_body_gender import (
    PersonInsertUpdatePersonPostBodyGender,
)
from ..models.person_insert_update_person_post_body_status import (
    PersonInsertUpdatePersonPostBodyStatus,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.person_insert_update_person_post_body_additional_names_type_0 import (
        PersonInsertUpdatePersonPostBodyAdditionalNamesType0,
    )
    from ..models.person_insert_update_person_post_body_person_additional_details import (
        PersonInsertUpdatePersonPostBodyPersonAdditionalDetails,
    )
    from ..models.person_insert_update_person_post_body_person_historical_name import (
        PersonInsertUpdatePersonPostBodyPersonHistoricalName,
    )
    from ..models.person_insert_update_person_post_body_social_media import (
        PersonInsertUpdatePersonPostBodySocialMedia,
    )


T = TypeVar("T", bound="PersonInsertUpdatePersonPostBody")


@_attrs_define
class PersonInsertUpdatePersonPostBody:
    """
    Attributes:
        status (PersonInsertUpdatePersonPostBodyStatus): Status
            >- `ACTIVE` Active
            >- `DECEASED` Deceased
            >- `INACTIVE` Inactive
            >- `PENDING` Pending
            >- `UNREGISTERED` UnRegistered
             Default: PersonInsertUpdatePersonPostBodyStatus.ACTIVE. Example: ACTIVE.
        gender (PersonInsertUpdatePersonPostBodyGender): The gender of the person
            >- `FEMALE` Female
            >- `MALE` Male
            >- `UNKNOWN` Unknown
             Example: MALE.
        name_full_local (str): The full name of the person in [local](#section/Introduction/Character-Sets-and-Names)
            language Example: John Smith.
        person_id (Union[Unset, UUID]): The unique identifier of the person Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        name_abbreviated (Union[None, Unset, str]): An abbreviated name for a person Example: Pat.
        language_local (Union[None, Unset, str]): The language code of the full name in
            [local](#section/Introduction/Character-Sets-and-Names) language. This code is a two letter (lower-case) ISO
            639-1 language code. Example: en.
        name_given_local (Union[None, Unset, str]): Given name of the person in [local](#section/Introduction/Character-
            Sets-and-Names) language Example: John.
        name_family_local (Union[None, Unset, str]): Family name of the person in
            [local](#section/Introduction/Character-Sets-and-Names) language Example: Smith.
        name_full_latin (Union[None, Unset, str]): The full name of the person in
            [latin](##section/Introduction/Character-Sets-and-Names) characters Example: John Smith.
        name_given_latin (Union[None, Unset, str]): Given name of the person in [latin](#section/Introduction/Character-
            Sets-and-Names) characters Example: John.
        name_family_latin (Union[None, Unset, str]): Family name of the person in
            [latin](#section/Introduction/Character-Sets-and-Names) characters Example: Smith.
        dob (Union[None, Unset, datetime.date]): Date of Birth Example: 1978-08-24.
        nationality (Union[None, Unset, str]): A 3 letter nationality code. We recommend you use ISO-3166 where
            available. Example: AUS.
        deceased (Union[None, Unset, datetime.date]): Date deceased Example: 2016-09-08.
        additional_names (Union['PersonInsertUpdatePersonPostBodyAdditionalNamesType0', None, Unset]): Additional names
            for the person. They are broken down by language, so you can have a different set of names per language
        additional_details (Union['PersonInsertUpdatePersonPostBodyPersonAdditionalDetails', None, Unset]): Additional
            person detail fields
        social (Union['PersonInsertUpdatePersonPostBodySocialMedia', None, Unset]): Social Media contacts
        historical_names (Union[None, Unset, list['PersonInsertUpdatePersonPostBodyPersonHistoricalName']]): Array of
            person historical names
        representing (Union[None, Unset, str]): Who the person or team was representing Example: AUSTRALIA.
        external_id (Union[None, Unset, str]): The Id of the data as set by the provider of the data Example: A123.
    """

    gender: PersonInsertUpdatePersonPostBodyGender
    name_full_local: str
    status: PersonInsertUpdatePersonPostBodyStatus = (
        PersonInsertUpdatePersonPostBodyStatus.ACTIVE
    )
    person_id: Union[Unset, UUID] = UNSET
    name_abbreviated: Union[None, Unset, str] = UNSET
    language_local: Union[None, Unset, str] = UNSET
    name_given_local: Union[None, Unset, str] = UNSET
    name_family_local: Union[None, Unset, str] = UNSET
    name_full_latin: Union[None, Unset, str] = UNSET
    name_given_latin: Union[None, Unset, str] = UNSET
    name_family_latin: Union[None, Unset, str] = UNSET
    dob: Union[None, Unset, datetime.date] = UNSET
    nationality: Union[None, Unset, str] = UNSET
    deceased: Union[None, Unset, datetime.date] = UNSET
    additional_names: Union[
        "PersonInsertUpdatePersonPostBodyAdditionalNamesType0", None, Unset
    ] = UNSET
    additional_details: Union[
        "PersonInsertUpdatePersonPostBodyPersonAdditionalDetails", None, Unset
    ] = UNSET
    social: Union["PersonInsertUpdatePersonPostBodySocialMedia", None, Unset] = UNSET
    historical_names: Union[
        None, Unset, list["PersonInsertUpdatePersonPostBodyPersonHistoricalName"]
    ] = UNSET
    representing: Union[None, Unset, str] = UNSET
    external_id: Union[None, Unset, str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.person_insert_update_person_post_body_additional_names_type_0 import (
            PersonInsertUpdatePersonPostBodyAdditionalNamesType0,
        )
        from ..models.person_insert_update_person_post_body_person_additional_details import (
            PersonInsertUpdatePersonPostBodyPersonAdditionalDetails,
        )
        from ..models.person_insert_update_person_post_body_social_media import (
            PersonInsertUpdatePersonPostBodySocialMedia,
        )

        status = self.status.value

        gender = self.gender.value

        name_full_local = self.name_full_local

        person_id: Union[Unset, str] = UNSET
        if not isinstance(self.person_id, Unset):
            person_id = str(self.person_id)

        name_abbreviated: Union[None, Unset, str]
        if isinstance(self.name_abbreviated, Unset):
            name_abbreviated = UNSET
        else:
            name_abbreviated = self.name_abbreviated

        language_local: Union[None, Unset, str]
        if isinstance(self.language_local, Unset):
            language_local = UNSET
        else:
            language_local = self.language_local

        name_given_local: Union[None, Unset, str]
        if isinstance(self.name_given_local, Unset):
            name_given_local = UNSET
        else:
            name_given_local = self.name_given_local

        name_family_local: Union[None, Unset, str]
        if isinstance(self.name_family_local, Unset):
            name_family_local = UNSET
        else:
            name_family_local = self.name_family_local

        name_full_latin: Union[None, Unset, str]
        if isinstance(self.name_full_latin, Unset):
            name_full_latin = UNSET
        else:
            name_full_latin = self.name_full_latin

        name_given_latin: Union[None, Unset, str]
        if isinstance(self.name_given_latin, Unset):
            name_given_latin = UNSET
        else:
            name_given_latin = self.name_given_latin

        name_family_latin: Union[None, Unset, str]
        if isinstance(self.name_family_latin, Unset):
            name_family_latin = UNSET
        else:
            name_family_latin = self.name_family_latin

        dob: Union[None, Unset, str]
        if isinstance(self.dob, Unset):
            dob = UNSET
        elif isinstance(self.dob, datetime.date):
            dob = self.dob.isoformat()
        else:
            dob = self.dob

        nationality: Union[None, Unset, str]
        if isinstance(self.nationality, Unset):
            nationality = UNSET
        else:
            nationality = self.nationality

        deceased: Union[None, Unset, str]
        if isinstance(self.deceased, Unset):
            deceased = UNSET
        elif isinstance(self.deceased, datetime.date):
            deceased = self.deceased.isoformat()
        else:
            deceased = self.deceased

        additional_names: Union[None, Unset, dict[str, Any]]
        if isinstance(self.additional_names, Unset):
            additional_names = UNSET
        elif isinstance(
            self.additional_names, PersonInsertUpdatePersonPostBodyAdditionalNamesType0
        ):
            additional_names = self.additional_names.to_dict()
        else:
            additional_names = self.additional_names

        additional_details: Union[None, Unset, dict[str, Any]]
        if isinstance(self.additional_details, Unset):
            additional_details = UNSET
        elif isinstance(
            self.additional_details,
            PersonInsertUpdatePersonPostBodyPersonAdditionalDetails,
        ):
            additional_details = self.additional_details.to_dict()
        else:
            additional_details = self.additional_details

        social: Union[None, Unset, dict[str, Any]]
        if isinstance(self.social, Unset):
            social = UNSET
        elif isinstance(self.social, PersonInsertUpdatePersonPostBodySocialMedia):
            social = self.social.to_dict()
        else:
            social = self.social

        historical_names: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.historical_names, Unset):
            historical_names = UNSET
        elif isinstance(self.historical_names, list):
            historical_names = []
            for historical_names_type_0_item_data in self.historical_names:
                historical_names_type_0_item = (
                    historical_names_type_0_item_data.to_dict()
                )
                historical_names.append(historical_names_type_0_item)

        else:
            historical_names = self.historical_names

        representing: Union[None, Unset, str]
        if isinstance(self.representing, Unset):
            representing = UNSET
        else:
            representing = self.representing

        external_id: Union[None, Unset, str]
        if isinstance(self.external_id, Unset):
            external_id = UNSET
        else:
            external_id = self.external_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "status": status,
                "gender": gender,
                "nameFullLocal": name_full_local,
            }
        )
        if person_id is not UNSET:
            field_dict["personId"] = person_id
        if name_abbreviated is not UNSET:
            field_dict["nameAbbreviated"] = name_abbreviated
        if language_local is not UNSET:
            field_dict["languageLocal"] = language_local
        if name_given_local is not UNSET:
            field_dict["nameGivenLocal"] = name_given_local
        if name_family_local is not UNSET:
            field_dict["nameFamilyLocal"] = name_family_local
        if name_full_latin is not UNSET:
            field_dict["nameFullLatin"] = name_full_latin
        if name_given_latin is not UNSET:
            field_dict["nameGivenLatin"] = name_given_latin
        if name_family_latin is not UNSET:
            field_dict["nameFamilyLatin"] = name_family_latin
        if dob is not UNSET:
            field_dict["dob"] = dob
        if nationality is not UNSET:
            field_dict["nationality"] = nationality
        if deceased is not UNSET:
            field_dict["deceased"] = deceased
        if additional_names is not UNSET:
            field_dict["additionalNames"] = additional_names
        if additional_details is not UNSET:
            field_dict["additionalDetails"] = additional_details
        if social is not UNSET:
            field_dict["social"] = social
        if historical_names is not UNSET:
            field_dict["historicalNames"] = historical_names
        if representing is not UNSET:
            field_dict["representing"] = representing
        if external_id is not UNSET:
            field_dict["externalId"] = external_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.person_insert_update_person_post_body_additional_names_type_0 import (
            PersonInsertUpdatePersonPostBodyAdditionalNamesType0,
        )
        from ..models.person_insert_update_person_post_body_person_additional_details import (
            PersonInsertUpdatePersonPostBodyPersonAdditionalDetails,
        )
        from ..models.person_insert_update_person_post_body_person_historical_name import (
            PersonInsertUpdatePersonPostBodyPersonHistoricalName,
        )
        from ..models.person_insert_update_person_post_body_social_media import (
            PersonInsertUpdatePersonPostBodySocialMedia,
        )

        d = dict(src_dict)
        status = PersonInsertUpdatePersonPostBodyStatus(d.pop("status"))

        gender = PersonInsertUpdatePersonPostBodyGender(d.pop("gender"))

        name_full_local = d.pop("nameFullLocal")

        _person_id = d.pop("personId", UNSET)
        person_id: Union[Unset, UUID]
        if isinstance(_person_id, Unset):
            person_id = UNSET
        else:
            person_id = UUID(_person_id)

        def _parse_name_abbreviated(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name_abbreviated = _parse_name_abbreviated(d.pop("nameAbbreviated", UNSET))

        def _parse_language_local(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        language_local = _parse_language_local(d.pop("languageLocal", UNSET))

        def _parse_name_given_local(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name_given_local = _parse_name_given_local(d.pop("nameGivenLocal", UNSET))

        def _parse_name_family_local(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name_family_local = _parse_name_family_local(d.pop("nameFamilyLocal", UNSET))

        def _parse_name_full_latin(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name_full_latin = _parse_name_full_latin(d.pop("nameFullLatin", UNSET))

        def _parse_name_given_latin(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name_given_latin = _parse_name_given_latin(d.pop("nameGivenLatin", UNSET))

        def _parse_name_family_latin(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name_family_latin = _parse_name_family_latin(d.pop("nameFamilyLatin", UNSET))

        def _parse_dob(data: object) -> Union[None, Unset, datetime.date]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                dob_type_0 = isoparse(data).date()

                return dob_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.date], data)

        dob = _parse_dob(d.pop("dob", UNSET))

        def _parse_nationality(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        nationality = _parse_nationality(d.pop("nationality", UNSET))

        def _parse_deceased(data: object) -> Union[None, Unset, datetime.date]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                deceased_type_0 = isoparse(data).date()

                return deceased_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.date], data)

        deceased = _parse_deceased(d.pop("deceased", UNSET))

        def _parse_additional_names(
            data: object,
        ) -> Union["PersonInsertUpdatePersonPostBodyAdditionalNamesType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                additional_names_type_0 = (
                    PersonInsertUpdatePersonPostBodyAdditionalNamesType0.from_dict(data)
                )

                return additional_names_type_0
            except:  # noqa: E722
                pass
            return cast(
                Union[
                    "PersonInsertUpdatePersonPostBodyAdditionalNamesType0", None, Unset
                ],
                data,
            )

        additional_names = _parse_additional_names(d.pop("additionalNames", UNSET))

        def _parse_additional_details(
            data: object,
        ) -> Union[
            "PersonInsertUpdatePersonPostBodyPersonAdditionalDetails", None, Unset
        ]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                additional_details_type_0 = (
                    PersonInsertUpdatePersonPostBodyPersonAdditionalDetails.from_dict(
                        data
                    )
                )

                return additional_details_type_0
            except:  # noqa: E722
                pass
            return cast(
                Union[
                    "PersonInsertUpdatePersonPostBodyPersonAdditionalDetails",
                    None,
                    Unset,
                ],
                data,
            )

        additional_details = _parse_additional_details(
            d.pop("additionalDetails", UNSET)
        )

        def _parse_social(
            data: object,
        ) -> Union["PersonInsertUpdatePersonPostBodySocialMedia", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                social_type_0 = PersonInsertUpdatePersonPostBodySocialMedia.from_dict(
                    data
                )

                return social_type_0
            except:  # noqa: E722
                pass
            return cast(
                Union["PersonInsertUpdatePersonPostBodySocialMedia", None, Unset], data
            )

        social = _parse_social(d.pop("social", UNSET))

        def _parse_historical_names(
            data: object,
        ) -> Union[
            None, Unset, list["PersonInsertUpdatePersonPostBodyPersonHistoricalName"]
        ]:
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
                    historical_names_type_0_item = (
                        PersonInsertUpdatePersonPostBodyPersonHistoricalName.from_dict(
                            historical_names_type_0_item_data
                        )
                    )

                    historical_names_type_0.append(historical_names_type_0_item)

                return historical_names_type_0
            except:  # noqa: E722
                pass
            return cast(
                Union[
                    None,
                    Unset,
                    list["PersonInsertUpdatePersonPostBodyPersonHistoricalName"],
                ],
                data,
            )

        historical_names = _parse_historical_names(d.pop("historicalNames", UNSET))

        def _parse_representing(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        representing = _parse_representing(d.pop("representing", UNSET))

        def _parse_external_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        external_id = _parse_external_id(d.pop("externalId", UNSET))

        person_insert_update_person_post_body = cls(
            status=status,
            gender=gender,
            name_full_local=name_full_local,
            person_id=person_id,
            name_abbreviated=name_abbreviated,
            language_local=language_local,
            name_given_local=name_given_local,
            name_family_local=name_family_local,
            name_full_latin=name_full_latin,
            name_given_latin=name_given_latin,
            name_family_latin=name_family_latin,
            dob=dob,
            nationality=nationality,
            deceased=deceased,
            additional_names=additional_names,
            additional_details=additional_details,
            social=social,
            historical_names=historical_names,
            representing=representing,
            external_id=external_id,
        )

        return person_insert_update_person_post_body
