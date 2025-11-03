from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/confidentialite')
def confidentialite():
    return render_template('confidentialité.html')

@app.route('/tableau')
def tableau():
    return render_template('tableau de bord.html')

@app.route('/generer')
def generer():
    return render_template('générer.html')

@app.route('/histoire')
def histoire():
    return render_template('histoire.html')

if __name__ == '__main__':
    app.run(debug=True)
