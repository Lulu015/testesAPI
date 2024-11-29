import requests
import pytest

# API'S utilizadas para os testes de integrgação:

# 1 - FIPE API HTTP REST: Retorna várias marcas de carros (nacionais e internacionais).
TABELA_FIPE_URL = "https://parallelum.com.br/fipe/api/v1/carros/marcas"

# 2 - Breaking Bad Quotes API: Retorna alguma fala aleatório de algum personagem da série Breaking Bad em inglês.
BREAKING_BAD_URL = "https://api.breakingbadquotes.xyz/v1/quotes"

# 3 - Random Dog API: Retorna uma imagem/vídeo aleatório de cachorro(s).
BIG_DOGS_URL = "https://random.dog/woof.json"

# 4 - Jikan API: Retorna informações sobre um mangá aleatório dentro da API.
JIKAN_URL = "https://api.jikan.moe/v4/random/manga"

# 5 - Evil Insult Generator API: Retorna algum comentário maldoso em vários idiomas por opção do usuário.
EVIL_URL = "https://evilinsult.com/generate_insult.php?lang=en&type=json"

#-----------------------------------------------------------

# 1º Teste - Teste para a Tabela FIPE
 
def test_tabela_api_code():
# Testa se a API do espaço retorna status code 200    
    response = requests.get("https://parallelum.com.br/fipe/api/v1/carros/marcas")
    assert response.status_code == 200 
    
def test_tabela_api_verification():
# Retorna todos os códigos e marcas registrados
    response = requests.get("https://parallelum.com.br/fipe/api/v1/carros/marcas")
    data = response.json()
    print(data)
    
# 2º Teste - Teste para as frases de Breaking Bad

def test_breaking_bad_code():
# Testa se a API do espaço retorna status code 200    
    response = requests.get("https://api.breakingbadquotes.xyz/v1/quotes")
    assert response.status_code == 200
    
def test_breaking_bad_verification():
# Retorna uma frase de algum personagem
    response = requests.get("https://api.breakingbadquotes.xyz/v1/quotes")
    data = response.json()
    print(data)
    
# 3º Teste - Teste para fotos/vídeos de Random Dog

def test_random_dog_code():
# Testa se a API do espaço retorna o status code 200
    response = requests.get("https://random.dog/woof.json")
    assert response.status_code == 200
    
def test_random_dog_verification():
# Retorna o link da imagem no prompt de comando (ou a foto/vídeo no navegador)
    response = requests.get("https://random.dog/woof.json")
    data = response.json()
    print(data)
    
# 4º Teste - Teste para a API Jikan 

def test_jikan_api_code():
# Testa se a API do espaço retorna o status code 200
    response = requests.get("https://api.jikan.moe/v4/random/manga")
    assert response.status_code == 200
    
def test_jikan_api_verification():
# Retorna informações sobre algum mangá aleatório dentro do API
    response = requests.get("https://api.jikan.moe/v4/random/manga")
    data = response.json()
    print(data)
    
# 5º Teste - Teste para as frases maldosas da API

def test_evil_api_code():
# Teste se a API do espaço retorna o status code 200
    response = requests.get("https://evilinsult.com/generate_insult.php?lang=en&type=json")
    assert response.status_code == 200
    
def test_evil_api_verification():
# Retorna alguma frase maldosa catalogada na API (em inglês)
    response = requests.get("https://evilinsult.com/generate_insult.php?lang=en&type=json")
    data = response.json()
    print(data)