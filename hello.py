import os
from queue import Queue

from flask import Flask, render_template, request
import random

app = Flask(__name__)
MAX_QUEUE_SIZE = 5
ORDERS_QUEUE = Queue(maxsize=MAX_QUEUE_SIZE)


def add_order_to_queue(order: str) -> None:
    """ Adds order to queue up to max size

    :param order: The order to be added to the queue
    :type order: str
    """
    if ORDERS_QUEUE.full():
        ORDERS_QUEUE.get()
    ORDERS_QUEUE.put(order)


def queue_to_list(q: Queue = ORDERS_QUEUE) -> list:
    """ Return deferenced elements in queue as a list

    :param q: Queue object to convert to list
    :type q: Queue
    :return: List of queue elements
    """
    return list(q.queue)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        order_number = request.form['order_num']
        add_order_to_queue(order=order_number)
    return render_template("index.html")


@app.route('/orders', methods=['GET'])
def display_orders():
    order_list = queue_to_list()
    print(f"Queue list: {order_list}")
    reversed_order_list = order_list[::-1]  # Makes displaying order numbers slightly easier
    return render_template("orders.html", orders=reversed_order_list)


# @app.errorhandler(404)
# def page_not_found(e):
#     return render_template('404.html'), 404

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug="True")
