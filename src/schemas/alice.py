from enum import StrEnum
from typing import Annotated, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

from src.resources.constants import YANDEX_VERSION


class AliceModel(BaseModel):
    model_config = ConfigDict(extra="ignore")


class AliceSkillRequestType(StrEnum):
    show_pull = "Show.Pull"
    simple_utterance = "SimpleUtterance"
    button_press = "ButtonPressed"


class AliceSkillSessionUser(AliceModel):
    user_id: str


class AliceSkillSessionApplication(AliceModel):
    application_id: str = Field(..., max_length=64)


class AliceSkillSession(AliceModel):
    message_id: int = Field(..., ge=0, le=99_999_999)
    session_id: str = Field(..., max_length=64)
    skill_id: str
    user_id: str = Field(..., max_length=64)
    new: bool
    user: AliceSkillSessionUser | None = None
    application: AliceSkillSessionApplication | None = None


class AliceSkillSimpleUtterance(AliceModel):
    type: Literal[AliceSkillRequestType.simple_utterance]
    command: str = ""
    original_utterance: str = ""


class AliceSkillButtonPressed(AliceModel):
    type: Literal[AliceSkillRequestType.button_press]
    payload: dict[str, Any] = Field(default_factory=dict)


class AliceSkillShowPull(AliceModel):
    type: Literal[AliceSkillRequestType.show_pull]
    show_type: str


AliceSkillRequestBody = Annotated[
    AliceSkillSimpleUtterance | AliceSkillButtonPressed | AliceSkillShowPull,
    Field(discriminator="type"),
]


class AliceSkillRequest(AliceModel):
    request: AliceSkillRequestBody
    session: AliceSkillSession
    version: str = YANDEX_VERSION


class AliceSkillResponseBody(AliceModel):
    text: str
    tts: str | None = None
    end_session: bool = False


class AliceSkillResponse(AliceModel):
    response: AliceSkillResponseBody
    version: str = YANDEX_VERSION
