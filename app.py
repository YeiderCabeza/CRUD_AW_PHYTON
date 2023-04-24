from flask import Flask, render_template, request , redirect
from flaskext.mysql import MySQL

app= Flask(__name__)

# referencia para la conexion de la bd
mysql = MySQL()
app.config['MYSQL_DATABASE_HOST']='localhost'
app.config['MYSQL_DATABASE_USER']='root'
app.config['MYSQL_DATABASE_PORT'] = 3309
app.config['MYSQL_DATABASE_PASSSWORD'] =''
app.config['MYSQL_DATABASE_DB']='bd_contactos'
mysql.init_app(app)


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
    
    sql="INSERT INTO `contacto` (`cont_nombres`, `cont_apellidos`, `cont_telefono`, `cont_correo`) VALUES ('{0}', '{1}', '{2}', '{3}');"
   
    conn= mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql.format(_nombres,_apellidos,_telefono,_correo))
    conn.commit()
    return render_template('usuarios/index.html')



@app.route('/delete/<int:id>')
def delete(id):
    conn= mysql.connect()
    cursor=conn.cursor()
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
    
    sql="UPDATE `contacto` SET `cont_nombres` = '{1}', `cont_apellidos` = '{2}', `cont_telefono` = '{3}', `cont_correo` = '{4}' WHERE `cont_id` = '{0}'"
   
    conn= mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql.format(id,_nombres,_apellidos,_telefono,_correo))
    conn.commit()
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
