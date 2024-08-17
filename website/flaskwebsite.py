from flask import Flask, render_template, request

from st_AI_n.responses import response

app = Flask(__name__, template_folder='./')

@app.route('/chat_stain', methods=['GET', 'POST'])
def chat_stain():
    output = None
    if request.method == 'POST':
        user_input = request.form['user_input']


        output = response(user_input)


    return render_template('ai.html', output=output)



if __name__ == '__main__':
    app.run(debug=True, port=80)
