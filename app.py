import os
from flask import Flask, render_template, request, redirect, session
# from flaskext.mysql import MySQL
from flask_mysqldb import MySQL
from datetime import datetime
import base64
from werkzeug.security import generate_password_hash, check_password_hash
import pymysql
import MySQLdb

# Crear la aplicación
app = Flask(__name__, template_folder='templates')

# Crear una llave secreta
app.secret_key = "dicresoft"

# Crear una conexión a la base de datos
mysql = MySQL()
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'jh'

# Inicializar la aplicación
mysql.init_app(app)

def generar_pagina_producto(idProducto):
    cursor = mysql.get_db().cursor()
    cursor.execute("SELECT * FROM producto WHERE idProducto = %s", (idProducto,))
    producto = cursor.fetchone()
    cursor.close()

    if producto:
        idProducto, nombre, cantidad, categoria, precio, imagen_blob, descripcion = producto
        imagen_base64 = base64.b64encode(imagen_blob).decode('utf-8')
        producto_dict = {
            'idProducto': idProducto,
            'nombre': nombre,
            'precio': precio,
            'imagen': imagen_base64,
            'descripcion': descripcion
        }

        with open(f'templates/sitio/productos{idProducto}.html', 'w') as f:
            f.write(render_template('sitio/producto_template.html', producto=producto_dict))

@app.route('/adminAGGProductos', methods=['GET', 'POST'])
def adminAGGProductos():
    if request.method == 'POST':
        try:
            nombre = request.form['nombre']
            cantidad = request.form['cantidad']
            categoria = request.form['categoria']
            precio = request.form['precio']
            imagen = request.files['imagen'].read()
            descripcion = request.form['descripcion']

            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO producto (nombre, cantidad, categoria, precio, imagen, descripcion) VALUES (%s, %s, %s, %s, %s, %s)",
                           (nombre, cantidad, categoria, precio, imagen, descripcion))
            conn.commit()
            idProducto = cursor.lastrowid
            cursor.close()
            conn.close()

            generar_pagina_producto(idProducto)
            return redirect('/adminAGGProductos')
        except Exception as e:
            print(f"Error al agregar el producto: {e}")
            return render_template('admin/adminAGGProductos.html', error="Error al agregar el producto. Por favor, intente nuevamente.")
    
    cursor = mysql.get_db().cursor()
    cursor.execute("SELECT * FROM producto")
    productos = cursor.fetchall()
    cursor.close()

    productos_con_imagenes = []
    for producto in productos:
        idProducto = producto[0]
        nombre = producto[1]
        cantidad = producto[2]
        categoria = producto[3]
        precio = producto[4]
        imagen_blob = producto[5]
        descripcion = producto[6]

        imagen_base64 = base64.b64encode(imagen_blob).decode('utf-8')

        productos_con_imagenes.append({
            'idProducto': idProducto,
            'nombre': nombre,
            'cantidad': cantidad,
            'categoria': categoria,
            'precio': precio,
            'imagen': imagen_base64,
            'descripcion': descripcion
        })

    return render_template('admin/adminAGGProductos.html', productos=productos_con_imagenes)

@app.route('/eliminarProducto/<int:idProducto>', methods=['POST'])
def eliminarProducto(idProducto):
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM producto WHERE idProducto = %s", (idProducto,))
        conn.commit()
        cursor.close()
        conn.close()
        return redirect('/adminAGGProductos')
    except Exception as e:
        print(f"Error al eliminar el producto: {e}")
        return redirect('/adminAGGProductos', error="Error al eliminar el producto. Por favor, intente nuevamente.")


@app.route('/productos/<int:idProducto>')
def producto(idProducto):
    cursor = mysql.get_db().cursor()
    cursor.execute("SELECT * FROM producto WHERE idProducto = %s", (idProducto,))
    producto = cursor.fetchone()
    cursor.close()

    if producto:
        idProducto, nombre, cantidad, categoria, precio, imagen_blob, descripcion = producto
        imagen_base64 = base64.b64encode(imagen_blob).decode('utf-8')
        producto_dict = {
            'idProducto': idProducto,
            'nombre': nombre,
            'precio': precio,
            'imagen': imagen_base64,
            'descripcion': descripcion
        }
        return render_template('sitio/producto_template.html', producto=producto_dict)
    else:
        return "Producto no encontrado", 404

