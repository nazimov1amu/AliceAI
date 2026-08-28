from datetime import datetime
from typing import Annotated
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field, PlainSerializer

CustomUUID = Annotated[
    UUID,
    PlainSerializer(lambda value: str(value), return_type=str, when_used="json"),
]

CustomDatetime = Annotated[
    datetime,
    PlainSerializer(
        lambda value: value.isoformat(), return_type=str, when_used="json"
    ),
]


class Customer(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    request_tenant_id: int = Field(alias="requestTenantID")
    request_id: CustomUUID = Field(alias="requestID")
    request_user_id: CustomUUID = Field(alias="requestUserID")
