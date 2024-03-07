def monitora():
    import psutil, conn
    from datas import datas

    # obter informações de uso de disco
    disk_usage = psutil.disk_usage('/')

    livre = (disk_usage.free / (2**30))
    livre = f'{livre:.2f}'

    cur = conn.conexao_bd.cursor()
    cur.execute(f"""update monitoramento set espaco_gb = '{livre}'
    WHERE mes_monitorado = {datas.mes_atual}""")
    conn.conexao_bd.commit()
    
    return f"""INFRA
    Espaço em disco (HD): {livre} GB
    """
