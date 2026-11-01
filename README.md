# Site Lemien Tecnologia

Site institucional da Lemien Tecnologia com duas frentes:

- **Recuperação de dados** de celulares com dano físico (atendimento e pagamento pelo WhatsApp).
- **Draco Forensic Tool**: assinatura mensal de R$ 99,00 do sistema de gestão de investigações.

## Estrutura

| Arquivo | O que é |
| --- | --- |
| `index.html` | Página inicial |
| `politica-de-privacidade.html` | Política de Privacidade (gerada a partir de `conteudo/`) |
| `termos-de-servico.html` | Termos de Serviço (gerados a partir de `conteudo/`) |
| `conteudo/*.md` | Texto dos documentos legais, para editar |
| `assets/` | Logos e estilo das páginas de documentos |
| `gerar_documentos.py` | Regera os HTML dos documentos a partir dos `.md` |

É um site estático: basta enviar os arquivos para a hospedagem (por exemplo, a pasta `public_html` na GoDaddy).

## Editar os documentos legais

1. Altere o texto em `conteudo/politica-de-privacidade.md` ou `conteudo/termos-de-servico.md`.
2. Rode `pip install markdown` (uma vez) e depois `python3 gerar_documentos.py`.

## Pendências

- Preencher os campos entre colchetes: CNPJ, endereço, e-mail, valor da avaliação, forma de entrega do pendrive, prazos e forma de pagamento.
- Revisão jurídica da política e dos termos antes de publicar.
