from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import TIMESTAMP
from .database import Base

class Post(Base):
    __tablename__ =  "posts"
    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable = False)
    content = Column(String, nullable = False)
    published = Column(Boolean, server_default='TRUE', nullable=False)
    create_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    owner_id = Column(Integer, ForeignKey("users.id",ondelete = "CASCADE"), nullable = False)
    owner = relationship("User")

class User(Base):
    __tablename__ = "users"
    email = Column(String, nullable=False, unique = True)
    password = Column(String, nullable = False)
    id = Column(Integer, primary_key = True, nullable = False)
    create_at = Column(TIMESTAMP(timezone=True), 
                        nullable =False, 
                        server_default = text('now()'))
    phone_number = Column(String)
class Vote(Base):
    __tablename__ = "votes"
    user_id = Column(Integer, ForeignKey("users.id",
                        ondelete = "CASCADE"),primary_key=True)
    post_id = Column(Integer, ForeignKey("posts.id",
                        ondelete = "CASCADE"),primary_key=True)