"""
Toteuta Flask-taustapalvelu, joka ilmoittaa, onko parametrina saatu luku alkuluku vai ei.
Hyödynnä toteutuksessa aiempaa tehtävää, jossa alkuluvun testaus tehtiin.
Esimerkiksi lukua 31 vastaava GET-pyyntö annetaan muodossa: http://127.0.0.1:3000/alkuluku/31.
Vastauksen on oltava muodossa: {"Number":31, "isPrime":true}.
"""
from flask import flask, request
app = flask(__name__)


@app.route('/alku/<luku>')
def alkulukutest(luku):
    on_alku = True
    # Erityiset
    if luku == 1:
        on_alku = False
    elif luku == 2:
        on_alku = True
    # Looppi ite. Alkaa kolmesta ja nousee kahden välein. Parilliset luvut eivät voi olla alkulukuja.
    else:
        for i in range(3, luku, 2):
            if luku % i == 0:
                print(f"{luku} On jaollinen luvulla {i}!")
                on_alku = False
                break
    return on_alku
