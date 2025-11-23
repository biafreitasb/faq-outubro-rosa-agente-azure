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

O agente foi direcionado para nunca realizar diagnósticos e sempre recomendar que o usuário vá ao médico para uma consulta presencial. Para auxiliar na prevenção, o agente pode verificar a quantidade de sintomas e também tirar dúvidas relacionadas ao assunto. Além disso, o agente foi guiado para não tratar sobre outros assuntos além da proposta. 

## 🔗 4. Links

 **Endpoint:** [aqui](https://beatriz-b-0371-resource.services.ai.azure.com/api/projects/beatriz-b-0371)

 **AI Foundry**: [aqui](https://ai.azure.com/?utm_source=chatgpt.com)

 **Documentação**: [aqui](https://ai.azure.com/doc/azure/ai-foundry/quickstarts/get-started-code?tid=168d4137-d6f6-45f8-aaa7-d1a70233095e)

## 🌟 5. Passo a passo resumido:

1. Acesse: https://ai.azure.com  
2. Clique em **"Create project"**  
3. Dê um nome para o projeto e confira as configurações
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




	
	
	
