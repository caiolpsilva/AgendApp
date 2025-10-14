# Manual do Usuário - Sistema de Reserva de Laboratórios

## 📖 Introdução

Bem-vindo ao Sistema de Reserva de Laboratórios de Informática! Este manual irá guiá-lo através de todas as funcionalidades disponíveis na aplicação, desde o primeiro acesso até operações avançadas.

## 🚀 Primeiros Passos

### Acesso ao Sistema

1. **URL de Acesso**: Abra seu navegador e acesse `http://127.0.0.1:8000` (ou o endereço fornecido pelo administrador)
2. **Página Inicial**: Você será automaticamente redirecionado para a página de login

### Fazendo Login

1. Na página de login, insira suas credenciais:
   - **Nome de usuário**: Seu nome de usuário fornecido pelo administrador
   - **Senha**: Sua senha pessoal
2. Clique no botão **"Entrar"**
3. Após login bem-sucedido, você será redirecionado para a página principal

> **Nota**: Se você esqueceu sua senha ou não possui credenciais, entre em contato com o administrador do sistema.

## 🏠 Página Principal (Dashboard)

Após o login, você verá a página principal com:

- **Cabeçalho**: Saudação com seu nome de usuário
- **Botão "+ Nova Reserva"**: Para criar uma nova reserva
- **Tabela de Reservas**: Lista todas as reservas existentes
- **Botão "Sair"**: Para fazer logout

### Entendendo a Tabela de Reservas

A tabela exibe as seguintes colunas:
- **Laboratório**: Nome do laboratório reservado
- **Data**: Data da reserva (formato dd/mm/yyyy)
- **Início**: Horário de início da reserva
- **Fim**: Horário de término da reserva
- **Professor**: Nome do usuário que fez a reserva
- **Ações**: Links para editar/excluir (apenas suas reservas)

## 📝 Criando uma Nova Reserva

1. Na página principal, clique no botão **"+ Nova Reserva"**
2. Você será direcionado para o formulário de criação

### Preenchendo o Formulário

**Campo Laboratório**:
- Selecione o laboratório desejado da lista suspensa
- Cada laboratório tem uma capacidade específica

**Campo Data**:
- Clique no campo de data para abrir o calendário
- Selecione a data desejada
- **Nota**: Não é possível reservar datas passadas

**Campo Horário de Início**:
- Digite ou selecione o horário de início
- Formato: HH:MM (ex: 08:00, 14:30)

**Campo Horário de Fim**:
- Digite ou selecione o horário de término
- Deve ser posterior ao horário de início

### Salvando a Reserva

1. Após preencher todos os campos, clique em **"Salvar"**
2. O sistema irá validar:
   - Se o horário de início é anterior ao horário de fim
   - Se não há conflitos com outras reservas no mesmo laboratório e data
3. Se tudo estiver correto, você será redirecionado para a página principal
4. Se houver erros, mensagens de validação aparecerão em vermelho

### Possíveis Erros de Validação

- **"O horário de início deve ser menor que o horário de fim"**: Ajuste os horários
- **"Já existe uma reserva neste laboratório nesse horário"**: Escolha outro horário ou laboratório

## ✏️ Editando uma Reserva

1. Na tabela de reservas, localize sua reserva
2. Clique no link **"Editar"** na coluna Ações
3. Você será direcionado para o formulário de edição (pré-preenchido com os dados atuais)
4. Modifique os campos necessários
5. Clique em **"Salvar alterações"**
6. As mesmas validações de criação se aplicam

> **Importante**: Você só pode editar suas próprias reservas. Reservas de outros professores aparecem com "—" na coluna Ações.

## 🗑️ Excluindo uma Reserva

1. Na tabela de reservas, localize sua reserva
2. Clique no link **"Excluir"** na coluna Ações
3. Você verá uma página de confirmação com os detalhes da reserva
4. Leia atentamente as informações
5. Clique em **"Confirmar Exclusão"** para prosseguir ou **"Cancelar"** para voltar

