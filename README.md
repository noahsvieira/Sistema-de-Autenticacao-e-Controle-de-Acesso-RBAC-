<div align="center">

# 🛡️ FastAPI RBAC & JWT Auth Service

**Arquitetura Back-end de alta performance focada em Autenticação Stateless e Controle de Acesso Baseado em Papéis (RBAC).**

![Python](https://img.shields.io/badge/Python-3.10+-000000?style=for-the-badge&logo=python&logoColor=00FF41)
![FastAPI](https://img.shields.io/badge/FastAPI-000000?style=for-the-badge&logo=fastapi&logoColor=00FF41)
![JWT](https://img.shields.io/badge/JWT-Stateless-000000?style=for-the-badge&logo=jsonwebtokens&logoColor=00FF41)
![OWASP](https://img.shields.io/badge/OWASP-Security_by_Design-000000?style=for-the-badge&logo=owasp&logoColor=00FF41)

</div>

---

## ⚡ Visão Geral do Sistema

Este microsserviço foi estruturado sob os princípios de **Security by Design**, implementando barreiras de segurança rigorosas na camada de aplicação para mitigar riscos comuns mapeados pelo **OWASP Top 10** (como falhas de controle de acesso e autenticação).

---

## 🏗️ Decisões de Arquitetura & Segurança

| Pilar Técnico | Implementação Prática |
| :--- | :--- |
| **🔐 Criptografia de Senhas** | Utilização de **Bcrypt** (`Passlib`) com *salt* automático, blindando o banco de dados contra ataques de força bruta e *rainbow tables*. |
| **🎟️ Autenticação Stateless** | Emissão e validação de tokens digitais via **PyJWT** com tempo de expiração (`exp`), eliminando a necessidade de sessões em memória no servidor. |
| **🛂 Autorização Granular** | Aplicação de Injeção de Dependências (`Depends`) do FastAPI para checagem estrita de escopos e papéis (`user` vs `admin`) antes de executar rotas críticas. |
| **🛡️ Sanitização de Payloads** | Validação automática de schemas na entrada e saída de dados com **Pydantic**, prevenindo injeções e vazamento de atributos sensíveis. |
| **🚦 Tratamento de Exceções** | Mapeamento explícito de códigos HTTP (`400`, `401`, `403`) sem exposição de rastros internos de erro (*stack traces*). |

---

## 🔌 Mapa de Endpoints & Permissões

| Método | Rota | Descrição Técnica | Nível de Acesso |
| :--- | :--- | :--- | :--- |
| `POST` | `/cadastro` | Registra uma nova identidade e atribui seu respectivo papel de acesso. | 🔓 Público |
| `POST` | `/login` | Valida credenciais e retorna um `access_token` assinado (Bearer JWT). | 🔓 Público |
| `GET` | `/sala-comum` | Recurso protegido acessível por qualquer token válido. | 🔑 Autenticado (`user` / `admin`) |
| `GET` | `/sala-do-chefe` | Área restrita blindada por validação estrita de privilégios. | 👑 Restrito (`role == admin`) |

---

## 🚀 Guia de Execução Local

Clone o repositório e suba o ambiente com os seguintes comandos no terminal:

```bash
# 1. Clone o projeto e acesse o diretório
git clone [https://github.com/noahsvieira/Sistema-de-Autenticacao-e-Controle-de-Acesso-RBAC-.git](https://github.com/noahsvieira/Sistema-de-Autenticacao-e-Controle-de-Acesso-RBAC-.git)
cd Sistema-de-Autenticacao-e-Controle-de-Acesso-RBAC-

# 2. Instale as dependências essenciais
pip install fastapi uvicorn pydantic "passlib[bcrypt]" pyjwt

# 3. Inicie o servidor ASGI em modo de desenvolvimento
uvicorn seguranca:app --reload
