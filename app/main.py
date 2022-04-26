# from fastapi import FastAPI
# import databases
# from sqlalchemy import select
# from sqlalchemy import desc
# from models.users import users_table
# from models.posts import posts_table

# from .routers import users
# users.include_router(users.router)  # видимо будут вопросы 

# from app.routers import posts
# users.include_router(posts.router)

# # берем параметры БД из переменных окружения
# DB_USER = 'postgres' #environ.get("DB_USER", "user")
# DB_PASSWORD = 'rootroot' #environ.get("DB_PASSWORD", "password")
# DB_HOST = 'localhost' #environ.get("DB_HOST", "localhost")
# DB_NAME = "warehouse"
# SQLALCHEMY_DATABASE_URL = (
#     f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:5432/{DB_NAME}"
# )
# # создаем объект database, который будет использоваться для выполнения запросов
# database = databases.Database(SQLALCHEMY_DATABASE_URL)


# app = FastAPI()


# @app.on_event("startup")
# async def startup():
#     # соединение с БД при запуске приложения
#     await database.connect()


# @app.on_event("shutdown")
# async def shutdown():
#     # соединение с БД разрываем при остановке приложения
#     await database.disconnect()


# @app.get("/")
# async def read_root():
#     # изменим рут таким образом, чтобы он брал данные из БД
#     query = (
#         select(
#             [
#                 posts_table.c.id,
#                 posts_table.c.created_at,
#                 posts_table.c.item,
#                 posts_table.c.unit_of_measure,
#                 posts_table.c.quantity,
#                 posts_table.c.price_wo_vat,
#                 posts_table.c.value_wo_vat,
#                 posts_table.c.user_id,
#                 users_table.c.name.label("user_name"),
#             ]
#         )
#         .select_from(posts_table.join(users_table))
#         .order_by(desc(posts_table.c.created_at))
#     )
#     return await database.fetch_all(query)
'''Second version''' 
import uvicorn
from app.models.database import database
from app.routers import posts, users
import fastapi # import FastAPI

aplic = fastapi.FastAPI()


@aplic.on_event("startup")
async def startup():
    await database.connect()


@aplic.on_event("shutdown")
async def shutdown():
    await database.disconnect()


aplic.include_router(users.router)
aplic.include_router(posts.router)

if __name__ == "__main__":
    uvicorn.run(aplic, host="0.0.0.0", port=8000)