@app.route('/catalogo')
def catalogo():
    cursor = mysql.get_db().cursor()
    cursor.execute("SELECT * FROM producto WHERE categoria = 'masvendidos'")
    productos = cursor.fetchall()
    cursor.close()

    productos_con_imagenes = []
    for producto in productos:
        idProducto = producto[0]
        nombre = producto[1]
        cantidad = producto[2]
        categoria = producto[3]
        precio = producto[4]
        imagen_blob = producto[5]
        descripcion = producto[6]

        imagen_base64 = base64.b64encode(imagen_blob).decode('utf-8')

        productos_con_imagenes.append({
            'idProducto': idProducto,
            'nombre': nombre,
            'cantidad': cantidad,
            'categoria': categoria,
            'precio': precio,
            'imagen': imagen_base64,
            'descripcion': descripcion
        })

    return render_template('sitio/catalogo.html', productos=productos_con_imagenes)

@app.route('/plantas')
def plantas():
    cursor = mysql.get_db().cursor()
    cursor.execute("SELECT * FROM producto WHERE categoria = 'plantas'")
    productos = cursor.fetchall()
    cursor.close()

    productos_con_imagenes = []
    for producto in productos:
        idProducto = producto[0]
        nombre = producto[1]
        cantidad = producto[2]
        categoria = producto[3]
        precio = producto[4]
        imagen_blob = producto[5]
        descripcion = producto[6]

        imagen_base64 = base64.b64encode(imagen_blob).decode('utf-8')

        productos_con_imagenes.append({
            'idProducto': idProducto,
            'nombre': nombre,
            'cantidad': cantidad,
            'categoria': categoria,
            'precio': precio,
            'imagen': imagen_base64,
            'descripcion': descripcion
        })

    return render_template('sitio/plantas.html', productos=productos_con_imagenes)

@app.route('/fertilizantes')
def fertilizantes():
    cursor = mysql.get_db().cursor()
    cursor.execute("SELECT * FROM producto WHERE categoria = 'fertilizantes'")
    productos = cursor.fetchall()
    cursor.close()

    productos_con_imagenes = []
    for producto in productos:
        idProducto = producto[0]
        nombre = producto[1]
        cantidad = producto[2]
        categoria = producto[3]
        precio = producto[4]
        imagen_blob = producto[5]
        descripcion = producto[6]

        imagen_base64 = base64.b64encode(imagen_blob).decode('utf-8')

        productos_con_imagenes.append({
            'idProducto': idProducto,
            'nombre': nombre,
            'cantidad': cantidad,
            'categoria': categoria,
            'precio': precio,
            'imagen': imagen_base64,
            'descripcion': descripcion
        })

    return render_template('sitio/fertilizantes.html', productos=productos_con_imagenes)

@app.route('/herramientas')
def herramientas():
    cursor = mysql.get_db().cursor()
    cursor.execute("SELECT * FROM producto WHERE categoria = 'herramientas'")
    productos = cursor.fetchall()
    cursor.close()

    productos_con_imagenes = []
    for producto in productos:
        idProducto = producto[0]
        nombre = producto[1]
        cantidad = producto[2]
        categoria = producto[3]
        precio = producto[4]
        imagen_blob = producto[5]
        descripcion = producto[6]

        imagen_base64 = base64.b64encode(imagen_blob).decode('utf-8')

        productos_con_imagenes.append({
            'idProducto': idProducto,
            'nombre': nombre,
            'cantidad': cantidad,
            'categoria': categoria,
            'precio': precio,
            'imagen': imagen_base64,
            'descripcion': descripcion
        })

    return render_template('sitio/herramientas.html', productos=productos_con_imagenes)

@app.route('/accesorios')
def accesorios():
    cursor = mysql.get_db().cursor()
    cursor.execute("SELECT * FROM producto WHERE categoria = 'accesorios'")
    productos = cursor.fetchall()
    cursor.close()

    productos_con_imagenes = []
    for producto in productos:
        idProducto = producto[0]
        nombre = producto[1]
        cantidad = producto[2]
        categoria = producto[3]
        precio = producto[4]
        imagen_blob = producto[5]
        descripcion = producto[6]

        imagen_base64 = base64.b64encode(imagen_blob).decode('utf-8')

        productos_con_imagenes.append({
            'idProducto': idProducto,
            'nombre': nombre,
            'cantidad': cantidad,
            'categoria': categoria,
            'precio': precio,
            'imagen': imagen_base64,
            'descripcion': descripcion
        })

    return render_template('sitio/accesorios.html', productos=productos_con_imagenes)


