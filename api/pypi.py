import requests

# Referências sobre o uso do requests:
#
# Fazendo requisições:
# https://docs.python-requests.org/en/master/user/quickstart/#make-a-request
# Usando JSON retornado:
# https://docs.python-requests.org/en/master/user/quickstart/#json-response-content

def version_exists(package_name, version):
    # TODO
    # Fazer requisição na API do PyPI para checar se a versão existe
    base_url = "https://pypi.org/pypi"
    url = f'{base_url}/{package_name}/{version}/json'

    response = requests.get(url)
    if response.status_code == 404:
        return False

    return True


def latest_version(package_name):
    # TODO
    # Fazer requisição na API do PyPI para descobrir a última versão
    # de um pacote. Retornar None se o pacote não existir.
    base_url = "https://pypi.org/pypi"
    url = f'{base_url}/{package_name}/json'

    response = requests.get(url)
    if response.status_code == 404:
        return None
    
    response = response.json()
    version = response['info']['version']
    
    return version
