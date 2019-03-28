from pymystem3 import Mystem
from pymorphy2 import MorphAnalyzer
pm = MorphAnalyzer()
m = Mystem()

def lemmatize(text, mystem=m):
    try:
        return "".join(m.lemmatize(text)).strip()
    except:
        return []

def lemmatize2(text):
    lemmas = []
    NOUN_count = 0
    for word in text.split():
        l = pm.parse(word)
        if(l[0].tag.POS == 'NOUN'):
            NOUN_count += 1
        lemmas.append(l[0].normal_form.strip())
    return lemmas, NOUN_count