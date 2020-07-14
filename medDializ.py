import threading
import time
from flask import Flask, request
import random



class Pacients:
    def __init__(self):
        weight = random.uniform(75.0, 100.0)
        weight = round(weight,1)
        self.weight =  weight # рандомный вес
        self.running = True

    def start_dializ(self):
        while self.running:
            self.weight -= 0.1
            self.weight = round(self.weight, 1)
            time.sleep(5)

    def end_dializ(self):
        self.running = False

    def get_weight(self):
        print(self.weight)
        return self.weight


app = Flask(__name__)
pacient = Pacients()


@app.route('/init')
def init():
    global pacient
    pacient = Pacients()
    return 'OK'


@app.route('/start_dializ')
def start_dializ():
    global pacient
    proc = threading.Thread(target=pacient.start_dializ)
    proc.start()
    return 'OK'


@app.route('/end_dializ')
def end_dializ():
    global pacient
    pacient.end_dializ()
    return 'OK'


@app.route('/get_weight')
def get_weight():
    global pacient
    return str(pacient.get_weight())


if __name__ == '__main__':
    app.run(port = 5002)


