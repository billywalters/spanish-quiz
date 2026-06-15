import json, sys, random
sys.stdout.reconfigure(encoding='utf-8')

random.seed(42)
qs = []
qid = [1]

def Q(**kw):
    q = {'id': f'ch2_{qid[0]}', **kw}
    qid[0] += 1
    qs.append(q)

def shuffle(lst):
    lst = list(lst)
    random.shuffle(lst)
    return lst

def mc_opts(correct, wrong_pool, n=3):
    wrong = [w for w in wrong_pool if w != correct]
    random.shuffle(wrong)
    return shuffle([correct] + wrong[:n])

# ── SUBJECT PRONOUNS ──────────────────────────────────────────────────────────

PRONOUNS = [
    ('yo',       'I'),
    ('tu',       'you (informal)'),
    ('el',       'he'),
    ('ella',     'she'),
    ('usted',    'you (formal)'),
    ('nosotros', 'we'),
    ('vosotros', 'you all (Spain)'),
    ('ellos',    'they (masc.)'),
    ('ellas',    'they (fem.)'),
    ('ustedes',  'you all'),
]

for es, en in PRONOUNS:
    wrong_en = [p[1] for p in PRONOUNS if p[1] != en]
    wrong_es = [p[0] for p in PRONOUNS if p[0] != es]
    Q(tier='beginner', type='multiple_choice', category='pronoun_vocabulary', topic='pronouns',
      question='What does the Spanish pronoun "' + es + '" mean?',
      options=mc_opts(en, wrong_en), answer=en,
      explanation='"' + es + '" = ' + en)
    Q(tier='beginner', type='multiple_choice', category='pronoun_vocabulary', topic='pronouns',
      question='Which Spanish pronoun means "' + en + '"?',
      options=mc_opts(es, wrong_es), answer=es,
      explanation='"' + en + '" in Spanish is "' + es + '"')

# ── ESTAR CONJUGATION ─────────────────────────────────────────────────────────

CONJ = [
    ('yo',                      'estoy',   'I am'),
    ('tu',                      'estas',   'you are'),
    ('el / ella / usted',       'esta',    'he/she/you is'),
    ('nosotros',                'estamos', 'we are'),
    ('vosotros',                'estais',  'you all are'),
    ('ellos / ellas / ustedes', 'estan',   'they/you all are'),
]

CONJ_DISPLAY = [
    ('yo',                      'estoy',   'I am'),
    ('tú',                      'estás',   'you are'),
    ('él / ella / usted',       'está',    'he/she/you is'),
    ('nosotros',                'estamos', 'we are'),
    ('vosotros',                'estáis',  'you all are'),
    ('ellos / ellas / ustedes', 'están',   'they/you all are'),
]

conj_forms = [c[1] for c in CONJ_DISPLAY]
conj_meanings = [c[2] for c in CONJ_DISPLAY]

for (subj_raw, form_raw, _), (subj, form, meaning) in zip(CONJ, CONJ_DISPLAY):
    wrong_forms = [c[1] for c in CONJ_DISPLAY if c[1] != form]
    wrong_meanings = [c[2] for c in CONJ_DISPLAY if c[2] != meaning]
    Q(tier='beginner', type='multiple_choice', category='verb_conjugation', topic='estar_verb',
      question='What is the "' + subj + '" form of the verb "estar"?',
      options=mc_opts(form, wrong_forms), answer=form,
      explanation=subj + ' -> ' + form + ' (' + meaning + ')')
    Q(tier='beginner', type='multiple_choice', category='verb_conjugation', topic='estar_verb',
      question='What does "' + form + '" mean?',
      options=mc_opts(meaning, wrong_meanings), answer=meaning,
      explanation='"' + form + '" means "' + meaning + '"')

