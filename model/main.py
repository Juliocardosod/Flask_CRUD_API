from configparser import ConfigParser
import os
import pyodbc as db
from model import lists as ls

cfg = ConfigParser()
cfg.read_file(open(os.path.join(os.path.dirname(__file__),"config.ini")))

#BANCO
bco_inst = cfg.get('BANCO','INSTANCIA')
bco_bco = cfg.get('BANCO','BANCO')
bco_usr = cfg.get('BANCO','USUARIO')
bco_senha = cfg.get('BANCO','SENHA')
bco_time = cfg.getint('BANCO', 'TIMEOUT')
bco_driver = cfg.get('BANCO','DRIVER')



# conn.setdecoding(db.SQL_CHAR, encoding='latin1')
# conn.setencoding('latin1')

def insertUsuario(nome, email, senha):

    return {"id": 1, "nome": nome, "senha": senha}

def registraBCO(): #Insere informações no banco
    # datahora = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    try:
        conn = db.connect('Driver={SQL Server};'
                        f'Server={bco_inst};'
                        f'Database={bco_bco};'
                        'Trusted_Connection=yes;'
                        f'UID={bco_usr};'
                        f'PWD={bco_senha}',
                        timeout = bco_time
                        )
        cursor = conn.cursor()
        cursor.execute(f"INSERT INTO REGISTRO_RECURSOS(datahora, mensagem) VALUES(convert(datetime, getdate(), 120), 'msg')")
        
        conn.commit()
        cursor.close()
        conn.close()
    except Exception as ex:
        print(f" Falha na gravação do banco: {ex}")

def selectUser(): #Seleciona
    conn = db.connect(f'Driver={bco_driver};'
                        f'Server={bco_inst};'
                        f'Database={bco_bco};'
                        f'UID={bco_usr};'
                        f'PWD={bco_senha}',
                        timeout = bco_time    
                        )
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM USERS")
    rows = cursor.fetchall()
    users = [] #ls.user()

    for row in rows:
        user = ls.user()
        user.id = row.user_id
        user.nome = row.user_name

        users.append(user)

    conn.close()

    return users
    # try:
        
    # except Exception as ex:
    #     print(f" Falha leitura do banco: {ex}")
        