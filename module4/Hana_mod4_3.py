from fastapi import FastAPI
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Database setup
DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()

# Table definition
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    age = Column(Integer)

# Create table
Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.post("/add-users")
def add_two_users():
    db = SessionLocal()

    user1 = User(name="Shamsa", age=20)
    user2 = User(name="Mariam", age=22)

    db.add(user1)
    db.add(user2)
    db.commit()
    db.close()

    return {"message": "2 users inserted successfully"}

#uvicorn Hana_mod4_3:app --reload(use in the terminal window)

#When you run the server and send a POST request to http://127.0.0.1:8000/add-users, 
# FastAPI receives the request, opens a database connection, inserts two new rows into the users table, 
# saves the changes, closes the connection, and sends back a confirmation message.