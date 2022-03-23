from flask import Flask
import sqlite3


app = Flask(__name__)

#testi 

def taxes2html(taxes):
    html = '<h1>Top 100 tax paying companies in 2020</h1>'
    html += '<table>'
    for tax in taxes:
        html += '<tr><td>{}</td><td>{}</td></tr>'.format(tax[0], tax[1])
    html += '</table>'
    return html

@app.route('/taxes')
def taxes():
    db = sqlite3.connect('test.db')
    cur = db.cursor()
    #cur.execute('select * from tax order by tax_paid desc limit 100')
    cur.execute('select * from tax where company like "%finland%"')
    taxes = cur.fetchall()
    db.close()
    return taxes2html(taxes)

#def taxes2html(taxes):



@app.route('/')
def index():
    return '<h1>Hello World!</h1>'

if __name__ == '__main__':
    app.run(debug=True)