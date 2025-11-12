# Envio de Mensagens com Supabase e Z-API
# Criar tabela no Supabase
 Crie um projeto no [Supabase](https://supabase.com/)  
 Vá em Table Editor/ New Table  
 Nome da tabela: `contatos`  
 Colunas:  
   id = int, auto increment, primary key  
  nome = text  
  telefone = text  
  Salve e adicione contatos de teste

# Variáveis de ambiente (.env)
.env
# Z-API
INSTANCE_NAME=nome_da_instancia
CLIENT_TOKEN=seu_client_token

# Supabase
SUPABASE_URL=https://SEU-PROJETO.supabase.co
SUPABASE_KEY=SUA_CHAVE_ANON

# Rodar o Projeto
pip install requests python-dotenv supabase
python main.py

# commit
git init 
