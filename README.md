---

# 🚀 App Motoboy V2

Aplicação em **Python + SQLite** para ajudar motoboys a controlarem **ganhos reais**, **custos por km**, **manutenção da moto** e **lucro líquido diário/mensal**.

Projeto desenvolvido com foco em **aprendizado prático**, organização de código e uso real no dia a dia.

---

## 🎯 Objetivo do Projeto

Criar um app simples e funcional que permita ao motoboy:

* Registrar ganhos diários
* Registrar quilometragem rodada
* Controlar abastecimentos
* Controlar manutenções da moto
* Calcular custo por km
* Calcular lucro líquido do dia
* Visualizar histórico de trabalho

Esse projeto também serve como **portfólio back-end**.

---

## 🧱 Tecnologias Utilizadas

* Python 3
* SQLite
* SQL
* Programação Orientada a Objetos (POO)
* Arquitetura em camadas (models, services, utils)

---

## ⚙️ Funcionalidades Atuais

* Cadastro de motoboy
* Cadastro de moto vinculada ao motoboy
* Registro de abastecimento
* Registro de manutenção
* Registro de dia de trabalho
* Cálculo de:

  * Quilometragem diária
  * Ganho bruto
  * Custos do dia
  * Lucro líquido

---

## 🧮 Lógica de Cálculo (Resumo)

* **KM do dia** = quilometragem final - quilometragem inicial
* **Custo de manutenção** = custo por km × km rodado
* **Lucro líquido** = ganho bruto - (combustível + manutenção)

---

## ▶️ Como Executar

1. Clone o repositório
2. Crie o banco SQLite usando o `schema.sql`
3. Execute o arquivo principal:

```
python app/fluxo_app.py
```

---

## 🛣️ Próximos Passos

* Interface melhor no terminal
* Relatórios mensais
* Exportação de dados
* Migração futura para PostgreSQL
* API com FastAPI
* Interface web ou mobile

---

## 🧠 Aprendizados

Este projeto foi criado para consolidar conhecimentos em:

* SQL na prática
* Organização de projeto
* Separação de responsabilidades
* Pensamento de produto real
* Backend aplicado a problemas do mundo real

---

## 👊 Autor

Projeto desenvolvido por isaias morais, estudante de programação e motoboy, com foco em backend Python e aplicações reais.
