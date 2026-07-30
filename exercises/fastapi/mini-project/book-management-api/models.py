from pydantic import BaseModel, ConfigDict, Field

class BookBase(BaseModel):
    title: str = Field(
        min_length=1,
        max_length=200
    )

    author: str = Field(
        min_length=2,
        max_length=100
    )

class BookCreate(BookBase):
    pass

class BookUpdate(BookBase):
    pass

class BookResponse(BookBase):
    model_config = ConfigDict(from_attributes=True)

    id: int = Field(
        gt=0,
        description="Book ID"
    )