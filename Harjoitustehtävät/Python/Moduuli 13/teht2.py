"""
Toteuta taustapalvelu, joka palauttaa annettua lentokentän ICAO-koodia
    vastaavan lentokentän nimen ja kaupungin JSON-muodossa.
Tiedot haetaan opintojaksolla käytetystä lentokenttätietokannasta.
Esimerkiksi EFHK-koodia vastaava GET-pyyntö annetaan muodossa: http://127.0.0.1:3000/kenttä/EFHK.
Vastauksen on oltava muodossa: {"ICAO":"EFHK", "Name":"Helsinki Vantaa Airport", "Municipality":"Helsinki"}.
"""
from flask import Flask, Response
import json
import mysql.connector

yhteys = mysql.connector.connect(
         host='localhost',
         port=3306,
         database='flight_game',
         user='user1',
         password='sala1',
         autocommit=True
         )
app = Flask(__name__)


@app.route('/kenttä/<icao>')
def airportfinder(icao):
    # Jostain syystä suoritus ei ikinä pysähdy ekaan virheeseen, vaan tulee aina vaan viimeinen eli 404.
    try:
        try:
            icao = icao.upper()
        except AttributeError:
            return Response(
                response="This is not a valid ICAO code. Error code 400",
                status=400, mimetype="application/json")

        query = f"SELECT name, municipality from airport WHERE ident= '{icao}'"
        kursori = yhteys.cursor()
        kursori.execute(query)
        tulos = kursori.fetchone()
        tulos = {"ICAO": icao, "Name": tulos[0], "Municipality": tulos[1]}
        jsonvast = json.dumps(tulos)
        return Response(response=jsonvast, mimetype="application/json")

    except TypeError:
        return Response(response="Can't find an airport with that ICAO -code. Error code 404",
                        status=404, mimetype="application/json")



if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
