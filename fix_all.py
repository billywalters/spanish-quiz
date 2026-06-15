"""Apply Spanish accent and spelling corrections to data/questions.json."""
import json, re, sys

sys.stdout.reconfigure(encoding='utf-8')

with open('data/questions.json', encoding='utf-8') as f:
    raw = f.read()

fixes = [
    # Accent fixes — order matters (longer patterns first to avoid partial matches)
    (r'\btacano\b', 'tacaño'),
    (r'\bninos\b', 'niños'),
    (r'\bninas\b', 'niñas'),
    (r'\bnino\b', 'niño'),
    (r'\bnina\b', 'niña'),
    (r'\bbano\b', 'baño'),
    (r'\blamparas\b', 'lámparas'),
    (r'\blampara\b', 'lámpara'),
    (r'\btelefono\b', 'teléfono'),
    (r'\btelevisión\b', 'televisión'),  # already correct, skip
    (r'\btelevision\b', 'televisión'),
    (r'\bcancion\b', 'canción'),
    (r'\bconversacion\b', 'conversación'),
    (r'\binvitacion\b', 'invitación'),
    (r'\bleccion\b', 'lección'),
    (r'\bilusion\b', 'ilusión'),
    (r'\bjardin\b', 'jardín'),
    (r'\blibreria\b', 'librería'),
    (r'\bpagina\b', 'página'),
    (r'\bsillon\b', 'sillón'),
    (r'\bfantasticos\b', 'fantásticos'),
    (r'\bfantasticas\b', 'fantásticas'),
    (r'\bfantastico\b', 'fantástico'),
    (r'\bsimpatico\b', 'simpático'),
    (r'\btipico\b', 'típico'),
    (r'\bdebil\b', 'débil'),
    (r'\bfragil\b', 'frágil'),
    (r'\bmarron\b', 'marrón'),
    (r'\bfelix\b', 'feliz'),
    (r'\bcafe\b', 'café'),
    # Spelling fixes
    (r'\bel gate\b', 'el gato'),
    (r'\bgate\b(?! keeper)', 'gato'),
    (r'\bmuchaco\b', 'muchacho'),
    (r'\bmechacho\b', 'muchacho'),
    (r'\bexcelenty\b', 'excelente'),
    (r'\btomoto\b', 'tomate'),
    (r'\blos bolsas\b', 'las bolsas'),
    (r'\bluzes\b', 'luces'),
    (r'\bunas casa\b', 'unas casas'),
    # el dia (special case - not caught by naive rule)
    (r'\bel dia\b', 'el día'),
]

result = raw
count = 0
for pattern, replacement in fixes:
    new_result = re.sub(pattern, replacement, result, flags=re.IGNORECASE)
    n = len(re.findall(pattern, result, flags=re.IGNORECASE))
    if n:
        count += n
    result = new_result

data = json.loads(result)
with open('data/questions.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Applied fixes: {count} replacements")
qs = data['chapters'][0]['questions']
print(f"Total questions: {len(qs)}")
