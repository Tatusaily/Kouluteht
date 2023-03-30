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
    try:
        if icao.isnumeric:
            raise AttributeError
        else:
            icao = icao.upper()

            query = f"SELECT name, municipality from airport WHERE ident= '{icao}'"
            kursori = yhteys.cursor()
            kursori.execute(query)
            tulos = kursori.fetchone()
            tulos = {"ICAO": icao, "Name": tulos[0], "Municipality": tulos[1]}
            jsonvast = json.dumps(tulos)
            return Response(response=jsonvast, mimetype="application/json")

    except AttributeError:
        return Response(
            response="This is not a valid ICAO code.",
            status=400, mimetype="application/json")
    except TypeError:
        return Response(response="Can't find an airport with that ICAO -code.",
                        status=404, mimetype="application/json")


# Jos käyttäjä kirjoittaa urlin väärin niin napataan se virhe
# En tee sillä virheellä mitään, mutta erotan sen muista virheistä tällä.
@app.errorhandler(404)
def notfound(error):
    return Response(response=f"{error}",
                    status=404, mimetype="application/json")


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