@app.route('/guardar_contacto', methods=['POST'])
def guardar_contacto():
    nombre = request.form['nombre']
    correo = request.form['email']
    telefono = request.form['telefono']
    mensaje = request.form['mensaje']
    fecha = datetime.now().strftime('%Y-%m-%d')
    estado = 'Pendiente'  

    cursor = mysql.connection.cursor()
    cursor.execute('INSERT INTO contacto (nombre, correo, telefono, fecha, estado, mensaje) VALUES (%s, %s, %s, %s, %s, %s)', 
               (nombre, correo, telefono, fecha, estado, mensaje))

    mysql.connection.commit()
    cursor.close()

    return redirect('contacto')

@app.route('/contacto')
def contacto():
    return render_template('sitio/contacto.html')


@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        correo = request.form['correo']
        contrasena = request.form['contrasena']
        confirmarContrasena = request.form['confirmarContrasena']
        
        # hashed_password = generate_password_hash(contrasena, method='sha256')
        hashed_password = generate_password_hash(contrasena, method='pbkdf2:sha256')

        rol = 'usuario'
        
        conn = mysql.connect()
        # conn = MySQLdb.connect()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO usuario (idUsuario, nombre, apellido, correo, contrasena, rol) VALUES (NULL, %s, %s, %s, %s, %s)', (nombre, apellido, correo, hashed_password, rol))
        conn.commit()
        cursor.close()
        conn.close()
        
        return redirect('inicioSesion')
    
    return render_template('sitio/registro.html')

@app.route('/inicioSesion', methods=['GET', 'POST'])
def inicioSesion():
    if request.method == 'POST':
        correo = request.form['correo']
        contrasena = request.form['contrasena']

        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM usuario WHERE correo = %s", (correo,))
        usuario = cursor.fetchone()
        cursor.close()
        conn.close()

        if usuario and check_password_hash(usuario[4], contrasena):  # La contraseña es la columna 4
            session['correo'] = correo
            return redirect('/')
        else:
            return render_template('sitio/index.html', error='Correo o contraseña incorrectos')

    return render_template('sitio/inicioSesion.html')

@app.route('/')
def index():
    return render_template('sitio/index.html')

#---------------------------------------------------------------------------

@app.route('/olvidarContrasena', methods=['GET', 'POST'])
def olvidarContrasena():
    return render_template('sitio/olvidarContrasena.html')

@app.route('/producto_template')
def producto_template():
    return render_template('sitio/producto_template.html')

@app.route('/adminMasvendidos')
def adminMasvendidos():
    return render_template('admin/adminMasvendidos.html')

@app.route('/adminFertilizantes')
def adminFertilizantes():
    return render_template('admin/adminFertilizantes.html')

@app.route('/adminHerramientas')
def adminHerramientas():
    return render_template('admin/adminHerramientas.html')

@app.route('/adminAccesorios')
def adminAccesorios():
    return render_template('admin/adminAccesorios.html')

@app.route('/servicios')
def servicios():
    return render_template('sitio/servicios.html')

@app.route('/cerrarSesion')
def cerrarSesion():
    return render_template('sitio/cerrarSesion.html')

@app.route('/carrito')
def carrito():
    return render_template('sitio/carrito.html')

@app.route('/perfil')
def perfil():
    return render_template('sitio/perfil.html')

@app.route('/fertilizante1')
def fertilizante1():
    return render_template('sitio/fertilizante1.html')

@app.route('/reclamaciones')
def reclamaciones():
    return render_template('sitio/reclamaciones.html')

@app.route('/fertilizante2')
def fertilizante2():
    return render_template('sitio/fertilizante2.html')

@app.route('/fertilizante3')
def fertilizante3():
    return render_template('sitio/fertilizante3.html')

@app.route('/fertilizante4')
def fertilizante4():
    return render_template('sitio/fertilizante4.html')

@app.route('/fertilizante5')
def fertilizante5():
    return render_template('sitio/fertilizante5.html')

@app.route('/fertilizante6')
def fertilizante6():
    return render_template('sitio/fertilizante6.html')

@app.route('/fertilizante7')
def fertilizante7():
    return render_template('sitio/fertilizante7.html')

@app.route('/fertilizante8')
def fertilizante8():
    return render_template('sitio/fertilizante8.html')

@app.route('/herramienta1')
def herramienta1():
    return render_template('sitio/herramienta1.html')

