from src.config.env_var_config import envConfig
from sqlmodel import create_engine,text
from sqlalchemy.ext.asyncio import AsyncEngine,create_async_engine


engine=AsyncEngine(
    create_engine(
        url=envConfig.DATABASE_URL,
        echo=True
    )
)


async def init_db():
    async with engine.begin() as conn:
        statement=text("SELECT 'user';")
        result= await conn.execute(statement)
        print(result.all())


