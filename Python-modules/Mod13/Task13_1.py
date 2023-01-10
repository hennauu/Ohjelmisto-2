#13. Taustapalvelun ja rajapinnan rakentaminen

from flask import Flask, request, Response
import json
import math

app = Flask(__name__)


@app.route('/alkuluku/<luku>')
def alkuluku(luku):
    try:
        luku = int(luku)
        for i in range(2, luku // 2 + 1):
            if luku % i == 0:
                response_dict = {"Number": luku, "isPrime": False}
                response_json = json.dumps(response_dict)
                return Response(response=response_json, status=200, mimetype="application/json")
        else:
            response_dict = {"Number": luku, "isPrime": True}
            response_json = json.dumps(response_dict)
            return Response(response=response_json, status=200, mimetype="application/json")

    except ValueError:
        response_json = json.dumps("Virheellinen syöte.")
        return Response(response=response_json, mimetype="application/json")


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)