# fill-blank conjugation
FILL_ESTAR = [
    ('Yo ___ en la clase.',              'estoy',   'I am in the class.'),
    ('Ella ___ enferma.',                'esta',    'She is sick.'),
    ('Nosotros ___ bien, gracias.',      'estamos', 'We are fine, thanks.'),
    ('Como ___ tu?',                     'estas',   'How are you?'),
    ('Ellos ___ cansados.',              '___ estan',   'They are tired.'),
    ('El restaurante ___ en la ciudad.', 'esta',    'The restaurant is in the city.'),
    ('Vosotros ___ alegres.',            'estais',  'You all are happy.'),
    ('Las doctoras ___ enfermas.',       'estan',   'The doctors are sick.'),
    ('Yo ___ feliz hoy.',                'estoy',   'I am happy today.'),
    ('Nosotros ___ en el carro.',        'estamos', 'We are in the car.'),
    ('Ellas ___ en el bano.',            'estan',   'They are in the bathroom.'),
    ('El ___ guapo.',                    'esta',    'He is handsome.'),
    ('La sopa ___ sabrosa.',             'esta',    'The soup is delicious.'),
]

FILL_ESTAR_DISPLAY = [
    ('Yo ___ en la clase.',               'estoy',   'I am in the class.'),
    ('Ella ___ enferma.',                 'está',    'She is sick.'),
    ('Nosotros ___ bien, gracias.',       'estamos', 'We are fine, thanks.'),
    ('¿Cómo ___ tú?',                    'estás',   'How are you?'),
    ('Ellos ___ cansados.',              'están',   'They are tired.'),
    ('El restaurante ___ en la ciudad.', 'está',    'The restaurant is in the city.'),
    ('Vosotros ___ alegres.',            'estáis',  'You all are happy.'),
    ('Las doctoras ___ enfermas.',       'están',   'The doctors are sick.'),
    ('Yo ___ feliz hoy.',                'estoy',   'I am happy today.'),
    ('Nosotros ___ en el carro.',        'estamos', 'We are in the car.'),
    ('Ellas ___ en el baño.',            'están',   'They are in the bathroom.'),
    ('Él ___ guapo.',                    'está',    'He is handsome.'),
    ('La sopa ___ sabrosa.',             'está',    'The soup is delicious.'),
]

for (_, form_raw, _), (sent, form, translation) in zip(FILL_ESTAR, FILL_ESTAR_DISPLAY):
    displayed = sent.replace('___', '______')
    Q(tier='beginner', type='fill_blank', category='estar_usage', topic='estar_verb',
      question='Complete the sentence with the correct form of "estar": "' + displayed + '"',
      answer=form,
      explanation=sent.replace('___', form) + ' = ' + translation)

Q(tier='beginner', type='multiple_choice', category='estar_usage', topic='estar_verb',
  question='Which subject pronoun goes with "estoy"?',
  options=shuffle(['yo', 'tú', 'él', 'nosotros']), answer='yo',
  explanation='"estoy" is the yo (I) form of estar.')
Q(tier='beginner', type='multiple_choice', category='estar_usage', topic='estar_verb',
  question='Which subject pronoun goes with "estamos"?',
  options=shuffle(['yo', 'tú', 'nosotros', 'ustedes']), answer='nosotros',
  explanation='"estamos" is the nosotros (we) form of estar.')
Q(tier='beginner', type='multiple_choice', category='estar_usage', topic='estar_verb',
  question='Which subject pronoun goes with "están"?',
  options=shuffle(['yo', 'tú', 'ella', 'ellos']), answer='ellos',
  explanation='"están" is the ellos/ellas/ustedes form of estar.')

# ── ADJECTIVES ────────────────────────────────────────────────────────────────

ADJS = [
    ('alegre',    'happy (merry)',      'alegre',    'alegres',    'mood'),
    ('bonito',    'pretty',            'bonita',    'bonitos',    'appearance'),
    ('bueno',     'good',              'buena',     'buenos',     'opinion'),
    ('cansado',   'tired',             'cansada',   'cansados',   'health'),
    ('contento',  'happy (contented)', 'contenta',  'contentos',  'mood'),
    ('delicioso', 'delicious',         'deliciosa', 'deliciosos', 'opinion'),
    ('enfermo',   'sick',              'enferma',   'enfermos',   'health'),
    ('enojado',   'angry',             'enojada',   'enojados',   'mood'),
    ('feliz',     'happy',             'feliz',     'felices',    'mood'),
    ('guapo',     'handsome',          'guapa',     'guapos',     'appearance'),
    ('hermoso',   'beautiful',         'hermosa',   'hermosos',   'appearance'),
    ('lindo',     'pretty',            'linda',     'lindos',     'appearance'),
    ('sabroso',   'delicious',         'sabrosa',   'sabrosos',   'opinion'),
]

