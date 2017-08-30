# Traitement à appliquer à toutes les strings avant comparaison
# (simplifications des caractères spéciaux)

def cleanString(order):
    order = order.strip('?!').replace("-", " ").replace("'", " ").lstrip().rstrip().lower()
    order = order.replace("â", "a").replace("ê", "e").replace("é", "e").replace("è", "e").replace("ù", "u").replace("à", "a").replace("ô", "o")

    return order

def cleanStringList(phrases):
    clean = []
    for i in phrases:
        clean.append(cleanString(i))
    return clean