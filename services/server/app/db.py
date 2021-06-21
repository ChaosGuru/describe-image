from sqlalchemy import create_engine
from sqlalchemy.orm import relationship, scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('postgresql+pg8000://king:6530@localhost:5432/engl_games', 
                       client_encoding='utf8')

Base = declarative_base()
Base.metadata.reflect(engine)

db_session = scoped_session(sessionmaker(bind=engine))