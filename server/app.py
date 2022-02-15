from flask import Flask, request, jsonify
from flask_cors import CORS
from googletrans import Translator #pip install googletrans==4.0.0-rc1

app = Flask(__name__)
CORS(app)

ListOfMessages = []
translator = Translator()


def trans(text):
    result=""
    result = translator.translate(text, src='ru', dest='en')
    return result.text

def retrans(text):
    result=""
    result = translator.translate(text, src='en', dest='ru')
    return result.text


@app.route('/')
def dafault_route():
    return 'Messenger Flask server is running! ' \
            f'<br> Count of Messages {len(ListOfMessages)}'\
            '<br> <a href="/status">Check status</a>'

# отправка сообщений
@app.route("/mes", methods=['POST'])
def SendMessage():
    msg=""
    msg = request.json
    print(msg)
    # messages.append({ "UserName":"RusAl","MessageText":"Privet na sto let!!!","TimeStamp":"2021-03-05T18:23:10.932973Z"})
    msg['MessageText'] = trans(msg['MessageText'])
    ListOfMessages.append(msg)
    print(msg)
    msgtext = f"{msg['UserName']} <{msg['TimeStamp']}>: {msg['MessageText']}"
    print(f"Всего сообщений: {len(ListOfMessages)} Посланное сообщение: {msgtext}")
    return f"Сообщение отослано успшно. Всего сообщений: {len(ListOfMessages)} ", 200

# получение сообщений
@app.route("/mes/<int:id>")
def GetMessage(id):
    print(id)
    if id >= 0 and id < len(ListOfMessages):
        print(ListOfMessages[id])
        return ListOfMessages[id], 200
    else:
        return "Not found", 400

@app.route('/trans', methods=['POST'])
def rtrans():
    text = request.json
    text = text['text']
    print(text)
    result=""
    result=retrans(text)
    return jsonify(result), 200, {'Content-Type': 'application/json'}

@app.route('/status')
def status():
    allmessages = ""
    for msg in ListOfMessages:
        allmessages += "<br> " + f"{msg['UserName']} <{msg['TimeStamp']}>: {msg['MessageText']}"
    allmessages +=f'<br> Count of Messages {len(ListOfMessages)}'
    return allmessages
if __name__ == '__main__':

    app.run(host='0.0.0.0')
app.run(host='0.0.0.0')


