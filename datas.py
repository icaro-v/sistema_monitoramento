from datetime import date
import calendar

hoje = date.today()

class Meses_e_Ano:
    def __init__(self):
        self.mes_atual = f"'{hoje.strftime('%m/%Y')}'"

        # verifica se o mês atual é janeiro
        if hoje.month == 1:
            mes_anterior = 12
            ano = hoje.year - 1
        else:
            mes_anterior = f'{int(hoje.month - 1):02}'
            ano = hoje.year

        self.mes_anterior = mes_anterior
        self.ano = ano

        self.ultimo_dia_mes_anterior = calendar.monthrange(self.ano, int(self.mes_anterior))[1]

        self.periodo = f"01/{self.mes_anterior}/{self.ano} - {self.ultimo_dia_mes_anterior}/{self.mes_anterior:02}/{self.ano}"

        self.periodoSQL = f"'{self.ano}-{self.mes_anterior}-01' and '{self.ano}-{self.mes_anterior}-{self.ultimo_dia_mes_anterior}'"

datas = Meses_e_Ano()

