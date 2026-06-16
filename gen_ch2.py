"""
Chapter 2 — The Verb Estar
Heavy focus on: picking the RIGHT form, understanding WHY (person/number),
and understanding WHICH USE (location / health / mood+condition / opinion).
"""
import json, sys, random
sys.stdout.reconfigure(encoding='utf-8')

random.seed(99)
qs = []
qid = [1]

def Q(**kw):
    qs.append({'id': f'ch2_{qid[0]}', **kw})
    qid[0] += 1

def sh(lst): lst = list(lst); random.shuffle(lst); return lst
def pool(correct, wrong, n=3):
    w = [x for x in wrong if x != correct]; random.shuffle(w)
    return sh([correct] + w[:n])

# ══════════════════════════════════════════════════════════════
#  SECTION 1 — SUBJECT PRONOUNS
# ══════════════════════════════════════════════════════════════

PRONOUNS = [
    ('yo',       'I',                  'singular', 'first'),
    ('tú',       'you (informal)',      'singular', 'second'),
    ('él',       'he',                 'singular', 'third'),
    ('ella',     'she',                'singular', 'third'),
    ('usted',    'you (formal)',        'singular', 'third'),
    ('nosotros', 'we',                 'plural',   'first'),
    ('vosotros', 'you all (Spain)',     'plural',   'second'),
    ('ellos',    'they (masc.)',        'plural',   'third'),
    ('ellas',    'they (fem.)',         'plural',   'third'),
    ('ustedes',  'you all',            'plural',   'third'),
]

for es, en, num, per in PRONOUNS:
    wrong_en = [p[1] for p in PRONOUNS if p[1] != en]
    wrong_es = [p[0] for p in PRONOUNS if p[0] != es]
    Q(tier='beginner', type='multiple_choice', category='pronoun_vocabulary', topic='pronouns',
      question=f'What does the Spanish pronoun "{es}" mean?',
      options=pool(en, wrong_en), answer=en,
      explanation=f'"{es}" = {en} ({per} person {num})')
    Q(tier='beginner', type='multiple_choice', category='pronoun_vocabulary', topic='pronouns',
      question=f'Which Spanish pronoun means "{en}"?',
      options=pool(es, wrong_es), answer=es,
      explanation=f'"{en}" in Spanish is "{es}"')

# ══════════════════════════════════════════════════════════════
#  SECTION 2 — ESTAR CONJUGATION + REASONING
# ══════════════════════════════════════════════════════════════

CONJ = [
    ('yo',                      'estoy',   'I am',            '1st person singular'),
    ('tú',                      'estás',   'you are',         '2nd person singular'),
    ('él / ella / usted',       'está',    'he/she/you is',   '3rd person singular'),
    ('nosotros',                'estamos', 'we are',          '1st person plural'),
    ('vosotros',                'estáis',  'you all are',     '2nd person plural'),
    ('ellos / ellas / ustedes', 'están',   'they/you all are','3rd person plural'),
]
forms    = [c[1] for c in CONJ]
meanings = [c[2] for c in CONJ]
reasons  = [c[3] for c in CONJ]

for subj, form, meaning, reason in CONJ:
    wrong_forms = [c[1] for c in CONJ if c[1] != form]
    wrong_meanings = [c[2] for c in CONJ if c[2] != meaning]
    wrong_reasons = [c[3] for c in CONJ if c[3] != reason]

    Q(tier='beginner', type='multiple_choice', category='verb_conjugation', topic='estar_verb',
      question=f'What is the "{subj}" form of "estar"?',
      options=pool(form, wrong_forms), answer=form,
      explanation=f'{subj} → {form} ({meaning}). {reason}.')

    Q(tier='beginner', type='multiple_choice', category='verb_conjugation', topic='estar_verb',
      question=f'What does "{form}" mean?',
      options=pool(meaning, wrong_meanings), answer=meaning,
      explanation=f'"{form}" means "{meaning}" — {reason}.')

    Q(tier='intermediate', type='multiple_choice', category='verb_conjugation', topic='estar_verb',
      question=f'Why do we use "{form}" for the subject "{subj}"?',
      options=pool(reason, wrong_reasons), answer=reason,
      explanation=f'"{subj}" requires "{form}" because it is {reason}.')

# Which subject goes with each form
Q(tier='beginner', type='multiple_choice', category='verb_conjugation', topic='estar_verb',
  question='Which subject uses "estoy"?',
  options=sh(['yo','tú','él','nosotros']), answer='yo',
  explanation='"estoy" = yo (1st person singular). Every other subject uses a different form.')
Q(tier='beginner', type='multiple_choice', category='verb_conjugation', topic='estar_verb',
  question='Which subject uses "estamos"?',
  options=sh(['yo','tú','nosotros','ustedes']), answer='nosotros',
  explanation='"estamos" = nosotros (1st person plural).')
