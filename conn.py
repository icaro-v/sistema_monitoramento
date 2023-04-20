import psycopg2

# define os parâmetros de conexão
host = '192.168.32.38'
database = 'Tarifador'
user = 'postgres'
password = 'Supinf12!'

# faz a conexão com o banco de dados
conexao_bd = psycopg2.connect(host=host, database=database, user=user, password=password)
