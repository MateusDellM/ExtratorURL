#url = "https://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100"
#url = "bytebank.com/cambio?moedaOrigem=real"
url =" "

#Sanitização da URL
#url = url.replace(" ","") ||||||| um boa forma de tirar algo da string
url = url.strip()


#validação da URL
if url =="":
    raise ValueError("A URL está vazia")


#Separa base e parametro
indice_interrogacao = url.find('?')
url_base = url[0:indice_interrogacao]   #busca até o primeiro parametro de busca separedo por interrogação
url_parametros = url[indice_interrogacao+1:]  #indice do busca separeda, iniciando da interrogação até o fim da sting
print(url_parametros)


#Busca O valor de um parametro
parametro_busca = 'moedaOrigem'
indice_parametros = url_parametros.find(parametro_busca)
indice_valor = indice_parametros + len(parametro_busca)+1
indice_e_comercial = url_parametros.find('&')
if indice_e_comercial ==-1:
    valor = url_parametros[indice_valor:]
else:
    valor= url_parametros[indice_valor:indice_e_comercial]

print(valor)

