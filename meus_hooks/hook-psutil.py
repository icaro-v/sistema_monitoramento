from PyInstaller.utils.hooks import collect_all

def hook(hook_api):
    # Adicionar informações do pacote psutil
    datas, binaries, hiddenimports = collect_all('psutil')
    hook_api.add_datas(datas)
    hook_api.add_binaries(binaries)
    hook_api.add_imports(*hiddenimports)
