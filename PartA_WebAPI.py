import sqlite3
from flask import Flask, jsonify, request, abort
from argparse import ArgumentParser

DB = 'db.sqlite'

def getRowDict(row):
    rowDict = {
        'id':row[0],
        'code':row[1],
        'name':row[2],
        'type':row[3]
    }
    return rowDict

app = Flask(__name__)

@app.route('/api/stations',methods=['GET'])
def index():
    db = sqlite3.connect(DB)
    cursor = db.cursor()
    cursor.execute('SELECT * FROM stations ORDER BY id')
    rows = cursor.fetchall()
    
    print(rows)
    
    db.close()
    
    rowsDict = []
    for row in rows:
        rowDict = getRowDict(row)
        rowsDict.append(rowDict)
        
    return jsonify(rowsDict),200


@app.route('/api/stations/<int:station>',methods=['GET'])
def show(station):
    db = sqlite3.connect(DB)
    cursor = db.cursor()
    cursor.execute('SELECT * FROM stations WHERE id = ?', (str(station),))
    row = cursor.fetchone()
    
    db.close()
    
    if row:
        rowDict = getRowDict(row)
        return jsonify(rowDict),200
    else:
        return jsonify(None),200


@app.route('/api/stations',methods=['POST'])
def store():
    if not request.json:
        abort(404)
        
    newStation = (
            request.json['code'],
            request.json['name'],
            request.json['type']
            )
    
    db = sqlite3.connect(DB)
    cursor = db.cursor()
    cursor.execute('''INSERT INTO stations(code,name,type) VALUES(?,?,?)''',newStation)
    stationID = cursor.lastrowid
    
    db.commit()
    
    response = {
            'id': stationID,
            'affected':db.total_changes
            }
    
    db.close()
        
    return jsonify(response),201


@app.route('/api/stations/<int:station>',methods=['PUT'])
def update(station):
    if not request.json:
        abort(404)
        
    if 'id' not in request.json:
        abort(400)

    if int(request.json['id']) != station:
        abort(400)

    updateStation = (
            request.json['code'],
            request.json['name'],
            request.json['type'],
            str(station))
    
    db = sqlite3.connect(DB)
    cursor = db.cursor()
    cursor.execute('''UPDATE stations SET code=?, name=?, type=? WHERE id=? ''',updateStation)
    db.commit()
    
    response = {
            'id': station,
            'affected':db.total_changes
            }
    
    db.close()
        
    return jsonify(response),201


@app.route('/api/stations',methods=['DELETE'])
def delete(station):
    if not request.json:
        abort(400)

    if 'id' not in request.json:
        abort(400)

    if int(request.json['id']) != station:
        abort(400)

    db = sqlite3.connect(DB)
    cursor = db.cursor()

    cursor.execute('DELETE FROM stations WHERE id=?', (str(station),))

    db.commit()

    response = {
        'id': station,
        'affected': db.total_changes,
    }

    db.close()

    return jsonify(response), 201


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('-p', '--port', default=8888, type=int, help='port to listen on')
    args = parser.parse_args()
    port = args.port

    app.run(host='127.0.0.1', port=port)