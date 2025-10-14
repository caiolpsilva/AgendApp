# Sistema de Reserva de Laboratórios de Informática

## 📋 Descrição

Aplicação web desenvolvida em Django para permitir que professores façam reservas de laboratórios de informática. O sistema oferece uma interface simples e responsiva, com funcionalidades completas de CRUD (Criar, Ler, Atualizar, Deletar) para reservas, além de autenticação individual de usuários.

##  Funcionalidades

- **Autenticação de Usuários**: Login individual para professores
- **Gerenciamento de Reservas**:
  - Criar novas reservas
  - Visualizar todas as reservas (ordenadas por data e horário)
  - Editar reservas próprias
  - Excluir reservas próprias
- **Validações Automáticas**:
  - Verificação de conflitos de horário
  - Validação de horários (início < fim)
- **Interface Responsiva**: Design adaptável para diferentes dispositivos
- **Registro Automático de Horários**: Persistência completa no banco de dados

## 🛠️ Tecnologias Utilizadas

- **Backend**: Django 5.2.7
- **Banco de Dados**: SQLite3
- **Frontend**: HTML5, CSS3 (em arquivos separados)
- **Autenticação**: Django Authentication System
- **Linguagem**: Python 3.x
- **Sistema Operacional**: Compatível com Windows, Linux e macOS

## 📁 Estrutura do Projeto

```
reserva_lab/
├── db.sqlite3                    # Banco de dados SQLite
├── manage.py                     # Script de gerenciamento Django
├── reserva_lab/                  # Configurações principais
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py              # Configurações do projeto
│   ├── urls.py                  # URLs principais
│   ├── wsgi.py
│   └── __pycache__/
├── reservas/                     # App principal
│   ├── __init__.py
│   ├── admin.py                 # Configurações do admin
│   ├── apps.py
│   ├── forms.py                 # Formulários Django
│   ├── models.py                # Modelos de dados
│   ├── tests.py
│   ├── urls.py                  # URLs do app
│   ├── views.py                 # Views (lógica)
│   ├── migrations/              # Migrações do banco
│   │   ├── 0001_initial.py
│   │   └── __init__.py
│   ├── static/                  # Arquivos estáticos
│   │   └── css/
│   │       ├── excluir_reserva.css
│   │       ├── form.css
│   │       ├── index.css
│   │       ├── login.css
│   │       └── style.css
│   └── templates/               # Templates HTML
│       ├── index.html
│       ├── criar_reserva.html
│       ├── editar_reserva.html
│       ├── excluir_reserva.html
│       └── registration/
│           └── login.html
└── static/                      # Arquivos estáticos coletados
```

## 🗄️ Modelo de Dados

### Laboratorio
- `id`: Chave primária (auto-incremento)
- `nome`: Nome do laboratório (máx. 100 caracteres)
- `capacidade`: Capacidade máxima de alunos

### Reserva
- `id`: Chave primária (auto-incremento)
- `laboratorio`: Chave estrangeira para Laboratorio
- `professor`: Chave estrangeira para User (Django auth)
- `data`: Data da reserva (DateField)
- `horario_inicio`: Horário de início (TimeField)
- `horario_fim`: Horário de fim (TimeField)

## 🎨 Design e Interface

- **Paleta de Cores**:
  - Fundo: #f4f6f9 (cinza claro)
  - Containers: Branco (#ffffff)
  - Botões: Azul (#3498db) com hover (#2980b9)
  - Cabeçalhos: Azul escuro (#2c3e50)
  - Texto: Cinza escuro (#333)

- **Fonte**: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif

- **Arquivos CSS Separados**:
  - `style.css`: Estilos globais e comuns
  - `index.css`: Estilos específicos da página principal
  - `form.css`: Estilos para formulários de criação/edição
  - `login.css`: Estilos da página de login
  - `excluir_reserva.css`: Estilos da página de exclusão

- **Layout Responsivo**:
  - Containers com largura máxima de 1000px (index) e 500px (formulários)
  - Padding e margens adaptáveis
  - Design mobile-friendly

## 🔧 Instalação e Configuração

### Pré-requisitos
- Python 3.8 ou superior
- Pip (gerenciador de pacotes Python)

### Passos de Instalação

1. **Clone o repositório** (ou copie os arquivos):
   ```bash
   git clone <url-do-repositorio>
   cd reserva_lab
   ```

2. **Crie um ambiente virtual** (recomendado):
   ```bash
   python -m venv venv
   # No Windows:
   venv\Scripts\activate
   # No Linux/macOS:
   source venv/bin/activate
   ```

3. **Instale as dependências**:
   ```bash
   pip install django
   ```

4. **Execute as migrações do banco de dados**:
   ```bash
   python manage.py migrate
   ```

5. **Crie um superusuário** (opcional, para acessar o admin):
   ```bash
   python manage.py createsuperuser
   ```

6. **Execute o servidor de desenvolvimento**:
   ```bash
   python manage.py runserver
   ```

7. **Acesse a aplicação**:
   - Abra o navegador em: http://127.0.0.1:8000
   - Para o painel admin: http://127.0.0.1:8000/admin

## 📖 Manual de Uso

### Primeiro Acesso
1. Acesse http://127.0.0.1:8000
2. Você será redirecionado para a página de login
3. Use as credenciais criadas ou entre em contato com o administrador

### Criando uma Reserva
1. Na página inicial, clique em "+ Nova Reserva"
2. Preencha os campos:
   - **Laboratório**: Selecione o laboratório desejado
   - **Data**: Escolha a data da reserva
   - **Horário de Início**: Defina o horário de início
   - **Horário de Fim**: Defina o horário de término
3. Clique em "Salvar"
4. O sistema validará automaticamente conflitos de horário

### Editando uma Reserva
1. Na lista de reservas, clique em "Editar" na reserva desejada
2. Modifique os campos necessários
3. Clique em "Salvar alterações"

### Excluindo uma Reserva
1. Na lista de reservas, clique em "Excluir" na reserva desejada
2. Confirme a exclusão clicando em "Confirmar Exclusão"

### Funcionalidades do Sistema
- **Validação de Conflitos**: O sistema impede reservas sobrepostas no mesmo laboratório
- **Acesso Restrito**: Usuários só podem editar/excluir suas próprias reservas
- **Interface Responsiva**: Funciona em desktop, tablet e mobile
- **Logout**: Botão "Sair" no final da página inicial

## 🔒 Segurança

- Autenticação obrigatória para todas as operações
- Validação de formulários no backend
- Proteção CSRF em todos os formulários
- Usuários só acessam suas próprias reservas

## 🧪 Testes

Para executar os testes (atualmente básicos):
```bash
python manage.py test
```

## 📊 Painel Administrativo

Acesse `/admin` para:
- Gerenciar laboratórios
- Visualizar todas as reservas
- Gerenciar usuários

## 🚀 Deploy em Produção

Para deploy em produção:
1. Configure `DEBUG = False` em settings.py
2. Defina `ALLOWED_HOSTS` adequadamente
3. Configure um servidor web (nginx, Apache)
4. Use um banco de dados mais robusto (PostgreSQL, MySQL)
5. Configure variáveis de ambiente para secrets

## 🤝 Contribuição

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`)
3. Commit suas mudanças (`git commit -am 'Adiciona nova feature'`)
4. Push para a branch (`git push origin feature/nova-feature`)
5. Abra um Pull Request

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

## 📞 Suporte

Para suporte, entre em contato com a equipe de desenvolvimento ou abra uma issue no repositório.

---

**Desenvolvido com ❤️ usando Django**
