from sqlmodel import (
    SQLModel,
    Session,
    create_engine,
    select
)

from ..utils.app_info import get_app_config_dir

from .base import (
    ModelProvider,
    AIModel,
    Theme,
    GlobalConfig
)

from .default import (
    DEFAULT_PROVIDERS,
    DEFAULT_THEMES,
    DEFAULT_CONFIG
)


DATABASE_PATH = (
    get_app_config_dir() / "grimlock.db"
)


DATABASE_URL = (
    f"sqlite:///{DATABASE_PATH}"
)


engine = create_engine(
    DATABASE_URL,
    echo=False
)


def get_session() -> Session:
    return Session(engine)


def init_db() -> None:
    SQLModel.metadata.create_all(
        engine
    )

    with get_session() as session:
        _init_providers(session)
        _init_themes(session)
        _init_global_config(session)



def _init_providers(session: Session) -> None:

    for provider_data in DEFAULT_PROVIDERS:

        provider = session.exec(
            select(ModelProvider)
            .where(
                ModelProvider.name == provider_data["name"]
            )
        ).first()


        if provider:
            continue


        provider = ModelProvider(
            name=provider_data["name"],
            api_key=provider_data.get("api_key"),
            base_url=provider_data.get("base_url")
        )


        session.add(provider)

        session.flush()


        models = []

        for model_data in provider_data["models"]:

            models.append(
                AIModel(
                    provider_id=provider.id,
                    name=model_data["name"],
                    max_context=model_data["max_context"]
                )
            )


        session.add_all(models)


    session.commit()



def _init_themes(session: Session) -> None:

    for theme_data in DEFAULT_THEMES:

        theme = session.exec(
            select(Theme)
            .where(
                Theme.name == theme_data["name"]
            )
        ).first()


        if theme:
            continue


        session.add(
            Theme(
                name=theme_data["name"]
            )
        )


    session.commit()



def _init_global_config(session: Session) -> None:

    config = session.exec(
        select(GlobalConfig)
    ).first()


    if config:
        return


    provider = session.exec(
        select(ModelProvider)
        .where(
            ModelProvider.name == DEFAULT_CONFIG["provider"]
        )
    ).first()


    if not provider:
        raise RuntimeError(
            f"Default provider "
            f"{DEFAULT_CONFIG['provider']} not found"
        )


    model = session.exec(
        select(AIModel)
        .where(
            AIModel.provider_id == provider.id,
            AIModel.name == DEFAULT_CONFIG["model"]
        )
    ).first()

    if not model:
        raise RuntimeError(
            f"Default model "
            f"{DEFAULT_CONFIG['model']} not found"
        )

    theme = session.exec(
        select(Theme)
        .where(
            Theme.name == DEFAULT_CONFIG["theme"]
        )
    ).first()


    if not theme:
        raise RuntimeError(
            f"Default theme "
            f"{DEFAULT_CONFIG['theme']} not found"
        )


    config = GlobalConfig(
        default_model_provider_id=provider.id,
        default_ai_model_id=model.id,
        theme_id=theme.id
    )


    session.add(config)

    session.commit()