from flask import Flask, Response
import json

app = Flask(__name__)
@app.route('/alkuluku/<luku1>')
def alkuluku(luku1):
    onAlku = False
    try:
        luku1 = int(luku1)
        if luku1 > 1:
            for i in range(2, luku1):
                if (luku1 % i) == 0:
                    onAlku = True
                    break
        if onAlku:
            isPrime = False

        else:
            isPrime = True
        tilakoodi = 200
        vastaus = {
            "status": tilakoodi,
            "Luku": luku1,
            "isPrime": isPrime
        }

    except ValueError:
        tilakoodi = 400
        vastaus = {
            "status": tilakoodi,
            "teksti": "Virheellinen luku"
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



