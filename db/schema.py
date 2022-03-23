from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (Column, String, Integer, Float, DateTime)
import datetime

Base = declarative_base()

class Tax(Base):
    __tablename__ = 'tax'
    id = Column(Integer, primary_key=True)
    company = Column(String)
    tax_paid = Column(Float)
    create_time = Column(DateTime, default=datetime.datetime.utcnow)

    def __repr__(self):
        return "<Tax(company='%s', tax_paid='%s')>" % (self.company, self.tax_paid)