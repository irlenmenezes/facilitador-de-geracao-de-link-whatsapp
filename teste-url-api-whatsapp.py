Hotel = input('Digite o Nome do Hotel:')
campanha_texto1 = "Olá, acabei de receber um e-mail de vocês com a promoção do Pacote de Desfile de Carnaval que inclui: Hospedagem no "
campanha_texto2 = " com Ingressos para Desfile das Escolas de Samba e Traslado."
texto_completo = f"{campanha_texto1}{Hotel}{campanha_texto2}"
link_whatsapp ="https://api.whatsapp.com/send/?phone=552100000000&text=" 
url_completa_whatsapp = f"{link_whatsapp}{texto_completo}"
print(url_completa_whatsapp)