for masc, en, fem, pl, use in ADJS:
    wrong_en = [a[1] for a in ADJS if a[1] != en]
    wrong_es = [a[0] for a in ADJS if a[0] != masc]
    Q(tier='beginner', type='multiple_choice', category='adjective_vocabulary', topic='adjectives',
      question='What does the Spanish adjective "' + masc + '" mean?',
      options=mc_opts(en, wrong_en), answer=en,
      explanation='"' + masc + '" = ' + en)
    Q(tier='beginner', type='multiple_choice', category='adjective_vocabulary', topic='adjectives',
      question='What is the Spanish word for "' + en + '"?',
      options=mc_opts(masc, wrong_es), answer=masc,
      explanation='"' + en + '" in Spanish is "' + masc + '"')
    if fem != masc:
        wrong_fem = [a[2] for a in ADJS if a[2] != fem and a[2] != masc]
        Q(tier='intermediate', type='multiple_choice', category='adjective_agreement', topic='adjectives',
          question='What is the feminine form of "' + masc + '"?',
          options=mc_opts(fem, wrong_fem[:3]), answer=fem,
          explanation='"' + masc + '" (masc.) changes to "' + fem + '" (fem.)')
    wrong_pl = [a[3] for a in ADJS if a[3] != pl]
    note = ' (feliz -> felices: z changes to c before -es)' if masc == 'feliz' else ''
    Q(tier='intermediate', type='multiple_choice', category='adjective_agreement', topic='adjectives',
      question='What is the plural form of "' + masc + '"?',
      options=mc_opts(pl, wrong_pl[:3]), answer=pl,
      explanation='"' + masc + '" -> plural: "' + pl + '"' + note)

# adjective agreement in sentences
AGREE = [
    ('El hombre esta ___.',         'cansado',   'cansada',   'tired (m)'),
    ('La mujer esta ___.',          'cansada',   'cansado',   'tired (f)'),
    ('La muchacha esta ___.',       'contenta',  'contento',  'happy (f)'),
    ('El muchacho esta ___.',       'contento',  'contenta',  'happy (m)'),
    ('La doctora esta ___.',        'enferma',   'enfermo',   'sick (f)'),
    ('El doctor esta ___.',         'enfermo',   'enferma',   'sick (m)'),
    ('La chica esta ___.',          'enojada',   'enojado',   'angry (f)'),
    ('El chico esta ___.',          'enojado',   'enojada',   'angry (m)'),
    ('Ella esta ___.',              'feliz',     'felices',   'happy'),
    ('Ella esta ___ hoy.',          'hermosa',   'hermoso',   'beautiful (f)'),
    ('El esta ___.',                'guapo',     'guapa',     'handsome (m)'),
    ('La comida esta ___.',         'buena',     'bueno',     'good (f)'),
    ('El pescado esta ___.',        'delicioso', 'deliciosa', 'delicious (m)'),
    ('La sopa esta ___.',           'sabrosa',   'sabroso',   'delicious (f)'),
    ('Los hombres estan ___.',      'cansados',  'cansado',   'tired (m.pl)'),
    ('Estamos ___.',                'alegres',   'alegre',    'happy (pl)'),
    ('Los doctores estan ___.',     'enfermos',  'enferma',   'sick (m.pl)'),
    ('Las mujeres estan ___.',      'contentas', 'contento',  'happy (f.pl)'),
]

AGREE_DISPLAY = [
    ('El hombre está ___.',         'cansado',   'cansada',   'tired (m)'),
    ('La mujer está ___.',          'cansada',   'cansado',   'tired (f)'),
    ('La muchacha está ___.',       'contenta',  'contento',  'happy (f)'),
    ('El muchacho está ___.',       'contento',  'contenta',  'happy (m)'),
    ('La doctora está ___.',        'enferma',   'enfermo',   'sick (f)'),
    ('El doctor está ___.',         'enfermo',   'enferma',   'sick (m)'),
    ('La chica está ___.',          'enojada',   'enojado',   'angry (f)'),
    ('El chico está ___.',          'enojado',   'enojada',   'angry (m)'),
    ('Ella está ___.',              'feliz',     'felices',   'happy'),
    ('Ella está ___ hoy.',          'hermosa',   'hermoso',   'beautiful (f)'),
    ('Él está ___.',                'guapo',     'guapa',     'handsome (m)'),
    ('La comida está ___.',         'buena',     'bueno',     'good (f)'),
    ('El pescado está ___.',        'delicioso', 'deliciosa', 'delicious (m)'),
    ('La sopa está ___.',           'sabrosa',   'sabroso',   'delicious (f)'),
    ('Los hombres están ___.',      'cansados',  'cansado',   'tired (m.pl)'),
    ('Estamos ___.',                'alegres',   'alegre',    'happy (pl)'),
    ('Los doctores están ___.',     'enfermos',  'enferma',   'sick (m.pl)'),
    ('Las mujeres están ___.',      'contentas', 'contento',  'happy (f.pl)'),
]

