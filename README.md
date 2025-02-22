# robo_web
# Automacao com Selenium para Múltiplos Monitores

## 📌 Visão Geral
Este script utiliza o Selenium para automatizar o login e a interação com um site específico, distribuindo múltiplas instâncias do navegador em diferentes monitores. Cada instância realiza uma série de cliques em elementos da página e, em seguida, posiciona a janela do navegador em um monitor específico.

---

## 🚀 Funcionalidades Principais
1. **Abrir múltiplas instâncias do navegador**: O código identifica quantos monitores estão disponíveis e abre até quatro instâncias do Chrome simultaneamente.
2. **Login automático**: O script insere credenciais de login e acessa a plataforma.
3. **Navegação automática**: Após o login, ele clica em botões específicos da interface para configurar a sessão.
4. **Distribuição entre monitores**: Cada instância do navegador é movida para um monitor específico e maximizada para melhor visualização.
5. **Execução em threads**: A automação é realizada de forma paralela usando threads para otimizar o desempenho.

---

## 🛠 Tecnologias Utilizadas
- **Python** 🐍
- **Selenium** (Automação Web)
- **PyAutoGUI** (Interação com a GUI)
- **PyGetWindow** (Manipulação de janelas)
- **ScreenInfo** (Detecção de múltiplos monitores)
- **WebDriver Manager** (Gerenciamento do driver do Chrome)
- **Threading** (Execução paralela de instâncias do navegador)

---

## 📂 Estrutura do Código
### 1️⃣ **Configuração Inicial**
- Define opções do Chrome para desativar notificações e pop-ups.
- Define listas de XPaths para elementos que serão clicados, organizados por monitor.
- Associa cada instância do navegador a um monitor específico.

### 2️⃣ **Detecção de Monitores**
- A função `obter_posicoes_monitores()` retorna a posição de cada monitor disponível.

### 3️⃣ **Função `mover_janela()`**
- Move e maximiza a janela do navegador no monitor correto.

### 4️⃣ **Função `abrir_pagina_e_realizar_acoes()`**
- Abre o navegador e faz login.
- Clica nos elementos especificados.
- Move o navegador para o monitor correspondente.

### 5️⃣ **Execução Paralela**
- O código abre até 4 instâncias do navegador em threads separadas, garantindo que a automação ocorra simultaneamente em múltiplos monitores.

---

## 🔧 Como Usar
1. Instale as dependências necessárias:
    ```sh
    pip install selenium webdriver-manager pyautogui pygetwindow screeninfo
    ```
2. Execute o script Python normalmente.
3. O código abrirá instâncias do Chrome, fará login e configurará a interface automaticamente.

---

## 📝 Observações
- Certifique-se de atualizar os XPaths conforme necessário para o site utilizado.
- O código foi projetado para funcionar em um ambiente com **até 4 monitores**.
- Pode ser necessário ajustar tempos de espera dependendo da velocidade da conexão e do carregamento do site.

---

## 📌 Contribuições
Caso queira melhorar o código ou adicionar novas funcionalidades, fique à vontade para abrir um Pull Request! 🚀

---

## 📜 Licença
Este projeto está sob a licença MIT. Sinta-se livre para modificar e usar conforme necessário.

---

Desenvolvido em Python 🐍.

