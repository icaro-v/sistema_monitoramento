import conn
from datetime import datetime

cur = conn.conexao_bd.cursor()
cur.execute("select mes_monitorado from monitoramento")
mes_bd = cur.fetchall()[-1][0]

mes_atual = datetime.now().month

if (mes_bd == mes_atual):
    pass
else:
    import rotina, fluxo, infra, envia

    msg1 = rotina.monitora()
    msg2 = fluxo.monitora()
    msg3 = infra.monitora()

    conn.conexao_bd.close()

    with open('monitorado.txt', 'w', encoding="UTF-8") as arquivo:   
        arquivo.write("""O monitoramento mensal do SOMA Tarifador foi concluído. 
    Seguem as informações para seu conhecimento:\n""")
        arquivo.write(f"{msg1}\n{msg2}\n{msg3}")

    envia.email()
