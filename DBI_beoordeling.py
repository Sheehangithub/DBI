import streamlit as st
import pandas as pd


# Functie om de feedback en cijfer te genereren op basis van de rubric
def get_feedback_and_grade(criterion, level):
    feedback_rubric = {
        "Analyseren - Informatie verzamelen en interpreteren": {
            "Onvoldoende (4)": "De student verzamelt beperkte en deels incorrecte informatie. De interpretatie is oppervlakkig en niet alle relevante aspecten van de bedrijfscontext worden geïdentificeerd.",
            "Voldoende (6)": "De student verzamelt voldoende relevante informatie over de bedrijfscontext, maar mist diepgang. De interpretatie is correct, maar standaard.",
            "Goed (8)": "De student verzamelt en interpreteert op systematische wijze relevante informatie, toont een goed begrip van de bedrijfscontext en identificeert de belangrijkste stakeholders.",
            "Zeer Goed (9)": "De student verzamelt en interpreteert zeer grondig en systematisch informatie, toont diepgaand inzicht in de context en brengt complexe relaties tussen stakeholders helder in kaart.",
            "Uitstekend (10)": "De student identificeert en interpreteert excellent en proactief alle relevante informatie, toont een uitzonderlijk diepgaand inzicht in de context en de dynamiek tussen stakeholders, en legt verbanden die niet voor de hand liggen."
        },
        "Analyseren - Requirements analyse": {
            "Onvoldoende (4)": "De requirements zijn onvolledig, vaag en/of niet meetbaar (non-SMART). Er wordt geen duidelijk onderscheid gemaakt tussen functionele en niet-functionele eisen.",
            "Voldoende (6)": "De student stelt meetbare (SMART) requirements op, maar deze zijn niet volledig dekkend voor het probleem. Het onderscheid tussen functioneel en niet-functioneel is aanwezig maar niet altijd consistent.",
            "Goed (8)": "De student stelt een dekkende set van SMART requirements op voor de oplossing, met een duidelijk en correct onderscheid tussen functionele en niet-functionele eisen.",
            "Zeer Goed (9)": "De student stelt een zeer complete en scherpe set van SMART requirements op en prioriteert deze op basis van duidelijke argumenten (bijv. MoSCoW), volledig afgestemd op de bedrijfsdoelen.",
            "Uitstekend (10)": "De student stelt een exceptioneel complete en inzichtelijke set van SMART requirements op, inclusief prioritering en validatie bij stakeholders, die de basis legt voor een superieure oplossing."
        },
        "Adviseren - Conclusies trekken": {
            "Onvoldoende (4)": "De conclusies zijn niet logisch, niet onderbouwd door de analyse en bieden geen helder antwoord op de centrale vraag.",
            "Voldoende (6)": "De student trekt logische conclusies die voortvloeien uit de analyse, maar deze zijn voorspelbaar en missen diepgang.",
            "Goed (8)": "De student trekt logische, scherpe en goed onderbouwde conclusies die een helder antwoord geven op de centrale vraag.",
            "Zeer Goed (9)": "De student trekt zeer scherpe en inzichtelijke conclusies, legt complexe verbanden en beantwoordt de centrale vraag op een overtuigende en genuanceerde manier.",
            "Uitstekend (10)": "De student trekt exceptioneel scherpe en vernieuwende conclusies, toont diepgaand synthetisch vermogen en formuleert een antwoord dat het probleem overstijgt."
        },
        "Adviseren - Oplossingsrichtingen en advies": {
            "Onvoldoende (4)": "Het advies is niet passend, niet haalbaar of onvoldoende onderbouwd. Er is geen duidelijke afweging van alternatieven.",
            "Voldoende (6)": "De student werkt enkele passende oplossingsrichtingen uit en geeft een haalbaar, onderbouwd advies. De afweging van alternatieven is summier.",
            "Goed (8)": "De student werkt meerdere relevante oplossingsrichtingen uit, weegt deze systematisch af en komt tot een overtuigend en goed onderbouwd advies.",
            "Zeer Goed (9)": "De student ontwikkelt creatieve en relevante oplossingsrichtingen, weegt deze af met een scherp oog voor impact en haalbaarheid, en presenteert een zeer overtuigend advies.",
            "Uitstekend (10)": "De student ontwikkelt innovatieve oplossingsrichtingen, weegt deze af met een strategische visie en levert een excellent, direct toepasbaar advies met duidelijke meerwaarde."
        },
        "Ontwerpen - Conceptueel en logisch ontwerp": {
            "Onvoldoende (4)": "Het ontwerp is onvolledig, inconsistent, of sluit niet aan bij de requirements. Modellen (indien gebruikt) zijn incorrect of onduidelijk.",
            "Voldoende (6)": "De student maakt een werkbaar conceptueel/logisch ontwerp dat de requirements grotendeels dekt, maar mist detail en elegantie.",
            "Goed (8)": "De student maakt een consistent, goed gedocumenteerd en passend conceptueel/logisch ontwerp dat volledig aansluit op de requirements.",
            "Zeer Goed (9)": "De student maakt een zeer elegant, efficiënt en goed doordacht ontwerp dat niet alleen de requirements dekt, maar ook anticipeert op toekomstige ontwikkelingen.",
            "Uitstekend (10)": "De student levert een exceptioneel, innovatief en robuust ontwerp dat een schoolvoorbeeld is van goede ontwerpprincipes en optimaal aansluit op de bedrijfscontext."
        },
        "Realiseren - Proof of Concept (PoC)": {
            "Onvoldoende (4)": "De PoC werkt niet of demonstreert de kernfunctionaliteit niet. De gebruikte technologie is niet passend of de code is van zeer lage kwaliteit.",
            "Voldoende (6)": "De student levert een werkende PoC die de haalbaarheid van de kern van het advies aantoont. De realisatie is functioneel, maar niet optimaal.",
            "Goed (8)": "De student levert een goed werkende en representatieve PoC die de kern van het advies overtuigend aantoont. De code is van voldoende kwaliteit.",
            "Zeer Goed (9)": "De student levert een zeer overtuigende en technisch nette PoC die niet alleen de haalbaarheid aantoont, maar ook de potentie van de oplossing laat zien.",
            "Uitstekend (10)": "De student levert een indrukwekkende, technisch hoogstaande PoC die de haalbaarheid en meerwaarde van het advies onomstotelijk bewijst."
        },
        "Manage & Control - Projectplanning en -uitvoering": {
            "Onvoldoende (4)": "De planning is onrealistisch en wordt niet gevolgd. De projectuitvoering is chaotisch en de communicatie is slecht.",
            "Voldoende (6)": "De student maakt een realistische planning en houdt de voortgang bij. De uitvoering is adequaat, maar er is weinig aandacht voor risicobeheersing.",
            "Goed (8)": "De student maakt een gedegen projectplan (incl. risico's) en stuurt de uitvoering effectief bij. De communicatie is helder en proactief.",
            "Zeer Goed (9)": "De student managet het project zeer professioneel met een scherp oog voor planning, risico's en kwaliteit. De uitvoering is efficiënt en de communicatie is uitstekend.",
            "Uitstekend (10)": "De student toont excellent projectmanagement, anticipeert proactief op alle mogelijke issues en leidt het project op een inspirerende en uiterst effectieve wijze."
        },
        "Professionele Vaardigheden - Communicatie en samenwerking": {
            "Onvoldoende (4)": "De communicatie (schriftelijk en mondeling) is onduidelijk en niet professioneel. De samenwerking in de groep is slecht en de student levert geen constructieve bijdrage.",
            "Voldoende (6)": "De communicatie is helder en de student toont een professionele basishouding. De student is een betrouwbaar teamlid en voert taken uit.",
            "Goed (8)": "De student communiceert professioneel en overtuigend, en levert een actieve en constructieve bijdrage aan het teamresultaat.",
            "Zeer Goed (9)": "De student is een zeer sterke communicator die anderen kan motiveren. De student neemt een proactieve en leidende rol in de samenwerking en verbetert het teamproces.",
            "Uitstekend (10)": "De student is een excellente en inspirerende communicator en een drijvende kracht in het team. De student tilt het team naar een hoger niveau en lost conflicten constructief op."
        }
    }

    grade_map = {
        "Onvoldoende (4)": 4, "Voldoende (6)": 6, "Goed (8)": 8,
        "Zeer Goed (9)": 9, "Uitstekend (10)": 10
    }

    return feedback_rubric.get(criterion, {}).get(level, ""), grade_map.get(level, 0)


