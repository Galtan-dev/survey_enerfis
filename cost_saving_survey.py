import streamlit as st

st.title("Dotazník pro energetická opatření")


# opatření: výměna starých svítidel za úsporná
st.header("1. Použití LED svítidel")
col1a, col2a, col3a = st.columns(3)

with col1a:
    q1 = st.radio("Používají se úsporná svítidla?", ["Ano", "Ne"], key="q1")

with col2a:
    q2 = st.radio("Je osvětlení v provozu více než 4 h denně?", ["Ano", "Ne"], key="q2")

with col3a:
    q3 = st.radio("Je osvětlení původní (starší 10 let)?", ["Ano", "Ne"], key="q3")

if q1 == "Ne" and q2 == "Ano" and q3 == "Ano":
    st.success("Na základě odpovědí doporučujeme posoudit výměnu za LED.")
    # Inicializace
    if "led_fields" not in st.session_state:
        st.session_state.led_fields = 1

    # Tlačítka vedle sebe
    col_add, col_remove = st.columns([1, 1])

    with col_add:
        if st.button("➕ Přidat další svítidlo"):
            st.session_state.led_fields += 1

    with col_remove:
        if st.button("➖ Odebrat poslední svítidlo"):
            if st.session_state.led_fields > 1:
                st.session_state.led_fields -= 1

    # Výpis všech sad vstupních polí
    for i in range(st.session_state.led_fields):
        col1a, col2a, col3a = st.columns(3)
        with col1a:
            #st.text_input("Typ svítidla", key=f"room_{i}")
            st.selectbox("Vyber typ svítidla", ["wolfram_60W", "wolfram_100W", "wolfram_40W"], key=f"svitidla_{i}")
        with col2a:
            st.text_input("Počet svítidel", key=f"lights_{i}")
        with col3a:
            st.text_input("Doba svícení za rok", key=f"hodin_{i}")
else:
    st.info("Na základě odpovědí není toto opatření pravděpodobně relevantní.")


# opatření: instalace stínících prvků
st.header("2. Instalace stínících prvků")
col1b, col2b, col3b = st.columns(3)

with col1b:
    q1_b = st.radio("Dochází během slunečních dnů k přehřívání místnosti", ["Ano", "Ne"], key="q1_b")

with col2b:
    q2_b = st.radio("Obsahuje místnost větší mnořství oken?", ["Ano", "Ne"], key="q2_b")

with col3b:
    q3_b = st.radio("Je místnost vystavena  přímému slunečnímu svitu", ["Ano", "Ne"], key="q3_b")

if q1_b == "Ano" and q2_b == "Ano" and q3_b == "Ano":
    st.success("Na základě odpovědí doporučujeme posoudit instalaci stínících prvků.")
    # Inicializace
    if "shade_fields" not in st.session_state:
        st.session_state.shade_fields = 1

    # Tlačítka vedle sebe
    col_add, col_remove = st.columns([1, 1])

    with col_add:
        if st.button("➕ Přidat další sadu oken"):
            st.session_state.shade_fields += 1

    with col_remove:
        if st.button("➖ Odebrat poslední sadu oken"):
            if st.session_state.shade_fields > 1:
                st.session_state.shade_fields -= 1

    # Výpis všech sad vstupních polí
    for i in range(st.session_state.shade_fields):
        col1b, col2b, col3b = st.columns(3)
        with col1b:
            #st.text_input("Typ svítidla", key=f"room_{i}")
            st.selectbox("Vyber žádaný typ stínidla", ["Exteriérové žaluzie", "Interiérové žaluzie", "Slunolamy", "Polopropustné fólie"], key=f"stínidlo_{i}")
        with col2b:
            st.text_input("Zadejte plochu oken pro zastínění [m2]", key=f"okna_plocha_{i}")
        with col3b:
            st.text_input("Roční spotřeba energie na chlazení [KWh]", key=f"cool_consump__{i}")
else:
    st.info("Na základě odpovědí není toto opatření pravděpodobně relevantní.")