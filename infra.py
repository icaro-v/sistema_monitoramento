def monitora():
    import psutil, conn
    from datetime import datetime

    # obter informações de uso de disco
    disk_usage = psutil.disk_usage('/')

    # total = (disk_usage.total / (2**30))
    # usado = (disk_usage.used / (2**30))
    livre = (disk_usage.free / (2**30))
    livre = f'{livre:.2f}'

    mes_monitorado = datetime.now().month 

    cur = conn.conexao_bd.cursor()
    cur.execute(f"""update monitoramento set espaco_gb = '{livre}'
    WHERE mes_monitorado = {mes_monitorado}""")
    conn.conexao_bd.commit()
    
    return f"""INFRA
    Espaço em disco (HD): {livre} GB
    """
