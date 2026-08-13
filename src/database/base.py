from sqlmodel import SQLModel, Field

class ModelProvider(SQLModel, table=True):
    __tablename__ = "model_provider"

    id: int | None = Field(
        default=None,
        primary_key=True
    )

    name: str = Field(
        index=True,
        unique=True
    )

    api_key: str | None

    base_url: str | None

class AIModel(SQLModel, table=True):
    __tablename__ = "ai_model"

    id: int | None = Field(
        default=None,
        primary_key=True
    )

    provider_id: int = Field(
        foreign_key="model_provider.id"
    )

    name: str = Field(
        index=True,
    )

    max_context: int

class Theme(SQLModel, table=True):
    __tablename__="theme"

    id: int | None = Field(
        default=None,
        primary_key=True
    )

    name: str = Field(
        index=True,
        unique=True
    )

class GlobalConfig(SQLModel, table=True):
    __tablename__ = "global_config"

    id: int | None = Field(
        default=None,
        primary_key=True
    )

    default_model_provider_id: int | None = Field(
        foreign_key="model_provider.id"
    )

    default_ai_model_id: int | None = Field(
        foreign_key="ai_model.id"
    )

    theme_id: int = Field(
        foreign_key="theme.id"
    )