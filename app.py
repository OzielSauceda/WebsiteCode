from flask import Flask, render_template, request

app = Flask(__name__)

def readDetails(filename):
    with open(filename, 'r') as f:
        return [line for line in f]

def writeToFile(filename, message):
    with open(filename, 'a') as f:
        f.write(message)

@app.route("/")
def frontPage():
    return render_template('base.html')

@app.route("/Hobbies")
def Hobbies():
    return render_template('Hobbies.html')

@app.route("/MyMichi")
def MyMichi():
    return render_template('MyMichi.html')

@app.route("/Education")
def Education():
    return render_template('Education.html')

@app.route('/form', methods=['GET', 'POST'])
def formDemo():
    name = None
    if request.method == 'POST':
        # if request.form['name']:
        #     name = request.form['name']
        if request.form['message']:
            writeToFile('static/comments.txt', request.form['message'])

    return render_template('form.html', name=name)

if __name__=="__main__":
    app.run(debug=True, port=2000)
    