@app.route('/herramienta2')
def herramienta2():
    return render_template('sitio/herramienta2.html')

@app.route('/herramienta3')
def herramienta3():
    return render_template('sitio/herramienta3.html')

@app.route('/herramienta4')
def herramienta4():
    return render_template('sitio/herramienta4.html')

@app.route('/herramienta5')
def herramienta5():
    return render_template('sitio/herramienta5.html')

@app.route('/producto1')
def producto1():
    return render_template('sitio/producto1.html')

@app.route('/producto5')
def producto5():
    return render_template('sitio/producto5.html')

@app.route('/accesorio3')
def accesorio3():
    return render_template('sitio/accesorio3.html')

@app.route('/accesorio1')
def accesorio1():
    return render_template('sitio/accesorio1.html')

@app.route('/accesorio2')
def accesorio2():
    return render_template('sitio/accesorio2.html')

@app.route('/accesorio4')
def accesorio4():
    return render_template('sitio/accesorio4.html')

@app.route('/accesorio5')
def accesorio5():
    return render_template('sitio/accesorio5.html')

@app.route('/accesorio6')
def accesorio6():
    return render_template('sitio/accesorio6.html')

@app.route('/accesorio7')
def accesorio7():
    return render_template('sitio/accesorio7.html')    

@app.route('/accesorio8')
def accesorio8():
    return render_template('sitio/accesorio8.html')

@app.route('/contactos')
def contactos():
    return render_template('sitio/contactos.html')

@app.route('/nosotros')
def nosotros():
    return render_template('sitio/nosotros.html')

@app.route('/servicio1')
def servicio1():
    return render_template('sitio/servicio1.html')

@app.route('/procedePago')
def procedePago():
    return render_template('sitio/procedePago.html')

@app.route('/agregarMetodoPago')
def agregarMetodoPago():
    return render_template('sitio/agregarMetodoPago.html')

@app.route('/metodoPago')
def metodoPago():
    return render_template('sitio/metodoPago.html')

@app.route('/finalizarCompra')
def finalizarCompra():
    return render_template('sitio/finalizarCompra.html')

@app.route('/infoPersonal')
def infoPersonal():
    return render_template('sitio/infoPersonal.html')

@app.route('/agregar_metodo_pago')
def agregar_metodo_pago():
    return render_template('sitio/agregar_metodo_pago.html')

@app.route('/cambiarContrasena')
def cambiarContrasena():
    return render_template('sitio/cambiarContrasena.html')

@app.route('/pedidos')
def pedidos():
    return render_template('sitio/pedidos.html')

@app.route('/notificaciones')
def notificaciones():
    return render_template('sitio/notificaciones.html')

@app.route('/producto2')
def producto2():
    return render_template('sitio/producto2.html')

@app.route('/producto3')
def producto3():
    return render_template('sitio/producto3.html')

@app.route('/producto4')
def producto4():
    return render_template('sitio/producto4.html')

@app.route('/producto6')
def producto6():
    return render_template('sitio/producto6.html')

@app.route('/producto7')
def producto7():
    return render_template('sitio/producto7.html')

@app.route('/planta3')
def planta3():
    return render_template('sitio/planta3.html')

@app.route('/planta1')
def planta1():
    return render_template('sitio/planta1.html')

@app.route('/planta2')
def planta2():
    return render_template('sitio/planta2.html')

@app.route('/planta4')
def planta4():
    return render_template('sitio/planta4.html')

@app.route('/planta5')
def planta5():
    return render_template('sitio/planta5.html')

@app.route('/planta6')
def planta6():
    return render_template('sitio/planta6.html')

@app.route('/planta7')
def planta7():
    return render_template('sitio/planta7.html')


# Ejemplo de cómo debería lucir tu función en app.py


@app.route('/solicitarServicio.html')
def solicitar_servicio():
    servicio = request.args.get('servicio')
    precio = request.args.get('precio')
    return render_template('sitio/solicitarServicio.html', servicio=servicio, precio=precio)


@app.route('/resultado')
def resultado():
    return render_template('sitio/resultado.html')


@app.route('/procesarSolicitud', methods=['POST'])
def procesarSolicitud():
    # Captura de datos
    nombre = request.form['nombre']
    apellido = request.form['apellido']
    # y así sucesivamente para otros campos
    return render_template('resultado.html', nombre=nombre, apellido=apellido)
        

if __name__ == '__main__':
    app.run(debug=True)
