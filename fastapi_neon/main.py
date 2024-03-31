# # # fastapi_neon/main.py
# # from typing import Union
# # from fastapi import FastAPI
# # app = FastAPI()
# # @app.get("/")
# # def read_root():
# #     return {"Hello": "World"}
# # @app.get("/items/{item_id}")
# # def read_item(item_id: int, q: Union[str, None] = None):
# #     return {"item_id": item_id, "q": q}


# # fastapi_neon/main.py

# from contextlib import asynccontextmanager

# from typing import Union, Optional

# from fastapi_neon import settings

# from sqlmodel import Field, Session, SQLModel, create_engine, select



# from fastapi import FastAPI



# class Todo(SQLModel, table=True):

#     id: Optional[int] = Field(default=None, primary_key=True)

#     content: str = Field(index=True)



# # only needed for psycopg 3 - replace postgresql

# # with postgresql+psycopg in settings.DATABASE_URL

# connection_string = str(settings.DATABASE_URL).replace(

#     "postgresql", "postgresql+psycopg2"

# )



# # recycle connections after 5 minutes

# # to correspond with the compute scale down

# engine = create_engine(

#     connection_string, connect_args={"sslmode": "require"}, pool_recycle=300

# )



# def create_db_and_tables():

#     SQLModel.metadata.create_all(engine)



# # The first part of the function, before the yield, will

# # be executed before the application starts

# @asynccontextmanager

# async def lifespan(app: FastAPI):

#     print("Creating tables..")

#     create_db_and_tables()

#     yield



# app = FastAPI(lifespan=lifespan)



# @app.get("/")

# def read_root():

#     return {"Hello": "World"}



# @app.post("/todos/")

# def create_todo(todo: Todo):

#     with Session(engine) as session:

#         session.add(todo)

#         session.commit()

#         session.refresh(todo)

#         return todo






#     return f"Todo with id {id} has been deleted"


# @app.get("/todos/")

# def read_todos():

#     with Session(engine) as session:

#         todos = session.exec(select(Todo)).all()

#         return todos



# main.py
from contextlib import asynccontextmanager
from typing import Union, Optional, Annotated
from fastapi_neon import settings
from sqlmodel import Field, Session, SQLModel, create_engine, select
from fastapi import FastAPI, Depends


class Todo(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    content: str = Field(index=True)


# only needed for psycopg 3 - replace postgresql
# with postgresql+psycopg in settings.DATABASE_URL
connection_string = str(settings.DATABASE_URL).replace(
    "postgresql", "postgresql+psycopg"
)


# recycle connections after 5 minutes
# to correspond with the compute scale down
engine = create_engine(
    connection_string, connect_args={"sslmode": "require"}, pool_recycle=300
)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


# The first part of the function, before the yield, will
# be executed before the application starts.
# https://fastapi.tiangolo.com/advanced/events/#lifespan-function
@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Creating tables..")
    create_db_and_tables()
    yield


app = FastAPI(lifespan=lifespan, title="Hello World API with DB", 
    version="0.0.1",
    servers=[
        {
            "url": "http://127.0.0.1:8000", # ADD NGROK URL Here Before Creating GPT Action
            "description": "Development Server"
        }
        ])

def get_session():
    with Session(engine) as session:
        yield session


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/todos/", response_model=Todo)
def create_todo(todo: Todo, session: Annotated[Session, Depends(get_session)]):
        session.add(todo)
        session.commit()
        session.refresh(todo)
        return todo


@app.get("/todos/", response_model=list[Todo])
def read_todos(session: Annotated[Session, Depends(get_session)]):
        todos = session.exec(select(Todo)).all()
        return todos