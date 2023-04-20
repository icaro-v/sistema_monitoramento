def monitora():
    import psutil

    # obter informações de uso de disco
    disk_usage = psutil.disk_usage('/')

    # total = (disk_usage.total / (2**30))
    # usado = (disk_usage.used / (2**30))
    livre = (disk_usage.free / (2**30))
    livre = f'{livre:.2f}'

    return f"""INFRA
    Espaço em disco (HD): {livre} GB\n
    """
