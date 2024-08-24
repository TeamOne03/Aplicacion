import os
from flask import Flask, render_template, request, redirect, send_from_directory, session, url_for, jsonify
from flaskext.mysql import MySQL
from werkzeug.security import generate_password_hash, check_password_hash
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

# Configurar la carpeta de subida de las imagenes
app.config['UPLOAD_FOLDER'] = 'static/img'

# Inicializar la aplicación
mysql.init_app(app)

# Función para generar una página de detalle de producto
def generar_pagina_producto(idProducto):
    # Obtiene un cursor para interactuar con la base de datos
    cursor = mysql.get_db().cursor()
    
    # Ejecuta una consulta para obtener el producto con el id proporcionado
    cursor.execute("SELECT * FROM producto WHERE idProducto = %s", (idProducto,))
    
    # Recupera el primer resultado de la consulta
    producto = cursor.fetchone()
    
    # Cierra el cursor después de completar la consulta
    cursor.close()

    # Verifica si el producto existe
    if producto:
        # Desempaqueta los valores de la tupla producto en variables individuales
        idProducto, nombre, cantidad, categoria, subcategoria, precio, imagen_ruta, descripcion = producto
        
        # Crea un diccionario con los detalles del producto que serán utilizados en la plantilla HTML
        producto_dict = {
            'idProducto': idProducto,
            'nombre': nombre,
            'precio': precio,
            'imagen': imagen_ruta,
            'descripcion': descripcion
        }

        # Abre un archivo en modo de escritura para crear una página de producto individual
        with open(f'templates/sitio/productos{idProducto}.html', 'w') as f:
            # Renderiza una plantilla HTML con los detalles del producto y escribe el resultado en el archivo
            f.write(render_template('sitio/producto_template.html', producto=producto_dict))

# Ruta para agregar y mostrar productos en la página de admin
@app.route('/adminAGGProductos', methods=['GET', 'POST'])
def adminAGGProductos():
    # Comprueba si la solicitud es de tipo POST (para agregar un producto)
    if request.method == 'POST':
        # Obtiene los datos del formulario enviados por el usuario
        nombre = request.form['nombre']
        cantidad = request.form['cantidad']
        categoria = request.form['categoria']
        subcategoria = request.form.get('subcategoria', '')  # Puede no estar presente en el caso de mas vendidos
        precio = request.form['precio']
        imagen = request.files['imagen']
        descripcion = request.form['descripcion']

        # Guarda la imagen en la carpeta 'static/img'
        imagen_ruta = os.path.join(app.config['UPLOAD_FOLDER'], imagen.filename)
        imagen.save(imagen_ruta)

        # Conecta a la base de datos y obtiene un cursor
        conn = mysql.connect()
        cursor = conn.cursor()
        
        # Ejecuta una consulta para insertar un nuevo producto en la base de datos
        cursor.execute(
            "INSERT INTO producto (nombre, cantidad, categoria, subcategoria, precio, imagen, descripcion) VALUES (%s, %s, %s, %s, %s, %s, %s)",
            (nombre, cantidad, categoria, subcategoria, precio, imagen.filename, descripcion)
        )
        
        # Confirma los cambios realizados en la base de datos
        conn.commit()
        
        # Obtiene el ID del último producto insertado
        idProducto = cursor.lastrowid
        
        # Cierra el cursor y la conexión
        cursor.close()
        conn.close()

        # Genera una página de detalle del producto
        generar_pagina_producto(idProducto)
        
        # Redirige a la página de administración de productos
        return redirect('/adminAGGProductos')
    
    # Si la solicitud es de tipo GET, conecta a la base de datos
    conn = mysql.connect()
    cursor = conn.cursor()
    
    # Ejecuta una consulta para obtener todos los productos
    cursor.execute("SELECT * FROM producto")
    
    # Recupera todos los resultados de la consulta
    productos = cursor.fetchall()
    
    # Cierra el cursor y la conexión
    cursor.close()
    conn.close()

    # Crea una lista para almacenar los productos con sus imágenes
    productos_con_imagenes = []
    
    # Recorre todos los productos y los agrega a la lista
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

    # Renderiza la plantilla HTML para mostrar los productos en la página de administración
    return render_template('admin/adminAGGProductos.html', productos=productos_con_imagenes)