all_adj_forms = []
for a in ADJS:
    all_adj_forms += [a[0], a[2], a[3]]
all_adj_forms = list(set(all_adj_forms))

for (_, c_raw, w_raw, _), (sent, correct, wrong1, hint) in zip(AGREE, AGREE_DISPLAY):
    wrong_pool = [w for w in all_adj_forms if w != correct]
    random.shuffle(wrong_pool)
    opts = shuffle([correct, wrong1] + wrong_pool[:2])
    full = sent.replace('___', correct)
    Q(tier='intermediate', type='multiple_choice', category='adjective_agreement', topic='adjectives',
      question='Choose the correct form of the adjective: "' + sent + '"',
      options=opts, answer=correct,
      explanation=full + ' (' + hint + ')')

# ── ESTAR USES — CONCEPTUAL ───────────────────────────────────────────────────

USES = ['location', 'health', 'changing mood or condition', 'personal opinion']

Q(tier='beginner', type='multiple_choice', category='estar_concept', topic='estar_uses',
  question='Estar is used to express four basic concepts. Which of the following is NOT one of them?',
  options=shuffle(['location', 'health', 'personal opinion', 'origin or nationality']),
  answer='origin or nationality',
  explanation='Estar expresses: location, health, changing mood/condition, and personal opinion. Origin and nationality use "ser".')

CONCEPT_QS = [
    ('Yo estoy en la clase.',           'location',                   'I am in the class.'),
    ('El restaurante esta en la ciudad.','location',                  'The restaurant is in the city.'),
    ('Ellas estan en el bano.',         'location',                   'They are in the bathroom.'),
    ('Ella esta enferma.',              'health',                     'She is sick.'),
    ('Yo estoy bien, gracias.',         'health',                     'I am fine, thanks.'),
    ('Los doctores estan enfermos.',    'health',                     'The doctors are sick.'),
    ('La muchacha esta contenta.',      'changing mood or condition', 'The girl is happy.'),
    ('Los hombres estan cansados.',     'changing mood or condition', 'The men are tired.'),
    ('Estamos alegres.',                'changing mood or condition', 'We are happy.'),
    ('La comida esta buena.',           'personal opinion',           'The meal is good (tastes good).'),
    ('El pescado esta delicioso.',      'personal opinion',           'The fish is delicious.'),
    ('Ella esta hermosa hoy.',          'personal opinion',           'She is pretty today (looks pretty).'),
]

CONCEPT_QS_DISPLAY = [
    ('Yo estoy en la clase.',              'location',                   'I am in the class.'),
    ('El restaurante está en la ciudad.',  'location',                   'The restaurant is in the city.'),
    ('Ellas están en el baño.',            'location',                   'They are in the bathroom.'),
    ('Ella está enferma.',                 'health',                     'She is sick.'),
    ('Yo estoy bien, gracias.',            'health',                     'I am fine, thanks.'),
    ('Los doctores están enfermos.',       'health',                     'The doctors are sick.'),
    ('La muchacha está contenta.',         'changing mood or condition', 'The girl is happy.'),
    ('Los hombres están cansados.',        'changing mood or condition', 'The men are tired.'),
    ('Estamos alegres.',                   'changing mood or condition', 'We are happy.'),
    ('La comida está buena.',              'personal opinion',           'The meal is good (tastes good).'),
    ('El pescado está delicioso.',         'personal opinion',           'The fish is delicious.'),
    ('Ella está hermosa hoy.',             'personal opinion',           'She is pretty today (looks pretty).'),
]