Q(tier='beginner', type='multiple_choice', category='verb_conjugation', topic='estar_verb',
  question='Which subject uses "estáis"?',
  options=sh(['yo','nosotros','vosotros','ustedes']), answer='vosotros',
  explanation='"estáis" = vosotros (2nd person plural, used in Spain).')
Q(tier='intermediate', type='multiple_choice', category='verb_conjugation', topic='estar_verb',
  question='Both "ellos" and "ustedes" use the same form of estar. Which form?',
  options=sh(['estoy','estás','está','están']), answer='están',
  explanation='"ellos", "ellas", and "ustedes" all use "están" (3rd person plural).')
Q(tier='intermediate', type='multiple_choice', category='verb_conjugation', topic='estar_verb',
  question='"Él", "ella", and "usted" all share the same form of estar. Which form?',
  options=sh(['estoy','estás','está','están']), answer='está',
  explanation='"él", "ella", and "usted" all use "está" (3rd person singular).')

# Fill-blank conjugation — context sentences
FILL = [
    ('Yo ___ en la clase.',                 'estoy',   'I am in the class.'),
    ('Ella ___ enferma.',                    'está',    'She is sick.'),
    ('Nosotros ___ bien, gracias.',          'estamos', 'We are fine, thanks.'),
    ('¿Cómo ___ tú?',                       'estás',   'How are you?'),
    ('Ellos ___ cansados.',                  'están',   'They are tired.'),
    ('El restaurante ___ en la ciudad.',     'está',    'The restaurant is in the city.'),
    ('Vosotros ___ alegres.',                'estáis',  'You all are happy.'),
    ('Las doctoras ___ enfermas.',           'están',   'The doctors are sick.'),
    ('Yo ___ feliz hoy.',                    'estoy',   'I am happy today.'),
    ('Nosotros ___ en el carro.',            'estamos', 'We are in the car.'),
    ('Ellas ___ en el baño.',                'están',   'They are in the bathroom.'),
    ('Él ___ guapo.',                        'está',    'He is handsome.'),
    ('La sopa ___ sabrosa.',                 'está',    'The soup is delicious.'),
    ('¿Cómo ___ Uds.?',                     'están',   'How are you all?'),
    ('Daniel ___ muy cansado hoy.',          'está',    'Daniel is very tired today.'),
    ('El teléfono y el libro ___ en la mesa.', 'están', 'The phone and the book are on the table.'),
    ('¿Dónde ___ ellos?',                   'están',   'Where are they?'),
    ('¿Dónde ___ el baño, por favor?',      'está',    'Where is the bathroom, please?'),
    ('El niño ___ enojado.',                 'está',    'The boy is angry.'),
    ('Los muchachos ___ alegres.',           'están',   'The boys are happy.'),
    ('Yo ___ contento.',                     'estoy',   'I am happy (contented).'),
    ('¿Quién ___ aquí?',                    'está',    'Who is here?'),
    ('La comida ___ buena.',                 'está',    'The meal is good.'),
    ('El pescado ___ delicioso.',            'está',    'The fish is delicious.'),
    ('Ella ___ hermosa hoy.',                'está',    'She is pretty today.'),
    ('Usted ___ cansado.',                   'está',    'You are tired.'),
    ('Tú ___ enojado.',                      'estás',   'You are angry.'),
]

for sent, form, translation in FILL:
    Q(tier='beginner', type='fill_blank', category='estar_usage', topic='estar_verb',
      question=f'Complete with the correct form of "estar": "{sent.replace("___","______")}"',
      answer=form,
      explanation=f'{sent.replace("___", form)} → {translation}')

# ══════════════════════════════════════════════════════════════
#  SECTION 3 — THE FOUR USES OF ESTAR (+ WHY)
# ══════════════════════════════════════════════════════════════

USES = ['location', 'health', 'changing mood or condition', 'personal opinion']

# Concept
Q(tier='beginner', type='multiple_choice', category='estar_concept', topic='estar_uses',
  question='Estar expresses four basic concepts. Which of these is NOT one of them?',
  options=sh(['location','health','personal opinion','nationality or origin']),
  answer='nationality or origin',
  explanation='Estar = location, health, mood/condition, personal opinion. Nationality/origin use "ser".')
Q(tier='beginner', type='multiple_choice', category='estar_concept', topic='estar_uses',
  question='Which verb expresses temporary states, changing conditions, and location?',
  options=sh(['ser','estar','tener','ir']), answer='estar',
  explanation='"Estar" covers temporary or changeable states. "Ser" covers permanent traits.')
