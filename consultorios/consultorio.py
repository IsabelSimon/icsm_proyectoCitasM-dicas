import doctors.conexion as conexion
connect = conexion.conectar()
database = connect[0]
cursor = connect[1]

class Consultorio:
    def __init__(self, consultorio):
        self.consultorio = consultorio
    
    def listar(self):
       sql = f"SELECT * FROM consultorios"
       cursor.execute(sql)
       result = cursor.fetchall()
       return result