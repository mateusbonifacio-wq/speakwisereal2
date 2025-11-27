# 🔐 Variáveis de Ambiente - SpeakWise Real

## Lista Completa de Variáveis de Ambiente

### Para o Backend (API)

| Variável | Obrigatória | Descrição | Exemplo |
|----------|-------------|-----------|---------|
| `GOOGLE_API_KEY` | ✅ Sim | Chave da API do Google Gemini | ` |
| `GOOGLE_MODEL` | ❌ Não | Modelo do Gemini a usar (padrão: `gemini-pro`) | `gemini-pro` |
| `ELEVENLABS_API_KEY` | ✅ Sim | Chave da API do ElevenLabs para transcrição |  |
| `ALLOWED_ORIGINS` | ❌ Não | URLs permitidas para CORS (separadas por vírgula) |  |

### Para o Frontend

| Variável | Obrigatória | Descrição | Exemplo |
|----------|-------------|-----------|---------|
| `REACT_APP_API_URL` | ❌ Não* | URL do backend (padrão: `http://localhost:8000`) | `https://seu-backend.vercel.app` |

*Obrigatória apenas em produção

## 📝 Como Configurar no Vercel

### 1. Acesse o Painel do Vercel
- Vá para [vercel.com](https://vercel.com)
- Faça login e selecione seu projeto

### 2. Adicione Variáveis de Ambiente
1. Vá em **Settings** → **Environment Variables**
2. Clique em **Add New**
3. Para cada variável:
   - **Name**: Nome da variável (ex: `GOOGLE_API_KEY`)
   - **Value**: Valor da variável
   - **Environment**: 
     - ✅ Production
     - ✅ Preview  
     - ✅ Development
4. Clique em **Save**

### 3. Variáveis para Adicionar

#### Backend Project:
```
GOOGLE_API_KEY=AIzaSyCdXunfTvMR6KuaeYNrcn7qEkb1BpydE6c
GOOGLE_MODEL=gemini-pro
ELEVENLABS_API_KEY=sk_7e226b20506d08ef688d4d0def661073228f89148fc93dca
ALLOWED_ORIGINS=https://seu-frontend.vercel.app
```

#### Frontend Project:
```
REACT_APP_API_URL=https://seu-backend.vercel.app
```

## ⚠️ Importante

1. **Após adicionar variáveis, faça um novo deploy**
2. **Não commite chaves de API no código**
3. **Use variáveis diferentes para produção e desenvolvimento**
4. **Revogue e regenere chaves se expostas acidentalmente**

## 🔄 Ordem de Deploy

1. **Primeiro**: Deploy do Backend
   - Adicione: `GOOGLE_API_KEY`, `GOOGLE_MODEL`, `ELEVENLABS_API_KEY`
   - Copie a URL do backend (ex: `https://seu-backend.vercel.app`)

2. **Segundo**: Deploy do Frontend
   - Adicione: `REACT_APP_API_URL` com a URL do backend
   - Atualize `ALLOWED_ORIGINS` no backend com a URL do frontend

## 🧪 Verificar Variáveis

### No Backend
Acesse: `https://seu-backend.vercel.app/health`

### No Frontend
As variáveis começam com `REACT_APP_` e são acessíveis via `process.env.REACT_APP_API_URL`

## 📚 Links Úteis

- [Vercel Environment Variables](https://vercel.com/docs/concepts/projects/environment-variables)
- [Google Gemini API Keys](https://makersuite.google.com/app/apikey)
- [ElevenLabs API Keys](https://elevenlabs.io/app/settings/api-keys)

