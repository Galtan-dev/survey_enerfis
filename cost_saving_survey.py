import streamlit as st

st.title("Dotazník pro energetická opatření")

# === 1. Použití LED svítidel ===
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
    if "led_fields" not in st.session_state:
        st.session_state.led_fields = 1

    col_add, col_remove = st.columns(2)
    with col_add:
        if st.button("➕ Přidat další svítidlo"):
            st.session_state.led_fields += 1
    with col_remove:
        if st.button("➖ Odebrat poslední svítidlo") and st.session_state.led_fields > 1:
            st.session_state.led_fields -= 1

    for i in range(st.session_state.led_fields):
        col1a, col2a, col3a = st.columns(3)
        with col1a:
            st.selectbox("Vyber typ svítidla", ["wolfram_60W", "wolfram_100W", "wolfram_40W"], key=f"svitidla_{i}")
        with col2a:
            st.text_input("Počet svítidel", key=f"lights_{i}")
        with col3a:
            st.text_input("Doba svícení za rok", key=f"hodin_{i}")
else:
    st.info("Na základě odpovědí není toto opatření pravděpodobně relevantní.")

# === 2. Instalace stínících prvků ===
st.header("2. Instalace stínících prvků")
col1b, col2b, col3b = st.columns(3)
with col1b:
    q1_b = st.radio("Dochází během slunečních dnů k přehřívání místnosti", ["Ano", "Ne"], key="q1_b")
with col2b:
    q2_b = st.radio("Obsahuje místnost větší množství oken?", ["Ano", "Ne"], key="q2_b")
with col3b:
    q3_b = st.radio("Je místnost vystavena přímému slunečnímu svitu", ["Ano", "Ne"], key="q3_b")

if q1_b == "Ano" and q2_b == "Ano" and q3_b == "Ano":
    st.success("Na základě odpovědí doporučujeme posoudit instalaci stínících prvků.")
    if "shade_fields" not in st.session_state:
        st.session_state.shade_fields = 1

    col_add, col_remove = st.columns(2)
    with col_add:
        if st.button("➕ Přidat další sadu oken"):
            st.session_state.shade_fields += 1
    with col_remove:
        if st.button("➖ Odebrat poslední sadu oken") and st.session_state.shade_fields > 1:
            st.session_state.shade_fields -= 1

    for i in range(st.session_state.shade_fields):
        col1b, col2b, col3b = st.columns(3)
        with col1b:
            st.selectbox("Vyber žádaný typ stínidla", ["Exteriérové žaluzie", "Interiérové žaluzie", "Slunolamy", "Polopropustné fólie"], key=f"stínidlo_{i}")
        with col2b:
            st.text_input("Plocha oken pro zastínění [m2]", key=f"okna_plocha_{i}")
        with col3b:
            st.text_input("Roční spotřeba energie na chlazení [kWh]", key=f"cool_consump_{i}")
else:
    st.info("Na základě odpovědí není toto opatření pravděpodobně relevantní.")

# === 3. Výměna radiátorových hlavic ===
st.header("3. Výměna radiátorových hlavic")
col1c, col2c, col3c = st.columns(3)
with col1c:
    q1_c = st.radio("Instalované hlavice jsou mechanické (ne termostatické)?", ["Ano", "Ne"], key="q1_c")
with col2c:
    q2_c = st.radio("Dochází k přetápění místností? (i o jednotky stupňů)", ["Ano", "Ne"], key="q2_c")
with col3c:
    q3_c = st.radio("Je budova ústředně vytápěna?", ["Ano", "Ne"], key="q3_c")

if q1_c == "Ano" and q2_c == "Ano" and q3_c == "Ano":
    st.success("Na základě odpovědí doporučujeme výměnu hlavic.")
    typy = st.multiselect("Zvolte typ nových hlavic:", ["termostaticka", "smart"])
    for typ in typy:
        col1, col2 = st.columns(2)
        with col1:
            st.number_input(f"Počet hlavic typu {typ}", min_value=0, key=f"hlavice_pocet_{typ}")
    st.number_input("Teplota interiéru [°C] (střední hodnota)", value=22.5, key="ti_stred")
    st.number_input("Požadovaná teplota [°C]", value=20.0, key="tpozadovana")
    st.slider("Odhad doby s přetápěním (v % času jak dlouho je v místnosti větší teplota než nastavená)", min_value=0.0, max_value=1.0, step=0.05, value=0.6, key="casove_pokryti")
    st.number_input("Roční spotřeba tepla [kWh]", min_value=0.0, key="spotreba_tepla")