Q(tier='intermediate', type='multiple_choice', category='estar_concept', topic='estar_uses',
  question='"He is a doctor." Which verb do you use in Spanish?',
  options=sh(['ser','estar','tener','hacer']), answer='ser',
  explanation='Professions and permanent identity use "ser": "Él es médico."')
Q(tier='intermediate', type='multiple_choice', category='estar_concept', topic='estar_uses',
  question='"The restaurant is in the city." Which verb do you use?',
  options=sh(['ser','estar','tener','ir']), answer='estar',
  explanation='Location always uses "estar", even for permanent locations: "El restaurante está en la ciudad."')
Q(tier='intermediate', type='multiple_choice', category='estar_concept', topic='estar_uses',
  question='Why does location use "estar" even when a place is permanently located somewhere?',
  options=sh(['Because location is always a temporary state',
              'Because "estar" expresses where something is, regardless of permanence',
              'Because "ser" is only for living things',
              'Because location is a personal opinion']),
  answer='Because "estar" expresses where something is, regardless of permanence',
  explanation='"Estar" is always used for location — it describes WHERE something is, which is a positional state even if the location never changes.')

# Identify the use — with WHY explanation built into each
USE_SENTENCES = [
    ('Yo estoy en la clase.',              'location',                   'I am in the class.',          'The sentence tells WHERE the speaker is — a location.'),
    ('El restaurante está en la ciudad.',  'location',                   'The restaurant is in the city.','The sentence tells WHERE the restaurant is — a location.'),
    ('Ellas están en el baño.',            'location',                   'They are in the bathroom.',    'The sentence tells WHERE they are — a location.'),
    ('¿Estás tú en el hospital?',          'location',                   'Are you in the hospital?',     'The question asks WHERE you are — a location.'),
    ('Yo estoy bien, gracias.',            'health',                     'I am fine, thanks.',           '"Bien" describes physical wellbeing — a health state.'),
    ('Ella está enferma.',                 'health',                     'She is sick.',                 '"Enferma" describes a temporary physical condition — health.'),
    ('Los doctores están enfermos.',       'health',                     'The doctors are sick.',        '"Enfermos" describes their temporary physical state — health.'),
    ('¿Cómo están Uds.?',                 'health',                     'How are you all?',             'Asking about someone\'s wellbeing uses "estar" for health.'),
    ('La muchacha está contenta.',         'changing mood or condition', 'The girl is happy.',           '"Contenta" is a temporary emotional state — mood/condition.'),
    ('Los hombres están cansados.',        'changing mood or condition', 'The men are tired.',           '"Cansados" is a temporary physical/emotional state — condition.'),
    ('Estamos alegres.',                   'changing mood or condition', 'We are happy.',                '"Alegres" is a temporary mood — changing mood or condition.'),
    ('¿Estás enojado?',                   'changing mood or condition', 'Are you angry?',               '"Enojado" is a temporary emotion — changing mood or condition.'),
    ('Daniel está muy cansado hoy.',       'changing mood or condition', 'Daniel is very tired today.',  '"Cansado" is a temporary physical state — condition. "Hoy" (today) reinforces its temporary nature.'),
    ('El niño está enojado.',              'changing mood or condition', 'The boy is angry.',            '"Enojado" is a temporary emotion — changing mood or condition.'),
    ('Yo estoy contento.',                 'changing mood or condition', 'I am contented.',              '"Contento" is a temporary feeling, not a permanent personality trait — mood/condition.'),
    ('La comida está buena.',              'personal opinion',           'The meal is good.',            '"Buena" here expresses how the meal tastes right now — a personal opinion about taste.'),
    ('El pescado está delicioso.',         'personal opinion',           'The fish is delicious.',       '"Delicioso" expresses how the fish tastes — a personal opinion.'),
    ('La sopa está sabrosa.',              'personal opinion',           'The soup is delicious.',       '"Sabrosa" expresses how the soup tastes — a personal opinion about taste.'),
    ('Ella está hermosa hoy.',             'personal opinion',           'She is pretty today.',         '"Hermosa hoy" expresses how she looks right now — a personal opinion about appearance.'),
    ('Él está guapo.',                     'personal opinion',           'He is handsome.',              '"Guapo" expresses how he looks — a personal opinion about appearance.'),
]

for sent, use, translation, why in USE_SENTENCES:
    wrong_uses = [u for u in USES if u != use]
    Q(tier='intermediate', type='multiple_choice', category='estar_concept', topic='estar_uses',
      question=f'"{sent}" — estar expresses…',
      options=sh([use] + wrong_uses), answer=use,
      explanation=f'"{sent}" ({translation}). {why}')
    # Why question
    wrong_why_uses = [u for u in USES if u != use]
    Q(tier='intermediate', type='multiple_choice', category='estar_concept', topic='estar_uses',
      question=f'"{sent}" — why does this use "estar" for {use}?',
      options=sh([why,
                  f'Because "{sent.split()[1] if len(sent.split())>1 else sent}" describes a permanent identity',
                  'Because it is an action verb',
                  'Because the subject is plural']),
      answer=why,
      explanation=why)

