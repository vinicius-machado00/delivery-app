from flask import Blueprint, jsonify, request

order_bp = Blueprint('order',__name__)

@order_bp.route('/order',methods=['POST'])

# JSON_Format: 
# {
#     "table" : Int, 
#     "food" : List, 
#     "drink": List
# }

def new_order():
    order_request = request.get_json()
    return "Pedido para a mesa {} feito com sucesso".format(order_request["table"])

@order_bp.route('/order',methods=['GET'])
def main_page_order():
    return 'Faça uma requisição com seu pedido'