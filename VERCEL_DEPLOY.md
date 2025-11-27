# Deploy no Vercel - SpeakWise Real

Guia completo para fazer deploy do SpeakWise Real no Vercel.

## 📋 Variáveis de Ambiente Necessárias

### Para o Backend (API)

No painel do Vercel, adicione estas variáveis de ambiente:

1. **GOOGLE_API_KEY**
   - Valor: Sua chave da API do Google Gemini
   - Exemplo: `AIzaSyCdXunfTvMR6KuaeYNrcn7qEkb1BpydE6c`

2. **GOOGLE_MODEL**
   - Valor: `gemini-pro` (ou outro modelo do Gemini)
   - Padrão: `gemini-pro`

3. **ELEVENLABS_API_KEY**
   - Valor: Sua chave da API do ElevenLabs
   - Exemplo: `sk_7e226b20506d08ef688d4d0def661073228f89148fc93dca`

### Para o Frontend

1. **REACT_APP_API_URL**
   - Valor: URL do seu backend deployado no Vercel
   - Exemplo: `https://seu-backend.vercel.app`
   - ⚠️ **Importante**: Adicione esta variável DEPOIS de fazer deploy do backend para obter a URL correta

## 🚀 Passo a Passo do Deploy

### Opção 1: Deploy Separado (Recomendado)

#### 1. Deploy do Backend

1. No Vercel, crie um novo projeto
2. Conecte o repositório GitHub
3. Configure o projeto:
   - **Root Directory**: `backend`
   - **Framework Preset**: Other
   - **Build Command**: (deixe vazio ou `pip install -r requirements.txt`)
   - **Output Directory**: (deixe vazio)
   - **Install Command**: `pip install -r requirements.txt`

4. Adicione as variáveis de ambiente:
   - `GOOGLE_API_KEY`
   - `GOOGLE_MODEL` (opcional, padrão: `gemini-pro`)
   - `ELEVENLABS_API_KEY`

5. Crie o arquivo `backend/vercel.json`:
```json
{
  "version": 2,
  "builds": [
    {
      "src": "app/main.py",
      "use": "@vercel/python"
    }
  ],
  "routes": [
    {
      "src": "/(.*)",
      "dest": "app/main.py"
    }
  ]
}
```

6. Faça o deploy e copie a URL (ex: `https://seu-backend.vercel.app`)

#### 2. Deploy do Frontend

1. No Vercel, crie outro projeto
2. Conecte o mesmo repositório GitHub
3. Configure o projeto:
   - **Root Directory**: `frontend`
   - **Framework Preset**: Create React App
   - **Build Command**: `npm run build`
   - **Output Directory**: `build`
   - **Install Command**: `npm install`

4. Adicione a variável de ambiente:
   - `REACT_APP_API_URL`: URL do backend que você copiou (ex: `https://seu-backend.vercel.app`)

5. Faça o deploy

### Opção 2: Deploy com Monorepo

Se quiser tudo em um projeto:

1. Crie `vercel.json` na raiz:
```json
{
  "version": 2,
  "builds": [
    {
      "src": "backend/app/main.py",
      "use": "@vercel/python"
    },
    {
      "src": "frontend/package.json",
      "use": "@vercel/static-build",
      "config": {
        "distDir": "build"
      }
    }
  ],
  "routes": [
    {
      "src": "/api/(.*)",
      "dest": "backend/app/main.py"
    },
    {
      "src": "/(.*)",
      "dest": "frontend/$1"
    }
  ]
}
```

2. Configure o projeto:
   - **Root Directory**: (raiz do projeto)
   - **Build Command**: `cd frontend && npm run build`
   - **Output Directory**: `frontend/build`

3. Adicione TODAS as variáveis de ambiente listadas acima

## 📝 Como Adicionar Variáveis de Ambiente no Vercel

1. Acesse seu projeto no Vercel
2. Vá em **Settings** → **Environment Variables**
3. Clique em **Add New**
4. Adicione cada variável:
   - **Name**: Nome da variável (ex: `GOOGLE_API_KEY`)
   - **Value**: Valor da variável
   - **Environment**: Selecione Production, Preview, e Development
5. Clique em **Save**
6. **Importante**: Após adicionar variáveis, faça um novo deploy

## 🔧 Arquivos de Configuração Necessários

### backend/vercel.json
```json
{
  "version": 2,
  "builds": [
    {
      "src": "app/main.py",
      "use": "@vercel/python"
    }
  ],
  "routes": [
    {
      "src": "/(.*)",
      "dest": "app/main.py"
    }
  ]
}
```

### frontend/vercel.json (opcional)
```json
{
  "buildCommand": "npm run build",
  "outputDirectory": "build",
  "devCommand": "npm start",
  "installCommand": "npm install"
}
```

## ⚠️ Ajustes Necessários no Código

### Atualizar CORS no Backend

No arquivo `backend/app/main.py`, atualize o CORS para aceitar o domínio do Vercel:

```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://localhost:5173",
        "https://seu-frontend.vercel.app",  # Adicione sua URL do Vercel
        "https://*.vercel.app"  # Ou aceite todos os subdomínios do Vercel
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

## 🧪 Testar o Deploy

1. Acesse a URL do frontend
2. Tente fazer upload de um áudio
3. Tente analisar um pitch
4. Verifique os logs no Vercel se houver erros

## 📚 Recursos Úteis

- [Documentação do Vercel para Python](https://vercel.com/docs/concepts/functions/serverless-functions/runtimes/python)
- [Documentação do Vercel para React](https://vercel.com/docs/concepts/deployments/overview)
- [Variáveis de Ambiente no Vercel](https://vercel.com/docs/concepts/projects/environment-variables)

## 🐛 Troubleshooting

### Erro: "Module not found"
- Certifique-se de que todas as dependências estão no `requirements.txt`
- Verifique se o `vercel.json` está configurado corretamente

### Erro: "Environment variable not set"
- Verifique se adicionou as variáveis no painel do Vercel
- Certifique-se de que fez um novo deploy após adicionar as variáveis

### Erro de CORS
- Atualize o CORS no backend com a URL do frontend
- Faça um novo deploy do backend

### Frontend não conecta ao backend
- Verifique se `REACT_APP_API_URL` está configurada corretamente
- Certifique-se de que a URL do backend está acessível