# Codigo para eliminar un producto
@app.route('/eliminarProducto/<int:idProducto>', methods=['POST'])
def eliminarProducto(idProducto):
    # Conecta a la base de datos y obtiene un cursor
    conn = mysql.connect()
    cursor = conn.cursor()
    
    # Ejecuta una consulta para eliminar el producto con el id especificado
    cursor.execute("DELETE FROM producto WHERE idProducto = %s", (idProducto,))
    
    # Confirma los cambios realizados en la base de datos
    conn.commit()
    
    # Cierra el cursor y la conexión
    cursor.close()
    conn.close()
    
    # Redirige a la página de administración de productos
    return redirect('/adminAGGProductos')

# Ruta para mostrar la pagina de el producto agregado
@app.route('/productos/<int:idProducto>')
def producto(idProducto):
    # Obtiene un cursor para interactuar con la base de datos
    cursor = mysql.get_db().cursor()
    
    # Ejecuta una consulta para obtener el producto con el id proporcionado
    cursor.execute("SELECT * FROM producto WHERE idProducto = %s", (idProducto,))
    
    # Recupera el primer resultado de la consulta
    producto = cursor.fetchone()
    
    # Cierra el cursor después de completar la consulta
    cursor.close()

    # Verifica si el producto existe
    if producto:
        # Desempaqueta los valores de la tupla producto en variables individuales
        idProducto, nombre, cantidad, categoria, subcategoria, precio, imagen_ruta, descripcion = producto
        
        # Crea un diccionario con los detalles del producto que serán utilizados en la plantilla HTML
        producto_dict = {
            'idProducto': idProducto,
            'nombre': nombre,
            'precio': precio,
            'imagen': imagen_ruta,
            'descripcion': descripcion,
            'cantidad_disponible': cantidad
        }
        
        # Renderiza la plantilla HTML con los detalles del producto
        return render_template('sitio/producto_template.html', producto=producto_dict)
    
    # Si el producto no existe devuelve un mensaje de error 404
    else:
        return "Producto no encontrado", 404

# Ruta para mostrar el catálogo de productos más vendidos
@app.route('/catalogo')
def catalogo():
    # Obtiene un cursor para interactuar con la base de datos
    cursor = mysql.get_db().cursor()
    
    # Ejecuta una consulta para obtener todos los productos de la categoría 'masvendidos'
    cursor.execute("SELECT * FROM producto WHERE categoria = 'masvendidos'")
    
    # Recupera todos los resultados de la consulta
    productos = cursor.fetchall()
    
    # Cierra el cursor después de completar la consulta
    cursor.close()

    # Crea una lista para almacenar los productos con sus imágenes
    productos_con_imagenes = []
    
    # Recorre todos los productos y los agrega a la lista
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

    # Renderiza la plantilla HTML para mostrar el catálogo
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

@app.route('/agregarTarjeta', methods=['POST'])
def agregarTarjeta():
    nombre = request.form['nombre']
    numTarjeta = request.form['numTarjeta']
    mes = request.form['meses']
    año = request.form['años']
    fechaExp = f"{año}-{mes}-01"
    cvv = request.form['cvv']
    
    conn = mysql.connect()
    cursor = conn.cursor()
    
    # Obtener el ID del usuario actual desde la sesión
    correo = session.get('correo')
    
    if not correo:
        return "Usuario no autenticado", 403
    
    # Obtener el ID del usuario actual
    cursor.execute("SELECT idUsuario FROM usuario WHERE correo = %s", (correo,))
    result = cursor.fetchone()
    
    if not result:
        return "Usuario no encontrado", 404
    
    idUsuario = result[0]
    
    # Obtener el ID del cliente asociado con el usuario
    cursor.execute("SELECT idCliente FROM cliente WHERE idUsuario = %s", (idUsuario,))
    result = cursor.fetchone()
    
    if result:
        idCliente = result[0]
    else:
        return "Cliente no encontrado", 404
    
    # Insertar nueva tarjeta
    cursor.execute("INSERT INTO tarjeta (nomTarjeta, numTarjeta, fechaExp, cvv, idCliente) VALUES (%s, %s, %s, %s, %s)", 
                   (nombre, numTarjeta, fechaExp, cvv, idCliente))
    conn.commit()
    
    # Obtener el ID de la tarjeta recién insertada
    idTarjeta = cursor.lastrowid
    
    # Actualizar el registro del cliente con el ID de la tarjeta
    cursor.execute("UPDATE cliente SET idTarjeta = %s WHERE idCliente = %s", (idTarjeta, idCliente))
    conn.commit()
    
    cursor.close()
    conn.close()
    
    return redirect(url_for('perfil'))