else:
    st.info("Tato sekce není na základě odpovědí relevantní.")

# === 4. Senzory pohybu na světla ===
st.header("4. Instalace senzorů pohybu na osvětlení")
col1d, col2d, col3d = st.columns(3)
with col1d:
    q1_d = st.radio("Dochází ke zbytečnému svícení ve společných prostorách (chodby, kuchyňky, ...?", ["Ano", "Ne"], key="q1_d")
with col2d:
    q2_d = st.radio("Nejsou místnosti aktuálně vybaveny senzory?", ["Ano", "Ne"], key="q2_d")
with col3d:
    q3_d = st.radio("Je osvětlení řízeno ručně nebo časovačem?", ["Ano", "Ne"], key="q3_d")

if q1_d == "Ano" and q2_d == "Ano" and q3_d == "Ano":
    st.success("Na základě odpovědí doporučujeme zvážit instalaci senzorů pohybu.")
    if "sensor_fields" not in st.session_state:
        st.session_state.sensor_fields = 1

    col_add, col_remove = st.columns(2)
    with col_add:
        if st.button("➕ Přidat místnost se senzory"):
            st.session_state.sensor_fields += 1
    with col_remove:
        if st.button("➖ Odebrat poslední místnost") and st.session_state.sensor_fields > 1:
            st.session_state.sensor_fields -= 1

    for i in range(st.session_state.sensor_fields):
        col1d, col2d, col3d = st.columns(3)
        with col1d:
            st.text_input("Název místnosti", key=f"sensor_mistnost_{i}")
        with col2d:
            st.number_input("Instalovaný výkon svítidel [kW]", min_value=0.0, key=f"sensor_vykon_{i}")
        with col3d:
            st.number_input("Odhad původní doby svícení za rok [h]", min_value=0, key=f"sensor_doba_{i}")
        col4d, col5d, col6d = st.columns(3)
        with col4d:
            st.number_input("Počet zaměstnanců", min_value=0, key=f"sensor_zam_{i}")
        with col5d:
            st.number_input("Počet pracovních dnů v roce", min_value=0, key=f"sensor_dny_{i}")
        with col6d:
            st.number_input("Počet senzorů v místnosti", min_value=0, key=f"sensor_pocet_{i}")
        st.markdown("---")
else:
    st.info("Tato sekce není relevantní.")

# === 5. Izolace potrubí ===
st.header("5. Izolace potrubí pro chlazení/topení")
col1e, col2e, col3e = st.columns(3)
with col1e:
    q1_e = st.radio("Jsou části potrubí vedeny v netemperovaných prostorách?", ["Ano", "Ne"], key="q1_e")
with col2e:
    q2_e = st.radio("Je izolace stará, poškozená nebo zcela chybí?", ["Ano", "Ne"], key="q2_e")
with col3e:
    q3_e = st.radio("Je médium v potrubí významně teplejší nebo chladnější než okolí?", ["Ano", "Ne"], key="q3_e")

if q1_e == "Ano" and q2_e == "Ano" and q3_e == "Ano":
    st.success("Na základě odpovědí doporučujeme zlepšit izolaci potrubí.")
    if "pipe_fields" not in st.session_state:
        st.session_state.pipe_fields = 1

    col_add, col_remove = st.columns(2)
    with col_add:
        if st.button("➕ Přidat větev potrubí"):
            st.session_state.pipe_fields += 1
    with col_remove:
        if st.button("➖ Odebrat poslední větev") and st.session_state.pipe_fields > 1:
            st.session_state.pipe_fields -= 1

    for i in range(st.session_state.pipe_fields):
        col1e, col2e, col3e, col4e = st.columns(4)
        with col1e:
            st.text_input("Název větve", key=f"pipe_nazev_{i}")
        with col2e:
            st.number_input("Délka potrubí [m]", min_value=0.0, key=f"pipe_delka_{i}")
        with col3e:
            st.number_input("Provozní hodiny za rok [h]", min_value=0, key=f"pipe_hodiny_{i}")
        with col4e:
            st.number_input("Tloušťka potrubí [m]", min_value=0, key=f"d_potrubi_{i}")
        col5e, col6e, col7e= st.columns(3)
        with col5e:
            st.text_input("Teplota média [°C]", key=f"medium_temp_{i}")
        with col6e:
            st.number_input("Teplota okolí [°C]", min_value=0.0, key=f"okoli_temp_{i}")
        with col7e:
            st.selectbox("Materiál", ["ocel", "měď", "plast"], key=f"material_{i}")
        st.markdown("---")


else:
    st.info("Tato sekce není relevantní.")
