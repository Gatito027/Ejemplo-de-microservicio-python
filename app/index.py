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

@app.route('/eliminarDatosAlumno', methods=['POST'])
def eliminar_datos_alumno():
    try:
        id = request.json.get('id')
        result = db.session.execute(text("SELECT eliminarUsuarioAlumno(:id)"), {'id': id})
        db.session.commit()
        if result.scalar():
            return jsonify("Eliminado con éxito")
        else:
            return jsonify("Error al eliminar")
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/insertarDatosAlumno', methods=['POST'])
def insertar_datos_alumno():
    try:
        password = request.json.get('password')
        nombre_usuario = request.json.get('nombre_usuario')
        correo_institucional = request.json.get('correo_institucional')
        nombre = request.json.get('nombre')
        apellidos = request.json.get('apellidos')
        matricula_dni = request.json.get('matricula_dni')
        genero = request.json.get('genero')
        universidad_origen_id = request.json.get('universidad_origen_id')
        #query
        result = db.session.execute(
            text("SELECT insertarUsuarioAlumno(:password, :nombre_usuario, :correo_institucional, :nombre, :apellidos, :matricula_dni, :genero, :universidad_origen_id)"), 
            {
                'password': password,
                'nombre_usuario': nombre_usuario,
                'correo_institucional': correo_institucional,
                'nombre': nombre,
                'apellidos': apellidos,
                'matricula_dni': matricula_dni,
                'genero': genero,
                'universidad_origen_id': universidad_origen_id
            }
        )
        db.session.commit()
        if result.scalar():
            return jsonify("Insertado con éxito")
        else:
            return jsonify("Error al insertar")
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/actualizarDatosAlumno', methods=['POST'])
def actualizar_datos_alumno():
    try:
        id = request.json.get('id')
        password = request.json.get('password')
        nombre_usuario = request.json.get('nombre_usuario')
        correo_institucional = request.json.get('correo_institucional')
        nombre = request.json.get('nombre')
        apellidos = request.json.get('apellidos')
        matricula_dni = request.json.get('matricula_dni')
        genero = request.json.get('genero')
        universidad_origen_id = request.json.get('universidad_origen_id')
        #query
        result = db.session.execute(
            text("SELECT actualizarUsuarioAlumno(:id, :password, :nombre_usuario, :correo_institucional, :nombre, :apellidos, :matricula_dni, :genero, :universidad_origen_id)"), 
            {
                'id': id,
                'password': password,
                'nombre_usuario': nombre_usuario,
                'correo_institucional': correo_institucional,
                'nombre': nombre,
                'apellidos': apellidos,
                'matricula_dni': matricula_dni,
                'genero': genero,
                'universidad_origen_id': universidad_origen_id
            }
        )
        db.session.commit()
        if result.scalar():
            return jsonify("Actualizado con éxito")
        else:
            return jsonify("Error al actualizar")
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=port)