# Esmeralda comenzamos

@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        correo = request.form['correo']
        contrasena = request.form['contrasena']
        confirmarContrasena = request.form['confirmarContrasena']
        celular = request.form['celular']
        pais = request.form['pais']
        ciudad = request.form['ciudad']
        sector = request.form['sector']
        calle = request.form['calle']

        if contrasena != confirmarContrasena:
            return render_template('sitio/registro.html', error='Las contraseñas proporcionadas no coinciden')

        hashed_password = generate_password_hash(contrasena, method='sha256')
        rol = 'usuario'
        idTarjeta = None  # No se necesita tarjeta al registrarse inicialmente

        conn = mysql.connect()
        cursor = conn.cursor()

        # Insertar en la tabla de usuario
        insertarUsuario = '''
            INSERT INTO usuario (nombre, apellido, correo, contrasena, rol)
            VALUES (%s, %s, %s, %s, %s)
        '''
        datoUsuario = (nombre, apellido, correo, hashed_password, rol)
        cursor.execute(insertarUsuario, datoUsuario)
        conn.commit()

        # Obtener el ID del usuario recién insertado
        idUsuario = cursor.lastrowid

        # Insertar en la tabla de cliente sin idTarjeta
        insertarCliente = '''
            INSERT INTO cliente (celular, pais, ciudad, sector, calle, foto, idUsuario)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        '''
        foto = 'valor'  # Valor por defecto para la foto
        datoCliente = (celular, pais, ciudad, sector, calle, foto, idUsuario)
        cursor.execute(insertarCliente, datoCliente)
        conn.commit()

        cursor.close()
        conn.close()

        return redirect(url_for('inicioSesion'))
    
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

        if usuario:  # Si el usuario es encontrado y la contrasena pertence al mismo correo entonces es redirigido al index ya con la opcion de poder editar su usuario, comprar y solicitar un servicio.
            hashed_password=usuario[4]
            session['correo']=correo
            return redirect('/')
        else:
            return render_template('sitio/inicioSesion.html', error='Correo o contraseña incorrectos')

    return render_template('sitio/inicioSesion.html')

# tarjetas

@app.route('/obtenerTarjetas', methods=['GET'])
def obtener_tarjetas():
    # Conectarse a la base de datos
    conn = mysql.connect()
    cursor = conn.cursor()

    # Obtener el ID del usuario actual desde la sesión
    correo = session.get('correo')

    if not correo:
        return jsonify({"error": "Usuario no autenticado"}), 403

    # Obtener el ID del usuario actual
    cursor.execute("SELECT idUsuario FROM usuario WHERE correo = %s", (correo,))
    result = cursor.fetchone()

    if not result:
        return jsonify({"error": "Usuario no encontrado"}), 404

    idUsuario = result[0]

    # Obtener el ID del cliente asociado con el usuario
    cursor.execute("SELECT idCliente FROM cliente WHERE idUsuario = %s", (idUsuario,))
    result = cursor.fetchone()

    if result:
        idCliente = result[0]
    else:
        return jsonify({"error": "Cliente no encontrado"}), 404

    # Consulta para obtener las tarjetas del cliente sin formateo de fecha
    cursor.execute("""
        SELECT idTarjeta, numTarjeta, fechaExp 
        FROM tarjeta 
        WHERE idCliente = %s
    """, (idCliente,))
    
    tarjetas = cursor.fetchall()

    # Crear una lista de diccionarios para enviar las tarjetas en formato JSON
    tarjetas_list = []
    for tarjeta in tarjetas:
        tarjetas_list.append({
            'idTarjeta': tarjeta[0],
            'numTarjeta': str(tarjeta[1]),  # Convertir numTarjeta a string para que coincida con el formato de la entrada
            'mesExpiracion': tarjeta[2].strftime('%m'),  # Formatear la fecha si es necesario
            'añoExpiracion': tarjeta[2].strftime('%Y'),
        })

    # Cerrar conexión
    cursor.close()
    conn.close()

    # Retornar las tarjetas en formato JSON
    return jsonify(tarjetas_list)


