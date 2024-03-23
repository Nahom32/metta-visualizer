from flask import Flask,jsonify,request
from application.node_processing import change_to_node_from_mult_files
from application.edge_processing import process_edges_one
from flask_swagger_ui import get_swaggerui_blueprint
from marshmallow import Schema, fields

app = Flask(__name__)
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.yaml'

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Hyperon Graph"
    }
)

app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

@app.route("/getconn", methods=["GET"])
def index():
    nodes = change_to_node_from_mult_files("../test_files/compound_nodes.metta")
    descriptors = change_to_node_from_mult_files("../test_files/descriptor_nodes.metta")
    idx = request.args.get("id")
    edges = process_edges_one("../test_files/compound_edges.metta",idx,nodes, descriptors,"id")
    print(edges)
    return edges

    
    
    
    
    