# --- App Layout ---
st.set_page_config(layout="wide", page_title="DBI Beoordelingsapp")

st.title("Beoordelingsapp: DBI Change in Action (BIMMIC30R3)")
st.markdown("---")

# Sidebar voor groepsselectie en studentnamen
with st.sidebar:
    st.header("Instellingen")
    group_selection = st.selectbox("Kies een groep", [f"Groep {i}" for i in range(1, 17)])

    st.subheader(f"Studenten in {group_selection}")
    student_names = [st.text_input(f"Naam Student {i + 1}", key=f"s{i}_{group_selection}") for i in range(4)]

# Initialiseer session state
if 'beoordeling' not in st.session_state:
    st.session_state.beoordeling = {}

# Hoofd-layout met de rubric
st.header(f"Rubric voor {group_selection}")
st.write("Selecteer per criterium de beoordeling. De feedback en het eindcijfer worden automatisch berekend.")

# Definieer de rubric structuur
rubric_structure = {
    "Analyseren (Weging 20%)": ["Analyseren - Informatie verzamelen en interpreteren",
                                "Analyseren - Requirements analyse"],
    "Adviseren (Weging 20%)": ["Adviseren - Conclusies trekken", "Adviseren - Oplossingsrichtingen en advies"],
    "Ontwerpen (Weging 15%)": ["Ontwerpen - Conceptueel en logisch ontwerp"],
    "Realiseren (Weging 15%)": ["Realiseren - Proof of Concept (PoC)"],
    "Manage & Control (Weging 15%)": ["Manage & Control - Projectplanning en -uitvoering"],
    "Professionele Vaardigheden (Weging 15%)": ["Professionele Vaardigheden - Communicatie en samenwerking"]
}

