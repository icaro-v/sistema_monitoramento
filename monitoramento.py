import conn, datas, envia, fluxo, infra, rotina
from datas import datas
from time import sleep

cur = conn.conexao_bd.cursor()
cur.execute("select MAX(mes_monitorado) from monitoramento")
mes_bd = cur.fetchall()[0][0]

sleep(2)

if (mes_bd != datas.mes_atual[1:-1]):
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
