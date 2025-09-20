import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.fixture_pbp_event_update_fixture_pbp_event_put_body_class import (
    FixturePbpEventUpdateFixturePBPEventPutBodyClass,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.fixture_pbp_event_update_fixture_pbp_event_put_body_current_scores import (
        FixturePbpEventUpdateFixturePBPEventPutBodyCurrentScores,
    )


T = TypeVar("T", bound="FixturePbpEventUpdateFixturePBPEventPutBody")


@_attrs_define
class FixturePbpEventUpdateFixturePBPEventPutBody:
    """
    Attributes:
        events (Union[Unset, Any]):
        class_ (Union[Unset, FixturePbpEventUpdateFixturePBPEventPutBodyClass]): The class of the event
            >- `clock` Information about the current status of the clock match
            >- `sport` A sporting action that relates to the running of the match
             Default: FixturePbpEventUpdateFixturePBPEventPutBodyClass.SPORT. Example: sport.
        event_type (Union[Unset, str]): See [Event
            Types](http://developer.connect.sportradar.com/datacore/streaming.html#section/Message-Types/event) for more
            information Example: substitution.
        event_id (Union[Unset, UUID]): Unique identifier of this event Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        play_id (Union[Unset, UUID]): Unique identifier of this play (group of events) Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        entity_id (Union[Unset, UUID]): The unique identifier of the team Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        person_id (Union[Unset, UUID]): The unique identifier of the person Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        sub_type (Union[Unset, str]): The Sub Type of event. See <b>Streaming API</b> documenation for more information.
            Example: out.
        options (Union[Unset, Any]):
        received (Union[Unset, int]): The UNIX timestamp when the event was received.
        status (Union[Unset, str]): The status of this message.  Options are `added` (Default); `updated` - meaning the
            content of this event has been edited; `deleted` - meaning this event has been deleted; `enriched` - meaning
            further information has been added to the event (not changed).
        success (Union[Unset, bool]): Whether the action was successful
        x (Union[Unset, float]): The x co-ordinate of the event. Represented as percentage from left (0) to right (100).
            Example: 56.
        y (Union[Unset, float]): The y co-ordinate of the event. Represented as precentage from top (0) to bottom (100).
            Example: 23.
        z (Union[Unset, float]): The z co-ordinate of the event. Represented as precentage from ground (0) to ceiling
            (100). Example: 10.
        clock (Union[Unset, str]): The time on the clock when the event occurred. ISO 8601 format. PTmmMss.ccS Example:
            PT12M34.5S.
        shot_clock (Union[Unset, str]): The time on the shot clock when the event occurred. ISO 8601 format. PTss.ccS
            Example: PT34.2S.
        event_time (Union[Unset, datetime.datetime]): The date/time (UTC) this event occurred. For inserted actions,
            this should be the time the action would have occurred, not the time of insertion. Example:
            2016-09-08T02:02:00Z.
        official_id (Union[Unset, UUID]): The unique ID of the official making this decision Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        zone (Union[Unset, str]): See [Event Types]() for more information
        scores (Union['FixturePbpEventUpdateFixturePBPEventPutBodyCurrentScores', None, Unset]): The current scores
        timestamp (Union[Unset, datetime.datetime]): The date/time (UTC) this event was sent. Example:
            2016-09-08T02:02:00Z.
        client_type (Union[Unset, str]): Type of the client that sent the event Example: InGame.
        client_id (Union[Unset, str]): ID of the client that sent the event Example: InGame:0.9.
        sport (Union[Unset, str]): Sport one letter code Example: h.
        topic (Union[Unset, str]): MQTT topic where the event was sent Example:
            s/h/h1s44/3c467c99-9e5d-11ee-91d0-2b012330fcf5/w/e.
        type_ (Union[Unset, str]): Type of the event message Example: event.
        sequence (Union[None, Unset, int]): Client event sequence number Example: 10.
    """

    events: Union[Unset, Any] = UNSET
    class_: Union[Unset, FixturePbpEventUpdateFixturePBPEventPutBodyClass] = (
        FixturePbpEventUpdateFixturePBPEventPutBodyClass.SPORT
    )
    event_type: Union[Unset, str] = UNSET
    event_id: Union[Unset, UUID] = UNSET
    play_id: Union[Unset, UUID] = UNSET
    entity_id: Union[Unset, UUID] = UNSET
    person_id: Union[Unset, UUID] = UNSET
    sub_type: Union[Unset, str] = UNSET
    options: Union[Unset, Any] = UNSET
    received: Union[Unset, int] = UNSET
    status: Union[Unset, str] = UNSET
    success: Union[Unset, bool] = UNSET
    x: Union[Unset, float] = UNSET
    y: Union[Unset, float] = UNSET
    z: Union[Unset, float] = UNSET
    clock: Union[Unset, str] = UNSET
    shot_clock: Union[Unset, str] = UNSET
    event_time: Union[Unset, datetime.datetime] = UNSET
    official_id: Union[Unset, UUID] = UNSET
    zone: Union[Unset, str] = UNSET
    scores: Union[
        "FixturePbpEventUpdateFixturePBPEventPutBodyCurrentScores", None, Unset
    ] = UNSET
    timestamp: Union[Unset, datetime.datetime] = UNSET
    client_type: Union[Unset, str] = UNSET
    client_id: Union[Unset, str] = UNSET
    sport: Union[Unset, str] = UNSET
    topic: Union[Unset, str] = UNSET
    type_: Union[Unset, str] = UNSET
    sequence: Union[None, Unset, int] = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.fixture_pbp_event_update_fixture_pbp_event_put_body_current_scores import (
            FixturePbpEventUpdateFixturePBPEventPutBodyCurrentScores,
        )

        events = self.events

        class_: Union[Unset, str] = UNSET
        if not isinstance(self.class_, Unset):
            class_ = self.class_.value

        event_type = self.event_type

        event_id: Union[Unset, str] = UNSET
        if not isinstance(self.event_id, Unset):
            event_id = str(self.event_id)

        play_id: Union[Unset, str] = UNSET
        if not isinstance(self.play_id, Unset):
            play_id = str(self.play_id)

        entity_id: Union[Unset, str] = UNSET
        if not isinstance(self.entity_id, Unset):
            entity_id = str(self.entity_id)

        person_id: Union[Unset, str] = UNSET
        if not isinstance(self.person_id, Unset):
            person_id = str(self.person_id)

        sub_type = self.sub_type

        options = self.options

        received = self.received

        status = self.status

        success = self.success

        x = self.x

        y = self.y

        z = self.z

        clock = self.clock

        shot_clock = self.shot_clock

        event_time: Union[Unset, str] = UNSET
        if not isinstance(self.event_time, Unset):
            event_time = self.event_time.isoformat()

        official_id: Union[Unset, str] = UNSET
        if not isinstance(self.official_id, Unset):
            official_id = str(self.official_id)

        zone = self.zone

        scores: Union[None, Unset, dict[str, Any]]
        if isinstance(self.scores, Unset):
            scores = UNSET
        elif isinstance(
            self.scores, FixturePbpEventUpdateFixturePBPEventPutBodyCurrentScores
        ):
            scores = self.scores.to_dict()
        else:
            scores = self.scores

        timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.timestamp, Unset):
            timestamp = self.timestamp.isoformat()

        client_type = self.client_type

        client_id = self.client_id

        sport = self.sport

        topic = self.topic

        type_ = self.type_

        sequence: Union[None, Unset, int]
        if isinstance(self.sequence, Unset):
            sequence = UNSET
        else:
            sequence = self.sequence

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if events is not UNSET:
            field_dict["events"] = events
        if class_ is not UNSET:
            field_dict["class"] = class_
        if event_type is not UNSET:
            field_dict["eventType"] = event_type
        if event_id is not UNSET:
            field_dict["eventId"] = event_id
        if play_id is not UNSET:
            field_dict["playId"] = play_id
        if entity_id is not UNSET:
            field_dict["entityId"] = entity_id
        if person_id is not UNSET:
            field_dict["personId"] = person_id
        if sub_type is not UNSET:
            field_dict["subType"] = sub_type
        if options is not UNSET:
            field_dict["options"] = options
        if received is not UNSET:
            field_dict["received"] = received
        if status is not UNSET:
            field_dict["status"] = status
        if success is not UNSET:
            field_dict["success"] = success
        if x is not UNSET:
            field_dict["x"] = x
        if y is not UNSET:
            field_dict["y"] = y
        if z is not UNSET:
            field_dict["z"] = z
        if clock is not UNSET:
            field_dict["clock"] = clock
        if shot_clock is not UNSET:
            field_dict["shotClock"] = shot_clock
        if event_time is not UNSET:
            field_dict["eventTime"] = event_time
        if official_id is not UNSET:
            field_dict["officialId"] = official_id
        if zone is not UNSET:
            field_dict["zone"] = zone
        if scores is not UNSET:
            field_dict["scores"] = scores
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp
        if client_type is not UNSET:
            field_dict["clientType"] = client_type
        if client_id is not UNSET:
            field_dict["clientId"] = client_id
        if sport is not UNSET:
            field_dict["sport"] = sport
        if topic is not UNSET:
            field_dict["topic"] = topic
        if type_ is not UNSET:
            field_dict["type"] = type_
        if sequence is not UNSET:
            field_dict["sequence"] = sequence

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.fixture_pbp_event_update_fixture_pbp_event_put_body_current_scores import (
            FixturePbpEventUpdateFixturePBPEventPutBodyCurrentScores,
        )

        d = dict(src_dict)
        events = d.pop("events", UNSET)

        _class_ = d.pop("class", UNSET)
        class_: Union[Unset, FixturePbpEventUpdateFixturePBPEventPutBodyClass]
        if isinstance(_class_, Unset):
            class_ = UNSET
        else:
            class_ = FixturePbpEventUpdateFixturePBPEventPutBodyClass(_class_)

        event_type = d.pop("eventType", UNSET)

        _event_id = d.pop("eventId", UNSET)
        event_id: Union[Unset, UUID]
        if isinstance(_event_id, Unset):
            event_id = UNSET
        else:
            event_id = UUID(_event_id)

        _play_id = d.pop("playId", UNSET)
        play_id: Union[Unset, UUID]
        if isinstance(_play_id, Unset):
            play_id = UNSET
        else:
            play_id = UUID(_play_id)

        _entity_id = d.pop("entityId", UNSET)
        entity_id: Union[Unset, UUID]
        if isinstance(_entity_id, Unset):
            entity_id = UNSET
        else:
            entity_id = UUID(_entity_id)

        _person_id = d.pop("personId", UNSET)
        person_id: Union[Unset, UUID]
        if isinstance(_person_id, Unset):
            person_id = UNSET
        else:
            person_id = UUID(_person_id)

        sub_type = d.pop("subType", UNSET)

        options = d.pop("options", UNSET)

        received = d.pop("received", UNSET)

        status = d.pop("status", UNSET)

        success = d.pop("success", UNSET)

        x = d.pop("x", UNSET)

        y = d.pop("y", UNSET)

        z = d.pop("z", UNSET)

        clock = d.pop("clock", UNSET)

        shot_clock = d.pop("shotClock", UNSET)

        _event_time = d.pop("eventTime", UNSET)
        event_time: Union[Unset, datetime.datetime]
        if isinstance(_event_time, Unset):
            event_time = UNSET
        else:
            event_time = isoparse(_event_time)

        _official_id = d.pop("officialId", UNSET)
        official_id: Union[Unset, UUID]
        if isinstance(_official_id, Unset):
            official_id = UNSET
        else:
            official_id = UUID(_official_id)

        zone = d.pop("zone", UNSET)

        def _parse_scores(
            data: object,
        ) -> Union[
            "FixturePbpEventUpdateFixturePBPEventPutBodyCurrentScores", None, Unset
        ]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                scores_type_0 = (
                    FixturePbpEventUpdateFixturePBPEventPutBodyCurrentScores.from_dict(
                        data
                    )
                )

                return scores_type_0
            except:  # noqa: E722
                pass
            return cast(
                Union[
                    "FixturePbpEventUpdateFixturePBPEventPutBodyCurrentScores",
                    None,
                    Unset,
                ],
                data,
            )

        scores = _parse_scores(d.pop("scores", UNSET))

        _timestamp = d.pop("timestamp", UNSET)
        timestamp: Union[Unset, datetime.datetime]
        if isinstance(_timestamp, Unset):
            timestamp = UNSET
        else:
            timestamp = isoparse(_timestamp)

        client_type = d.pop("clientType", UNSET)

        client_id = d.pop("clientId", UNSET)

        sport = d.pop("sport", UNSET)

        topic = d.pop("topic", UNSET)

        type_ = d.pop("type", UNSET)

        def _parse_sequence(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        sequence = _parse_sequence(d.pop("sequence", UNSET))

        fixture_pbp_event_update_fixture_pbp_event_put_body = cls(
            events=events,
            class_=class_,
            event_type=event_type,
            event_id=event_id,
            play_id=play_id,
            entity_id=entity_id,
            person_id=person_id,
            sub_type=sub_type,
            options=options,
            received=received,
            status=status,
            success=success,
            x=x,
            y=y,
            z=z,
            clock=clock,
            shot_clock=shot_clock,
            event_time=event_time,
            official_id=official_id,
            zone=zone,
            scores=scores,
            timestamp=timestamp,
            client_type=client_type,
            client_id=client_id,
            sport=sport,
            topic=topic,
            type_=type_,
            sequence=sequence,
        )

        return fixture_pbp_event_update_fixture_pbp_event_put_body
