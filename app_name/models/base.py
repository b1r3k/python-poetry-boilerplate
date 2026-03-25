from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker, AsyncAttrs
from sqlalchemy.orm import DeclarativeBase, MappedAsDataclass


class Base(MappedAsDataclass, AsyncAttrs, DeclarativeBase):
    pass


async def init_db(database_url: str, ssl_mode: str = "disable"):
    connect_args: dict = {}
    if ssl_mode and ssl_mode != "disable":
        connect_args["ssl"] = ssl_mode
    engine = create_async_engine(database_url, echo=True, future=True, connect_args=connect_args)

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    return async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
