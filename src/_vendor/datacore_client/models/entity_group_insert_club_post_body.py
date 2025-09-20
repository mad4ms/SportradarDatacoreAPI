from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..models.entity_group_insert_club_post_body_status import (
    EntityGroupInsertClubPostBodyStatus,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.entity_group_insert_club_post_body_additional_names import (
        EntityGroupInsertClubPostBodyAdditionalNames,
    )
    from ..models.entity_group_insert_club_post_body_club_address import (
        EntityGroupInsertClubPostBodyClubAddress,
    )
    from ..models.entity_group_insert_club_post_body_club_historical_name import (
        EntityGroupInsertClubPostBodyClubHistoricalName,
    )
    from ..models.entity_group_insert_club_post_body_colors import (
        EntityGroupInsertClubPostBodyColors,
    )
    from ..models.entity_group_insert_club_post_body_contact_details import (
        EntityGroupInsertClubPostBodyContactDetails,
    )
    from ..models.entity_group_insert_club_post_body_entity_additional_details import (
        EntityGroupInsertClubPostBodyEntityAdditionalDetails,
    )
    from ..models.entity_group_insert_club_post_body_social_media import (
        EntityGroupInsertClubPostBodySocialMedia,
    )


T = TypeVar("T", bound="EntityGroupInsertClubPostBody")


@_attrs_define
class EntityGroupInsertClubPostBody:
    """
    Attributes:
        status (EntityGroupInsertClubPostBodyStatus): Status
            >- `ACTIVE` Active
            >- `INACTIVE` Inactive
            >- `PENDING` Pending
             Example: ACTIVE.
        name_full_local (str): The full name of the club in the [local](#section/Introduction/Character-Sets-and-Names)
            language Example: Los Angeles Armadillos.
        entity_group_id (Union[Unset, UUID]): The unique identifier of the club Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        international_reference (Union[None, Unset, str]): The international reference for this club given by the sport
            governing body Example: CA3243-3.
        additional_names (Union[Unset, EntityGroupInsertClubPostBodyAdditionalNames]):
        name_full_latin (Union[None, Unset, str]): The full name of the club in [latin](#section/Introduction/Character-
            Sets-and-Names) characters Example: Los Angeles Armadillos.
        code_local (Union[None, Unset, str]): The code of the club in the [local](#section/Introduction/Character-Sets-
            and-Names) language Example: TEST.
        code_latin (Union[None, Unset, str]): The code of the club in [latin](#section/Introduction/Character-Sets-and-
            Names) characters Example: TEST.
        address (Union['EntityGroupInsertClubPostBodyClubAddress', None, Unset]): Street Address for the club
        social (Union['EntityGroupInsertClubPostBodySocialMedia', None, Unset]): Social Media contacts
        details (Union['EntityGroupInsertClubPostBodyEntityAdditionalDetails', None, Unset]): Additional detail fields
        contacts (Union['EntityGroupInsertClubPostBodyContactDetails', None, Unset]): Public contact fields
        colors (Union[Unset, EntityGroupInsertClubPostBodyColors]):
        historical_names (Union[None, Unset, list['EntityGroupInsertClubPostBodyClubHistoricalName']]): Array of club
            historical names
        external_id (Union[None, Unset, str]): The Id of the data as set by the provider of the data Example: A123.
        default_venue_id (Union[None, UUID, Unset]): The unique identifier of the default venue Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        alternate_venue_ids (Union[Unset, list[UUID]]):
    """

    status: EntityGroupInsertClubPostBodyStatus
    name_full_local: str
    entity_group_id: Union[Unset, UUID] = UNSET
    international_reference: Union[None, Unset, str] = UNSET
    additional_names: Union[Unset, "EntityGroupInsertClubPostBodyAdditionalNames"] = (
        UNSET
    )
    name_full_latin: Union[None, Unset, str] = UNSET
    code_local: Union[None, Unset, str] = UNSET
    code_latin: Union[None, Unset, str] = UNSET
    address: Union["EntityGroupInsertClubPostBodyClubAddress", None, Unset] = UNSET
    social: Union["EntityGroupInsertClubPostBodySocialMedia", None, Unset] = UNSET
    details: Union[
        "EntityGroupInsertClubPostBodyEntityAdditionalDetails", None, Unset
    ] = UNSET
    contacts: Union["EntityGroupInsertClubPostBodyContactDetails", None, Unset] = UNSET
    colors: Union[Unset, "EntityGroupInsertClubPostBodyColors"] = UNSET
    historical_names: Union[
        None, Unset, list["EntityGroupInsertClubPostBodyClubHistoricalName"]
    ] = UNSET
    external_id: Union[None, Unset, str] = UNSET
    default_venue_id: Union[None, UUID, Unset] = UNSET
    alternate_venue_ids: Union[Unset, list[UUID]] = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.entity_group_insert_club_post_body_club_address import (
            EntityGroupInsertClubPostBodyClubAddress,
        )
        from ..models.entity_group_insert_club_post_body_contact_details import (
            EntityGroupInsertClubPostBodyContactDetails,
        )
        from ..models.entity_group_insert_club_post_body_entity_additional_details import (
            EntityGroupInsertClubPostBodyEntityAdditionalDetails,
        )
        from ..models.entity_group_insert_club_post_body_social_media import (
            EntityGroupInsertClubPostBodySocialMedia,
        )

        status = self.status.value

        name_full_local = self.name_full_local

        entity_group_id: Union[Unset, str] = UNSET
        if not isinstance(self.entity_group_id, Unset):
            entity_group_id = str(self.entity_group_id)

        international_reference: Union[None, Unset, str]
        if isinstance(self.international_reference, Unset):
            international_reference = UNSET
        else:
            international_reference = self.international_reference

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
        elif isinstance(self.address, EntityGroupInsertClubPostBodyClubAddress):
            address = self.address.to_dict()
        else:
            address = self.address

        social: Union[None, Unset, dict[str, Any]]
        if isinstance(self.social, Unset):
            social = UNSET
        elif isinstance(self.social, EntityGroupInsertClubPostBodySocialMedia):
            social = self.social.to_dict()
        else:
            social = self.social

        details: Union[None, Unset, dict[str, Any]]
        if isinstance(self.details, Unset):
            details = UNSET
        elif isinstance(
            self.details, EntityGroupInsertClubPostBodyEntityAdditionalDetails
        ):
            details = self.details.to_dict()
        else:
            details = self.details

        contacts: Union[None, Unset, dict[str, Any]]
        if isinstance(self.contacts, Unset):
            contacts = UNSET
        elif isinstance(self.contacts, EntityGroupInsertClubPostBodyContactDetails):
            contacts = self.contacts.to_dict()
        else:
            contacts = self.contacts

        colors: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.colors, Unset):
            colors = self.colors.to_dict()

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

        external_id: Union[None, Unset, str]
        if isinstance(self.external_id, Unset):
            external_id = UNSET
        else:
            external_id = self.external_id

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

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "status": status,
                "nameFullLocal": name_full_local,
            }
        )
        if entity_group_id is not UNSET:
            field_dict["entityGroupId"] = entity_group_id
        if international_reference is not UNSET:
            field_dict["internationalReference"] = international_reference
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
        if details is not UNSET:
            field_dict["details"] = details
        if contacts is not UNSET:
            field_dict["contacts"] = contacts
        if colors is not UNSET:
            field_dict["colors"] = colors
        if historical_names is not UNSET:
            field_dict["historicalNames"] = historical_names
        if external_id is not UNSET:
            field_dict["externalId"] = external_id
        if default_venue_id is not UNSET:
            field_dict["defaultVenueId"] = default_venue_id
        if alternate_venue_ids is not UNSET:
            field_dict["alternateVenueIds"] = alternate_venue_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.entity_group_insert_club_post_body_additional_names import (
            EntityGroupInsertClubPostBodyAdditionalNames,
        )
        from ..models.entity_group_insert_club_post_body_club_address import (
            EntityGroupInsertClubPostBodyClubAddress,
        )
        from ..models.entity_group_insert_club_post_body_club_historical_name import (
            EntityGroupInsertClubPostBodyClubHistoricalName,
        )
        from ..models.entity_group_insert_club_post_body_colors import (
            EntityGroupInsertClubPostBodyColors,
        )
        from ..models.entity_group_insert_club_post_body_contact_details import (
            EntityGroupInsertClubPostBodyContactDetails,
        )
        from ..models.entity_group_insert_club_post_body_entity_additional_details import (
            EntityGroupInsertClubPostBodyEntityAdditionalDetails,
        )
        from ..models.entity_group_insert_club_post_body_social_media import (
            EntityGroupInsertClubPostBodySocialMedia,
        )

        d = dict(src_dict)
        status = EntityGroupInsertClubPostBodyStatus(d.pop("status"))

        name_full_local = d.pop("nameFullLocal")

        _entity_group_id = d.pop("entityGroupId", UNSET)
        entity_group_id: Union[Unset, UUID]
        if isinstance(_entity_group_id, Unset):
            entity_group_id = UNSET
        else:
            entity_group_id = UUID(_entity_group_id)

        def _parse_international_reference(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        international_reference = _parse_international_reference(
            d.pop("internationalReference", UNSET)
        )

        _additional_names = d.pop("additionalNames", UNSET)
        additional_names: Union[Unset, EntityGroupInsertClubPostBodyAdditionalNames]
        if isinstance(_additional_names, Unset):
            additional_names = UNSET
        else:
            additional_names = EntityGroupInsertClubPostBodyAdditionalNames.from_dict(
                _additional_names
            )

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

        def _parse_address(
            data: object,
        ) -> Union["EntityGroupInsertClubPostBodyClubAddress", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                address_type_0 = EntityGroupInsertClubPostBodyClubAddress.from_dict(
                    data
                )

                return address_type_0
            except:  # noqa: E722
                pass
            return cast(
                Union["EntityGroupInsertClubPostBodyClubAddress", None, Unset], data
            )

        address = _parse_address(d.pop("address", UNSET))

        def _parse_social(
            data: object,
        ) -> Union["EntityGroupInsertClubPostBodySocialMedia", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                social_type_0 = EntityGroupInsertClubPostBodySocialMedia.from_dict(data)

                return social_type_0
            except:  # noqa: E722
                pass
            return cast(
                Union["EntityGroupInsertClubPostBodySocialMedia", None, Unset], data
            )

        social = _parse_social(d.pop("social", UNSET))

        def _parse_details(
            data: object,
        ) -> Union["EntityGroupInsertClubPostBodyEntityAdditionalDetails", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                details_type_0 = (
                    EntityGroupInsertClubPostBodyEntityAdditionalDetails.from_dict(data)
                )

                return details_type_0
            except:  # noqa: E722
                pass
            return cast(
                Union[
                    "EntityGroupInsertClubPostBodyEntityAdditionalDetails", None, Unset
                ],
                data,
            )

        details = _parse_details(d.pop("details", UNSET))

        def _parse_contacts(
            data: object,
        ) -> Union["EntityGroupInsertClubPostBodyContactDetails", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                contacts_type_0 = EntityGroupInsertClubPostBodyContactDetails.from_dict(
                    data
                )

                return contacts_type_0
            except:  # noqa: E722
                pass
            return cast(
                Union["EntityGroupInsertClubPostBodyContactDetails", None, Unset], data
            )

        contacts = _parse_contacts(d.pop("contacts", UNSET))

        _colors = d.pop("colors", UNSET)
        colors: Union[Unset, EntityGroupInsertClubPostBodyColors]
        if isinstance(_colors, Unset):
            colors = UNSET
        else:
            colors = EntityGroupInsertClubPostBodyColors.from_dict(_colors)

        def _parse_historical_names(
            data: object,
        ) -> Union[
            None, Unset, list["EntityGroupInsertClubPostBodyClubHistoricalName"]
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
                        EntityGroupInsertClubPostBodyClubHistoricalName.from_dict(
                            historical_names_type_0_item_data
                        )
                    )

                    historical_names_type_0.append(historical_names_type_0_item)

                return historical_names_type_0
            except:  # noqa: E722
                pass
            return cast(
                Union[
                    None, Unset, list["EntityGroupInsertClubPostBodyClubHistoricalName"]
                ],
                data,
            )

        historical_names = _parse_historical_names(d.pop("historicalNames", UNSET))

        def _parse_external_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        external_id = _parse_external_id(d.pop("externalId", UNSET))

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

        entity_group_insert_club_post_body = cls(
            status=status,
            name_full_local=name_full_local,
            entity_group_id=entity_group_id,
            international_reference=international_reference,
            additional_names=additional_names,
            name_full_latin=name_full_latin,
            code_local=code_local,
            code_latin=code_latin,
            address=address,
            social=social,
            details=details,
            contacts=contacts,
            colors=colors,
            historical_names=historical_names,
            external_id=external_id,
            default_venue_id=default_venue_id,
            alternate_venue_ids=alternate_venue_ids,
        )

        return entity_group_insert_club_post_body