# ══════════════════════════════════════════════════════════════
#  SECTION 4 — EXERCISE 2.1 STYLE: FORM + USE + REASON
# ══════════════════════════════════════════════════════════════

EX21 = [
    # (sentence_with_blank, correct_form, use_category, form_reason, use_reason)
    ('Daniel ___ muy cansado hoy.',
     'está', 'changing mood or condition',
     '3rd person singular — Daniel is one person (él)',
     '"Cansado" is a temporary physical state, not a permanent trait'),
    ('El teléfono y el libro ___ en la mesa.',
     'están', 'location',
     '3rd person plural — two things joined by "y" make a plural subject',
     'The sentence tells WHERE the phone and book are — location'),
    ('La mujer ___ bien, el hombre ___ enfermo.',
     'está', 'health',
     '3rd person singular — each subject (la mujer, el hombre) is singular',
     '"Bien" and "enfermo" both describe physical wellbeing — health'),
    ('¿Cómo ___ Uds.?',
     'están', 'health',
     '3rd person plural — "Uds." (ustedes) is always treated as 3rd person plural',
     'Asking how someone feels uses "estar" for health'),
    ('¿Dónde ___ ellos?',
     'están', 'location',
     '3rd person plural — "ellos" is plural',
     '"¿Dónde?" asks about location — where they are'),
    ('¿Dónde ___ el baño, por favor?',
     'está', 'location',
     '3rd person singular — "el baño" is singular',
     '"¿Dónde?" asks about location — where the bathroom is'),
    ('El niño ___ enojado y la niña ___ triste.',
     'está', 'changing mood or condition',
     '3rd person singular — each subject (el niño, la niña) is singular',
     '"Enojado" and "triste" are temporary emotional states — mood/condition'),
    ('Los muchachos ___ alegres.',
     'están', 'changing mood or condition',
     '3rd person plural — "los muchachos" is plural',
     '"Alegre" is a temporary emotional state — mood/condition'),
    ('Yo ___ contento.',
     'estoy', 'changing mood or condition',
     '1st person singular — "yo" always takes "estoy"',
     '"Contento" is a temporary feeling, not a permanent personality trait'),
    ('¿Quién ___ aquí?',
     'está', 'location',
     '3rd person singular — "¿Quién?" is treated as singular by default',
     '"Aquí" (here) indicates location — the question asks who is present somewhere'),
    ('El pescado ___ delicioso.',
     'está', 'personal opinion',
     '3rd person singular — "el pescado" is singular',
     '"Delicioso" expresses how the fish tastes right now — a personal opinion'),
    ('Nosotros ___ en el tren.',
     'estamos', 'location',
     '1st person plural — "nosotros" takes "estamos"',
     'The sentence tells WHERE we are — location'),
    ('Tú ___ cansado después del trabajo.',
     'estás', 'changing mood or condition',
     '2nd person singular — "tú" takes "estás"',
     '"Cansado" after work is a temporary physical state — condition'),
    ('Usted ___ en el hospital.',
     'está', 'location',
     '3rd person singular — "usted" is treated as 3rd person singular',
     'The sentence tells WHERE you are — location'),
    ('Ella ___ hermosa hoy.',
     'está', 'personal opinion',
     '3rd person singular — "ella" is singular',
     '"Hermosa hoy" expresses how she looks right now — personal opinion about appearance'),
]

for sent, form, use, form_reason, use_reason in EX21:
    wrong_forms = [c[1] for c in CONJ if c[1] != form]
    wrong_uses  = [u for u in USES if u != use]
    wrong_form_reasons = [c[3] for c in CONJ if c[3] != form_reason]

    Q(tier='intermediate', type='multiple_choice', category='estar_application', topic='estar_uses',
      question=f'Fill in the blank: "{sent.replace("___","______")}" — which form of estar?',
      options=pool(form, wrong_forms), answer=form,
      explanation=f'{sent.replace("___", form)} — {form_reason}.')

    Q(tier='intermediate', type='multiple_choice', category='estar_application', topic='estar_uses',
      question=f'"{sent.replace("___", form)}" — this sentence uses estar to express…',
      options=sh([use] + wrong_uses), answer=use,
      explanation=f'{use_reason}.')

    Q(tier='advanced', type='multiple_choice', category='estar_application', topic='estar_uses',
      question=f'"{sent.replace("___","______")}" — why do we use "{form}" here?',
      options=pool(form_reason, wrong_form_reasons + ['Because the sentence is negative', 'Because the adjective ends in -o']),
      answer=form_reason,
      explanation=f'We use "{form}" because: {form_reason}.')

    Q(tier='advanced', type='multiple_choice', category='estar_application', topic='estar_uses',
      question=f'"{sent.replace("___", form)}" — why does this use estar for {use}?',
      options=sh([use_reason,
                  'Because the adjective is masculine',
                  'Because the subject is permanent',
                  'Because "ser" is used for actions']),
      answer=use_reason,
      explanation=use_reason)

