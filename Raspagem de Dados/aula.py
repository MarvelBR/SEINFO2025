import requests
import pandas as pd
import bs4 as bs

url = "https://api.github.com/search/repositories"
parametros = {"q": "language:python"}
resposta = requests.get(url, parametros)
#print(resposta.text)
tmp = resposta.json()
#print(tmp)
#print(tmp['total_count'])
#print(tmp['items'][0])

#print(tmp['items'][0]['full_name'])
#print(tmp['items'][0]['html_url'])
#print(tmp['items'][0]['description'])

dados = []
for item in tmp['items']:
    dados.append({
        "nome": item['full_name'],
        "url": item['html_url'],
        "descricao": item['description']
    })

meus_dados = pd.DataFrame(dados)
#meus_dados.to_csv('Raspagem de Dados/meus_dados.csv')

#Notas Taquigraficas
#Ir para algum site de exemplo, inspecionar a página, dar refresh na pagina, ir para a parte de redes, 
# pegar a informação que nós queremos, copiar o valor como cURL e ir no site de converter o valor 🗿🗿🗿🗿🗿🗿🗿🗿

#tudo aqui em baixo foi oq foi convertido!
cookies = {
    'ASPSESSIONIDAGDBRBQQ': 'NBIDINECIPPBJBABOKBIPEGE',
    'BALANCEID': 'mycluster.node1',
    '_ga_FFSPP8TF7Y': 'GS2.1.s1756144101$o1$g1$t1756144479$j30$l0$h0',
    '_ga': 'GA1.1.2038668159.1756144102',
    'clickedDetails': '%7B%22parentTagName%22%3A%22A%22%2C%22text%22%3A%22%22%2C%22tagName%22%3A%22SPAN%22%2C%22classes%22%3A%22glyphicon%20glyphicon-file%22%2C%22id%22%3A%22%22%2C%22url%22%3A%22https%3A%2F%2Fwww.camara.leg.br%2Finternet%2Fsitaqweb%2FresultadoPesquisaDiscursos.asp%3FtxOrador%3D%26txPartido%3D%26txUF%3D%26dtInicio%3D%26dtFim%3D%26txTexto%3DInternet%26txSumario%3D%26basePesq%3Dplenario%26CampoOrdenacao%3DdtSessao%26PageSize%3D50%26TipoOrdenacao%3DDESC%26btnPesq%3DPesquisar%22%7D',
    '__gsas': 'ID=463024b9d305a21d:T=1756144180:RT=1756144180:S=ALNI_MYSDjnaV7NNyqGUv1_g1Z_YFl1rdA',
    'ASPSESSIONIDAGRABSSA': 'EGKDNPDCOGPIKDOHEGIFNNMC',
    'ASPSESSIONIDAGRCBTTB': 'JOKDNMDCGNOBPMGENHIANPDO',
    'ASPSESSIONIDQWQTADTS': 'IAJJPLDCEKBGGMBHEKJIGMJG',
    'ASPSESSIONIDCGTCDQTA': 'KCDIABDCKEMMOLKPKMLMFAEC',
    'ASPSESSIONIDCGTBCSTB': 'DMPDJODCMMPBKCHFBKFENGDO',
    'ASPSESSIONIDACDBRBQQ': 'BEIDINECMMJGKBEDAEHMHDBH',
    'ASPSESSIONIDSSQSCDSS': 'EBOHJHDCJPEKPDGFGHFMIAAK',
    'ASPSESSIONIDQSQTDCTT': 'IKDNBJECEOBDKNGKEDPBDPKK',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:134.0) Gecko/20100101 Firefox/134.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'pt-BR,pt;q=0.8,en-US;q=0.5,en;q=0.3',
    # 'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Referer': 'https://www2.camara.leg.br/',
    'Connection': 'keep-alive',
    # 'Cookie': 'ASPSESSIONIDAGDBRBQQ=NBIDINECIPPBJBABOKBIPEGE; BALANCEID=mycluster.node1; _ga_FFSPP8TF7Y=GS2.1.s1756144101$o1$g1$t1756144479$j30$l0$h0; _ga=GA1.1.2038668159.1756144102; clickedDetails=%7B%22parentTagName%22%3A%22A%22%2C%22text%22%3A%22%22%2C%22tagName%22%3A%22SPAN%22%2C%22classes%22%3A%22glyphicon%20glyphicon-file%22%2C%22id%22%3A%22%22%2C%22url%22%3A%22https%3A%2F%2Fwww.camara.leg.br%2Finternet%2Fsitaqweb%2FresultadoPesquisaDiscursos.asp%3FtxOrador%3D%26txPartido%3D%26txUF%3D%26dtInicio%3D%26dtFim%3D%26txTexto%3DInternet%26txSumario%3D%26basePesq%3Dplenario%26CampoOrdenacao%3DdtSessao%26PageSize%3D50%26TipoOrdenacao%3DDESC%26btnPesq%3DPesquisar%22%7D; __gsas=ID=463024b9d305a21d:T=1756144180:RT=1756144180:S=ALNI_MYSDjnaV7NNyqGUv1_g1Z_YFl1rdA; ASPSESSIONIDAGRABSSA=EGKDNPDCOGPIKDOHEGIFNNMC; ASPSESSIONIDAGRCBTTB=JOKDNMDCGNOBPMGENHIANPDO; ASPSESSIONIDQWQTADTS=IAJJPLDCEKBGGMBHEKJIGMJG; ASPSESSIONIDCGTCDQTA=KCDIABDCKEMMOLKPKMLMFAEC; ASPSESSIONIDCGTBCSTB=DMPDJODCMMPBKCHFBKFENGDO; ASPSESSIONIDACDBRBQQ=BEIDINECMMJGKBEDAEHMHDBH; ASPSESSIONIDSSQSCDSS=EBOHJHDCJPEKPDGFGHFMIAAK; ASPSESSIONIDQSQTDCTT=IKDNBJECEOBDKNGKEDPBDPKK',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-site',
    'Sec-Fetch-User': '?1',
    'Priority': 'u=0, i',
}

