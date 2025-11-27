# 🔧 Correção do Erro 500 - FUNCTION_INVOCATION_FAILED

## Problema
O Vercel está retornando erro 500 porque a função serverless está falhando na inicialização.

## ✅ Soluções

### Solução 1: Configurar Root Directory (RECOMENDADO)

Esta é a solução mais simples e confiável:

1. **No painel do Vercel:**
   - Vá em **Settings** → **General**
   - Em **Root Directory**, clique em **Edit**
   - Digite: `backend`
   - Clique em **Save**

2. **Configure o Framework:**
   - Framework Preset: **Other**
   - Build Command: (deixe vazio)
   - Output Directory: (deixe vazio)
   - Install Command: `pip install -r requirements.txt`

3. **Adicione as variáveis de ambiente (OBRIGATÓRIO):**
   - Vá em **Settings** → **Environment Variables**
   - Adicione cada uma:
     - `GOOGLE_API_KEY` = `AIzaSyCdXunfTvMR6KuaeYNrcn7qEkb1BpydE6c`
     - `GOOGLE_MODEL` = `gemini-pro`
     - `ELEVENLABS_API_KEY` = `sk_7e226b20506d08ef688d4d0def661073228f89148fc93dca`
   - **IMPORTANTE**: Selecione **Production**, **Preview** e **Development** para cada variável

4. **Faça um novo deploy:**
   - Vá em **Deployments**
   - Clique nos três pontos do último deploy
   - Clique em **Redeploy**

### Solução 2: Verificar os Logs

Se ainda não funcionar:

1. **No Vercel, vá em:**
   - **Deployments** → Selecione o último deploy
   - Clique em **Runtime Logs** ou **Build Logs**

2. **Procure por erros como:**
   - `GOOGLE_API_KEY environment variable is not set`
   - `ELEVENLABS_API_KEY environment variable is not set`
   - `ModuleNotFoundError`
   - `ImportError`

3. **Corrija os erros encontrados**

## ⚠️ Erros Comuns

### Erro: "GOOGLE_API_KEY environment variable is not set"
**Solução**: Adicione a variável `GOOGLE_API_KEY` nas Environment Variables do Vercel

### Erro: "ELEVENLABS_API_KEY environment variable is not set"
**Solução**: Adicione a variável `ELEVENLABS_API_KEY` nas Environment Variables do Vercel

### Erro: "ModuleNotFoundError: No module named 'google'"
**Solução**: Certifique-se de que o `requirements.txt` está correto e que o Install Command está configurado como `pip install -r requirements.txt`

### Erro: "ImportError"
**Solução**: Verifique se o Root Directory está configurado como `backend`

## 📝 Checklist

Antes de fazer deploy, certifique-se de:

- [ ] Root Directory configurado como `backend`
- [ ] Install Command: `pip install -r requirements.txt`
- [ ] Variável `GOOGLE_API_KEY` adicionada
- [ ] Variável `GOOGLE_MODEL` adicionada (ou deixe padrão)
- [ ] Variável `ELEVENLABS_API_KEY` adicionada
- [ ] Todas as variáveis selecionadas para Production, Preview e Development
- [ ] Novo deploy feito após adicionar variáveis

## 🧪 Testar

Após o deploy bem-sucedido:

1. Acesse: `https://seu-projeto.vercel.app/`
   - Deve retornar: `{"service": "SpeakWise Real", "status": "running", "version": "1.0.0"}`

2. Acesse: `https://seu-projeto.vercel.app/health`
   - Deve retornar: `{"status": "healthy"}`

3. Acesse: `https://seu-projeto.vercel.app/docs`
   - Deve mostrar a documentação Swagger da API

## 💡 Dica

Se ainda tiver problemas, verifique os **Runtime Logs** no Vercel. Eles mostrarão o erro exato que está acontecendo.

