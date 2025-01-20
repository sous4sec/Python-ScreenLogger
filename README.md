# 👁️ **ScreenLogger** - PYTHON
Um **ScreenLogger simples** feito em **Python** que envia **Capturas de Tela** para o seu e-mail.

## 📚 Sobre

Este projeto foi criado para um trabalho escolar e é baseado em outros projetos open-source encontrados no GitHub. Foi desenvolvido inteiramente para fins educacionais.

## 🔧 Funcionalidades

- **Envio de Capturas de Tela por E-mail**: Captura e envia capturas de tela do seu PC, junto com informações como **Hostname, Sistema, Usuário e IP**.
- **Configurações Personalizáveis**: Agora, as variáveis ajustáveis são carregadas de um arquivo `.env`, facilitando a personalização.
- **Integração com o Início Automático**: Ao ser convertido em um **executável**, o programa será automaticamente copiado para a **pasta de Inicialização** do Windows.

## 🛠️ **Principais Funções**
![Principais Funções](https://github.com/user-attachments/assets/54deb6db-15dd-4f27-bb21-49e410000769)

- ✅ **Captura de Capturas de Tela**
- ✅ **Recuperação de Hostname**
- ✅ **Informações do Usuário**
- ✅ **Endereço IP**
- ✅ **Integração com a Inicialização Automática**

## ⚙️ **Configurações Padrão**

As configurações agora são carregadas a partir de um arquivo `.env`. Exemplos de variáveis que podem ser ajustadas:

- `EMAIL_SENDER`: Endereço de e-mail do remetente.
- `EMAIL_RECEIVER`: Endereço de e-mail do destinatário.
- `EMAIL_PASSWORD`: Senha do aplicativo para o e-mail.
- `IMAGES_DIR`: Diretório onde as capturas de tela serão salvas.
- `SMTP_SERVER`: Servidor SMTP para envio de e-mails.
- `SMTP_PORT`: Porta do servidor SMTP.

Exemplo de conteúdo do arquivo `.env`:
```env
EMAIL_SENDER=emailsender@example.com
EMAIL_RECEIVER=emailreceiver@example.com
EMAIL_PASSWORD=yourapppassword
IMAGES_DIR=C:\IMAGES
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
```

## 🛡️ **Testes de Antivírus**

![Teste Antivirus 1](https://github.com/user-attachments/assets/9bddf949-9f72-4810-b819-be4c866aee9e)  
![Teste Antivirus 2](https://github.com/user-attachments/assets/e5bb72a7-e698-4806-9774-933af345e2e6)

## 💾 **Como Criar o Executável (EXE)**

Caso queira rodar o **ScreenLogger** como um arquivo executável, utilize a biblioteca [AutoPyToExe](https://pypi.org/project/auto-py-to-exe/).

Após obter o arquivo **.exe**, certifique-se de que o nome do arquivo está correto no seu script, e que o arquivo será copiado para a **pasta de Inicialização** do Windows, garantindo a execução na inicialização.

## 👨‍💻 **Créditos**

Este projeto é baseado em contribuições de outros projetos open-source. Se você for o criador original de algum código utilizado, entre em contato para o devido reconhecimento.

