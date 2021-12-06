import random
import streamlit as st

pronouns = ["já", "ty", "on/ona", "my", "vy", "oni"]

#nakupovat =  ["nakupovat", "nakupuju", "nakupuješ", "nakupuje", "nakupujeme", "nakupujete", "nakupují", "to shop"]
vařit = {
    "infinitiv": "vařit",
    "present": ["vařím", "vaříš", "vaří", "vaříme", "vaříte", "vaří"],
    "past": ["vařil jsem", "vařil jsi", "vařil/vařila", "vařili jsme", "vařili jste", "vařili"],
    "future": ["budu vařit", "budeš vařit", "bude vařit", "budeme vařit", "budete vařit", "budou vařit"],
    "translation": "to cook"
}

nakupovat = {
    "infinitiv": "nakupovat",
    "present": ["nakupuju", "nakupuješ", "nakupuje", "nakupujeme", "nakupujete", "nakupují"],
    "past": ["nakupoval jsem", "nakupoval jsi", "nakupoval/nakupovala", "nakupovali jsme", "nakupovali jste", "nakupovali"],
    "future": ["budu nakupovat", "budeš nakupovat", "bude nakupovat", "budeme nakupovat", "budete nakupovat", "budou nakupovat"],
    "translation": "to shop"
}

plavat = {
    "infinitiv": "plavat",
    "present": ["plavu", "plaveš", "plave", "plaveme", "plavete", "plavou"],
    "past": ["plaval jsem", "plaval jsi", "plaval/plavala", "plavali jsme", "plavali jste", "plavali"],
    "future": ["budu plavat", "budeš plavat", "bude plavat", "budeme plavat", "budete plavat", "budou plavat"],
    "translation": "to swim"
}

verbs = [nakupovat, vařit, plavat]

if 'answer' not in st.session_state:
    st.session_state.answer = "answer_0"

ChosenVerb = ""
if 'ChosenVerb' not in st.session_state:
    st.session_state.ChosenVerb = "0"

ChosenPronoun = ""
if 'ChosenPronoun' not in st.session_state:
    st.session_state.ChosenPronoun = "0"

ConjugatedForm = ""
if 'ConjugatedForm' not in st.session_state:
    st.session_state.ConjugatedForm = "0"

Tense = ""
if 'Tense' not in st.session_state:
    st.session_state.Tense = "present"

def ChooseEx(Tense):
    ChosenVerb = random.choice(verbs) #chooses random verb
    ChosenPronoun = random.choice(pronouns) #chooses random pronoun
    ConjugatedForm = ChosenVerb[Tense][pronouns.index(ChosenPronoun)]
    # elif Tense == "past":
    #     ConjugatedForm = ChosenVerb[Tense][pronouns.index(ChosenPronoun)]
    # elif:
    #     ConjugatedForm = ChosenVerb[Tense][pronouns.index(ChosenPronoun)]
    # else:
        
    print(ChosenPronoun, ConjugatedForm, "("+ChosenVerb['infinitiv']+")")
    st.session_state.ChosenVerb = ChosenVerb
    st.session_state.ChosenPronoun = ChosenPronoun
    st.session_state.ConjugatedForm = ConjugatedForm
    return ChosenVerb, ChosenPronoun, ConjugatedForm
    
def VerifyAnswer(answer, ConjugatedForm):
    if st.session_state.answer == st.session_state.ConjugatedForm:
        result = '<p style="font-family:sans-serif; color:Green; font-size: 32px;">Correct</p>'
        st.markdown(result, unsafe_allow_html=True)
        #st.text("Correct")
    else:
        result = '<p style="font-family:sans-serif; color:Red; font-size: 32px;">Wrong</p>'
        st.markdown(result, unsafe_allow_html=True)
        st.text("Correct answer: " + st.session_state.ChosenPronoun + " " + st.session_state.ConjugatedForm)
        # st.text("False, " + st.session_state.ChosenPronoun + " " + st.session_state.ConjugatedForm)

st.header("Czech Practice")

Tense = st.selectbox("Selected Symbol:", ['present','past','future','mixed'], key='Tense')
if Tense == "mixed":
    Tense = random.choice(["present", "past", "future"])

start = st.button('Start')
if start:
    ChooseEx(Tense)
    st.text("Complete:")
    st.text(str(st.session_state.ChosenPronoun) + " (" + str(st.session_state.ChosenVerb['infinitiv']) + ")" + " - " + Tense)
    answer = st.text_input("", key='answer')

if st.button('Check answer'):
    VerifyAnswer(st.session_state.answer, st.session_state.ConjugatedForm)
    st.write("Your answer :", st.session_state.ChosenPronoun, st.session_state.answer, " (", st.session_state.ChosenVerb['translation'], ")")

# streamlit run c:\Users\cyril\Documents\Python\CzechWebApp\CzechWebApp.py  
