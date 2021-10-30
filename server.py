import json
from flask import Flask

from Password import Password

app = Flask(__name__)

@app.route('/password/genertion/<count_symbols>')
def generation_password(count_symbols):
    password = Password()
    if count_symbols.isdigit():
        password.generation(int(count_symbols))
    else:
        password.generation(None)

    response = app.response_class(
        response=json.dumps({
            "version_app": "0.0.4",
            "count_array_symbols": f'{len(password.get_array_symbols)}',
            "count_variant": f'{password.count_variant}',
            "password": f'{password.password}'
            }),
        status=200,
        minetype='application/json'
    )

    return response

if __name__ == "__main__":
    app.run(host="127.0.0.1", port="5000")
