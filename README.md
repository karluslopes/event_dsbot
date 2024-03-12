# FUNCIONALIDADES

**1. Criação de Eventos**
1.1. Agendamento de eventos
1.2. Definições de permissões de acesso
1.3. Definições de canais de eventos
1.4. Predefinições de Eventos

**2. Distribuição de Espólios**
2.1. Participação percentual por tempo relativo
2.2. Taxação administrativa
2.3. Possibilidade de ajustes percentuais

**3. Rankeamento**
3.1. Colocação por participação de espólios
3.2. Colocação por tempo de participação
3.3. Definições de XP e Cargos por níveis de participação



# PARÂMENTROS DE EVENTOS
1. Tipo (Selecionável e Personalisável, Obrigatório)
2. Data e Hora (Selecionável, Obrigatório)
3. Cargos Permitidos (Selecionável, Opcional)
4. Canal de Voz (Selecionável, Opcional)
5. Permitir visitante? (S/n)
6. Evento c/ Espólios? (S/n)
7. Ativar tópico? (S/n)
8. Confirmação de Inscrição (Pelo Membro/ Pelo Criador)
9. Incuir Descrição? (S/n)



# PARÂMETROS DE DISTRIBUIÇÃO DE ESPÓLIOS
1. Cronômetro por Reação (Início e fim do evento)
2. Definição de Valor do Espólio
3. Ajustes de participações



# PARÂMETROS DE CONFIGURAÇÕES
**1. Permissões**
1.1. Cargo Administrador
1.2. Cargo Usuário
1.3. Cargo padrão de permissão de participação
1.4. Cargo padrão de @Evento
1.5. Cargos visitantes por padrão
1.6. Aceitar visitantes por padrão? (S/n)

**2. Canais**
2.1. Canal de Voz padrão de eventos
2.2. Chat de Ping de Eventos
2.3. Chat de Espólios
2.4. Chat de Ranking
2.5. Ativação de Tópico de Ping por padrão (S/n)

**3. Espólios**
3.1. Taxa Administrativa (%)
3.2. Ativação de Espólios por padrão (S/n)

**4. XP**
4.1. XP/hora
4.2. Níveis/XP
4.3. Cargos/Níveis
4.4. Manter apenas a ultima promoção?
4.5. Mensagem de Nivelamento automática
4.6. Mensagem de Promoção automática

**5. Predefinições**
5.1. Cadastros de Tipos de Eventos
5.2. Editar/Excluir de Predefinições

**6. Ajustes**
6.1. Adicionar/ Remover/ Definir XP de membro
6.2. Limpar todos os dados.


# ESTRUTURA DO BANCO DE DADOS

**Tabela de Permissões (ID Roles)**
- ID (STR)
- ADM (BOOL)
- USER (BOOL)
- PARTICIPANT (BOOL)
- VISITOR (BOOL)

**Tabela de Patentes (ID Roles)**
- ID (STR)
- LEVEL ASSIGMENT (INT)
- MESSAGE ASSIGMENT (STR)

**Tabela de Registro de Atividade (ID Members)**
- ID (STR)
- DATE (INT)
- TIME (INT)
- XP (INT)
- LEVEL (INT)

**Tabela de Definições de Sistema**
- DEFAULT VOICE CHANNEL (STR)
- PING CHANNEL (STR)
- SPLIT CHANNEL SPLIT (STR)
- RANKING CHANNEL (STR)
- AUTO ENABLE VISITOR (BOOL)
- EVENT ROLE (STR)
- AUTO CREATE TOPIC (BOOL)
- ADMIN FEE (FLOAT)
- AUTO ENABLE SPLIT (BOOL)
- XP MODIFIER (INT)
- XP BASE LEVEL (INT)
- AUTO MESSAGE LEVEL (STR)

**Tabela de Eventos Agendados**
- NAME
- DATE/TIME
- VOICE CHANNEL
- ALLOW VISITOR
- ENABLE SPLIT
- ENABLE PING TOPIC
- AUTO REGISTRATION CONFIRM
- INCLUDE DESCRIPTION