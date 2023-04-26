from flask import Flask, render_template, request , redirect, send_from_directory, flash, url_for
from flaskext.mysql import MySQL
from datetime import datetime
import os

app= Flask(__name__)
app.secret_key="YDCP"
# referencia para la conexion de la bd
mysql = MySQL()
app.config['MYSQL_DATABASE_HOST']='localhost'
app.config['MYSQL_DATABASE_USER']='root'
app.config['MYSQL_DATABASE_PORT'] = 3309
app.config['MYSQL_DATABASE_PASSSWORD'] =''
app.config['MYSQL_DATABASE_DB']='bd_contactos'
mysql.init_app(app)


CARPETA = os.path.join('imgns')
app.config['CARPETA']=CARPETA

# el nombre no tiene nada que ver nomnbrefoto/ puede ser cualquier nombre 
@app.route('/imgns/<nombreFoto>')
def imgns(nombreFoto):
    return send_from_directory(app.config['CARPETA'],nombreFoto)

# referencia para que el usuario cada vez que reflesque la pagina se ejecute la sequencia sql
@app.route('/')
def index():
    sql="SELECT * FROM `contacto`;"
    conn= mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql)
    
    usuarios=cursor.fetchall()
    print(usuarios)
    
    conn.commit()
    return render_template('usuarios/index.html', usuarios = usuarios)



@app.route('/create')
def create():
    return render_template('usuarios/create.html')



@app.route('/store', methods=['POST'])
def storage():
    # .file si no referimos a un archivo
    # _foto=request.files['foto']
    _nombres=request.form['txtNombres']
    _apellidos=request.form['txtApellidos']
    _correo=request.form['txtCorreo']
    _telefono=request.form['txtTelefono']
    _imagen=request.files['txtImagen']
    
    sql="INSERT INTO `contacto` (`cont_nombres`, `cont_apellidos`, `cont_telefono`, `cont_correo`,`cont_imagen`) VALUES ('{0}', '{1}', '{2}', '{3}', '{4}');"
   
    if _nombres=='' or _apellidos=='' or _correo=='' or _telefono=='' or _imagen=='':
            flash('Recuerda llenar los datos')
            return redirect(url_for('create'))
   
    ahora = datetime.now()
    tiempo=ahora.strftime("%Y%H%M%S")
    
    if _imagen != "":
        nuevoNombreImg = tiempo+_imagen.filename
        _imagen.save("imgns/"+nuevoNombreImg)
   
    conn= mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql.format(_nombres,_apellidos,_telefono,_correo,nuevoNombreImg)) 
    conn.commit()
    return redirect('/')



@app.route('/delete/<int:id>')
def delete(id):
    conn= mysql.connect()
    cursor=conn.cursor()
    
    # A la hora de eliminar,borrar la imagen de la carpeta 
    cursor.execute("SELECT cont_imagen FROM contacto WHERE cont_id ={0}".format(id))
    fila=cursor.fetchall()
    os.remove(os.path.join(app.config['CARPETA'],fila[0][0]))
       
    
    # dos formas diferente de realizar esta consulta
    # cursor.execute("DELETE FROM contacto WHERE cont_id =%s",(id))
    cursor.execute("DELETE FROM contacto WHERE cont_id ={0}".format(id))
    
    conn.commit()
    return redirect('/')


@app.route('/edit/<int:id>')
def edit(id):
    conn= mysql.connect()
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM contacto WHERE cont_id ={0}".format(id))
    
    usuarios=cursor.fetchall()
    print(usuarios)
    
    
    
    return render_template('usuarios/edit.html', usuarios = usuarios)



@app.route('/write', methods=['POST'])
def editando():
    # .file si no referimos a un archivo
    # _foto=request.files['foto']
    
    _nombres=request.form['txtNombres']
    _apellidos=request.form['txtApellidos']
    _correo=request.form['txtCorreo']
    _telefono=request.form['txtTelefono']
    id=request.form['txtId']
    _imagen=request.files['txtImagen']
    
    sql="UPDATE `contacto` SET `cont_nombres` = '{1}', `cont_apellidos` = '{2}', `cont_telefono` = '{3}', `cont_correo` = '{4}' WHERE `cont_id` = '{0}'"
   
    conn= mysql.connect()
    cursor=conn.cursor()
    
    
    ahora = datetime.now()
    tiempo=ahora.strftime("%Y%H%M%S")
    
    # remplaza la imagen que editas, elimina y actualiza la imagen 
    if _imagen != "":
        
        nuevoNombreImg = tiempo+_imagen.filename
        _imagen.save("imgns/"+nuevoNombreImg)
        
        cursor.execute("SELECT cont_imagen FROM contacto WHERE cont_id =%s",id)
        # cursor.execute("SELECT cont_imagen FROM contacto WHERE cont_id ={0}".format(id))
        fila=cursor.fetchall()
        
        os.remove(os.path.join(app.config['CARPETA'],fila[0][0]))
        cursor.execute("UPDATE contacto SET cont_imagen=%s WHERE cont_id = %s",(nuevoNombreImg,id))
        # cursor.execute("UPDATE contacto SET cont_imagen='{1}' WHERE cont_id = {0}".format(id,nuevoNombreImg))
        conn.commit()
        
        
    cursor.execute(sql.format(id,_nombres,_apellidos,_telefono,_correo,nuevoNombreImg))
    conn.commit()
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
