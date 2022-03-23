from db.schema import Base, Tax
from db.create import create_db
import db
create_db(Base, db.engine)