import os
from flask import Flask, render_template, request, redirect, send_from_directory, session, url_for
# from flaskext.mysql import MySQL
from flask_mysqldb import MySQL
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
# import pymysql
# import bcrypt

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
    
    # Insertar nueva tarjeta
    cursor.execute("INSERT INTO tarjeta (nomTarjeta, numTarjeta, fechaExp, cvv) VALUES (%s, %s, %s, %s)", 
                   (nombre, numTarjeta, fechaExp, cvv))
    conn.commit()
    
    # Obtener el ID de la tarjeta recién insertada
    idTarjeta = cursor.lastrowid
    
    # Obtener el ID del usuario actual desde la sesión
    idUsuario = session.get('user_id')
    
    # Verificar si el usuario ya tiene un registro en la tabla cliente
    cursor.execute("SELECT idCliente FROM cliente WHERE idUsuario = %s", (idUsuario,))
    resultado = cursor.fetchone()
    
    if resultado:
        idCliente = resultado[0]
        # Actualizar el registro del cliente con el ID de la tarjeta
        cursor.execute("UPDATE cliente SET idTarjeta = %s WHERE idCliente = %s", (idTarjeta, idCliente))
    else:
        # Si el cliente no existe, puedes manejar el error o realizar una acción apropiada
        return "Cliente no encontrado", 404

    conn.commit()
    cursor.close()
    conn.close()
    
    return redirect(url_for('perfil'))

@app.route('/actualizarCliente/<int:idUsuario>', methods=['POST'])
def actualizarCliente(idUsuario):
    idTarjeta = request.form['idTarjeta']
    celular = request.form['celular']
    pais = request.form['pais']
    ciudad = request.form['ciudad']
    sector = request.form['sector']
    calle = request.form['calle']
    
    conn = mysql.connect()
    cursor = conn.cursor()
    
    # Verificar si el cliente existe
    cursor.execute("SELECT idCliente FROM cliente WHERE idUsuario = %s", (idUsuario,))
    resultado = cursor.fetchone()
    
    if resultado:
        idCliente = resultado[0]
        # Actualizar la tabla cliente con el idTarjeta
        cursor.execute('''
            UPDATE cliente 
            SET celular = %s, pais = %s, ciudad = %s, sector = %s, calle = %s, idTarjeta = %s
            WHERE idCliente = %s
        ''', (celular, pais, ciudad, sector, calle, idTarjeta, idCliente))
        conn.commit()
    else:
        # Si el cliente no existe, puedes manejar el error o realizar una acción apropiada
        return "Cliente no encontrado", 404

    cursor.close()
    conn.close()

    return "Cliente actualizado exitosamente"

# Ruta para el inicio
@app.route('/')
def index():
    return render_template('sitio/index.html')

# --------------------------------------------------------------------------------------------------------------------------------
# ruta para cuando aun el cliente no se ha registrado y quiero que se registre: a esta parte somos enviados si no estamos registrados cuando intentamos solicitar un servicio, cuando queremos ir a perfil y cuando intentamos agregar algun producto al carrito, ya que para acceder a estas paginas se necesita que el usuario se agregue para acceder a ciertas informaciones mas personales.

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
        idTarjeta = 1541254

        conn = mysql.connect()
        cursor = conn.cursor()

        # Insertar en la tabla de usuario los datos correspondiente a esta desde el formulario de registro
        insertarUsuario= '''
            INSERT INTO usuario (idUsuario, nombre, apellido, correo, contrasena, rol)
            VALUES (NULL, %s, %s, %s, %s, %s)
        '''
        datoUsuario = (nombre, apellido, correo, hashed_password, rol)
        
        cursor.execute(insertarUsuario, datoUsuario)
        conn.commit()

        # Obtener el ID del usuario recién insertado que se genera automaticamente se registra un nuevo usuario
        idUsuario = cursor.lastrowid

        # Insertar en la tabla de cliente los datos restantes obtenidos en el formulario de registro
        foto = 'valor'
        insertarCliente = '''
            INSERT INTO cliente (idCliente, celular, pais, ciudad, sector, calle, foto, idUsuario, idTarjeta)
            VALUES (NULL, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        '''
        datoCliente = (celular, pais, ciudad, sector, calle, foto, idUsuario, idTarjeta)  # Asignar None a idTarjeta si es opcional, en este caso como aun la tabla de idTarjeta no esta conectada puede dar conflictos.
        
        cursor.execute(insertarCliente, datoCliente)
        conn.commit()

        cursor.close()
        conn.close()

        return redirect('inicioSesion') # Si los pasos anteriores son correctos el usuario es redirigido a inicio de sesion para continuar el proceso, de lo contrario seria devuelto de nuevo a registro.
    
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

@app.route('/perfil')
def perfil():
    if 'correo' in session:
        correo = session['correo']  # Verifica que el usuario esté autenticado

        # Conexión a la base de datos
        conn = mysql.connect()
        cursor = conn.cursor()

        # Obtener nombre y apellido del usuario
        cursor.execute('SELECT nombre, apellido FROM usuario WHERE correo = %s', (correo,))
        usuario = cursor.fetchone()

        # Obtener el idUsuario asociado al correo
        cursor.execute('SELECT idUsuario FROM usuario WHERE correo = %s', (correo,))
        idUsuario = cursor.fetchone()

        if usuario and idUsuario:
            idUsuario = idUsuario[0]

            # Obtener el sector del cliente
            cursor.execute('SELECT sector FROM cliente WHERE idUsuario = %s', (idUsuario,))
            cliente = cursor.fetchone()
            sector = cliente[0] if cliente else ''  # Manejo del caso en que no se encuentre el sector

            # Renderiza la plantilla con los datos del usuario y sector
            response = render_template('sitio/perfil.html', nombre=usuario[0], apellido=usuario[1], sector=sector)
        else:
            response = redirect('/inicioSesion')

        # Cerrar el cursor y la conexión
        cursor.close()
        conn.close()
        return response
    else:
        return redirect('/inicioSesion')


