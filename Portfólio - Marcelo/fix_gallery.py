from pathlib import Path
import re

path = Path(r"c:\Users\Marcelo\Desktop\Portfólio\Portfólio - Marcelo\automacao.html")
text = path.read_text(encoding="utf-8")

patterns = [
    (
        r'(?s)<div class="gallery-item has-photo tall reveal">.*?</div>',
        '<div class="gallery-item has-photo tall reveal"><img src="imagens/ImgVisaoGeral.png" alt="Visão geral do braço robótico"></div>'
    ),
    (
        r'(?s)<div class="gallery-item reveal reveal-d1">.*?<span class="label">Eletrônica &amp; solda</span>.*?</div>',
        '<div class="gallery-item has-photo reveal reveal-d1"><img src="imagens/ImgCircuito.png" alt="Circuito eletrônico do projeto"></div>'
    ),
    (
        r'(?s)<div class="gallery-item reveal reveal-d1">.*?<span class="label">Protoboard</span>.*?</div>',
        '<div class="gallery-item has-photo reveal reveal-d1"><img src="imagens/ImgProtoboard.png" alt="Montagem no protoboard"></div>'
    ),
    (
        r'(?s)<div class="gallery-item reveal reveal-d2">.*?<span class="label">Diagrama de fiação</span>.*?</div>',
        '<div class="gallery-item has-photo reveal reveal-d2"><img src="imagens/ImgDiagrama.png" alt="Diagrama de fiação do sistema"></div>'
    ),
    (
        r'(?s)<div class="gallery-item reveal reveal-d2">.*?<span class="label">Montagem das engrenagens</span>.*?</div>',
        '<div class="gallery-item has-photo reveal reveal-d2"><img src="imagens/ImgMotores.png" alt="Motores e montagem das engrenagens"></div>'
    ),
]

for pattern, replacement in patterns:
    text, count = re.subn(pattern, replacement, text, count=1)
    print(f"replaced {count} block")

path.write_text(text, encoding="utf-8")
print("done")