# ══════════════════════════════════════════════════════════════
#  SECTION 5 — ADJECTIVE VOCABULARY + CATEGORY
# ══════════════════════════════════════════════════════════════

ADJS = [
    ('alegre',    'happy (merry)',      'alegre',    'alegres',    'changing mood or condition'),
    ('bonito',    'pretty',            'bonita',    'bonitos',    'personal opinion'),
    ('bueno',     'good',              'buena',     'buenos',     'personal opinion'),
    ('cansado',   'tired',             'cansada',   'cansados',   'changing mood or condition'),
    ('contento',  'happy (contented)', 'contenta',  'contentos',  'changing mood or condition'),
    ('delicioso', 'delicious',         'deliciosa', 'deliciosos', 'personal opinion'),
    ('enfermo',   'sick',              'enferma',   'enfermos',   'health'),
    ('enojado',   'angry',             'enojada',   'enojados',   'changing mood or condition'),
    ('feliz',     'happy',             'feliz',     'felices',    'changing mood or condition'),
    ('guapo',     'handsome',          'guapa',     'guapos',     'personal opinion'),
    ('hermoso',   'beautiful',         'hermosa',   'hermosos',   'personal opinion'),
    ('lindo',     'pretty',            'linda',     'lindos',     'personal opinion'),
    ('sabroso',   'delicious',         'sabrosa',   'sabrosos',   'personal opinion'),
]

ADJ_CATEGORY_WHY = {
    'alegre':    '"Alegre" (merry/happy) is a temporary emotional state.',
    'bonito':    '"Bonito" (pretty) expresses a subjective opinion about appearance.',
    'bueno':     '"Bueno" with estar expresses how something tastes or feels right now — a personal opinion.',
    'cansado':   '"Cansado" (tired) is a temporary physical state — it comes and goes.',
    'contento':  '"Contento" (contented/happy) is a temporary feeling, not a permanent personality trait.',
    'delicioso': '"Delicioso" expresses how something tastes — a subjective personal opinion.',
    'enfermo':   '"Enfermo" (sick) describes a temporary physical condition — health.',
    'enojado':   '"Enojado" (angry) is a temporary emotional state — mood.',
    'feliz':     '"Feliz" (happy) is a temporary emotional state — mood.',
    'guapo':     '"Guapo" (handsome) expresses how someone looks right now — personal opinion about appearance.',
    'hermoso':   '"Hermoso" (beautiful) expresses how someone/something looks — personal opinion.',
    'lindo':     '"Lindo" (pretty) expresses a subjective opinion about appearance.',
    'sabroso':   '"Sabroso" (delicious) expresses how something tastes — personal opinion.',
}

for masc, en, fem, pl, cat in ADJS:
    wrong_en  = [a[1] for a in ADJS if a[1] != en]
    wrong_es  = [a[0] for a in ADJS if a[0] != masc]
    wrong_cat = [u for u in USES if u != cat]

    Q(tier='beginner', type='multiple_choice', category='adjective_vocabulary', topic='adjectives',
      question=f'What does the adjective "{masc}" mean?',
      options=pool(en, wrong_en), answer=en,
      explanation=f'"{masc}" = {en}')

    Q(tier='beginner', type='multiple_choice', category='adjective_vocabulary', topic='adjectives',
      question=f'What is the Spanish adjective for "{en}"?',
      options=pool(masc, wrong_es), answer=masc,
      explanation=f'"{en}" = "{masc}"')

    Q(tier='intermediate', type='multiple_choice', category='estar_concept', topic='estar_uses',
      question=f'When you use "estar" with "{masc}", which category of estar usage does it represent?',
      options=sh([cat] + wrong_cat), answer=cat,
      explanation=ADJ_CATEGORY_WHY[masc])

    Q(tier='intermediate', type='multiple_choice', category='estar_concept', topic='estar_uses',
      question=f'Why does "{masc}" use "estar" rather than "ser"?',
      options=sh([ADJ_CATEGORY_WHY[masc],
                  f'Because "{masc}" is a permanent, unchanging trait',
                  f'Because "{masc}" is a nationality or origin',
                  f'Because "{masc}" only applies to places']),
      answer=ADJ_CATEGORY_WHY[masc],
      explanation=ADJ_CATEGORY_WHY[masc])

    # Feminine form
    if fem != masc:
        wrong_fem = [a[2] for a in ADJS if a[2] != fem and a[2] != masc]
        Q(tier='intermediate', type='multiple_choice', category='adjective_agreement', topic='adjectives',
          question=f'What is the feminine form of "{masc}"?',
          options=pool(fem, wrong_fem), answer=fem,
          explanation=f'"{masc}" (m.) → "{fem}" (f.) — adjectives ending in -o change to -a.')

    # Plural
    wrong_pl = [a[3] for a in ADJS if a[3] != pl]
    note = ' (feliz → felices: z → c before -es)' if masc == 'feliz' else ''
    Q(tier='intermediate', type='multiple_choice', category='adjective_agreement', topic='adjectives',
      question=f'What is the plural form of "{masc}"?',
      options=pool(pl, wrong_pl), answer=pl,
      explanation=f'"{masc}" → "{pl}" (plural){note}.')

