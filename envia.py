def email():
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText

    # lendo o arquivo gerado após monitoramento
    with open("monitorado.txt", 'r', encoding="UTF-8") as texto:
        mensagem = texto.read()

    # configurações de envio de e-mail
    remetente = 'monitoramento.tarifador@gmail.com'
    destinatario = 'icaropython@gmail.com'
    senha = "zsgvmuwbugwuxhwl"

    # construção do e-mail
    msg = MIMEMultipart() 
    msg['From'] = remetente
    msg['To'] = destinatario
    msg['Subject'] = f"Monitoramento APST - {'Nome do Cliente'}." #assunto
    msg.attach(MIMEText(mensagem, 'plain'))

    # enviando o e-mail
    s = smtplib.SMTP("smtp.gmail.com: 587")
    s.starttls()
    s.login(remetente, senha)
    s.sendmail(remetente, destinatario, mensagem.encode('utf-8'))
    del msg
    s.quit()