for (_, use, _), (sent, _, translation) in zip(CONCEPT_QS, CONCEPT_QS_DISPLAY):
    wrong_uses = [u for u in USES if u != use]
    Q(tier='intermediate', type='multiple_choice', category='estar_concept', topic='estar_uses',
      question='"' + sent + '" — this uses estar to express…',
      options=shuffle([use] + wrong_uses[:3]), answer=use,
      explanation='"' + sent + '" (' + translation + ') uses estar for ' + use + '.')

Q(tier='intermediate', type='multiple_choice', category='estar_concept', topic='estar_uses',
  question='Which verb is used to express temporary states, location, and changing conditions?',
  options=shuffle(['ser', 'estar', 'tener', 'ir']), answer='estar',
  explanation='"Estar" is used for location, health, mood, and personal opinion. "Ser" is used for permanent traits.')

Q(tier='intermediate', type='multiple_choice', category='estar_concept', topic='estar_uses',
  question='"She is in the class." Which verb would you use in Spanish?',
  options=shuffle(['ser', 'estar', 'tener', 'hacer']), answer='estar',
  explanation='Location uses "estar": "Ella esta en la clase."')

Q(tier='intermediate', type='multiple_choice', category='estar_concept', topic='estar_uses',
  question='"He is a doctor." Which verb would you use in Spanish?',
  options=shuffle(['ser', 'estar', 'tener', 'ir']), answer='ser',
  explanation='Professions and permanent identity use "ser": "El es medico."')

# ── QUESTION WORDS & LOCATION WORDS ──────────────────────────────────────────

QWS = [
    ('Como?',       'how?',   'question_words'),
    ('Donde?',      'where?', 'question_words'),
    ('Quien?',      'who?',   'question_words'),
    ('aqui / aca',  'here',   'location_words'),
    ('alli / alla', 'there',  'location_words'),
]
QWS_DISPLAY = [
    ('¿Cómo?',      'how?',   'question_words'),
    ('¿Dónde?',     'where?', 'question_words'),
    ('¿Quién?',     'who?',   'question_words'),
    ('aquí / acá',  'here',   'location_words'),
    ('allí / allá', 'there',  'location_words'),
]

for (_, en, topic), (es, _, _) in zip(QWS, QWS_DISPLAY):
    wrong_en = [q[1] for q in QWS_DISPLAY if q[1] != en]
    wrong_es = [q[0] for q in QWS_DISPLAY if q[0] != es]
    Q(tier='beginner', type='multiple_choice', category='noun_vocabulary', topic=topic,
      question='What does "' + es + '" mean?',
      options=mc_opts(en, wrong_en + ['what?', 'when?', 'why?', 'over there']), answer=en,
      explanation='"' + es + '" = ' + en)
    Q(tier='beginner', type='multiple_choice', category='noun_vocabulary', topic=topic,
      question='What is the Spanish word for "' + en + '"?',
      options=mc_opts(es, wrong_es + ['porque?', 'cuando?', 'alla']), answer=es,
      explanation='"' + en + '" in Spanish is "' + es + '"')

# ── TRANSLATIONS ───────────────────────────────────────────────────────────────

TRANS_ES = [
    ('Yo estoy bien, gracias.',            'I am fine, thanks.',            'estar_verb'),
    ('Ella esta enferma.',                  'She is sick.',                  'estar_verb'),
    ('Los doctores estan enfermos.',        'The doctors are sick.',         'estar_verb'),
    ('Como estan Uds.?',                    'How are you all?',              'estar_verb'),
    ('Estamos bien.',                       'We are well.',                  'estar_verb'),
    ('La muchacha esta contenta.',          'The girl is happy.',            'adjectives'),
    ('Los hombres estan cansados.',         'The men are tired.',            'adjectives'),
    ('Estamos alegres.',                    'We are happy.',                 'adjectives'),
    ('Estas enojado?',                      'Are you angry?',                'adjectives'),
    ('La comida esta buena.',               'The meal is good.',             'adjectives'),
    ('El pescado esta delicioso.',          'The fish is delicious.',        'adjectives'),
    ('La sopa esta sabrosa.',               'The soup is delicious.',        'adjectives'),
    ('Ella esta hermosa hoy.',              'She is pretty today.',          'adjectives'),
    ('El esta guapo.',                      'He is handsome.',               'adjectives'),
    ('Nosotros estamos en el carro.',       'We are in the car.',            'estar_verb'),
    ('El restaurante esta en la ciudad.',   'The restaurant is in the city.','estar_verb'),
    ('Ellas estan en el bano.',             'They are in the bathroom.',     'estar_verb'),
    ('Estas tu en el hospital?',            'Are you in the hospital?',      'estar_verb'),
    ('Estoy feliz.',                        'I am happy.',                   'adjectives'),
]

