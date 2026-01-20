import streamlit as st
import pandas as pd

# --- KONFIGURATION & REZEPT ---
# Hier definierst du den Namen des Gerichts
gericht_name = "Raclette Mengen"

# Hier definierst du die Zutaten pro EINER Person
# Format: "Zutat": [Menge, "Einheit"]
basis_mengen = {
    "Kartoffel": [150, "g"],
    "Faschiertes": [80, "g"],
    "Fleisch (Rind+Huhn)": [180, "g"],
    "Gnocchi": [70, "g"],
    "Spatzl": [50, "g"],
    "Mais": [20, "g"],
    "Datteln (+Speck dazu)": [30, "g"],
    "Käse": [3, "Scheiben"],
    "Zucchini": "",
    "Paprika": "",
    "Champignons": "",
    "Saucen": "",
    "Pesto": "",
    "Salate": "",
    "Spatzlkäse": "",
    "Tomaten": "",
    "Mozzarella (kleine Bällchen)": "",
    "Tortilla Chips": "",
    "Jalapenos": ""
}

# --- APP LAYOUT ---
st.set_page_config(page_title="Mengenrechner", page_icon="🍳")

st.title(f"🍳 {gericht_name} - Rechner")
st.write("Wähle die Anzahl der Personen aus, um die Einkaufsliste zu berechnen.")

# --- EINGABE ---
# Ein Schieberegler für die Anzahl der Personen (Standardwert: 4)
personen = st.slider("Wie viele Personen essen mit?", min_value=1, max_value=20, value=6)

st.write("---")

# --- BERECHNUNG ---
berechnete_zutaten = []

for zutat, details in basis_mengen.items():
    if type(details) == list:
        menge_pro_person = details[0]
        einheit = details[1]
    
        # Die eigentliche Mathe-Magie
        total_menge = menge_pro_person * personen
        total_menge_str = f"{int(total_menge)}"
    else:
        total_menge_str = f''
        einheit = f''
        
    berechnete_zutaten.append({
        "Zutat": zutat,
        "Menge": total_menge_str,
        "Einheit": einheit
    })

# --- AUSGABE ---
# Umwandeln in einen schönen DataFrame (Tabelle) für die Anzeige
df = pd.DataFrame(berechnete_zutaten)

# Tabelle anzeigen (ohne Index-Nummern links)
st.subheader(f"Einkaufsliste für {personen} Personen:")
st.table(df)

# Optional: Ein Button zum "Drucken" (simuliert)
st.info("💡 Tipp: Mache einen Screenshot dieser Liste oder kopiere sie.")