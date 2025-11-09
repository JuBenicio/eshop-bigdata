🛍️ E-Shop Brasil – Sistema de Gestão de Clientes com Big Data

📘 Introdução

Este projeto foi desenvolvido como parte da disciplina Advanced Databases and Big Data, com o objetivo de demonstrar na prática a utilização de bancos de dados NoSQL, tecnologias em contêiner e ferramentas de análise de dados.

A aplicação E-Shop Brasil simula um sistema de gerenciamento de clientes de uma loja virtual, permitindo inserir, visualizar e gerenciar registros em tempo real por meio de uma interface web simples e intuitiva.


---

⚙️ Objetivos do Projeto

Aplicar conceitos de Big Data e bancos de dados avançados na prática.

Utilizar o MongoDB como banco de dados NoSQL.

Executar o ambiente em contêineres Docker.

Desenvolver uma interface de controle com Streamlit (Python).

Demonstrar a integração entre banco, contêiner e aplicação web.



---

🧠 Tecnologias Utilizadas

Tecnologia	Função

🐳 Docker	Criação e execução do ambiente em contêiner
🍃 MongoDB	Banco de dados NoSQL usado para armazenar os clientes
🐍 Python	Linguagem principal do projeto
🎨 Streamlit	Interface web interativa
⚙️ PyMongo	Conector entre Python e MongoDB



---

🏗️ Arquitetura do Projeto

eshop-bigdata/
├── app.py                # Aplicação principal (Streamlit)
├── docker-compose.yml    # Configuração do container do MongoDB
├── requirements.txt      # Dependências do projeto
├── exemplos/             # Prints e capturas da aplicação
└── README.md             # Documentação do projeto


---

🚀 Como Executar o Projeto

🔹 1. Clonar o repositório

git clone https://github.com/JuBenicio/eshop-bigdata.git
cd eshop-bigdata

🔹 2. Subir o container do MongoDB

docker compose up -d

Verifique se o container está rodando:

docker ps

🔹 3. Executar a aplicação

python -m streamlit run app.py

Abra o navegador e acesse:
👉 http://localhost:8501


---

🧩 Descrição da Aplicação

A aplicação E-Shop Brasil permite:

Cadastrar novos clientes (Nome e E-mail)

Exibir a lista de clientes cadastrados

Editar e excluir registros (opcional, caso implementado)


Quando o usuário preenche os campos e clica em Salvar, as informações são armazenadas diretamente no MongoDB.
Abaixo do formulário, os dados aparecem atualizados automaticamente.


---

📸 Exemplo de Funcionamento

Etapa	Descrição	Imagem

1️⃣	Tela inicial	Interface da aplicação com os campos de entrada
2️⃣	Cadastro	Inserção de cliente e mensagem de sucesso
3️⃣	Listagem	Lista de clientes cadastrados no MongoDB



---

🎥 Demonstração em Vídeo

Apresentação do projeto (pitch e demonstração):
🔗 [Link do vídeo no YouTube – inserir aqui após gravar]

O vídeo mostra a execução da aplicação, a estrutura do código e a explicação das tecnologias utilizadas (Docker, MongoDB e Streamlit).




---

🧾 Conclusão

O projeto permitiu aplicar conceitos teóricos de Big Data e bancos de dados não relacionais em um ambiente real.
A integração entre Docker, MongoDB e Streamlit mostrou como é possível construir soluções escaláveis, simples e eficientes para análise e gerenciamento de dados.

Além disso, o trabalho reforçou o aprendizado sobre o uso de contêineres e a importância da flexibilidade dos bancos NoSQL em aplicações modernas.


---

👩‍💻 Autora

Julia Benicio
Disciplina: Advanced Databases and Big Data
Instituição: UniFECAF
Ano: 2025

🔗 Repositório no GitHub: https://github.com/JuBenicio/eshop-bigdata