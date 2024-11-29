# 🖥 Testes de Integração em APIs Públicas 
Este repositório contêm testes feitos em APIs públicas, feitos em Python e pytest. 
O objetivo é simular interações reais com a API, validando as respostas recebidas e o comportamento geral das requisições.

# 🔧 APIs Utilizadas para os testes: 
API de consulta da Tabela FIPE, que fornece preços médios de veículos no mercado.
- URL: https://parallelum.com.br/fipe/api/v1/carros/marcas 

API que retorna alguma frase da série Breaking Bad
- URL: https://api.breakingbadquotes.xyz/v1/quotes

API que que retorna algum(a) foto/vídeo de cachorro(s)
- URL: https://random.dog/woof.json

API que retorna informações sobre algum mangá catalogado
- URL: https://api.jikan.moe/v4/random/manga

API que retorna algum comentário maldoso (idioma por padrão: Inglês)
- URL: https://evilinsult.com/generate_insult.php?lang=en&type=json

# ⚙ Pré-requisitos
- Python
- Pytest
- Requisits
> [!TIP]
> Caso queira saber sobre detalhes maiores de pré-requisitos, recomendo que acesse o arquivo `<requirements.txt>`.

# 📘 Estrutura dos testes
Cada teste dentro do código possui um comentário para detalhar o processo de teste, indicando o resultado esperado. Os testes se constituem de:
- Verificação de Status (200)
- Verificação de dados presentes pelos GETs
