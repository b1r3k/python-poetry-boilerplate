from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker, AsyncAttrs
from sqlalchemy.orm import DeclarativeBase, MappedAsDataclass


class Base(MappedAsDataclass, AsyncAttrs, DeclarativeBase):
    pass


async def init_db(database_url: str):
    engine = create_async_engine(database_url, echo=True, future=True)

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    return async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
