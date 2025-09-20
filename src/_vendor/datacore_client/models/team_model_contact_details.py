from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="TeamModelContactDetails")


@_attrs_define
class TeamModelContactDetails:
    """Public contact fields

    Attributes:
        fax (Union[None, Unset, str]): Fax number
        phone (Union[None, Unset, str]): Primary phone number
        phone_secondary (Union[None, Unset, str]): Secondary phone number
        email (Union[None, Unset, str]): Primary email address
    """

    fax: Union[None, Unset, str] = UNSET
    phone: Union[None, Unset, str] = UNSET
    phone_secondary: Union[None, Unset, str] = UNSET
    email: Union[None, Unset, str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        fax: Union[None, Unset, str]
        if isinstance(self.fax, Unset):
            fax = UNSET
        else:
            fax = self.fax

        phone: Union[None, Unset, str]
        if isinstance(self.phone, Unset):
            phone = UNSET
        else:
            phone = self.phone

        phone_secondary: Union[None, Unset, str]
        if isinstance(self.phone_secondary, Unset):
            phone_secondary = UNSET
        else:
            phone_secondary = self.phone_secondary

        email: Union[None, Unset, str]
        if isinstance(self.email, Unset):
            email = UNSET
        else:
            email = self.email

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if fax is not UNSET:
            field_dict["fax"] = fax
        if phone is not UNSET:
            field_dict["phone"] = phone
        if phone_secondary is not UNSET:
            field_dict["phoneSecondary"] = phone_secondary
        if email is not UNSET:
            field_dict["email"] = email

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_fax(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        fax = _parse_fax(d.pop("fax", UNSET))

        def _parse_phone(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        phone = _parse_phone(d.pop("phone", UNSET))

        def _parse_phone_secondary(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        phone_secondary = _parse_phone_secondary(d.pop("phoneSecondary", UNSET))

        def _parse_email(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        email = _parse_email(d.pop("email", UNSET))

        team_model_contact_details = cls(
            fax=fax,
            phone=phone,
            phone_secondary=phone_secondary,
            email=email,
        )

        return team_model_contact_details