# Agreement in sentences
AGREE = [
    ('El hombre está ___.',      'cansado',   'tired (m.sg)',      ['cansada','cansados','cansadas']),
    ('La mujer está ___.',       'cansada',   'tired (f.sg)',      ['cansado','cansados','cansadas']),
    ('La muchacha está ___.',    'contenta',  'happy (f.sg)',      ['contento','contentos','contentas']),
    ('El muchacho está ___.',    'contento',  'happy (m.sg)',      ['contenta','contentos','contentas']),
    ('La doctora está ___.',     'enferma',   'sick (f.sg)',       ['enfermo','enfermos','enfermas']),
    ('El doctor está ___.',      'enfermo',   'sick (m.sg)',       ['enferma','enfermos','enfermas']),
    ('La chica está ___.',       'enojada',   'angry (f.sg)',      ['enojado','enojados','enojadas']),
    ('El chico está ___.',       'enojado',   'angry (m.sg)',      ['enojada','enojados','enojadas']),
    ('Ella está ___.',           'feliz',     'happy (f.sg)',      ['felices','feliz','alegre']),
    ('Él está ___.',             'guapo',     'handsome (m.sg)',   ['guapa','guapos','guapas']),
    ('La comida está ___.',      'buena',     'good (f.sg)',       ['bueno','buenos','buenas']),
    ('El pescado está ___.',     'delicioso', 'delicious (m.sg)',  ['deliciosa','deliciosos','deliciosas']),
    ('La sopa está ___.',        'sabrosa',   'delicious (f.sg)',  ['sabroso','sabrosos','sabrosas']),
    ('Los hombres están ___.',   'cansados',  'tired (m.pl)',      ['cansado','cansada','cansadas']),
    ('Las mujeres están ___.',   'cansadas',  'tired (f.pl)',      ['cansado','cansada','cansados']),
    ('Estamos ___.',             'alegres',   'happy (pl)',        ['alegre','alegro','alegros']),
    ('Los doctores están ___.',  'enfermos',  'sick (m.pl)',       ['enfermo','enferma','enfermas']),
    ('Ella está ___ hoy.',       'hermosa',   'beautiful (f.sg)',  ['hermoso','hermosos','hermosas']),
]

for sent, correct, hint, wrongs in AGREE:
    opts = sh([correct] + wrongs[:3])
    Q(tier='intermediate', type='multiple_choice', category='adjective_agreement', topic='adjectives',
      question=f'Choose the correct form: "{sent}"',
      options=opts, answer=correct,
      explanation=f'{sent.replace("___", correct)} — {hint}: adjectives must agree in gender and number with the subject.')

# ══════════════════════════════════════════════════════════════
#  SECTION 6 — QUESTION WORDS & LOCATION WORDS
# ══════════════════════════════════════════════════════════════

QWS = [
    ('¿Cómo?',      'how?',   'question_words'),
    ('¿Dónde?',     'where?', 'question_words'),
    ('¿Quién?',     'who?',   'question_words'),
    ('aquí / acá',  'here',   'location_words'),
    ('allí / allá', 'there',  'location_words'),
]
for es, en, topic in QWS:
    wrong_en = [q[1] for q in QWS if q[1] != en]
    wrong_es = [q[0] for q in QWS if q[0] != es]
    Q(tier='beginner', type='multiple_choice', category='noun_vocabulary', topic=topic,
      question=f'What does "{es}" mean?',
      options=pool(en, wrong_en + ['what?','when?','why?','over there']), answer=en,
      explanation=f'"{es}" = {en}')
    Q(tier='beginner', type='multiple_choice', category='noun_vocabulary', topic=topic,
      question=f'What is the Spanish for "{en}"?',
      options=pool(es, wrong_es + ['¿Por qué?','¿Cuándo?','acá']), answer=es,
      explanation=f'"{en}" = "{es}"')

