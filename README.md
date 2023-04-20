# soma-tarifador-monitorador

O monitorador foi feito para poupar tempo e automaizar o monitoramento mensal realizado nos clientes APST do Soma Tarifador.

A automação verifica:
 - o espaço disponível no disco onde foi instalado o tarifador
 - as rotinas de backup (hora, data, e pasta onde são salvos os arquivos de backup)
 - fluxo de ligações captadas pelo tarifador
 
Após as verificações, o Monitorador cria e alimenta um arquivo txt com os dados coletados.
O txt é transformado no corpo de um e-mail e, posteriormente, enviado para o e-mail suporte.tarifador@gmail.com
