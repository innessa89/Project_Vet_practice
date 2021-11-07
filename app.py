from flask import Flask,render_template
from controllers.animal_controller import animals_blueprint
from controllers.owner_controller import owners_blueprint
from controllers.vet_controller import vets_blueprint
# from controllers.treatment_controller import treatments_blueprint

app = Flask(__name__)

app.register_blueprint(animals_blueprint)
@app.route('/')
def animals():
    return render_template('index.html')


app.register_blueprint(owners_blueprint)
@app.route('/')
def owners():
    return render_template('index.html')

app.register_blueprint(vets_blueprint)
@app.route('/')
def vets():
    return render_template('index.html')


# app.register_blueprint(treatments_blueprint)
# @app.route('/')
# def treatments():
#     return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)