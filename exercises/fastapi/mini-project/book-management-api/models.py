from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    field_validator
)

class BookBase(BaseModel):
    title: str = Field(
        min_length=1,
        max_length=200
    )

    author: str = Field(
        min_length=2,
        max_length=100
    )

    @field_validator("title", "author")
    @classmethod
    def validate_not_blank(
        cls,
        value: str
    ) -> str:
        value = value.strip()

        if not value:
            raise ValueError(
                "must not be blank"
            )

        return value

class BookCreate(BookBase):
    pass

class BookUpdate(BookBase):
    pass

class BookPatch(BaseModel):
    title: str | None = Field(
        default=None,
        min_length=1,
        max_length=200
    )

    author: str | None = Field(
        default=None,
        min_length=2,
        max_length=100
    )

    @field_validator("title", "author")
    @classmethod
    def validate_not_blank(
        cls,
        value: str | None
    ) -> str | None:
        if value is None:
            return value

        value = value.strip()

        if not value:
            raise ValueError("must not be blank")

        return value

class BookResponse(BookBase):
    model_config = ConfigDict(from_attributes=True)

    id: int = Field(
        gt=0,
        description="Book ID"
    )