import os
from flask import Flask, jsonify
Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:mimiau@localhost/COIL'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
port = int(os.environ.get('PORT', 5000))


class PlataformaAlumno(db.Model):
    __tablename__ = 'plataforma_alumno'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    apellidos = db.Column(db.String(50), nullable=False)
    matricula_dni = db.Column(db.String(20), nullable=False)
    genero = db.Column(db.String(1), nullable=False)
    id_usuario_id_id = db.Column(db.Integer, nullable=False)
    universidad_origen_id = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'apellidos': self.apellidos,
            'matricula_dni': self.matricula_dni,
            'genero': self.genero,
            'id_usuario_id_id': self.id_usuario_id_id,
            'universidad_origen_id': self.universidad_origen_id
        }

@app.route("/")
def home():
    return "Hello, this is a Flask Microservice"
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=port)

#consultar datos alumnos
@app.route('/alumnos', methods=['GET'])
def get_alumnos():
    alumnos = PlataformaAlumno.query.all()
    return jsonify([alumno.to_dict() for alumno in alumnos])
if __name__ == '__main__':
    app.run(debug=True)