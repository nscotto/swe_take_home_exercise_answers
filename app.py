from calculator import infix_eval, prefix_eval
from flask import Flask, request, render_template
from urllib.parse import unquote

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', defaults={'q': None,})
@app.route('/<string:q>')
def index(q=None):
    process = {'infix': infix_eval, 'prefix': prefix_eval}

    # check query string
    if request.args and 'mode' in request.args and 'op' in request.args:
        mode = request.args['mode']
        operation = unquote(request.args['op'])
        try:
            result = process[mode](operation)
            return render_template(
                'index.html', operation=operation, result=result, mode=mode)
        except:
            pass

    return render_template('index.html')


if __name__ == '__main__':
    app.run()
