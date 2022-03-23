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
