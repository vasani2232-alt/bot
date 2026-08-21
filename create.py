from flask import Flask, request, render_template_string

app = Flask(__name__)

html = '''
<h2>Mini Chatbot</h2>
<form method="POST">
    <input name="msg" placeholder="Type message">
    <button type="submit">Send</button>
</form>
{% if reply %}
<p><b>Bot:</b> {{reply}}</p>
{% endif %}
'''

@app.route('/', methods=['GET', 'POST'])
def chat():
    reply = ""
    if request.method == 'POST':
        msg = request.form['msg'].lower()

        if msg == 'hello':
            reply = 'Hello, How can I help you?'
        # elif msg == 'how can i help u':
        #     reply = 'Python is great for AI.'
        elif msg == 'python':
            reply = 'Python is great for AI.'
        elif msg == 'great':
            reply = 'Thank You!'
        else:
            reply = 'I am still learning.'

    return render_template_string(html, reply=reply)

if __name__ == '__main__':
    app.run(debug=True)