from flask import Flask, render_template
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




@app.route('/')
def index():
    sql="INSERT INTO `contacto` (`cont_nombres`, `cont_apellidos`, `cont_telefono`, `cont_correo`) VALUES ('luis rafael', 'gutierrez palacios', '435266277', 'palacios@gmail.com');"
    conn= mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql)
    conn.commit()
    
    
    return render_template('usuarios/index.html')

if __name__ == '__main__':
    app.run(debug=True)
