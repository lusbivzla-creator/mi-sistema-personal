from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Lista inicial mejorada con campos extra
personal_list = [
    {"nombre": "Andreina", "apellido": "Ortega", "telefono": "+584140667077", "fecha": "2026-06-10", "color": "bg-pink-200"},
    {"nombre": "Ragnar", "apellido": "Vikingo", "telefono": "+58XXXXXXXXX", "fecha": "2026-06-01", "color": "bg-blue-200"}
]

@app.route('/')
def index():
    return render_template('index.html', personal=personal_list)

@app.route('/personal')
def personal():
    return render_template('personal.html', personal=personal_list)

# Ruta para agregar personal con todos los campos
@app.route('/agregar_personal', methods=['POST'])
def agregar_personal():
    nuevo_empleado = {
        "nombre": request.form.get('nombre'),
        "apellido": request.form.get('apellido'),
        "telefono": request.form.get('telefono'),
        "fecha": request.form.get('fecha_ingreso'),
        "color": "bg-gray-200"
    }
    personal_list.append(nuevo_empleado)
    return redirect(url_for('personal'))

# Ruta para detalle, ahora recibe el índice (id) del empleado
@app.route('/detalle_personal')
def detalle_personal():
    # Buscamos el índice en la URL (ej: /detalle_personal?index=0)
    index = int(request.args.get('index', 0))
    empleado = personal_list[index]
    return render_template('detalle_personal.html', empleado=empleado)

if __name__ == '__main__':
    app.run(debug=True)