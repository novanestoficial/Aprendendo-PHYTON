# Roteiro de estudos — Python para automação de faturamento (1-2 semanas)

Início: 2026-08-01. Foco: sair sabendo o suficiente de Python para construir e defender em entrevista um script real de automação de faturamento. Nada de Python genérico sem aplicação nesse objetivo.

Cada dia tem: **conceitos**, **analogia com Java**, **armadilhas comuns pra quem vem de Java**, e **exercício prático** (todos giram em torno de pedido → cálculo → fatura).

---

## Bibliotecas que vamos usar (e por quê)

| Biblioteca | Pra que serve aqui | Equivalente mental em Java |
|---|---|---|
| `decimal` | Cálculo monetário sem erro de ponto flutuante | `BigDecimal` |
| `csv` (stdlib) | Ler/escrever pedidos em CSV | `opencsv` / `BufferedReader` manual |
| `openpyxl` | Ler/escrever planilhas `.xlsx` | Apache POI |
| `pandas` | Manipular tabelas de pedidos em lote (opcional, mas comum no mercado) | não tem equivalente direto — pense numa `List<Map<>>` com superpoderes |
| `smtplib` + `email` (stdlib) | Enviar e-mail com a fatura | `JavaMail` |
| `python-dotenv` | Guardar senha/API key fora do código | `application.properties` / variáveis de ambiente do Spring |
| `venv` + `pip` | Isolar dependências do projeto | Maven/Gradle (mas sem versionamento central tipo Maven Central por padrão) |

Instale isso quando chegar no dia certo — não precisa instalar tudo agora.

---

## Dia 1 — Sintaxe básica e fundamentos

**Conceitos:** variáveis, tipos (`int`, `float`, `str`, `bool`), operadores, `if/elif/else`, `for`, `while`, f-strings, funções (`def`).

**Analogia Java:** Python não declara tipo (`String nome = "David"` → `nome = "David"`); tipagem é dinâmica mas forte (não faz `"3" + 3` igual JS). Bloco de código é definido por indentação, não `{}`. Não existe `;` no fim da linha (funciona, mas é considerado erro de estilo). `System.out.println` → `print()`. Interpolação de string: `String.format` / concat → f-string `f"{var}"`.

**Armadilhas comuns:**
- Misturar espaços e tabs na indentação quebra o código (`IndentationError`).
- Esquecer os `:` no fim de `if`, `for`, `def`.
- `range(5)` vai de 0 a 4, igual `for(int i=0;i<5;i++)` — não inclui o 5.
- Não existe `switch` clássico (só a partir do `match` no Python 3.10+, sintaxe diferente).

**Exercício:** função `calcular_total(preco_unitario, quantidade)` que retorna o total, com `print` formatado em `f"R$ {total:.2f}"`.

---

## Dia 2 — Estruturas de dados

**Conceitos:** listas, tuplas, dicionários, sets, compreensão de lista (`list comprehension`), slicing.

**Analogia Java:** lista → `ArrayList` (mas dinâmica em tipo); tupla → praticamente um `record` imutável sem nome de campos; dict → `HashMap` (mas preserva ordem de inserção desde Python 3.7); set → `HashSet`.

**Armadilhas comuns:**
- Listas são mutáveis e passadas por referência — mudar dentro de uma função afeta fora, igual em Java com objetos, mas gente que vem de Java às vezes espera cópia por padrão como em `int`/`String`.
- **Nunca** use lista mutável como valor padrão de parâmetro (`def f(itens=[])`) — é um bug clássico, a lista é compartilhada entre chamadas.
- Dict não tem `getOrDefault` com esse nome — é `dict.get(chave, valor_padrao)`.

**Exercício:** modelar um "pedido" como dict: `{"cliente": "Ana", "itens": [{"produto": "Caneta", "preco": 2.5, "qtd": 10}]}`. Escrever função que soma o total do pedido.

---

## Dia 3 — POO em Python

**Conceitos:** `class`, `__init__`, `self`, métodos, herança, `@property`, `__str__`/`__repr__`.

**Analogia Java:** `self` = `this`, mas explícito como primeiro parâmetro de todo método. `__init__` = construtor. Não existe `private` de verdade — convenção é prefixo `_` (protegido) ou `__` (name mangling, "quase privado"). Getters/setters raramente são escritos à mão — usa-se `@property` só quando precisa de lógica. Herança: `class Filha(Mae):` (sem `implements`/`extends` separados — interfaces em Python são "duck typing" ou `abc.ABC`).

**Armadilhas comuns:**
- Esquecer `self` como primeiro parâmetro de método de instância.
- Esperar encapsulamento real como Java — em Python é combinado, não imposto pelo compilador.
- Confundir atributo de classe (compartilhado) com atributo de instância (definido no `__init__`).

**Exercício:** classe `Pedido` com `cliente`, `itens` (lista de `Item`), método `calcular_total()` e `__str__` que imprime um resumo tipo nota.

---

## Dia 4 — Ambiente, módulos e tratamento de erros

**Conceitos:** `venv`, `pip install`, `import`, `try/except/finally`, exceções customizadas.

**Analogia Java:** `venv` + `pip` ≈ um Maven/Gradle bem mais simples, sem repositório central de builds — `pip install X` baixa do PyPI. `try/except` = `try/catch`, mas você captura por tipo (`except ValueError:`) igual Java. Não existe checked exception — nada obriga a declarar o que uma função pode lançar.

**Armadilhas comuns:**
- Usar `except:` genérico (equivalente a `catch (Exception e)` capturando tudo, inclusive erros que deveriam quebrar o programa) — evite, capture o tipo específico.
- Esquecer de ativar o `venv` antes de rodar/instalar (o pip global vira bagunça).

