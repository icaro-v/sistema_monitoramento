import psycopg2
import socket

ip_local = socket.gethostbyname(socket.gethostname())

# define os parâmetros de conexão
host = 'ip_local'
database = 'Tarifador'
user = 'postgres'
password = 'Supinf12!'

# faz a conexão com o banco de dados
conexao_bd = psycopg2.connect(host=host, database=database, user=user, password=password)
