from flask import Flask, jsonify, request
from flask_cors import CORS
from controllers import wip
#from werkzeug import exceptions


server = Flask(__name__)
CORS(server)


@server.route('/')
def home():
    return jsonify({'message': 'Working without errors'}), 200


@server.route('/wip', methods=['GET,' 'POST'])
def wip_handler():
    fns = {
        'GET': wip.index,
        'POST': wip.create
    }

    resp, code = fns[request.method](request)
    return jsonify(resp), code

@server.errorhandler(exceptions.NotFound)
def handle_404(err):
    return {'message': f'Nope {err}'}, 404

if __name__ == "__main__":
    server.run(debug=True)