# Question word + estar usage
Q(tier='intermediate', type='multiple_choice', category='estar_concept', topic='estar_uses',
  question='"¿Dónde está el baño?" — which use of estar does this sentence show?',
  options=sh(USES), answer='location',
  explanation='"¿Dónde?" asks about location. "Está" (3rd person singular) because "el baño" is singular.')
Q(tier='intermediate', type='multiple_choice', category='estar_concept', topic='estar_uses',
  question='"¿Cómo estás tú?" — which use of estar does this sentence show?',
  options=sh(USES), answer='health',
  explanation='"¿Cómo estás?" asks about someone\'s wellbeing — health/condition.')
Q(tier='intermediate', type='multiple_choice', category='estar_concept', topic='estar_uses',
  question='"¿Quién está aquí?" — why do we use "está" and not "están"?',
  options=sh(['Because "¿Quién?" is treated as singular by default',
              'Because "aquí" requires singular',
              'Because the sentence is a question',
              'Because "estar" never uses "están" with question words']),
  answer='Because "¿Quién?" is treated as singular by default',
  explanation='"¿Quién?" (who?) is grammatically treated as 3rd person singular, so it uses "está".')

# ══════════════════════════════════════════════════════════════
#  SECTION 7 — TRANSLATIONS (EXERCISE 2.2 STYLE)
# ══════════════════════════════════════════════════════════════

TRANS_ES_EN = [
    ('Yo estoy bien, gracias.',             'I am fine, thanks.',                'estar_verb'),
    ('Ella está enferma.',                   'She is sick.',                      'estar_verb'),
    ('Los doctores están enfermos.',         'The doctors are sick.',             'estar_verb'),
    ('¿Cómo están Uds.?',                   'How are you all?',                  'estar_verb'),
    ('Estamos bien.',                        'We are well.',                      'estar_verb'),
    ('La muchacha está contenta.',           'The girl is happy.',                'adjectives'),
    ('Los hombres están cansados.',          'The men are tired.',                'adjectives'),
    ('Estamos alegres.',                     'We are happy.',                     'adjectives'),
    ('¿Estás enojado?',                     'Are you angry?',                    'adjectives'),
    ('La comida está buena.',                'The meal is good.',                 'adjectives'),
    ('El pescado está delicioso.',           'The fish is delicious.',            'adjectives'),
    ('La sopa está sabrosa.',               'The soup is delicious.',            'adjectives'),
    ('Ella está hermosa hoy.',               'She is pretty today.',              'adjectives'),
    ('Él está guapo.',                       'He is handsome.',                   'adjectives'),
    ('Nosotros estamos en el carro.',        'We are in the car.',                'estar_verb'),
    ('El restaurante está en la ciudad.',    'The restaurant is in the city.',    'estar_verb'),
    ('Ellas están en el baño.',              'They are in the bathroom.',         'estar_verb'),
    ('¿Estás tú en el hospital?',           'Are you in the hospital?',          'estar_verb'),
    ('Estoy feliz.',                         'I am happy.',                       'adjectives'),
    ('Daniel está muy cansado hoy.',         'Daniel is very tired today.',       'estar_verb'),
    ('El teléfono y el libro están en la mesa.', 'The phone and the book are on the table.', 'estar_verb'),
]
for es, en, topic in TRANS_ES_EN:
    Q(tier='intermediate', type='fill_blank', category='translation', topic=topic,
      question=f'Translate to English: "{es}"',
      answer=en, explanation=f'"{es}" = "{en}"')

TRANS_EN_ES = [
    ('I am fine, thanks.',               'Yo estoy bien, gracias.',            'estar_verb'),
    ('She is sick.',                     'Ella está enferma.',                  'estar_verb'),
    ('We are in the car.',               'Nosotros estamos en el carro.',       'estar_verb'),
    ('The girl is happy.',               'La muchacha está contenta.',          'adjectives'),
    ('The men are tired.',               'Los hombres están cansados.',         'adjectives'),
    ('Are you angry?',                   '¿Estás enojado?',                    'adjectives'),
    ('The meal is good.',                'La comida está buena.',               'adjectives'),
    ('He is handsome.',                  'Él está guapo.',                      'adjectives'),
    ('I am happy.',                      'Estoy feliz.',                        'adjectives'),
    ('How are you all?',                 '¿Cómo están Uds.?',                  'estar_verb'),
    ('I am in the yellow house.',        'Yo estoy en la casa amarilla.',       'estar_verb'),
    ('The white flower is in the window.','La flor blanca está en la ventana.','estar_verb'),
    ('We are in the train.',             'Nosotros estamos en el tren.',        'estar_verb'),
    ('I am fine, thanks.',               'Estoy bien, gracias.',                'estar_verb'),
    ('The red blouses are in the store.','Las blusas rojas están en la tienda.','estar_verb'),
]
for en, es, topic in TRANS_EN_ES:
    Q(tier='intermediate', type='fill_blank', category='translation', topic=topic,
      question=f'Translate to Spanish: "{en}"',
      answer=es, explanation=f'"{en}" = "{es}"')

