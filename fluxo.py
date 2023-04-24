def monitora():
    import calendar
    from datetime import datetime
    import conn

    ano = datetime.now().year
    mes = datetime.now().month - 1
    ultimo_dia_mes = calendar.monthrange(ano, mes)[1]
    periodo = f"01/{mes:02}/{ano} - {ultimo_dia_mes}/{mes:02}/{ano}"

    cur = conn.conexao_bd.cursor()
    
    cur.execute(f"select count(*) from cadcha where teldata between '{ano}-{mes}-01' and '{ano}-{mes}-{ultimo_dia_mes}'" )
    lig_mensais = cur.fetchall()[0][0]

    cur.execute('SELECT count(*) FROM cadram')
    qtde_ram = cur.fetchall()[0][0]
    qtde_ram = f'{qtde_ram:02}'

    cur.execute(f"select count(*) from cadcha c where teldata between '{ano}-{mes}-01' and '{ano}-{mes}-{ultimo_dia_mes}' and aorecebida = 'S'")
    lig_entrada = cur.fetchall()[0][0]

    cur.execute(f"select count(*) from cadcha c where teldata between '{ano}-{mes}-01' and '{ano}-{mes}-{ultimo_dia_mes}' and aorecebida = 'N'")
    lig_saida = cur.fetchall()[0][0]
    
    cur.execute(f"""select count(*) from (
SELECT MAX(NREG) MAXNREG
               FROM CADCHA
              
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


    cur.execute("select distinct extract(day from teldata) from cadcha")
    lista = cur.fetchall()
    dias = []

    for dia in lista:
        dias.append(int(dia[0]))
    
    dias = sorted(dias)

    return f"""
FLUXO DE LIGAÇÕES
    Período: {periodo}
    Fluxo mensal de ligações: {lig_mensais}
    Ligações de entrada: {lig_entrada}
    Ligações de saída: {lig_saida}
    Ligações duplicadas: {lig_duplicadas}
    Quantidade de ramais: {qtde_ram}
    Dias tarifados: {dias}
    """