weging = {
    "Analyseren - Informatie verzamelen en interpreteren": 0.10,
    "Analyseren - Requirements analyse": 0.10,
    "Adviseren - Conclusies trekken": 0.10,
    "Adviseren - Oplossingsrichtingen en advies": 0.10,
    "Ontwerpen - Conceptueel en logisch ontwerp": 0.15,
    "Realiseren - Proof of Concept (PoC)": 0.15,
    "Manage & Control - Projectplanning en -uitvoering": 0.15,
    "Professionele Vaardigheden - Communicatie en samenwerking": 0.15
}

options = ["Onvoldoende (4)", "Voldoende (6)", "Goed (8)", "Zeer Goed (9)", "Uitstekend (10)"]
final_feedback_text = ""
total_grade = 0.0
all_grades = {}

for main_criterion, sub_criteria in rubric_structure.items():
    st.subheader(main_criterion)
    for sub_criterion in sub_criteria:
        # Unieke key voor elk widget
        widget_key = f"{group_selection}_{sub_criterion}"

        # Huidige selectie ophalen of default instellen
        current_selection = st.session_state.beoordeling.get(widget_key, "Voldoende (6)")

        selected_level = st.selectbox(
            label=sub_criterion.split(" - ")[1],
            options=options,
            index=options.index(current_selection),  # set default
            key=f"select_{widget_key}"
        )

        # Update de state
        st.session_state.beoordeling[widget_key] = selected_level

        # Feedback en cijfer ophalen
        feedback, grade = get_feedback_and_grade(sub_criterion, selected_level)
        st.info(f"Feedback: {feedback}")

        # Voeg toe aan eindfeedback en berekening
        if grade >= 4:
            final_feedback_text += f"**{sub_criterion.split(' - ')[1]}**:\n{feedback}\n\n"
            total_grade += grade * weging[sub_criterion]
            all_grades[sub_criterion.split(" - ")[1]] = grade

# --- Eindbeoordeling en export ---
st.markdown("---")
st.header("Eindbeoordeling")

# Bereken eindcijfer
final_grade_rounded = round(total_grade, 1)

col1, col2 = st.columns(2)

with col1:
    st.subheader("Berekend Eindcijfer")
    # Toon cijfer met kleur
    if final_grade_rounded < 5.5:
        st.error(f"**{final_grade_rounded}**")
    else:
        st.success(f"**{final_grade_rounded}**")

with col2:
    st.subheader("Cijfers per onderdeel")
    # Toon dataframe met cijfers per onderdeel
    df_grades = pd.DataFrame(list(all_grades.items()), columns=['Onderdeel', 'Cijfer'])
    st.dataframe(df_grades.set_index('Onderdeel'))

st.subheader("Samengestelde Eindfeedback")
feedback_area = st.text_area("Feedback (je kunt hier nog aanpassingen doen)", final_feedback_text, height=300)

# --- NIEUW: Downloadknop ---
st.subheader("Download de beoordeling")

# Maak de output string voor het tekstbestand
# Gebruik de (mogelijk aangepaste) tekst uit de feedback_area
admin_output = f"""
Beoordeling voor: {group_selection}
Studenten: {', '.join(filter(None, student_names))}
Eindcijfer: {final_grade_rounded}
---
Samenvatting cijfers:
{df_grades.to_string(index=False)}
---
Feedback:
{feedback_area}
"""

# Dynamische bestandsnaam gebaseerd op de geselecteerde groep
file_name = f"Beoordeling_{group_selection.replace(' ', '_')}.txt"

st.download_button(
    label="Download beoordeling als .txt",
    data=admin_output,
    file_name=file_name,
    mime="text/plain"
)

st.info("Klik op de knop hierboven om de volledige beoordeling als een tekstbestand lokaal op te slaan.")

# De oude st.code is nu vervangen door de download knop en is niet meer nodig.