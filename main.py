from flask import Flask, render_template, request

import aiml
import os
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

kernel = aiml.Kernel()
if os.path.isfile("bot_brain.brn"):
    kernel.bootstrap(brainFile = "bot_brain.brn")
else:
    kernel.bootstrap(learnFiles = "std-startup.xml", commands = "load aiml b")
    kernel.saveBrain("bot_brain.brn")

app = Flask(__name__)

@app.route('/send', methods=['GET', 'POST'])
def send():
    if request.method == 'POST':
        message = request.form['mensagem']

        if message == "sair":
            exit()

        else:
            bot_response = kernel.respond(message)
            #print bot_response

        return render_template('index.html', bot_response = bot_response)


    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
