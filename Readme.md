    API de Integração Inicial para o Mercado Livre

Esta API tem a finalidade de auxiliar na integração com o Mercado Livre.

Todos os módulos listados no arquivo requirements.txt devem ser instalados em suas respectivas versões.

O arquivo main.py contém as rotas iniciais para que a integração seja realizada e o seu produto seja publicado com sucesso.

No arquivo gerador_accesstoken.py, como o próprio nome já diz, realiza a atualização do token de acesso.
Caso não saiba como adquirir o access token, não se preocupe, no final desta documentação há um link para um canal no YouTube que ensina passo a passo e ainda fornece mais informações sobre a integração e parametrização deste código.

O arquivo refresh_loop.py foi criado com a finalidade de testar a renovação do Access_Token. Recomendo que, antes de subir a aplicação, você realize os devidos testes e valide as atualizações.

A pasta sql_app contém os arquivos referentes ao banco de dados, onde já existem tabelas e campos criados.
No arquivo database.py, você realizará a configuração da sua instância. No meu caso, utilizei o banco de dados Postgres, mas você pode usar outro de sua preferência. (Caso use outro modelo de BD, faça os devidos ajustes no código).

A pasta scripts contém vários arquivos de acordo com a documentação completa do Mercado Livre. Caso deseje realizar a integração de outras funcionalidades, basta adicioná-las ao código.

Link do canal no YouTube ensinando a como obter o Access_Token:
https://www.youtube.com/watch?v=l4qpOFXlCmA

Recomendo que vejam os demais vídeos deste canal, pois ele possui vários tutoriais relacionados à integração com o Mercado Livre.



    English

Initial Integration API for Mercado Libre

This API aims to assist with the integration with Mercado Libre.

All modules listed in the requirements.txt file must be installed in their respective versions.

The main.py file contains the initial routes for the integration to be completed successfully and for your product to be published.

The gerador_accesstoken.py file, as the name suggests, updates the access token.
If you do not know how to acquire the access token, do not worry, at the end of this documentation there is a link to a YouTube channel that provides a step-by-step guide and more information about the integration and parameterization of this code.

The refresh_loop.py file was created to test the Access_Token refresh. I recommend performing the necessary tests and validating the updates before deploying the application.

The sql_app folder contains files related to the database, where tables and fields are already created.
In the database.py file, you will configure your instance. In my case, I used the Postgres database, but you can use another one of your choice. (If you use another type of database, make the necessary adjustments in the code).

The scripts folder contains various files according to the complete documentation of Mercado Libre. If you want to integrate additional functionalities, just add them to the code.

Link to the YouTube channel teaching how to obtain the Access_Token:
https://www.youtube.com/watch?v=l4qpOFXlCmA

I recommend watching the other videos on this channel as it has several tutorials related to the integration with Mercado Libre.