@app.route('/infoPersonal', methods=['GET', 'POST'])
def infoPersonal():
    if 'correo' not in session:
        return redirect('/inicioSesion')

    correo = session['correo']
    
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

            return "success"
        
        cursor.close()
        conn.close()
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

            cursor.close()
            conn.close()
            return render_template('sitio/infoPersonal.html', nombre=nombre, apellido=apellido, celular=celular, pais=pais, ciudad=ciudad, sector=sector, calle=calle)
        else:
            cursor.close()
            conn.close()
            return redirect('/inicioSesion')

#---------------------------------------------------------------------------

# Ruta para servir las imágenes
@app.route('/static/img/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

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

@app.route('/guardar_contacto', methods=['POST'])
def guardar_contacto():
    nombre = request.form['nombre']
    correo = request.form['email']
    telefono = request.form['telefono']
    mensaje = request.form['mensaje']
    fecha = datetime.now().strftime('%Y-%m-%d')
    estado = 'Pendiente'

    # Crear un cursor para la conexión a la base de datos
    conn = mysql.connect()
    cursor = conn.cursor()

    # Ejecutar la consulta SQL
    cursor.execute('INSERT INTO contacto (nombre, correo, telefono, fecha, estado, mensaje) VALUES (%s, %s, %s, %s, %s, %s)', 
                   (nombre, correo, telefono, fecha, estado, mensaje))

    # Commit los cambios
    conn.commit()

    # Cerrar el cursor y la conexión
    cursor.close()
    conn.close()

    return redirect('contacto')

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

@app.route('/confirmacion')
def confirmacion():
    return render_template('sitio/confirmacion.html')


@app.route('/solicitarServicio')
def mostrar_formulario():
    servicio = request.args.get('servicio')
    precio = request.args.get('total')
    return render_template('sitio/solicitarServicio.html', servicio=servicio, total=precio)




@app.route('/solicitarServicio', methods=['POST'])
def solicitar_servicio():
    if 'correo' in session:
        correo = session['correo']
        
        # Obtén los datos del formulario
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        tipoServicio = request.form['proyecto']
        telefono = request.form['telefono']
        servicioAdicional = ', '.join(request.form.getlist('servicios[]'))
        requerimiento = request.form['requerimiento']
        enterar = request.form['enterar']
        fecha = request.form['fecha']
        precio = request.form['total']
        
        # Conexión a la base de datos
        conn = mysql.connect()
        cursor = conn.cursor()

        # Obtener idUsuario usando el correo del usuario
        cursor.execute('SELECT idUsuario FROM usuario WHERE correo = %s', (correo,))
        idUsuario = cursor.fetchone()

        if idUsuario:
            idUsuario = idUsuario[0]
            
            # Obtener idCliente usando idUsuario desde la tabla cliente
            cursor.execute('SELECT idCliente FROM cliente WHERE idUsuario = %s', (idUsuario,))
            idCliente = cursor.fetchone()

            if idCliente:
                idCliente = idCliente[0]
                
                # Inserción en la tabla servicio
                cursor.execute('INSERT INTO servicio (nombre, apellido, correo, tipoServicio, telefono, servicioAdicional, requerimiento, enterar, fecha, precio, idCliente) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)', 
                               (nombre, apellido, correo, tipoServicio, telefono, servicioAdicional, requerimiento, enterar, fecha, precio, idCliente))
                
                conn.commit()
                response = redirect('/resultado')
            else:
                # Maneja el caso si no se encuentra el idCliente
                response = redirect('/error')
        else:
            # Maneja el caso si no se encuentra el idUsuario
            response = redirect('/error')

        # Cerrar el cursor y la conexión
        cursor.close()
        conn.close()
        return response
    else:
        return redirect('/inicioSesion')


def calcular_precio(servicios_adicionales, precio_inicial):
    precio_total = int(precio_inicial)
    if 'Mantenimiento' in servicios_adicionales:
        precio_total += 2000
    if 'Diseños de jardines' in servicios_adicionales:
        precio_total += 2500
    if 'Poda de planta' in servicios_adicionales:
        precio_total += 1500
    if 'Abonado' in servicios_adicionales:
        precio_total += 1000
    if 'Sistema de detección de plagas' in servicios_adicionales:
        precio_total += 2500
    if 'Tratamiento fitosanitario' in servicios_adicionales:
        precio_total += 3000
    if 'Eliminación de mala hierbas' in servicios_adicionales:
        precio_total += 1000
    if 'Revisión de sistema de riego' in servicios_adicionales:
        precio_total += 3500
    if 'Césped artificial' in servicios_adicionales:
        precio_total += 400
    if 'Control y programación de riego' in servicios_adicionales:
        precio_total += 3500
    
    return precio_total

@app.route('/resultado')
def resultado():
    return render_template('sitio/resultado.html')








@app.route('/olvidarContrasena', methods=['GET', 'POST'])
def olvidarContrasena():
    return render_template('sitio/olvidarContrasena.html')

if __name__ == '__main__':
    app.run(debug=True)
