import requests
from bs4 import BeautifulSoup

def coletar_noticias(url: str, limite: int = 11) -> list:
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f'Erro ao acessar o site: {e}')
        return []

    soup = BeautifulSoup(response.text, 'html.parser')
    noticias = soup.find_all('a', class_='feed-post-link')

    resultado = []
    for noticia in noticias[:limite]:
        titulo = noticia.text.strip()
        link = noticia['href']
        resultado.append((titulo, link))
    return resultado

def salvar_em_arquivo(dados: list, caminho: str):
    with open(caminho, 'w', encoding='utf-8') as f:
        for titulo, link in dados:
            f.write(f'{titulo}\n{link}\n\n')

if __name__ == '__main__':
    URL = 'https://g1.globo.com/'
    noticias = coletar_noticias(URL)
    salvar_em_arquivo(noticias, 'resultado.txt')
    print(f'{len(noticias)} notícias salvas em resultado.txt.')
