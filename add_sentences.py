import json, sys
sys.stdout.reconfigure(encoding='utf-8')

# Example sentences for every ch1 vocabulary word
# Each entry: "spanish_word_key": [{"es": "...", "en": "..."}, ...]
SENTENCES = {
    # ANIMALS
    "el gato":       [{"es": "El gato es pequeño y negro.", "en": "The cat is small and black."}],
    "el perro":      [{"es": "El perro es grande y fuerte.", "en": "The dog is big and strong."}],
    "el animal":     [{"es": "El animal es fantástico.", "en": "The animal is fantastic."}],

    # COLORS (used as adjectives in sentences)
    "amarillo":      [{"es": "El libro es amarillo.", "en": "The book is yellow."}],
    "anaranjado":    [{"es": "El tomate es anaranjado.", "en": "The tomato is orange."}],
    "azul":          [{"es": "El mapa es azul.", "en": "The map is blue."}],
    "blanco":        [{"es": "La blusa es blanca.", "en": "The blouse is white."}],
    "gris":          [{"es": "El perro es gris.", "en": "The dog is gray."}],
    "marrón, pardo": [{"es": "El gato es marrón.", "en": "The cat is brown."}],
    "morado":        [{"es": "La flor es morada.", "en": "The flower is purple."}],
    "moreno":        [{"es": "El muchacho es moreno.", "en": "The boy is brown-skinned."}],
    "negro":         [{"es": "El carro es negro.", "en": "The car is black."}],
    "rojo":          [{"es": "La silla es roja.", "en": "The chair is red."}],
    "rosado":        [{"es": "La lámpara es rosada.", "en": "The lamp is pink."}],
    "verde":         [{"es": "La planta es verde.", "en": "The plant is green."}],

    # FOOD & DRINK
    "la cerveza":    [{"es": "La cerveza es fría.", "en": "The beer is cold."}],
    "la comida":     [{"es": "La comida es fantástica.", "en": "The meal is fantastic."}],
    "el vino":       [{"es": "El vino es bueno.", "en": "The wine is good."}],
    "el café":       [{"es": "El café es caliente.", "en": "The coffee is hot."}],

    # GENERAL — clothing / objects
    "la blusa":         [{"es": "La blusa es blanca y bonita.", "en": "The blouse is white and pretty."}],
    "la bolsa":         [{"es": "La bolsa es grande.", "en": "The bag is big."}],
    "el libro":         [{"es": "El libro es interesante.", "en": "The book is interesting."}],
    "el tomate":        [{"es": "El tomate es rojo.", "en": "The tomato is red."}],
    "la canción":       [{"es": "La canción es alegre.", "en": "The song is happy."}],
    "la conversación":  [{"es": "La conversación es interesante.", "en": "The conversation is interesting."}],
    "la invitación":    [{"es": "La invitación es para el amigo.", "en": "The invitation is for the friend."}],
    "la lección":       [{"es": "La lección es difícil.", "en": "The lesson is difficult."}],
    "la ilusión":       [{"es": "La ilusión es típica.", "en": "The illusion is typical."}],
    "el drama":         [{"es": "El drama es interesante.", "en": "The drama is interesting."}],
    "la verdad":        [{"es": "La verdad es importante.", "en": "The truth is important."}],
    "el idioma":        [{"es": "El idioma es fantástico.", "en": "The language is fantastic."}],
    "el mapa":          [{"es": "El mapa es grande.", "en": "The map is big."}],
    "la actitud":       [{"es": "La actitud es positiva.", "en": "The attitude is positive."}],
    "el poema":         [{"es": "El poema es bonito.", "en": "The poem is pretty."}],
    "el problema":      [{"es": "El problema es pequeño.", "en": "The problem is small."}],
    "el programa":      [{"es": "El programa es interesante.", "en": "The program is interesting."}],
    "la foto":          [{"es": "La foto es bonita.", "en": "The photograph is pretty."}],
    "el sistema":       [{"es": "El sistema es típico.", "en": "The system is typical."}],
    "la mano":          [{"es": "La mano es pequeña.", "en": "The hand is small."}],
    "la suerte":        [{"es": "La suerte es buena.", "en": "The luck is good."}],

    # GENERAL — adjectives
    "agradable":    [{"es": "La persona es agradable.", "en": "The person is agreeable."}],
    "fantástico":   [{"es": "El libro es fantástico.", "en": "The book is fantastic."}],
    "horrible":     [{"es": "El problema es horrible.", "en": "The problem is horrible."}],
    "tacaño":       [{"es": "El hombre es tacaño.", "en": "The man is stingy."}],
    "alegre":       [{"es": "La muchacha es alegre.", "en": "The girl is happy."}],
    "feliz":        [{"es": "El niño es feliz.", "en": "The boy is happy."}],
    "inteligente":  [{"es": "La estudiante es inteligente.", "en": "The student is intelligent."}],
    "típico":       [{"es": "El problema es típico.", "en": "The problem is typical."}],
    "barato":       [{"es": "El libro es barato.", "en": "The book is inexpensive."}],
    "feo":          [{"es": "El mapa es feo.", "en": "The map is ugly."}],
    "interesante":  [{"es": "La lección es interesante.", "en": "The lesson is interesting."}],
    "triste":       [{"es": "La canción es triste.", "en": "The song is sad."}],
    "caro":         [{"es": "El hotel es caro.", "en": "The hotel is expensive."}],
    "flaco":        [{"es": "El gato es flaco.", "en": "The cat is thin."}],
    "joven":        [{"es": "La amiga es joven.", "en": "The friend is young."}],
    "viejo":        [{"es": "El hombre es viejo.", "en": "The man is old."}],
    "débil":        [{"es": "El animal es débil.", "en": "The animal is weak."}],
    "frágil":       [{"es": "La lámpara es frágil.", "en": "The lamp is fragile."}],
    "maravilloso":  [{"es": "El idioma es maravilloso.", "en": "The language is marvelous."}],
    "pequeño":      [{"es": "El niño es pequeño.", "en": "The boy is small."}],
    "fuerte":       [{"es": "El hombre es fuerte.", "en": "The man is strong."}],

    # HOME
    "la cama":       [{"es": "La cama es grande.", "en": "The bed is big."}],
    "la lámpara":    [{"es": "La lámpara es pequeña.", "en": "The lamp is small."}],
    "el teléfono":   [{"es": "El teléfono es nuevo.", "en": "The telephone is new."}],
    "la mesa":       [{"es": "La mesa es grande y bonita.", "en": "The table is big and pretty."}],
    "la silla":      [{"es": "La silla es roja.", "en": "The chair is red."}],
    "la ventana":    [{"es": "La ventana es grande.", "en": "The window is big."}],
    "la televisión": [{"es": "La televisión es nueva.", "en": "The television is new."}],
    "la radio":      [{"es": "La radio es pequeña.", "en": "The radio is small."}],
    "la luz":        [{"es": "La luz es blanca.", "en": "The light is white."}],

    # NATURE
    "la planta":  [{"es": "La planta es verde.", "en": "The plant is green."}],
    "el clima":   [{"es": "El clima es fantástico.", "en": "The climate is fantastic."}],
    "el día":     [{"es": "El día es bonito.", "en": "The day is pretty."}],
    "el planeta": [{"es": "El planeta es grande.", "en": "The planet is big."}],
    "la flor":    [{"es": "La flor es rosada y bonita.", "en": "The flower is pink and pretty."}],
    "la piel":    [{"es": "La piel es frágil.", "en": "The skin is fragile."}],

    # PEOPLE
    "el amigo":       [{"es": "El amigo es inteligente y agradable.", "en": "The friend is intelligent and agreeable."}],
    "la amiga":       [{"es": "La amiga es joven y alegre.", "en": "The friend is young and happy."}],
    "el artista":     [{"es": "El artista es fantástico.", "en": "The (male) artist is fantastic."}],
    "la artista":     [{"es": "La artista es inteligente.", "en": "The (female) artist is intelligent."}],
    "el dentista":    [{"es": "El dentista es agradable.", "en": "The (male) dentist is agreeable."}],
    "la dentista":    [{"es": "La dentista es inteligente.", "en": "The (female) dentist is intelligent."}],
    "el hermano":     [{"es": "El hermano es joven y fuerte.", "en": "The brother is young and strong."}],
    "el pianista":    [{"es": "El pianista es fantástico.", "en": "The (male) pianist is fantastic."}],
    "el muchacho":    [{"es": "El muchacho es inteligente.", "en": "The boy is intelligent."}],
    "la hermana":     [{"es": "La hermana es alegre.", "en": "The sister is happy."}],
    "la pianista":    [{"es": "La pianista es fantástica.", "en": "The (female) pianist is fantastic."}],
    "el niño":        [{"es": "El niño es pequeño y alegre.", "en": "The little boy is small and happy."}],
    "el taxista":     [{"es": "El taxista es agradable.", "en": "The (male) cabdriver is agreeable."}],
    "la taxista":     [{"es": "La taxista es inteligente.", "en": "The (female) cabdriver is intelligent."}],
    "la muchacha":    [{"es": "La muchacha es inteligente y alegre.", "en": "The girl is intelligent and happy."}],
    "la niña":        [{"es": "La niña es pequeña y feliz.", "en": "The little girl is small and happy."}],
    "la persona":     [{"es": "La persona es agradable.", "en": "The person is agreeable."}],
    "el cantante":    [{"es": "El cantante es fantástico.", "en": "The male singer is fantastic."}],
    "la cantante":    [{"es": "La cantante es maravillosa.", "en": "The female singer is marvelous."}],
    "el doctor":      [{"es": "El doctor es inteligente.", "en": "The doctor is intelligent."}],
    "el estudiante":  [{"es": "El estudiante es inteligente y joven.", "en": "The male student is intelligent and young."}],
    "el hombre":      [{"es": "El hombre es fuerte.", "en": "The man is strong."}],
    "la estudiante":  [{"es": "La estudiante es inteligente.", "en": "The female student is intelligent."}],
    "el gerente":     [{"es": "El gerente es agradable.", "en": "The male manager is agreeable."}],
    "la gerente":     [{"es": "La gerente es inteligente.", "en": "The female manager is intelligent."}],
    "el presidente":  [{"es": "El presidente es importante.", "en": "The male president is important."}],
    "la presidente":  [{"es": "La presidente es inteligente.", "en": "The female president is intelligent."}],
    "la amistad":     [{"es": "La amistad es importante.", "en": "The friendship is important."}],
    "la mujer":       [{"es": "La mujer es inteligente y alegre.", "en": "The woman is intelligent and happy."}],

    # PLACES
    "el banco":    [{"es": "El banco es grande.", "en": "The bank is big."}],
    "el baño":     [{"es": "El baño es pequeño.", "en": "The bathroom is small."}],
    "la casa":     [{"es": "La casa es grande y bonita.", "en": "The house is big and pretty."}],
    "la iglesia":  [{"es": "La iglesia es vieja.", "en": "The church is old."}],
    "la tienda":   [{"es": "La tienda es pequeña.", "en": "The store is small."}],
    "el hospital": [{"es": "El hospital es grande.", "en": "The hospital is big."}],
    "el hotel":    [{"es": "El hotel es caro.", "en": "The hotel is expensive."}],
    "la ciudad":   [{"es": "La ciudad es grande y fantástica.", "en": "The city is big and fantastic."}],
    "la clase":    [{"es": "La clase es interesante.", "en": "The class is interesting."}],

    # TRANSPORTATION
    "el carro":  [{"es": "El carro es negro y nuevo.", "en": "The car is black and new."}],
    "el tren":   [{"es": "El tren es rápido.", "en": "The train is fast."}],
}

with open('data/ch1.json', encoding='utf-8') as f:
    ch = json.load(f)

if 'study' not in ch:
    ch['study'] = {}
ch['study']['wordExamples'] = SENTENCES

with open('data/ch1.json', 'w', encoding='utf-8') as f:
    json.dump(ch, f, ensure_ascii=False, indent=2)

print(f'Added {len(SENTENCES)} word example sets to ch1.json')
