from flask import Flask, send_from_directory
import os

app = Flask(__name__, static_folder='.', static_url_path='')

# 🔹 Page d'accueil
@app.route('/')
def home():
    return send_from_directory('.', 'index.html')

# 🔹 Toutes les autres pages HTML (about, contact, etc.)
@app.route('/<path:filename>')
def serve_file(filename):
    # Si c'est un fichier existant, on l'envoie directement
    if os.path.exists(filename):
        return send_from_directory('.', filename)
    # Sinon on renvoie vers l'accueil
    return send_from_directory('.', 'index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
