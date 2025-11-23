# Azure Frontier Girls

## 🤖🩷 Agente de Apoio ao Autoexame de Câncer de Mama – Azure AI Foundry
⚠️ **Importante:** Este agente **não substitui profissionais de saúde**. Ele serve apenas como ferramenta de apoio educativo.

Este projeto apresenta um agente inteligente criado no Azure AI Foundry para auxiliar mulheres a realizar o autoexame de mama, oferecendo:

* Explicações baseadas em PDFs especializados

* Um teste automático de sintomas

* Orientações personalizadas para saber quando procurar um médico

## 📌 1. Objetivo do Projeto

O agente foi desenvolvido para:

1. Reunir conhecimento sobre prevenção e autoexame de câncer de mama.

2. Receber sintomas marcados pela usuária.

3. Calcular um índice de alerta baseado na quantidade de sintomas identificados.

4. Informar, com base na pontuação, se:

    1. A situação é tranquila, ou

    2. É recomendado procurar um médico.

Ser facilmente integrável a outras ferramentas, como Power Automate.

## 🧠 2. Arquitetura do Agente
### 2.1. Componentes principais
| Componente  | Função |
| ------------- |:-------------:|
| Componente	Função      | Modelo	gpt-4o-mini (2024-07-18)     |
| Conhecimento (Vector Store)      | PDFs enviados sobre autoexame     |
| Instruções do sistema      | Definem a personalidade e comportamento do agente     |
| Ação personalizada      | Script que calcula o risco com base nos sintomas     |

## 📄 3. Instruções usadas

Você é um agente de apoio à saúde da mulher, especializado em orientar sobre o autoexame de câncer de mama.

Tarefas que deve realizar:

1. Perguntar à usuária se ela deseja realizar uma triagem de sinais.
2. Fazer perguntas simples como:
   - Sentiu algum nódulo?
   - Observou alterações na pele?
   - Houve secreção no mamilo?
   - Alguma dor localizada?
3. Registrar as respostas.
4. Contar quantos sintomas foram relatados.
5. Fornecer uma recomendação:
   - Se 0 sintomas → tranquilizar e sugerir rotina normal.
   - Se 1–2 sintomas → orientar a observar por alguns dias e procurar médico se persistir.
   - Se ≥ 3 sintomas → recomendar consulta médica. Saliente que a opinião médica é imprescindível, e que isso é apenas um alerta.
   
NUNCA faça diagnósticos.  
Sempre encoraje avaliação profissional se houver dúvida.

Você pode usar as informações dos PDFs enviados pelo usuário como base.

## Passo a passo resumido:

1. Acesse: https://ai.azure.com  
2. Clique em **"Create project"**  
3. Dê um nome para o projeto  
4. Na barra lateral clique em **"Agentes"**  
5. Clique em **"Criar agente"**
6. Preencha:
   - Nome do agente
   - Instruções do sistema (system instructions)
   - Modelos e configurações
7. Na aba **"Knowledge Sources"**, adicione os PDFs (upload)
8. Na aba **"Actions"**, crie a ação de Teste de Sintomas (código logo abaixo)
9. Clique em **"Playground"** para testar
10. Publique o agente para gerar o **link público** (explicado mais abaixo)




	
	
	
