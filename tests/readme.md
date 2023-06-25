# Caso de Teste: Verificar a existência e validade do favicon (Teste Integração)

Esse tipo de teste envolve a interação entre componentes diferentes de um sistema, como a comunicação entre o aplicativo e um servidor web. Ele verifica se esses componentes estão funcionando corretamente juntos e se as interações ocorrem como o esperado.

## def test_favicon():

Dados de Entrada:

- website_url: "http://127.0.0.1:8000" (URL do website)

Etapa a ser seguida:

- Fazer uma requisição para a URL do website usando o método GET.
- Verificar se a resposta é bem-sucedida (código de status 200).
- Construir a URL do favicon usando a URL do website: favicon_url = website_url + "/static/images/favicon.ico."
- Fazer uma requisição HEAD para a URL do favicon.
- Verificar se a resposta da URL do favicon é bem-sucedida (código de status 200 ou 304).
- Obter o tipo de conteúdo (Content-Type) da resposta.
- Verificar se o tipo de conteúdo é "image/x-icon", indicando que é um favicon válido.

Resultados Esperados:

- A requisição para a URL do website retorna um código de status 200.
- A requisição para a URL do favicon retorna um código de status 200 ou 304.
- O tipo de conteúdo do favicon é "image/x-icon".

Critérios de Aprovação:

- Todos os resultados esperados são verificados sem erros. Caso contrário, uma mensagem de falha é exibida indicando a etapa em que o teste falhou.
É importante ressaltar que este caso de teste assume que o servidor local está em execução na URL "http://127.0.0.1:8000" e que o favicon está localizado em "/static/images/favicon.ico" dentro do servidor.
- Resultado:

![Img](/tests/img/test_favicon.png)

# Caso de Teste: Verifica se o acesso ao website é bem-sucedido (Teste Integração)

Esse tipo de teste está relacionado à integração entre os componentes do sistema, nesse caso, a integração entre o código que realiza a requisição HTTP e o website que está sendo testado.

Dados de entrada:

- URL: "http://127.0.0.1:8000/"

Etapa a ser seguida:

- Enviar uma solicitação HTTP GET para a URL fornecida.
- Obter a resposta da solicitação.

Resultados Esperados:

- O código de status da resposta deve ser igual a 200.

Critérios de Aprovação:

- Se o código de status da resposta for igual a 200, o teste é aprovado. Caso contrário, o teste falha.

- Resultado:

![Img](/tests/img/test_access.png)


# Caso de Teste: Verificar botoes, adicao de turma, HTML (Teste Integração, Sistema, Aceitação)

Teste de GUI (Interface Gráfica do Usuário) ou teste de interface do usuário. interação com um navegador web (usando a biblioteca Selenium) para testar a funcionalidade de adicionar uma turma em um site local (http://127.0.0.1:8000/). O código também faz uso de técnicas de web scraping (usando a biblioteca BeautifulSoup) para analisar o conteúdo HTML da página e contar o número de elementos com a classe "ui segment". O teste também inclui asserções para verificar se o número de elementos aumentou corretamente após a adição da turma.

    - Integração: pois envolve a interação com diferentes componentes e tecnologias, como Selenium para automação do navegador, BeautifulSoup para análise do conteúdo HTML e requests para fazer solicitações HTTP.
    - Sistema: determinar se os componentes de um sistema computacional (envolvendo outros componentes de software e/ou de hardware) se integram bem e realizam as funcionalidades que lhes foram especificadas.
    - Aceitação: o objetivo dos testes de aceitação é determinar se o software funciona da maneira esperada no desenvolvimento de software..

## def test_adicionar_turma():

Dados de Entrada:

- URL: "http://127.0.0.1:8000/"
- Turma ID: "388777"
- Time Slot: "156"

Etapa a ser seguida:

- Abrir o navegador Chrome.
- Acessar a URL fornecida.
- Maximizar a janela do navegador.
- Localizar o campo de entrada "turma_id" pelo nome e inserir o valor "388777".
- Localizar o campo de entrada "time_slot" pelo nome e inserir o valor "156".
- Encontrar o botão "Continue" na página e clicar nele.
- Realizar uma requisição GET para a mesma URL.
- Analisar o conteúdo HTML da resposta usando o BeautifulSoup.
- Encontrar todos os elementos <div> com a classe "ui segment".
- Contar o número de elementos encontrados.
- Realizar uma nova requisição GET para a mesma URL.
- Analisar o conteúdo HTML da resposta usando o BeautifulSoup.
- Encontrar todos os elementos <div> com a classe "ui segment" novamente.
- Contar o número de elementos encontrados novamente.

Resultados Esperados:

- O número de elementos "ui segment" após clicar no botão "Continue" deve ser igual ao número de elementos antes de clicar adicionado de 1.

Critérios de Aprovação:

- O teste é considerado aprovado se o número de elementos "ui segment" após clicar no botão "Continue" for igual ao número de elementos antes de clicar adicionado de 1. Caso contrário, o teste é considerado falho.

- Resultado:

![Img](/tests/img/test_system_turma.png)


# Versão do produto

![Img](/tests/img/produto.png)