params = {
    'txOrador': '',
    'txPartido': '',
    'txUF': '',
    'dtInicio': '',
    'dtFim': '',
    'txTexto': 'Internet',
    'txSumario': '',
    'basePesq': 'plenario',
    'CampoOrdenacao': 'dtSessao',
    'PageSize': '50',
    'TipoOrdenacao': 'DESC',
    'btnPesq': 'Pesquisar',
}

response = requests.get(
    'https://www.camara.leg.br/internet/sitaqweb/resultadoPesquisaDiscursos.asp',
    params=params,
    cookies=cookies,
    headers=headers,
)
#print(response.text)

html = bs.BeautifulSoup(response.text, 'html.parser')
#print(html)

tabela = html.find('table')
elementos = tabela.find_all('tr', {'class':'even'})
#print(elementos)
#print(len(elementos))
#print(elementos[0])

#print(elementos[0].find_all("td")[5])

dados = []
for celula in elementos:
    try:
        data = celula.find_all("td")[0].text
        sessao = celula.find_all("td")[1].text.strip()
        fase = celula.find_all("td")[2].text.strip()
        link = 'https://www.camara.leg.br/internet/sitaqweb/' + celula.find_all("td")[3].a['href'].replace('\r', '').replace('\t', '').replace('\n', '')
        nome = celula.find_all("td")[5].text.strip().replace(', -----', '')
        dados.append({
            "data": data,
            "sessao": sessao,
            "fase": fase,
            "link": link,
            "nome": nome
        })
    except:
        continue

meus_dados = pd.DataFrame(dados)
#print(meus_dados2)

#aqui pegamos o cURL de um link
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:134.0) Gecko/20100101 Firefox/134.0',
}

response = requests.get(
    'https://www.camara.leg.br/internet/sitaqweb/TextoHTML.asp?etapa=5&nuSessao=16.2025.N&nuQuarto=4557582&nuOrador=1&nuInsercao=1&dtHorarioQuarto=12:04&sgFaseSessao=HO&Data=21/08/2025&txApelido=Jo%C3%A3o%20Roberto%20Marinho&txFaseSessao=Homenagem&txTipoSessao=Ordin%C3%A1ria%20-%20CD&dtHoraQuarto=12:04&txEtapa=',
    cookies=cookies,
    headers=headers,
)

html = bs.BeautifulSoup(response.text, 'html.parser')
#print(html)

def buscar_tramites(link):
    headers = {'User-Agent': ''} #nome aleatorio pq esse site nao verifica! (Vazio funcionaria tbm)
    try:
        #print(link)
        resposta = requests.get(link, headers=headers, timeout=30)
        resposta.encoding = resposta.apparent_encoding
        texto = resposta.text
        taquigrafica = bs.BeautifulSoup(texto, 'html.parser')
        return taquigrafica.text.replace('\r', '').replace('\t', '').replace('\n', '')
    
    except:
        print("Deu erro")
        return "-1"
    
teste = buscar_tramites('https://www.camara.leg.br/internet/sitaqweb/TextoHTML.asp?etapa=5&nuSessao=155.2025&nuQuarto=4557408&nuOrador=1&nuInsercao=1&dtHorarioQuarto=22:48&sgFaseSessao=OD&Data=20/08/2025&txApelido=Gilson%20Marques&txFaseSessao=Ordem%20do%20Dia&txTipoSessao=Ordin%C3%A1ria%20-%20CD&dtHoraQuarto=22:48&txEtapa=')
#print(teste)

meus_dados['texto'] = meus_dados['link'].apply(buscar_tramites)
print(meus_dados)