TRANS_ES_DISPLAY = [
    ('Yo estoy bien, gracias.',            'I am fine, thanks.'),
    ('Ella está enferma.',                  'She is sick.'),
    ('Los doctores están enfermos.',        'The doctors are sick.'),
    ('¿Cómo están Uds.?',                   'How are you all?'),
    ('Estamos bien.',                       'We are well.'),
    ('La muchacha está contenta.',          'The girl is happy.'),
    ('Los hombres están cansados.',         'The men are tired.'),
    ('Estamos alegres.',                    'We are happy.'),
    ('¿Estás enojado?',                     'Are you angry?'),
    ('La comida está buena.',               'The meal is good.'),
    ('El pescado está delicioso.',          'The fish is delicious.'),
    ('La sopa está sabrosa.',               'The soup is delicious.'),
    ('Ella está hermosa hoy.',              'She is pretty today.'),
    ('Él está guapo.',                      'He is handsome.'),
    ('Nosotros estamos en el carro.',       'We are in the car.'),
    ('El restaurante está en la ciudad.',   'The restaurant is in the city.'),
    ('Ellas están en el baño.',             'They are in the bathroom.'),
    ('¿Estás tú en el hospital?',           'Are you in the hospital?'),
    ('Estoy feliz.',                        'I am happy.'),
]

for (_, en, topic), (es, _) in zip(TRANS_ES, TRANS_ES_DISPLAY):
    Q(tier='intermediate', type='fill_blank', category='translation', topic=topic,
      question='Translate to English: "' + es + '"',
      answer=en,
      explanation='"' + es + '" = "' + en + '"')

TRANS_EN = [
    ('I am fine, thanks.',         'Yo estoy bien, gracias.',           'estar_verb'),
    ('She is sick.',               'Ella esta enferma.',                 'estar_verb'),
    ('We are in the car.',         'Nosotros estamos en el carro.',      'estar_verb'),
    ('The girl is happy.',         'La muchacha esta contenta.',         'adjectives'),
    ('The men are tired.',         'Los hombres estan cansados.',        'adjectives'),
    ('Are you angry?',             'Estas enojado?',                     'adjectives'),
    ('The meal is good.',          'La comida esta buena.',              'adjectives'),
    ('He is handsome.',            'El esta guapo.',                     'adjectives'),
    ('I am happy.',                'Estoy feliz.',                       'adjectives'),
    ('How are you all?',           'Como estan Uds.?',                   'estar_verb'),
]

TRANS_EN_DISPLAY = [
    ('I am fine, thanks.',         'Yo estoy bien, gracias.'),
    ('She is sick.',               'Ella está enferma.'),
    ('We are in the car.',         'Nosotros estamos en el carro.'),
    ('The girl is happy.',         'La muchacha está contenta.'),
    ('The men are tired.',         'Los hombres están cansados.'),
    ('Are you angry?',             '¿Estás enojado?'),
    ('The meal is good.',          'La comida está buena.'),
    ('He is handsome.',            'Él está guapo.'),
    ('I am happy.',                'Estoy feliz.'),
    ('How are you all?',           '¿Cómo están Uds.?'),
]

for (en, _, topic), (_, es) in zip(TRANS_EN, TRANS_EN_DISPLAY):
    Q(tier='intermediate', type='fill_blank', category='translation', topic=topic,
      question='Translate to Spanish: "' + en + '"',
      answer=es,
      explanation='"' + en + '" = "' + es + '"')

print(f'Total questions: {len(qs)}')

ch2 = {
    "id": "ch2",
    "title": "Chapter 2 — The Verb Estar",
    "description": "Subject pronouns, the verb estar, adjectives of condition, and the four uses of estar",
    "questions": qs
}

with open('data/ch2.json', 'w', encoding='utf-8') as f:
    json.dump(ch2, f, ensure_ascii=False, indent=2)
print('Wrote data/ch2.json')