> **Atenção**: Esta ação não pode ser desfeita. A reserva será permanentemente removida do sistema.

## 🔍 Visualizando Reservas

### Todas as Reservas
- A página principal mostra **todas** as reservas do sistema
- Ordenadas por data e horário (mais antigas primeiro)
- Você pode ver reservas de todos os professores

### Suas Reservas
- Suas reservas são destacadas (você pode editá-las/excluí-las)
- Reservas de outros professores são apenas para visualização

## 🚪 Fazendo Logout

Para sair do sistema:
1. Role até o final da página principal
2. Clique no botão **"Sair"**
3. Você será redirecionado para a página de login

> **Dica de Segurança**: Sempre faça logout quando terminar de usar o sistema, especialmente em computadores compartilhados.

## 📱 Usando em Dispositivos Móveis

O sistema é totalmente responsivo e funciona perfeitamente em:
- **Smartphones**: Interface otimizada para telas pequenas
- **Tablets**: Layout adaptável
- **Computadores**: Interface completa

### Dicas para Mobile
- Use o navegador em modo paisagem para melhor visualização
- Toque nos campos de data/hora para abrir seletores nativos
- Deslize a tela para ver todas as reservas

## ❓ Solução de Problemas

### Problemas Comuns

**"Credenciais inválidas"**
- Verifique se o nome de usuário e senha estão corretos
- Considere maiúsculas/minúsculas
- Entre em contato com o administrador se persistir

**"Erro ao salvar reserva"**
- Verifique se todos os campos estão preenchidos
- Certifique-se de que o horário de fim é posterior ao início
- Tente outro horário/laboratório se houver conflito

**"Página não carrega"**
- Verifique sua conexão com a internet
- Tente atualizar a página (F5)
- Limpe o cache do navegador

**"Botão não funciona"**
- Certifique-se de estar logado
- Verifique se você tem permissões para a ação
- Tente recarregar a página

### Validações do Sistema

O sistema possui várias validações automáticas:

1. **Horários**: Início deve ser anterior ao fim
2. **Conflitos**: Não permite reservas sobrepostas no mesmo laboratório
3. **Datas**: Não permite reservas em datas passadas
4. **Permissões**: Só permite editar/excluir reservas próprias

## 📞 Suporte

Se você encontrou um problema não listado acima:

1. **Anote os detalhes**: O que você estava fazendo, qual erro apareceu
2. **Tire um print** da tela (se possível)
3. **Entre em contato** com o administrador do sistema ou equipe de TI

### Informações Úteis para Suporte
- Seu nome de usuário
- Data e hora do problema
- Descrição exata do erro
- Navegador utilizado
- Dispositivo (computador, celular, etc.)

## 🔒 Dicas de Segurança

- **Nunca compartilhe** sua senha com outras pessoas
- **Faça logout** sempre que sair do computador
- **Mantenha seu navegador atualizado**
- **Use uma senha forte** (combinação de letras, números e símbolos)
- **Não acesse** o sistema em redes públicas sem VPN

## 🎯 Dicas e Boas Práticas

### Planejamento de Reservas
- **Reserve com antecedência** para garantir disponibilidade
- **Verifique conflitos** antes de confirmar
- **Considere a capacidade** do laboratório para seu número de alunos

### Organização
- **Mantenha suas reservas atualizadas** se houver mudanças
- **Cancele reservas** que não serão utilizadas
- **Use horários realistas** para suas aulas

### Eficiência
- **Use a visualização de lista** para ver todas as reservas
- **Acesse regularmente** para acompanhar suas reservas
- **Configure lembretes** para suas reservas importantes

---

**Última atualização**: Outubro 2024
**Versão do Sistema**: 1.0
**Framework**: Django 5.2.7

Para mais informações técnicas, consulte o README.md do projeto.
