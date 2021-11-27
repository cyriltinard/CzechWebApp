import random

pronouns = ["já", "ty", "on/ona", "my", "vy", "oni"]

#nakupovat =  ["nakupovat", "nakupuju", "nakupuješ", "nakupuje", "nakupujeme", "nakupujete", "nakupují", "to shop"]
vařit = {
    "infinitiv": "vařit",
    "present": ["vařím", "vaříš", "vaří", "vaříme", "vaříte", "vaří"],
    "translation": "to cook"
}

nakupovat = {
    "infinitiv": "nakupovat",
    "present": ["nakupuju", "nakupuješ", "nakupuje", "nakupujeme", "nakupujete", "nakupují"],
    "translation": "to shop"
}

plavat = {
    "infinitiv": "plavat",
    "present": ["plavu", "plaveš", "plave", "plaveme", "plavete", "plavou"],
    "translation": "to swim"
}

verbs = [nakupovat, vařit, plavat]

ChosenVerb = random.choice(verbs) #chooses random verb
ChosenPronoun = random.choice(pronouns) #chooses random pronoun
ConjugatedForm = ChosenVerb['present'][pronouns.index(ChosenPronoun)]

print(ChosenPronoun, ConjugatedForm, "("+ChosenVerb['infinitiv']+")")