**Exercício:** criar `venv`, instalar `python-dotenv`, envolver o cálculo do pedido em `try/except` tratando item com preço negativo ou quantidade inválida, lançando uma exceção customizada `PedidoInvalidoError`.

---

## Dia 5 — Cálculo monetário preciso (núcleo da vaga)

**Conceitos:** por que `float` é perigoso pra dinheiro (`0.1 + 0.2 != 0.3`), módulo `decimal`, arredondamento (`ROUND_HALF_UP`), formatação de moeda.

**Analogia Java:** `decimal.Decimal` ≈ `BigDecimal`. Assim como em Java você nunca usa `double` pra dinheiro, em Python nunca use `float` — sempre `Decimal`, e sempre crie `Decimal` a partir de string (`Decimal("10.50")`), nunca de float (`Decimal(10.50)` já nasce com erro de precisão herdado do float).

**Armadilhas comuns:**
- `Decimal(0.1)` ≠ `Decimal("0.1")` — a primeira herda o erro de ponto flutuante.
- Misturar `Decimal` com `float` numa operação (`TypeError`).

**Exercício:** reescrever o cálculo do `Pedido` usando `Decimal`, aplicar imposto (ex.: 8%) e desconto (ex.: 5% acima de certo valor), arredondando corretamente pra 2 casas decimais.

---

## Dia 6 — Arquivos e CSV

**Conceitos:** `open()`, context manager (`with`), módulo `csv` (`DictReader`/`DictWriter`).

**Analogia Java:** `with open(...) as f:` ≈ try-with-resources. `csv.DictReader` ≈ ler CSV linha a linha pra um `Map<String,String>`.

**Armadilhas comuns:**
- Esquecer `with` e não fechar o arquivo manualmente (funciona, mas é o hábito errado).
- Todo valor lido de CSV vem como `str` — esquecer de converter pra `Decimal`/`int` é erro clássico.

**Exercício:** criar um `pedidos.csv` com colunas `cliente,produto,preco_unitario,quantidade`, ler com `DictReader` e gerar uma lista de objetos `Pedido`.

---

## Dia 7 — Planilhas (openpyxl / pandas)

**Conceitos:** ler/escrever `.xlsx` com `openpyxl`; visão geral de `pandas` (`DataFrame`, `read_excel`, `groupby`) pra quem quiser ir além.

**Analogia Java:** Apache POI, mas com API muito mais enxuta.

**Armadilhas comuns:**
- Índices de linha/coluna do `openpyxl` começam em 1, não em 0 (diferente de quase tudo em Python).
- `pandas` pode inferir tipo errado pra colunas de dinheiro (lê como float) — sempre validar/converter pra `Decimal` depois de importar.

**Exercício:** ler pedidos de uma planilha `.xlsx` com `openpyxl`, gerar uma nova aba/arquivo com o total calculado por pedido.

---

## Dia 8 — Envio automático (e-mail / mensagem)

**Conceitos:** `smtplib` + `email.message.EmailMessage` pra enviar e-mail; alternativa: simular envio via "webhook" (print formatado ou salvar em log) se não quiser configurar SMTP real.

**Analogia Java:** `JavaMail` — bem mais verboso em Java, Python é mais direto.

**Armadilhas comuns:**
- Colocar senha de e-mail direto no código — usar `.env` + `python-dotenv` (⚠️ nunca commitar `.env` no Git — adicionar ao `.gitignore`).
- Provedores modernos (Gmail) exigem "senha de app", não a senha normal da conta.

**Exercício:** função `enviar_fatura(pedido, total)` que monta um corpo de e-mail com o valor formatado e envia (ou loga, se preferir não configurar SMTP de verdade).

---

## Dia 9-10 — Projeto final integrado

Juntar tudo num projeto único, estruturado como pastas de verdade (não um único arquivo), pronto pra subir no GitHub:

```
automacao-faturamento/
├── README.md
├── requirements.txt
├── .env.example
├── .gitignore
├── src/
│   ├── modelos.py       # classes Pedido, Item
│   ├── calculo.py       # regras de imposto/desconto com Decimal
│   ├── importador.py    # ler pedidos de CSV/xlsx
│   ├── notificador.py   # enviar fatura por e-mail
│   └── main.py          # orquestra o fluxo
└── dados/
    └── pedidos_exemplo.csv
```

Fluxo: `main.py` lê pedidos de `dados/pedidos_exemplo.csv` → calcula total (imposto + desconto) com `Decimal` → gera texto de fatura formatado → "envia" (e-mail real ou log) → salva relatório de faturas geradas.

**Armadilha comum:** projeto Java tende a vir com muita camada (service/repository/controller) por hábito do Spring — em Python, pra um script de automação desse porte, isso é over-engineering. Módulos simples e funções bem separadas bastam; não recrie Spring em Python.

---

## Dia 11-12 — Polimento e preparação pra entrevista

- Escrever `README.md` explicando o problema de negócio (faturamento manual → automático), como rodar, e prints/exemplos de saída.
- Adicionar testes básicos com `unittest` ou `pytest` (comparável a JUnit) pro cálculo de total — é isso que mostra maturidade de dev, não só "sei Python".
- Subir pro GitHub (github.com/novanestoficial).
- Revisar mentalmente: por que `Decimal` e não `float`? Por que separar `calculo.py` de `notificador.py`? O que faria diferente com mais tempo (ex.: banco de dados em vez de CSV, fila de mensagens em vez de e-mail direto)?

---

## Como retomar isso numa conversa nova

Este roteiro e o `CONTEXTO.md` (nesta mesma pasta) resumem o objetivo. Numa conversa nova, basta pedir pro Claude ler o `CONTEXTO.md` e dizer em qual dia você está.