@app.route('/eliminarTarjeta', methods=['POST'])
def eliminar_tarjeta():
    data = request.get_json()

    # Verificar que el idTarjeta esté presente en la solicitud
    if 'idTarjeta' not in data:
        return jsonify({'error': 'El idTarjeta es requerido.'}), 400

    idTarjeta = data['idTarjeta']

    # Conectar a la base de datos
    conn = mysql.connect()
    cursor = conn.cursor()

    # Ejecutar la consulta de eliminación
    cursor.execute("DELETE FROM tarjeta WHERE idTarjeta = %s", (idTarjeta,))
    conn.commit()

    # Verificar si se eliminó alguna fila
    if cursor.rowcount == 0:
        cursor.close()
        conn.close()
        return jsonify({'error': 'No se encontró la tarjeta con el id especificado.'}), 404

    # Cerrar la conexión
    cursor.close()
    conn.close()

    return jsonify({'message': 'Tarjeta eliminada exitosamente.'})

# tarjetas

# factuta 

@app.route('/procesar_compra', methods=['POST'])
def procesar_compra():
    if 'correo' not in session:
        return redirect(url_for('login'))

    if 'direccionEnvio' not in request.form or 'nombreProducto' not in request.form or 'total' not in request.form:
        return "Datos incompletos", 400

    direccion_envio = request.form['direccionEnvio']
    nombre_producto = request.form['nombreProducto']
    total = request.form['total']

    correo_usuario = session['correo']
    
    conn = mysql.connect()
    cursor = conn.cursor()

    cursor.execute("SELECT idUsuario FROM usuario WHERE correo = %s", (correo_usuario,))
    result = cursor.fetchone()
    if result:
        id_usuario = result[0]
    else:
        cursor.close()
        conn.close()
        return "Usuario no encontrado", 404

    cursor.execute("SELECT idCliente FROM cliente WHERE idUsuario = %s", (id_usuario,))
    result = cursor.fetchone()
    if result:
        id_cliente = result[0]
    else:
        cursor.close()
        conn.close()
        return "Cliente no encontrado", 404

    # Aquí no se verifica el producto, solo se almacenan los nombres directamente
    fecha_pedido = datetime.now().strftime('%Y-%m-%d')
    estado = 'pendiente'
    
    cursor.execute("""
        INSERT INTO pedidos (fechaPedido, estado, direccionEnvio, productos, idCliente)
        VALUES (%s, %s, %s, %s, %s)
    """, (fecha_pedido, estado, direccion_envio, nombre_producto, id_cliente))

    conn.commit()
    cursor.close()
    conn.close()

    return redirect(url_for('finalizarCompra'))

# factura

@app.route('/perfil')
def perfil():
    if 'correo' in session:
        correo = session['correo'] # Aqui se estable una condicion para poder ingresar a registro, si el usuario no ha iniciado sesion no puede acceder y es redirigido al inicio de sesion, si este ya inciio sesion entonces puede acceder.

        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute('SELECT nombre, apellido FROM usuario WHERE correo = %s', (correo,))
        usuario = cursor.fetchone()
        cursor.close()
        conn.close()

        # El codigo de aqui sirve para que cuando se inicie sesion los valores de nombre y apellido aparezcan en en la pagina de perfil.
        if usuario:
            return render_template('sitio/perfil.html', nombre=usuario[0], apellido=usuario[1])
        else:
            return redirect('/inicioSesion')
    else:
        return redirect('/inicioSesion')

