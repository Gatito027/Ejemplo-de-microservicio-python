import os
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:mimiau@localhost/COIL'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
port = int(os.environ.get('PORT', 5000))

@app.route("/")
def home():
    return "Hello, this is a Flask Microservice"

@app.route('/alumnos', methods=['GET'])
def get_alumnos():
    try:
        result = db.session.execute(text("SELECT * FROM get_alumnos()"))
        alumnos = []
        for row in result:
            alumno = {
                'id': row.id,
                'nombre': row.nombre,
                'apellidos': row.apellidos,
                'matricula_dni': row.matricula_dni,
                'genero': row.genero,
                'id_usuario_id_id': row.id_usuario_id_id,
                'universidad_origen_id': row.universidad_origen_id
            }
            alumnos.append(alumno)
        return jsonify(alumnos)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/datosAlumno', methods=['GET'])
def get_datos_alumno():
    try:
        result = db.session.execute(text("SELECT * FROM obtenerUsuarioAlumno()"))
        datosAlumnos = []
        for row in result:
            datosAlumno = {
                'id': row.id,
                'correo_institucional': row.correo_institucional,
                'nombre_usuario': row.nombre_usuario,
                'nombre': row.nombre,
                'apellidos': row.apellidos,
                'matricula': row.matricula,
                'genero': row.genero
            }
            datosAlumnos.append(datosAlumno)
        return jsonify(datosAlumnos)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

from flask import request

@app.route('/eliminarDatosAlumno', methods=['POST'])
def eliminar_datos_alumno():
    try:
        id = request.json.get('id')
        result = db.session.execute(text("SELECT eliminarUsuarioAlumno(:id)"), {'id': id})
        db.session.commit()  # Asegúrate de confirmar la transacción
        if result.scalar():
            return jsonify("Eliminado con éxito")
        else:
            return jsonify("Error al eliminar")
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=port)
