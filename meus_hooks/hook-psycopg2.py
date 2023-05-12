from PyInstaller.utils.hooks import collect_data_files

def hook(hook_api):
    # Adicionar informações do pacote psycopg2
    datas = collect_data_files('psycopg2')
    binaries = []
    hiddenimports = ['psycopg2._psycopg']

    hook_api.add_datas(datas)
    hook_api.add_binaries(binaries)
    hook_api.add_imports(*hiddenimports)
