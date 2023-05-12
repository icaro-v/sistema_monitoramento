def monitora():
    import conn
    from datas import datas

    cur = conn.conexao_bd.cursor()
    
    cur.execute(f"select count(*) from cadcha where teldata between {datas.periodoSQL}" )
    lig_mensais = cur.fetchall()[0][0]

    cur.execute('SELECT count(*) FROM cadram')
    qtde_ram = cur.fetchall()[0][0]
    qtde_ram = f'{qtde_ram:02}'

    cur.execute(f"select count(*) from cadcha c where teldata between {datas.periodoSQL} and aorecebida = 'S'")
    lig_entrada = cur.fetchall()[0][0]

    cur.execute(f"select count(*) from cadcha c where teldata between {datas.periodoSQL} and aorecebida = 'N'")
    lig_saida = cur.fetchall()[0][0]
    
    cur.execute(f"""select count(*) from (
SELECT MAX(NREG) MAXNREG
               FROM CADCHA
              WHERE teldata >= '01/01/{datas.ano}'
              GROUP BY RAMALDESTINO,
                       TELEFONE,
                       CIDADE,
                       TRONCO,
                       OPERADORA,
                       TELINI,
                       TELFIM,
                       TELDUR,
                       TELDURTAR,
                       TIPO,
                       TELPRETOT,
                       TELDATA
             HAVING COUNT(*) > 1) as tabela
""")
    lig_duplicadas = cur.fetchall()[0][0]

    if (int(lig_duplicadas) > 0):
        cur.execute("SELECT public.p_remove_duplicada();")


    cur.execute(f"select distinct extract(day from teldata) from cadcha where teldata between {datas.periodoSQL}")
    lista = cur.fetchall()
    dias = []

    for dia in lista:
        dias.append(int(dia[0]))
    
    dias = sorted(dias)

    cur.execute(f"""update monitoramento SET periodo = '{datas.periodo}', 
    fluxo = {lig_mensais},
    entrada = {lig_entrada},
    saida = {lig_saida},
    duplicada = {lig_duplicadas},
    qtde_ram = {qtde_ram},
    dias = '{dias}' WHERE mes_monitorado = {datas.mes_atual};""")
    conn.conexao_bd.commit()

    return f"""
FLUXO DE LIGAÇÕES
    Período: {datas.periodo}
    Fluxo mensal de ligações: {lig_mensais}
    Ligações de entrada: {lig_entrada}
    Ligações de saída: {lig_saida}
    Ligações duplicadas: {lig_duplicadas}
    Quantidade de ramais: {qtde_ram}
    Dias tarifados: {dias}
    """