@app.route('/infoPersonal', methods=['GET', 'POST'])
def infoPersonal():
    if 'correo' in session:
        correo = session['correo']
        try:
            # Conexión a la base de datos
            conn = mysql.connect()
            cursor = conn.cursor()

            if request.method == 'POST':
                # Obtiene los datos del formulario
                nombre = request.form.get('nombre')
                apellido = request.form.get('apellido')
                celular = request.form.get('celular')
                pais = request.form.get('pais')
                ciudad = request.form.get('ciudad')
                sector = request.form.get('sector')
                calle = request.form.get('calle')

                # Obtén el idUsuario asociado al correo
                cursor.execute('SELECT idUsuario FROM usuario WHERE correo = %s', (correo,))
                idUsuario = cursor.fetchone()
                
                if idUsuario:
                    idUsuario = idUsuario[0]

                    # Actualiza la información del usuario
                    actualizarUsuario = '''
                    UPDATE usuario SET nombre = %s, apellido = %s WHERE idUsuario = %s
                    '''
                    usuarioDato = (nombre, apellido, idUsuario)
                    cursor.execute(actualizarUsuario, usuarioDato)
                    conn.commit()

                    # Actualiza la información del cliente
                    actualizarCliente = '''
                    UPDATE cliente SET celular = %s, pais = %s, ciudad = %s, sector = %s, calle = %s WHERE idUsuario = %s
                    '''
                    clienteDato = (celular, pais, ciudad, sector, calle, idUsuario)
                    cursor.execute(actualizarCliente, clienteDato)
                    conn.commit()

                return redirect('/perfil')

            else:
                # Obtén el idUsuario asociado al correo
                cursor.execute('SELECT idUsuario, nombre, apellido FROM usuario WHERE correo = %s', (correo,))
                usuario = cursor.fetchone()
                
                if usuario:
                    idUsuario, nombre, apellido = usuario

                    # Obtén datos del cliente usando idUsuario
                    cursor.execute('SELECT celular, pais, ciudad, sector, calle FROM cliente WHERE idUsuario = %s', (idUsuario,))
                    cliente = cursor.fetchone()

                    if cliente:
                        celular, pais, ciudad, sector, calle = cliente
                    else:
                        celular = pais = ciudad = sector = calle = ''

                    return render_template('sitio/infoPersonal.html', nombre=nombre, apellido=apellido, celular=celular, pais=pais, ciudad=ciudad, sector=sector, calle=calle)
                else:
                    return redirect('/inicioSesion')
                
        except Exception as e:
            print(f"Error: {e}")
            return "Hubo un problema al procesar la solicitud.", 500

        finally:
            cursor.close()
            conn.close()
    else:
        return redirect('/inicioSesion')

# Esmeralda

# Ruta para survir las imágenes
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
    if 'correo' in session:
        correo = session['correo']

        conn = mysql.connect()
        cursor = conn.cursor()

        # Obtener idUsuario basado en el correo
        cursor.execute('SELECT idUsuario FROM usuario WHERE correo = %s', (correo,))
        usuario = cursor.fetchone()
        
        if usuario:
            idUsuario = usuario[0]

            # Obtener el sector y la calle basado en idUsuario
            cursor.execute('SELECT sector, calle FROM cliente WHERE idUsuario = %s', (idUsuario,))
            cliente = cursor.fetchone()
            sector = cliente[0] if cliente else ''
            calle = cliente[1] if cliente else ''
            
            cursor.close()
            conn.close()
            
            # Pasar el sector, la calle y el correo a la plantilla
            return render_template('sitio/metodoPago.html', sector=sector, calle=calle, correo=correo)

    # En caso de que 'correo' no esté en la sesión, se devuelve la plantilla con un sector y calle vacíos
    return render_template('sitio/metodoPago.html', sector='', calle='', correo='')


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

@app.route('/cambiarContrasena')
def cambiarContrasena():
    return render_template('sitio/cambiarContrasena.html')

@app.route('/cerrarSesion')
def cerrarSesion():
    return render_template('sitio/cerrarSesion.html')

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

@app.route('/olvidarContrasena', methods=['GET', 'POST'])
def olvidarContrasena():
    return render_template('sitio/olvidarContrasena.html')

if __name__ == '__main__':
    app.run(debug=True)
