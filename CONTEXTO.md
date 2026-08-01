# Contexto deste repositório

**Leia este arquivo no início de qualquer conversa nova neste diretório.**

## Quem é o David
- 18 anos, cursando ADS na Estácio.
- Mais de 1 ano de experiência com Java + Spring Boot (lógica, POO, APIs REST, Git/GitHub, PostgreSQL).
- Dois projetos reais no GitHub (github.com/novanestoficial):
  - Sistema de gestão de oficina mecânica (Java/Spring Boot)
  - AprovaIA — SaaS de preparação para o ENEM com IA
- Já sabe programar bem em Java. Não precisa de aula de lógica/POO do zero — precisa de tradução Java → Python por analogia.

## Objetivo deste repositório
Aprender Python aplicado a **automação de faturamento/pagamento** em ~1-2 semanas (início: 2026-08-01), para se candidatar a uma vaga de automação numa empresa onde um amigo trabalha. A vaga ainda vai abrir; o requisito confirmado é saber Python.

**O que a automação da empresa faz** (confirmado com o amigo): hoje, quando um cliente faz um pedido, alguém calcula e fatura manualmente. A automação deve calcular o valor total automaticamente (com impostos/descontos quando fizer sentido) e enviar esse valor ao cliente — eliminando o passo manual. É automação de **processo de negócio/financeiro**, não scraping nem RPA de navegador.

## Escopo de aprendizado (prioridade)
1. Sintaxe básica de Python (por analogia com Java)
2. Manipulação de dados/números — cálculo monetário preciso (`decimal`, não `float`)
3. Leitura/escrita de planilhas/CSV (`openpyxl`, `pandas`, `csv`)
4. Envio automático de mensagem/e-mail com o valor calculado (`smtplib`, ou simulação de API de mensagem)

## Entregável final
Projeto prático real para subir no GitHub como prova de capacidade antes da entrevista:
script que lê um pedido → calcula o valor total automaticamente (com impostos/descontos) → "envia" o valor formatado ao cliente.

## Como o Claude deve ensinar
- Sempre relacionar conceitos novos com o equivalente em Java (ex.: `self` vs `this`, `pip`/`venv` vs Maven/Gradle, duck typing vs interfaces).
- Apontar, a cada etapa, erros comuns de quem vem de Java para Python (indentação em vez de chaves, tipagem dinâmica, mutabilidade de listas/dicts, `==` vs `is`, etc).
- Priorizar sempre o que é relevante para automação de faturamento — evitar Python genérico sem aplicação nesse contexto.

## Roteiro de estudos
Ver `ROTEIRO.md` neste mesmo diretório para o cronograma dia a dia.

## Curso complementar
David está fazendo o curso **"Python 3 - Curso Completo do Básico ao Avançado"** (Udemy, instrutor Leonardo Leitão) como base teórica. O curso é genérico (do básico ao avançado) — não é focado em automação/faturamento. Papel do Claude: apoiar tirando dúvidas do curso, traduzir os conceitos por analogia com Java, e sempre que possível conectar o que ele está vendo no curso com o `ROTEIRO.md` e o objetivo final (projeto de automação de faturamento). Perguntar em qual módulo/aula do curso ele está para dar suporte pontual.
