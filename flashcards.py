#!/usr/bin/env python3

from sys import stdin

all_cards = {
    'italian_dynamics': {
        'Estinto': 'As quiet as possible',
        'Fortepiano': 'Loud then immediately soft',
        'Calando': 'Getting softer / dying away',
        'Morendo': 'Dying away',
        'Niente': 'Nothing ( = silence )',
        'Perdendosi': 'Dying away',
        'Smorzando': 'Dying away in tone and speed',
        'Crescendo (cresc.)': 'Gradually getting louder',
        'Decrescendo (decresc.)': 'Gradually getting softer',
        'Diminuendo (dim.)': 'Gradually getting softer',
        'Forte (f)': 'Loud',
        'Mezzo forte (mf)': 'Moderately loud',
        'Fortissimo (ff)': 'Very loud',
        'Fortississimo (fff)': 'Extremely loud',
        'Piano (p)': 'Soft',
        'Mezzo piano (mp)': 'Moderately soft',
        'Pianissimo': 'Very soft',
        'Pianississimo': 'Extremely soft',
    },
    'italian_tempo': {
        'Tempo': 'time',
        'A tempo': 'in time',
        'Misura': 'measure',
        'Alla misura': 'in strict time',
        'Rubato': 'with freedom of time',
        'Senza misura': 'in free time',
        'Adagio': 'slowly',
        'Adagietto': 'rather slow',
        'Largo': 'slow and stately',
        'Larghetto': 'rather slow',
        'Lento': 'slow',
        'Grave': 'very slow and solemn',
        'Alla breve': 'with a minim beat',
        'Lunga pausa': 'long pause',
        'Allargando': 'broadening',
        'Rallentando (rall.)': 'gradually getting slower',
        'Ritardando (rit.)': 'gradually getting slower',
        'Ritenuto (rit.)': 'gradually getting slower',
        'Smorzando': 'dying away in tone and speed',
        'Andante': 'at a walking pace',
        'Andantino': 'slightly faster than andante',
        'Comodo': 'comfortably',
        'Moderato': 'At a moderate speed',
        'Allegro': 'fast',
        'Allegro assai': 'very fast',
        'Allegro moderato': 'moderately fast',
        'Allegretto': 'fairly quick',
        'Presto': 'very fast',
        'Vivace': 'lively and quick',
        'Vivo': 'lively and quick',
        'Tosto': 'swift, rapid',
        'Volante': 'flying, quick',
        'Agitato': 'agitated',
        'Doppio movimento': 'twice as fast',
        'Affrettando': 'hurrying',
        'Incalzando': 'getting quicker',
        'Stringendo': 'gradually getting faster',
        'Accelerando': 'getting faster',
    },
    'french_tempo': {
        'Lent': 'slow',
        'Cédez': 'yield, relax the speed',
        'Ralentir': 'slow down',
        'En retenant': 'holding back',
        'Retenu': 'held back',
        'Modéré': 'moderate speed',
        'Presser': 'hurry',
        'En pressant': 'hurrying',
        'Vite': 'quick',
        'Vif': 'lively',
    },
    'german_tempo': {
        'Langsam': 'slow',
        'Mässig': 'at a moderate speed',
        'Lebhaft': 'lively',
        'Schnell': 'fast',
        'Bewegt': 'with movement, agitated',
    },
    'italian_articulation': {
        'Sforzando': 'forced, accented',
        'Sforzato': 'forced, accented',
        'Tenuto': 'held for the full value',
        'Forza': 'force',
        'Marcato': 'emphatic, accented',
        'Staccato': 'short and detached',
        'Staccaissimo': 'very short and detached',
    },
    'italian_expression': {
        'Delicato': 'delicately',
        'Dolce': 'sweetly',
        'Semplice': 'simply',
        'Amabile': 'pleasant',
        'Piacevole': 'pleasant',
        'Grazioso': 'graceful',
        'Tranquillo': 'calm',
        'Giocoso': 'playful',
        'Scherzando': 'playfully, joking',
        'Amore': 'love',
        'Amoroso': 'loving',
        'Affettuoso': 'tenderly, affectionately',
        'Teneramente': 'tenderly',
        'Tenerezza': 'tenderly',
        'Appassionato': 'passionately',
        'Anima': 'spirit',
        'Fuoco': 'fire',
        'Animando': 'becoming more lively',
        'Animato': 'animated, lively',
        'Lusingando': 'coaxing',
        'Brio': 'vigour',
        'Energico': 'energetically',
        'Deciso': 'with determination',
        'Nobilmente': 'nobly',
        'Maestoso': 'majestically',
        'Risoluto': 'bold, strong',
        'Marziale': 'in a military style',
        'Cantabile': 'in a singing style',
        'Cantando': 'singing',
        'Sonoro': 'resonant, with a rich tone',
        'Dolente': 'sad, mournful',
        'Dolore': 'grief',
        'Doloroso': 'sorrowful',
        'Lacrimoso': 'sadly',
        'Mesto': 'sad',
        'Piangevole': 'plaintive, like a lament',
        'Tristamento': 'sadly',
        'Triste': 'sad',
        'Espressivo': 'expressive',
        'Largamente': 'broadly',
        'Sostenuto': 'sustained',
        'Legato': 'smoothly',
        'Leggiero': 'lightly, nimbly',
        'Pesante': 'heavy',
        'Rinforzando': 'reinforcing',
        'Ritmico': 'rhythmically',
    },
    'french_german_expression': {
        'Animé': 'animated',
        'Douce': 'sweetly',
        'En dehors': 'prominent',
        'Légèrement': 'lightly',
        'Breit': 'broad, expansive',
        'Fröhlich': 'cheerful, joyful',
        'Ruhig': 'peaceful',
        'Süss': 'sweet',
        'Traurig': 'sad',
        'Zart': 'tender, delicate',
    },
    'other_italian': {
        'Al, alla': 'in the style of',
        'Assai': 'very',
        'Ben': 'well',
        'Come': 'as, similar to',
        'Con, col': 'with',
        'E, ed': 'and',
        'Facile': 'easy',
        'Giusto': 'proper, exact',
        'Ma': 'but',
        'Meno': 'less',
        'Mezzo': 'half / moderately',
        'Molto': 'extremely',
        'Mosso': 'movement',
        'Non': 'not',
        'Ossia': 'or, alternatively',
        'Più': 'more',
        'Pochettino': 'rather little',
        'Poco': 'a little',
        'Possible': 'possible',
        'Primo, prima': 'first',
        'Quasi': 'as if, resembling',
        'Secondo, seconda': 'second',
        'Sempre': 'always',
        'Senza': 'without',
        'Simile (sim.)': 'in the same way',
        'Sopra': 'above',
        'Sotto': 'below',
        'Subito': 'suddenly',
        'Tanta': 'so much',
        'Troppo': 'too much',
        'Voce': 'voice',
    },
    'other_french': {
        'Assez': 'enough',
        'Avec': 'with',
        'Et': 'and',
        'Mais': 'but',
        'Moins': 'less',
        'Non': 'not',
        'Peu': 'little',
        'Plus': 'more',
        'Sans': 'without',
        'Très': 'very',
        'Un, Une': 'one',
    },
    'other_german': {
        'Aber': 'but',
        'Ausdruck': 'expression',
        'Ein': 'one',
        'Einfach': 'simple',
        'Etwas': 'somewhat, rather',
        'Immer': 'always',
        'Mit': 'with',
        'Nicht': 'not',
        'Ohne': 'without',
        'Sehr': 'very',
        'Und': 'and',
        'Voll': 'full',
        'Wenig': 'little',
        'Wieder': 'again',
        'Zu': 'to, too',
    }
}

def test_loop(category):
    cards = all_cards[category]
    incorrect = [ word for word in cards ]
    attempt = 0
    while incorrect:
        print("Attempt %s" % attempt)
        incorrect_this_time = []
        for word in incorrect:
            print('\n%s' % word)
            stdin.readline()
            print(cards[word])
            print('\nCorrect?')
            answer = stdin.readline()[0]
            if answer not in ('y', 'Y'):
                incorrect_this_time.append(word)
        incorrect = incorrect_this_time
        attempt += 1

    print("All correct!")


def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('category')
    args = parser.parse_args()
    test_loop(args.category)

if __name__ == '__main__':
    import sys
    sys.exit(main())
