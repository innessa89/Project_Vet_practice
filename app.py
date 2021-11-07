from flask import Flask,render_template
from controllers.vet_practice_controller import animals_blueprint

app = Flask(__name__)


app.register_blueprint(animals_blueprint)

@app.route('/')
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)