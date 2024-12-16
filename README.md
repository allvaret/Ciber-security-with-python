# Criptografia Híbrida com RSA e AES

Este projeto Python demonstra a criptografia híbrida usando RSA para troca de chaves e AES para criptografia de dados. Ele fornece uma implementação básica de criptografia e descriptografia de mensagens.

## Visão Geral

O código inclui as seguintes funcionalidades:

*   **Geração de Chaves RSA:** Gera um par de chaves RSA de 2048 bits (chave pública e privada).
*   **Criptografia:** Criptografa uma mensagem usando AES-256 no modo CBC, com um IV (vetor de inicialização) gerado aleatoriamente. A chave AES em si é criptografada usando a chave pública RSA do destinatário.
*   **Descriptografia:** Descriptografa a mensagem usando a chave privada RSA correspondente para obter a chave AES e usa esta chave para descriptografar o texto cifrado.

## Estrutura do Código

O código é organizado nas seguintes funções:

*   `generate_rsa_keys()`: Gera um par de chaves RSA.
*   `encrypt_message(message, rsa_public_key)`: Criptografa a mensagem fornecida usando uma abordagem híbrida com RSA e AES.
*   `decrypt_message(encrypted_data, rsa_private_key)`: Descriptografa a mensagem criptografada usando a chave privada.

## Análise de Segurança e Melhorias

A seguir estão algumas das preocupações de segurança identificadas e possíveis melhorias:

*   **Modo Criptográfico:**
    *   **Problema:** Usar o modo CBC pode ser vulnerável a certos tipos de ataques e não autentica os dados.
    *   **Melhoria:** Há métodos mais modernos como AES-GCM, que adiciona autenticação e é mais seguro por design.
*   **Tamanho da Chave:**
    *   **Problema:** Utilizamos um tamanho de chave RSA fixo.
    *   **Melhoria:** Permita tamanhos de chave ajustáveis.
*   **Segurança da Entrada do Usuário:**
    *   **Problema:** O uso de `input()` sem ser polido pode ser inseguro, lembre-se que é um ambiente de testes.
    *   **Melhoria:** Adicione sanitização, use um mecanismo de entrada de console seguro ou leia as entradas de um arquivo.
*   **Falta de Autenticação:**
    *   **Problema:** O código atual não possui autenticação de mensagens, tornando-o vulnerável a ataques man-in-the-middle.
    *   **Melhoria:** Adicione um código de autenticação de mensagens (MAC) ou assinatura digital para garantir a integridade e autenticidade da mensagem.

## Como Usar

1.  **Clone o repositório**
2.  **Execute o arquivo `MainCH.py`**: `python "MainCH.py"`
3.  **Insira sua mensagem quando solicitado**
4.  **O código irá imprimir:**
    *   A chave AES gerada e o IV (para depuração)
    *   A mensagem criptografada
    *   A mensagem descriptografada

## Nota de Segurança Importante

Este código é destinado a fins educacionais e não deve ser usado em sistemas de produção sem abordar as preocupações de segurança e aplicar as melhorias recomendadas. A criptografia requer implementação cuidadosa para evitar vulnerabilidades e requer boas práticas.


