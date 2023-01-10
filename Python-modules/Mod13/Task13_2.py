import mysql.connector
from flask import Flask, Response

yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='root',
    password='henna',
    autocommit=True
)

app = Flask(__name__)


@app.route('/kentta/<ident>')
def tiedot(ident):
    sql = "SELECT ident, name, municipality FROM airport WHERE ident = '" + ident + "'"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchone()
    print(tulos)

    json = {
        "ICAO": tulos[0],
        "Name": tulos[2],
        "Municipality": tulos[1]
    }
    return json


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)