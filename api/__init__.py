from flask import jsonify, abort

def generate_json(taxes):
    data = []

    line = 0

    for tax in taxes:
        line += 1
        data.insert(line, [tax.company, tax.tax_paid])

    response = jsonify({'data': data})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response