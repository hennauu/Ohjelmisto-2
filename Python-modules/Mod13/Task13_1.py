#13. Taustapalvelun ja rajapinnan rakentaminen

from flask import Flask, request, Response
import json
import math


app = Flask(__name__)


@app.route('/num')
def get_num():
    args = request.args
    try:
        num1 = float(args.get("number1"))
        num2 = float(args.get("number2"))
        sum_of_nums = num1 + num2
        response_dict = {"num1": num1, "num2": num2, "sum": sum_of_nums}
        response_json = json.dumps(response_dict)
        return Response(response=response_json, status=200,
                        mimetype="application/json")
    except TypeError:
        response_json = json.dumps({"message": "invalid parameters: missing?",
                                    "status": "400 Bad request"})
        return Response(response=response_json, status=400,
                        mimetype="application/json")
    except ValueError:
        # TODO: convert response to json & fix mimetype
        return "invalid parameter value, not a number?"

@app.route('/moro/<yourname>/<location>')
def moromoro(yourname, location):
    # example request: http://localhost:5000/moro/matti/espoo
    return f"Moro {yourname} olet paikassa {location}"

@app.errorhandler(404)
def page_not_found(error):
    # convert exception object (error) to string
    error_text = str(error)
    response_json = json.dumps({"error": error_text})
    return Response(response=response_json, status=404,
                    mimetype="application/json")

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)


