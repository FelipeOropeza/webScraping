# Web Scraping de Notícias - B2BFlow

Este projeto foi desenvolvido como parte do processo seletivo da B2BFlow para a vaga de Estágio em Desenvolvimento Python.

Ele realiza um scraping no portal [G1](https://g1.globo.com) e coleta as 10 principais manchetes do momento, salvando os títulos e links no arquivo `resultado.txt`.

## Tecnologias

- Python 3
- requests
- BeautifulSoup4

## Como executar

1. **Clone este repositório**
2. **Instale as dependências**:
   ```bash
   pip install -r requirements.txt
    
3. **Execute o scraper**:
   ```bash
   python scraper.py
4. Veja o resultado em `resultado.txt`.
