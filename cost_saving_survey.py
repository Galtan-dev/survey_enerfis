import streamlit as st

st.title("Dotazník pro energetická opatření")

# 1. LED osvětlení
st.header("1. Použití LED světel")

use_led = st.radio("Používají se stále žárovky nebo zářivky?", ["Ano", "Ne"])
if use_led == "Ano":
    pocet_svitidel = st.number_input("Počet svítidel", min_value=0)
    prikon = st.number_input("Příkon na svítidlo [W]", min_value=0)
    hodiny = st.number_input("Doba svícení za den [h]", min_value=0.0)
    dny = st.number_input("Počet dní v týdnu", min_value=1, max_value=7)

# 2. Stínění
st.header("2. Stínění oken")
prehrivani = st.radio("Dochází v létě k přehřívání?", ["Ano", "Ne"])
okna_orientace = st.radio("Jsou okna orientována na jih/jihovýchod?", ["Ano", "Ne"])

if prehrivani == "Ano" and okna_orientace == "Ano":
    plocha = st.number_input("Plocha oken [m²]", min_value=0.0)
    sklo = st.text_input("Typ skla")
    stineni = st.text_input("Typ stínění (žaluzie, fólie...)")

# tlačítko pro výstup
if st.button("Spočítej efektivitu"):
    st.success("Tady bude výstup podle výpočtů skriptu!")
