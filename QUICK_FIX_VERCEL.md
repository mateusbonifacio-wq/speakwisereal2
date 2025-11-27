# 🔧 Correção Rápida - Erro 404 no Vercel

## Problema
O Vercel está retornando erro 404 porque não encontra a aplicação corretamente.

## ✅ Solução

### Opção 1: Configurar Root Directory no Vercel (Mais Simples)

1. **No painel do Vercel:**
   - Vá em **Settings** → **General**
   - Em **Root Directory**, selecione **Edit**
   - Digite: `backend`
   - Clique em **Save**

2. **Configure o Framework:**
   - Framework Preset: **Other**
   - Build Command: (deixe vazio)
   - Output Directory: (deixe vazio)
   - Install Command: `pip install -r requirements.txt`

3. **Adicione as variáveis de ambiente:**
   - `GOOGLE_API_KEY`
   - `GOOGLE_MODEL=gemini-pro`
   - `ELEVENLABS_API_KEY`
   - `ALLOWED_ORIGINS` (URL do frontend quando fizer deploy)

4. **Faça um novo deploy**

### Opção 2: Usar o arquivo vercel.json na raiz

O arquivo `vercel.json` já foi criado na raiz do projeto. Se ainda não funcionar:

1. **No painel do Vercel:**
   - Vá em **Settings** → **General**
   - **Root Directory**: (deixe vazio ou remova)
   - O Vercel usará o `vercel.json` da raiz

2. **Adicione as variáveis de ambiente** (mesmas da Opção 1)

3. **Faça um novo deploy**

## 📝 Variáveis de Ambiente Obrigatórias

No Vercel → Settings → Environment Variables, adicione:

```
GOOGLE_API_KEY=AIzaSyCdXunfTvMR6KuaeYNrcn7qEkb1BpydE6c
GOOGLE_MODEL=gemini-pro
ELEVENLABS_API_KEY=sk_7e226b20506d08ef688d4d0def661073228f89148fc93dca
```

## 🧪 Testar

Após o deploy, acesse:
- `https://seu-projeto.vercel.app/` - Deve retornar JSON com status
- `https://seu-projeto.vercel.app/health` - Deve retornar `{"status": "healthy"}`
- `https://seu-projeto.vercel.app/docs` - Documentação da API (Swagger)

## ⚠️ Se ainda não funcionar

1. Verifique os **Build Logs** no Vercel para ver erros
2. Verifique os **Runtime Logs** para erros em tempo de execução
3. Certifique-se de que todas as variáveis de ambiente foram adicionadas
4. Faça um novo deploy após qualquer alteração

