<div align="center">

# 🛡️ FastAPI RBAC & JWT Auth Service

**Arquitetura Back-end segura para Autenticação Stateless e Controle de Acesso Granular.**

![Python](https://img.shields.io/badge/Python-3.10+-000000?style=for-the-badge&logo=python&logoColor=00FF41)
![FastAPI](https://img.shields.io/badge/FastAPI-000000?style=for-the-badge&logo=fastapi&logoColor=00FF41)
![JWT](https://img.shields.io/badge/JWT-Stateless-000000?style=for-the-badge&logo=jsonwebtokens&logoColor=00FF41)
![OWASP](https://img.shields.io/badge/OWASP-Top_10_Security-000000?style=for-the-badge&logo=owasp&logoColor=00FF41)

</div>

---

### 🏗️ Arquitetura & Segurança (`Security by Design`)

| Pilar Técnico | Implementação no Código |
| :--- | :--- |
| **🔐 Hashing Criptográfico** | Senhas protegidas com **Bcrypt** (`Passlib`) e *salt* automático contra força bruta. |
| **🎟️ Autenticação Stateless** | Emissão e validação de tokens assinados via **PyJWT** com expiração (`exp`). |
| **🛂 Controle de Acesso (RBAC)** | Injeção de dependências (`Depends`) validando escopos (`user` vs `admin`). |
| **🛡️ Sanitização de Payloads** | Schemas estritos com **Pydantic**, bloqueando dados malformados e vazamento de hashes. |
| **🚦 Respostas Padronizadas** | Tratamento explícito de exceções HTTP (`400`, `401`, `403`) sem expor *stack traces*. |

---

### 🔌 Mapa de Endpoints

| Método | Rota | Descrição | Escopo Exigido |
| :--- | :--- | :--- | :--- |
| `POST` | `/cadastro` | Registra usuário com atribuição de papel (`usuario` ou `admin`). | 🔓 Pública |
| `POST` | `/login` | Autentica credenciais e gera o `access_token` (Bearer JWT). | 🔓 Pública |
| `GET` | `/sala-comum` | Área protegida acessível a qualquer identidade autenticada. | 🔑 `Bearer Token` |
| `GET` | `/sala-do-chefe` | Área administrativa restrita por validação de privilégio. | 👑 `Bearer Token (admin)` |

---

### 🚀 Como Executar Localmente

```bash
# 1. Clone o repositório e acesse a pasta
git clone [https://github.com/noahsvieira/Sistema-de-Autenticacao-e-Controle-de-Acesso-RBAC-.git](https://github.com/noahsvieira/Sistema-de-Autenticacao-e-Controle-de-Acesso-RBAC-.git)
cd Sistema-de-Autenticacao-e-Controle-de-Acesso-RBAC-

# 2. Instale as dependências
pip install fastapi uvicorn pydantic "passlib[bcrypt]" pyjwt

# 3. Inicie o servidor ASGI
uvicorn seguranca:app --reload
```

> 📖 Após iniciar, acesse **`http://127.0.0.1:8000/docs`** para testar os fluxos no **Swagger UI** (use o botão *Authorize* para injetar o token).

---

<div align="center">
  Desenvolvido por <b>Noah Souza Vieira</b> — Back-end & DevSecOps<br><br>
  <a href="https://linkedin.com/in/noah-ti"><img src="https://img.shields.io/badge/LinkedIn-000000?style=flat-square&logo=linkedin&logoColor=00FF41" /></a>
  <a href="https://github.com/noahsvieira"><img src="https://img.shields.io/badge/GitHub-000000?style=flat-square&logo=github&logoColor=00FF41" /></a>
</div>
