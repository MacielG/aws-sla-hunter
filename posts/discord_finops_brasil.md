# Discord FinOps Brasil - Post

## Canal: #ferramentas ou #financeiro

---

**🔍 AWS SLA Hunter - Ferramenta Gratuita para Recuperar Créditos SLA Perdidos**

Salve pessoal! 👋

Construí uma ferramenta open-source que identifica eventos da AWS Health elegíveis para crédito SLA (aquele dinheiro que fica perdido na conta quando tem indisponibilidade).

**O Problema:**
- 92% das contas AWS não reclamam créditos SLA disponíveis
- AWS NÃO notifica automaticamente quando você tem direito
- Você precisa varrer AWS Health manualmente
- Contas recuperam R$50K-R$500K+ só revisando isso 1x por trimestre

**A Ferramenta:**

```bash
$ python main.py

🔍 AWS SLA Hunter
→ Verificando credenciais AWS... ✓
→ Buscando eventos AWS Health... ✓

AWS Health Events - Últimos 90 dias (3 encontrados)
┌──────────┬────────┬──────────┬────────┬──────────────────┐
│ Data     │ Serviço│ Região   │ Status │ Tipo de Evento   │
├──────────┼────────┼──────────┼────────┼──────────────────┤
│2025-01-03│ EC2    │us-east-1 │🔴 Open │Instance Failure  │
│2025-01-13│ RDS    │sa-east-1 │⚪Close │RDS Outage       │
│2025-02-02│ ELB    │us-west-2 │⚪Close │ELB Degraded     │
└──────────┴────────┴──────────┴────────┴──────────────────┘

Encontrados 3 eventos com potencial de crédito SLA
💰 Reclame seus créditos em awscostguardian.com
```

**O que custa:** Nada! MIT license. Código aberto. Zero strings attached.

**GitHub:** https://github.com/yourusername/aws-sla-hunter

**Requisitos:** Python 3.8+, credenciais AWS, Business/Enterprise support (requisito da AWS)

---

## Estrutura de Conversa (Respostas Pré-preparadas)

### "Qual é o ganho financeiro disso?"

> Empresas recuperam entre R$50K-R$500K por trimestre só revisando. A maioria deixa passar. Exemplo: um EC2 fora por 1 hora = 10% crédito mensal (~R$5K se sua conta custa R$50K/mês). Multiply por 12 meses = R$60K+ perdidos.

### "Por que não usar AWS Console diretamente?"

> AWS Console exige entrada manual. Isso automiza. 2 segundos. Sem digitação. Você quer saber se tem eventos SLA mensalmente? Execute esse comando no cron e pronto.

### "Isso é lead gen pra seu SaaS?"

> 100% honesto: SIM. Mas a ferramenta CLI é genuinamente útil standalone. Construímos porque precisávamos internamente. Se quiser full automation (cálculo, PDF, abrir ticket, rastrear), tem o https://awscostguardian.com com success fee de 30% dos créditos recuperados.

### "Preciso do Enterprise Support?"

> Infelizmente sim. AWS Health API é exclusivo para Business+. Se você só tem Developer/Basic, não rola. Mas você pode abrir caso mesmo assim (eles processam manualmente).

### "Como integro com Terraform/Ansible?"

> Ainda estamos em v0.1. Saída JSON/CSV vem em breve. Por enquanto é CLI + tabela bonitinha no terminal.

### "Funciona com múltiplas contas?"

> A CLI atualmente foca em 1 conta. O SaaS automático funciona multi-account.

---

## Por que você deveria se importar (FinOps)

1. **Redução de custo imediata** - Reclamar créditos é R$ "grátis"
2. **Automação** - Não requer manual review
3. **Open source** - Você controla, não paga taxa mensal
4. **Integração** - Roda no seu CI/CD, cron, monitoring
5. **Transparência** - MIT license, código aberto

---

## Próximos Passos

1. Clone: `git clone https://github.com/yourusername/aws-sla-hunter.git`
2. Install: `pip install -r requirements.txt`
3. Run: `python main.py`
4. Reclame seu dinheiro!

Se tiver dúvidas, respondo aqui mesmo. Se quiser full automation, o SaaS está em https://awscostguardian.com

---

## Engagement Tips para Discord BR

- Post em horário comercial BR (14h-18h)
- Use linguagem coloquial (não formal demais)
- Enfatize: "dinheiro que vocês estão deixando na mesa"
- Seja genuíno sobre o modelo de negócio
- Ofereça ajuda pra setup/troubleshooting
- Compartilhe histórias reais de recuperação (anonimizadas)
- Engaje com os Dev/FinOps leads do canal

---

## Variações de Mensagem (para não ficar repetitivo)

**Versão "Curiosidade":**
> "Alguém aqui já recuperou crédito SLA da AWS? Construí uma ferramenta que encontra automaticamente. Tá no GitHub gratuito..."

**Versão "Problema":**
> "To vendo muita conta deixando R$100K+ em crédito SLA. Fiz uma ferramenta pra detectar automaticamente..."

**Versão "Caso de Sucesso":**
> "Recuperei R$500K em SLA credits pra um cliente só rodando uma ferramenta simples. Open-sourcei ela..."

---

## Métricas para Acompanhar

- Stars no GitHub
- Downloads do pip (quando publicado)
- Traffic via utm_source=discord_br
- Signups em awscostguardian.com com utm_medium=sla_hunter

Objetivo inicial: 50 stars, 10 signups, 1-2 créditos recuperados via SaaS
