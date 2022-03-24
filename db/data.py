from flask import session
from .schema import Tax
from . import Session

def start():
    session = Session()
    return session

def insert(company, tax_paid, session):
    session.add(Tax(company=company, tax_paid=string2float(tax_paid)))

def stop(session):
    session.commit()
    session.close()

def string2float(string):
    return float(string.replace(',', '.'))

def get_taxes():
    session = Session()
    taxes = session.query(Tax).limit(1000).all()
    #taxes = session.query(Tax).all()
    return taxes
    