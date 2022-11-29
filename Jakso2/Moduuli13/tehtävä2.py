from flask import Flask, Response
import json
import mysql.connector

app = Flask(__name__)
@app.route('/kenttä/<icao>')
def hae(icao):
    try:
        icao = icao
        def haenimi(icao):
            tuple = (icao,)
            sql = '''SELECT name FROM airport 
            WHERE ident= %s'''
            kursori = yhteys.cursor()
            kursori.execute(sql, tuple)
            tulos = kursori.fetchone()
            return tulos;

        def haemuni(icao):
            tuple = (icao,)
            sql = '''SELECT municipality FROM airport 
            WHERE ident= %s'''
            kursori = yhteys.cursor()
            kursori.execute(sql, tuple)
            tulos = kursori.fetchone()
            return tulos;

        yhteys = mysql.connector.connect(
            host='127.0.0.1',
            port=3306,
            database='flight_game',
            user='root',
            password='Torstai22#',
            autocommit=True
        )

        nimi = haenimi(icao)
        muni =haemuni(icao)

        tilakoodi = 200
        vastaus = {
            "status": tilakoodi,
            "icao": icao,
            "name": nimi,
            "municipality": muni,
        }

    except ValueError:
        tilakoodi = 400
        vastaus = {
            "status": tilakoodi,
            "teksti": "Virheellinen yhteenlaskettava"
        }

    jsonvast = json.dumps(vastaus)
    return Response(response=jsonvast, status=tilakoodi, mimetype="application/json")

@app.errorhandler(404)
def page_not_found(virhekoodi):
    vastaus = {
        "status" : "404",
        "teksti" : "Virheellinen päätepiste"
    }
    jsonvast = json.dumps(vastaus)
    return Response(response=jsonvast, status=404, mimetype="application/json")

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)