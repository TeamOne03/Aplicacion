import os
from flask import Flask, render_template, request, redirect, send_from_directory
from flaskext.mysql import MySQL
from datetime import datetime

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

# Configurar la carpeta de subida
app.config['UPLOAD_FOLDER'] = 'static/img'

# Inicializar la aplicación
mysql.init_app(app)

def generar_pagina_producto(idProducto):
    cursor = mysql.get_db().cursor()
    cursor.execute("SELECT * FROM producto WHERE idProducto = %s", (idProducto,))
    producto = cursor.fetchone()
    cursor.close()

    if producto:
        idProducto, nombre, cantidad, categoria, subcategoria, precio, imagen_ruta, descripcion = producto
        producto_dict = {
            'idProducto': idProducto,
            'nombre': nombre,
            'precio': precio,
            'imagen': imagen_ruta,
            'descripcion': descripcion
        }

        with open(f'templates/sitio/productos{idProducto}.html', 'w') as f:
            f.write(render_template('sitio/producto_template.html', producto=producto_dict))

@app.route('/adminAGGProductos', methods=['GET', 'POST'])
def adminAGGProductos():
    if request.method == 'POST':
        nombre = request.form['nombre']
        cantidad = request.form['cantidad']
        categoria = request.form['categoria']
        subcategoria = request.form.get('subcategoria', '')  # Puede no estar presente
        precio = request.form['precio']
        imagen = request.files['imagen']
        descripcion = request.form['descripcion']

        # Guardar la imagen en la carpeta 'static/img'
        imagen_ruta = os.path.join(app.config['UPLOAD_FOLDER'], imagen.filename)
        imagen.save(imagen_ruta)

        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO producto (nombre, cantidad, categoria, subcategoria, precio, imagen, descripcion) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                       (nombre, cantidad, categoria, subcategoria, precio, imagen.filename, descripcion))
        conn.commit()
        idProducto = cursor.lastrowid
        cursor.close()
        conn.close()

        generar_pagina_producto(idProducto)
        return redirect('/adminAGGProductos')
    
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM producto")
    productos = cursor.fetchall()
    cursor.close()
    conn.close()

    productos_con_imagenes = []
    for producto in productos:
        idProducto = producto[0]
        nombre = producto[1]
        cantidad = producto[2]
        categoria = producto[3]
        subcategoria = producto[4]
        precio = producto[5]
        imagen_ruta = producto[6]
        descripcion = producto[7]

        productos_con_imagenes.append({
            'idProducto': idProducto,
            'nombre': nombre,
            'cantidad': cantidad,
            'categoria': categoria,
            'subcategoria': subcategoria,
            'precio': precio,
            'imagen': imagen_ruta,
            'descripcion': descripcion
        })

    return render_template('admin/adminAGGProductos.html', productos=productos_con_imagenes)

@app.route('/eliminarProducto/<int:idProducto>', methods=['POST'])
def eliminarProducto(idProducto):
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM producto WHERE idProducto = %s", (idProducto,))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect('/adminAGGProductos')

@app.route('/productos/<int:idProducto>')
def producto(idProducto):
    cursor = mysql.get_db().cursor()
    cursor.execute("SELECT * FROM producto WHERE idProducto = %s", (idProducto,))
    producto = cursor.fetchone()
    cursor.close()

    if producto:
        idProducto, nombre, cantidad, categoria, subcategoria, precio, imagen_ruta, descripcion = producto
        producto_dict = {
            'idProducto': idProducto,
            'nombre': nombre,
            'precio': precio,
            'imagen': imagen_ruta,
            'descripcion': descripcion,
            'cantidad_disponible': cantidad
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
        subcategoria = producto[4]  # no incluye subcategoria
        precio = producto[5]
        imagen_ruta = producto[6]  
        descripcion = producto[7]

        productos_con_imagenes.append({
            'idProducto': idProducto,
            'nombre': nombre,
            'cantidad': cantidad,
            'categoria': categoria,
            'precio': precio,
            'imagen': imagen_ruta,
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
        subcategoria = producto[4]  # Incluye subcategoria
        precio = producto[5]
        imagen_ruta = producto[6]  
        descripcion = producto[7]

        productos_con_imagenes.append({
            'idProducto': idProducto,
            'nombre': nombre,
            'cantidad': cantidad,
            'categoria': categoria,
            'subcategoria': subcategoria,
            'precio': precio,
            'imagen': imagen_ruta,
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
        subcategoria = producto[4]  # Incluye subcategoria
        precio = producto[5]
        imagen_ruta = producto[6]  
        descripcion = producto[7]

        productos_con_imagenes.append({
            'idProducto': idProducto,
            'nombre': nombre,
            'cantidad': cantidad,
            'categoria': categoria,
            'subcategoria': subcategoria,
            'precio': precio,
            'imagen': imagen_ruta,
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
        subcategoria = producto[4]  # Incluye subcategoria
        precio = producto[5]
        imagen_ruta = producto[6]  
        descripcion = producto[7]

        productos_con_imagenes.append({
            'idProducto': idProducto,
            'nombre': nombre,
            'cantidad': cantidad,
            'categoria': categoria,
            'subcategoria': subcategoria,
            'precio': precio,
            'imagen': imagen_ruta,
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
        subcategoria = producto[4]  # Incluye subcategoria
        precio = producto[5]
        imagen_ruta = producto[6]  
        descripcion = producto[7]

        productos_con_imagenes.append({
            'idProducto': idProducto,
            'nombre': nombre,
            'cantidad': cantidad,
            'categoria': categoria,
            'subcategoria': subcategoria,
            'precio': precio,
            'imagen': imagen_ruta,
            'descripcion': descripcion
        })

    return render_template('sitio/accesorios.html', productos=productos_con_imagenes)


# Ruta para servir las imágenes
@app.route('/static/img/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

# Ruta para el inicio
@app.route('/')
def index():
    return render_template('sitio/index.html')

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

@app.route('/inicioSesion')
def inicioSesion():
    return render_template('sitio/inicioSesion.html')

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

@app.route('/inicio_sesion')
def inicio_sesion():
    return render_template('sitio/inicio_sesion.html')

@app.route('/metodoPago')
def metodoPago():
    return render_template('sitio/metodoPago.html')

@app.route('/finalizarCompra')
def finalizarCompra():
    return render_template('sitio/finalizarCompra.html')

@app.route('/contacto')
def contacto():
    return render_template('sitio/contacto.html')

@app.route('/info_personal')
def info_personal():
    return render_template('sitio/info_personal.html')

@app.route('/agregar_metodo_pago')
def agregar_metodo_pago():
    return render_template('sitio/agregar_metodo_pago.html')

@app.route('/cambiar_contrasena')
def cambiar_contrasena():
    return render_template('sitio/cambiar_contrasena.html')

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

if __name__ == '__main__':
    app.run(debug=True)
