def monitora():
    import os, conn
    from glob import glob
    from datetime import datetime
    from datas import datas

    cur = conn.conexao_bd.cursor()

    #configurando nome/local do arquivo de backup
    pasta_backup  = "C:/Backup_Tarifador/compactado"   

    #procura pelo arquivo e devolve a data e hora da criação
    busca_arquivo  = os.path.join(pasta_backup, '*_TARIFADOR.rar')
    bkps = glob(busca_arquivo)

    if(bkps):
        data_modificacao = os.path.getmtime(bkps[-1])    
        data_hora_ultimo_bkp  = datetime.fromtimestamp(data_modificacao) #transforma em uma data legível

        hora_ultimo_bkp = data_hora_ultimo_bkp.strftime('%Hh%M')
        dia_ultimo_bkp = data_hora_ultimo_bkp.strftime('%d/%m/%Y')         

        cur.execute(f"insert into monitoramento (mes_monitorado, dt_ultimo_bkp, hr_ultimo_bkp, local_bkp) values ({datas.mes_atual}, '{dia_ultimo_bkp}', '{hora_ultimo_bkp}', '{pasta_backup}');")
        conn.conexao_bd.commit()
        
        return f"""\nROTINA DE BACKUP 
    Data do último backup: {dia_ultimo_bkp} 
    Horário de execução: {hora_ultimo_bkp}
    Local de armazenamento: {pasta_backup}"""

    else:
        cur.execute(f"insert into monitoramento (mes_monitorado, dt_ultimo_bkp, hr_ultimo_bkp, local_bkp) values ({datas.mes_atual}, '-', '-', 'Sem backup');")
        conn.conexao_bd.commit()

        return f"""\nROTINA DE BACKUP
    Não há backups na pasta {pasta_backup}"""