# ══════════════════════════════════════════════════════════════
#  OUTPUT
# ══════════════════════════════════════════════════════════════

print(f'Total questions: {len(qs)}')

# Count by category
from collections import Counter
cats = Counter(q['category'] for q in qs)
for cat, n in cats.most_common():
    print(f'  {cat}: {n}')

ch2 = {
    'id': 'ch2',
    'title': 'Chapter 2 — The Verb Estar',
    'description': 'Subject pronouns, the verb estar, adjectives of condition, and the four uses of estar',
    'study': {
        'wordExamples': {
            'yo':       [{'es': 'Yo estoy en la clase.', 'en': 'I am in the class.'}],
            'tú':       [{'es': '¿Cómo estás tú?', 'en': 'How are you?'}],
            'él':       [{'es': 'Él está cansado.', 'en': 'He is tired.'}],
            'ella':     [{'es': 'Ella está enferma.', 'en': 'She is sick.'}],
            'usted':    [{'es': 'Usted está en el hospital.', 'en': 'You are in the hospital.'}],
            'nosotros': [{'es': 'Nosotros estamos bien.', 'en': 'We are fine.'}],
            'vosotros': [{'es': 'Vosotros estáis alegres.', 'en': 'You all are happy.'}],
            'ellos':    [{'es': 'Ellos están cansados.', 'en': 'They are tired.'}],
            'ellas':    [{'es': 'Ellas están en el baño.', 'en': 'They are in the bathroom.'}],
            'ustedes':  [{'es': '¿Cómo están ustedes?', 'en': 'How are you all?'}],
            'estoy':    [{'es': 'Yo estoy feliz hoy.', 'en': 'I am happy today.'}],
            'estás':    [{'es': '¿Estás enojado?', 'en': 'Are you angry?'}],
            'está':     [{'es': 'El restaurante está en la ciudad.', 'en': 'The restaurant is in the city.'}],
            'estamos':  [{'es': 'Nosotros estamos en el carro.', 'en': 'We are in the car.'}],
            'estáis':   [{'es': 'Vosotros estáis contentos.', 'en': 'You all are content.'}],
            'están':    [{'es': 'Los doctores están enfermos.', 'en': 'The doctors are sick.'}],
            '¿Cómo?':   [{'es': '¿Cómo estás?', 'en': 'How are you?'}],
            '¿Dónde?':  [{'es': '¿Dónde está el baño?', 'en': 'Where is the bathroom?'}],
            '¿Quién?':  [{'es': '¿Quién está aquí?', 'en': 'Who is here?'}],
            'aquí / acá':  [{'es': 'Yo estoy aquí.', 'en': 'I am here.'}],
            'allí / allá': [{'es': 'El perro está allí.', 'en': 'The dog is there.'}],
            'alegre':    [{'es': 'Estamos alegres hoy.', 'en': 'We are happy today.'}],
            'bonito':    [{'es': 'La flor está bonita.', 'en': 'The flower is pretty.'}],
            'bueno':     [{'es': 'La comida está buena.', 'en': 'The meal is good.'}],
            'cansado':   [{'es': 'El hombre está cansado.', 'en': 'The man is tired.'}],
            'contento':  [{'es': 'Yo estoy contento hoy.', 'en': 'I am content today.'}],
            'delicioso': [{'es': 'El pescado está delicioso.', 'en': 'The fish is delicious.'}],
            'enfermo':   [{'es': 'Ella está enferma.', 'en': 'She is sick.'}],
            'enojado':   [{'es': 'El niño está enojado.', 'en': 'The boy is angry.'}],
            'feliz':     [{'es': 'Estoy feliz hoy.', 'en': 'I am happy today.'}],
            'guapo':     [{'es': 'Él está guapo hoy.', 'en': 'He is handsome today.'}],
            'hermoso':   [{'es': 'Ella está hermosa hoy.', 'en': 'She is beautiful today.'}],
            'lindo':     [{'es': 'La ciudad está linda.', 'en': 'The city looks pretty.'}],
            'sabroso':   [{'es': 'La sopa está sabrosa.', 'en': 'The soup is delicious.'}],
        }
    },
    'questions': qs,
}

with open('data/ch2.json', 'w', encoding='utf-8') as f:
    json.dump(ch2, f, ensure_ascii=False, indent=2)
print('Wrote data/ch2.json')
