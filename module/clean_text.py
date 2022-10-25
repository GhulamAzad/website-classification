import en_core_web_sm
import spacy as sp

sp.prefer_gpu()
# anconda prompt ko run as adminstrator and copy paste this:python -m spacy download en
nlp = en_core_web_sm.load()


def clean_text(doc):
    '''
    Clean the document. Remove pronouns, stopwords, lemmatize the words and lowercase them
    '''
    doc = nlp(doc)
    tokens = []
    exclusion_list = ["nan"]
    for token in doc:
        if token.is_stop or token.is_punct or token.text.isnumeric() or (token.text.isalnum() == False) or token.text in exclusion_list:
            continue
        token = str(token.lemma_.lower().strip())
        tokens.append(token)
    return " ".join(tokens)
