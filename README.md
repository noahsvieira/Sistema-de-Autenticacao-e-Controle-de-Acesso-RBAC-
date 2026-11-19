# fastapi-rbac-auth

Microsserviço de autenticação e controle de acesso desenvolvido para garantir segurança em nível de aplicação, utilizando arquitetura stateless e validação estrita de permissões.

---

### Contexto & Objetivo
Construído para resolver o problema comum de escalabilidade em rotas protegidas. O projeto implementa um fluxo onde a emissão de tokens JWT elimina a necessidade de consultas excessivas ao banco de dados, enquanto o mecanismo de RBAC (Role-Based Access Control) blinda endpoints sensíveis contra acessos indevidos.

---

### Stack & Decisões Técnicas

- **Core:** Python 3.10+ / FastAPI (escolhido pela alta performance assíncrona e documentação OpenAPI nativa).
- **Segurança:** Passlib com `bcrypt` para hash de credenciais com salt automático.
- **Sessão:** `PyJWT` para assinatura e validação de tokens com tempo de vida útil controlado (`exp`).
- **Validação:** Schemas estritos via `Pydantic` para sanitização de payload na borda da API.

---

### Estrutura de Endpoints

```text
POST /cadastro   -> Registra novo usuário e define nível de permissão (user/admin)
POST /login      -> Valida credenciais e retorna Bearer Token assinado
GET  /sala-comum -> Endpoint protegido (requer autenticação válida)
GET  /sala-chefe -> Endpoint restrito (requer privilégio de administrador)
