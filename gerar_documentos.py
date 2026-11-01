import markdown, sys
TPL='''<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} | Lemien Tecnologia</title>
<link rel="icon" href="assets/logo-marca.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Anton&family=Barlow:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/documentos.css">
</head>
<body>
<header><div class="wrap topo">
<a class="marca" href="index.html"><img src="assets/logo-marca.png" alt=""><span>LEMIEN TECNOLOGIA</span></a>
<a class="voltar" href="index.html">Voltar ao site</a>
</div></header>
<main class="wrap doc">
{body}
</main>
<footer><div class="wrap">Lemien Tecnologia · <a href="politica-de-privacidade.html">Política de privacidade</a> · <a href="termos-de-servico.html">Termos de serviço</a> · <a href="https://wa.me/5511967471150">WhatsApp (11) 96747-1150</a></div></footer>
</body>
</html>
'''
for src,out,title in [('conteudo/politica-de-privacidade.md','politica-de-privacidade.html','Política de Privacidade'),('conteudo/termos-de-servico.md','termos-de-servico.html','Termos de Serviço')]:
    body=markdown.markdown(open(src).read(),extensions=['tables'])
    open(out,'w').write(TPL.format(title=title,body=body))
