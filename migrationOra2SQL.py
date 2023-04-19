import cx_Oracle

uid = "UC008CBRF_QAS"  # usuário
pwd = "008-cbrf-qas"  # senha
db = "BRFQAS"  # string de conexão do Oracle, configurado no
# cliente Oracle, arquivo tnsnames.ora

connection = cx_Oracle.connect(uid + "/" + pwd + "@" + db)  # cria a conexão
cursor = connection.cursor()  # cria um cursor

cursor.execute("SELECT * from all_users")  # consulta sql
result = cursor.fetchone()  # busca o resultado da consulta
if result == None:
    print
    "Nenhum Resultado"
    exit
else:
    while result:
        print
        result[0]
        result = cursor.fetchone()
cursor.close()
connection.close()