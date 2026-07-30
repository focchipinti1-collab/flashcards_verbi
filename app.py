import random
 
import streamlit as st
 
# ==============================================================================
# CONFIGURAZIONE PAGINA
# ==============================================================================
st.set_page_config(
    page_title="Flashcards di Italiano 🇮🇹",
    page_icon="🇮🇹",
    layout="centered",
    initial_sidebar_state="expanded",
)
 
# ==============================================================================
# DATI DEI VERBI
# ==============================================================================
VERBI = [
    {"infinito": "Studiare", "gruppo": "1ª coniugazione (-are)", "io": "studio",
     "eng": "to study", "frase_it": "Ogni sera studio l'italiano.",
     "frase_en": "Every evening I study Italian.", "emoji": "📚✏️"},
    {"infinito": "Parlare", "gruppo": "1ª coniugazione (-are)", "io": "parlo",
     "eng": "to speak / to talk", "frase_it": "Parlo italiano e inglese.",
     "frase_en": "I speak Italian and English.", "emoji": "🗣️💬"},
    {"infinito": "Abitare", "gruppo": "1ª coniugazione (-are)", "io": "abito",
     "eng": "to live", "frase_it": "Abito in una piccola casa a Roma.",
     "frase_en": "I live in a small house in Rome.", "emoji": "🏠🔑","sinonimi": ["vivere"]},
    {"infinito": "Cantare", "gruppo": "1ª coniugazione (-are)", "io": "canto",
     "eng": "to sing", "frase_it": "Mi piace cantare sotto la doccia.",
     "frase_en": "I like singing in the shower.", "emoji": "🎤🎶"},
    {"infinito": "Suonare", "gruppo": "1ª coniugazione (-are)", "io": "suono",
     "eng": "to play (an instrument)", "frase_it": "Suono il pianoforte da cinque anni.",
     "frase_en": "I've played the piano for five years.", "emoji": "🎸🎹"},
    {"infinito": "Vivere", "gruppo": "2ª coniugazione (-ere)", "io": "vivo",
     "eng": "to live", "frase_it": "Vivo in Italia.",
     "frase_en": "I live in Italy.", "emoji": "🌍🏡","sinonimi": ["abitare"]},
    {"infinito": "Prendere", "gruppo": "2ª coniugazione (-ere)", "io": "prendo",
     "eng": "to take", "frase_it": "Prendo l'autobus per andare al lavoro.",
     "frase_en": "I take the bus to go to work.", "emoji": "🚌✋"},
    {"infinito": "Cucinare", "gruppo": "1ª coniugazione (-are)", "io": "cucino",
     "eng": "to cook", "frase_it": "La domenica cucino per tutta la famiglia.",
     "frase_en": "On Sundays I cook for the whole family.", "emoji": "👩‍🍳🍝"},
    {"infinito": "Mangiare", "gruppo": "1ª coniugazione (-are)", "io": "mangio",
     "eng": "to eat", "frase_it": "Mangio la pasta ogni giorno.",
     "frase_en": "I eat pasta every day.", "emoji": "🍕🍽️"},
    {"infinito": "Cercare", "gruppo": "1ª coniugazione (-are)⚠️VERBO IN -CARE = tu CERCHI/noi CERCHIAMO", "io": "cerco",
     "eng": "to look for / to search", "frase_it": "Cerco un buon ristorante in centro.",
     "frase_en": "I'm looking for a good restaurant downtown.", "emoji": "🔍🗺️"},
    {"infinito": "Lavorare", "gruppo": "1ª coniugazione (-are)", "io": "lavoro",
     "eng": "to work", "frase_it": "Lavoro in un ufficio a Milano.",
     "frase_en": "I work in an office in Milan.", "emoji": "💼⚙️"},
    {"infinito": "Scrivere", "gruppo": "2ª coniugazione (-ere)", "io": "scrivo",
     "eng": "to write", "frase_it": "Scrivo una email al mio professore.",
     "frase_en": "I'm writing an email to my professor.", "emoji": "✍️📝"},
    {"infinito": "Leggere", "gruppo": "2ª coniugazione (-ere)", "io": "leggo",
     "eng": "to read", "frase_it": "Leggo un libro prima di dormire.",
     "frase_en": "I read a book before sleeping.", "emoji": "📖👓"},
    {"infinito": "Vedere", "gruppo": "2ª coniugazione (-ere)", "io": "vedo",
     "eng": "to see", "frase_it": "Vedo il mare dalla finestra.",
     "frase_en": "I see the sea from the window.", "emoji": "👀"},
    {"infinito": "Chiedere", "gruppo": "2ª coniugazione (-ere)", "io": "chiedo",
     "eng": "to ask", "frase_it": "Chiedo scusa per il ritardo.",
     "frase_en": "I apologize for being late.", "emoji": "❓🙋"},
    {"infinito": "Credere", "gruppo": "2ª coniugazione (-ere)", "io": "credo",
     "eng": "to believe", "frase_it": "Credo che tu abbia ragione.",
     "frase_en": "I believe you're right.", "emoji": "💭"},
    {"infinito": "Vincere", "gruppo": "2ª coniugazione (-ere)", "io": "vinco",
     "eng": "to win", "frase_it": "La mia squadra vince sempre.",
     "frase_en": "My team always wins.", "emoji": "🏆🥇"},
    {"infinito": "Perdere", "gruppo": "2ª coniugazione (-ere)", "io": "perdo",
     "eng": "to lose", "frase_it": "Non voglio perdere il treno.",
     "frase_en": "I don't want to miss the train.", "emoji": "😔📉"},
    {"infinito": "Bere", "gruppo": "2ª coniugazione (irregolare!!)", "io": "bevo",
     "eng": "to drink", "frase_it": "Bevo un caffè ogni mattina.",
     "frase_en": "I drink a coffee every morning.", "emoji": "☕🥤"},
    {"infinito": "Dormire", "gruppo": "3ª coniugazione (-ire)", "io": "dormo",
     "eng": "to sleep", "frase_it": "Dormo otto ore ogni notte.",
     "frase_en": "I sleep eight hours every night.", "emoji": "😴🛏️"},
    {"infinito": "Preferire", "gruppo": "3ª coniugazione (-ire, -isc-)", "io": "preferisco",
     "eng": "to prefer", "frase_it": "Preferisco il mare alla montagna.",
     "frase_en": "I prefer the sea to the mountains.", "emoji": "⭐🏖️"},
    {"infinito": "Partire", "gruppo": "3ª coniugazione (-ire)", "io": "parto",
     "eng": "to leave / to depart", "frase_it": "Domani parto per Firenze.",
     "frase_en": "Tomorrow I'm leaving for Florence.", "emoji": "✈️🧳"},
    {"infinito": "Offrire", "gruppo": "3ª coniugazione (-ire)", "io": "offro",
     "eng": "to offer", "frase_it": "Offro io!",
     "frase_en": "It's on me!", "emoji": "🎁💰"},
    {"infinito": "Finire", "gruppo": "3ª coniugazione (-ire, -isc-)", "io": "finisco",
     "eng": "to finish", "frase_it": "Finisco i compiti alle sei.",
     "frase_en": "I finish my homework at six.", "emoji": "✅🏁"},
    {"infinito": "Capire", "gruppo": "3ª coniugazione (-ire, -isc-)", "io": "capisco",
     "eng": "to understand", "frase_it": "Non capisco questa parola.",
     "frase_en": "I don't understand this word.", "emoji": "💡🧠"},
]
N = len(VERBI)
 
# ==============================================================================
# STILE — TEMA ITALIA
# ==============================================================================
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;900&family=Quicksand:wght@400;500;600;700&display=swap');
 
    html, body, [class*="css"]  {
        font-family: 'Quicksand', sans-serif;
    }
 
    .stApp {
        background: radial-gradient(circle at 10% 10%, rgba(0,140,69,0.08), transparent 40%),
                    radial-gradient(circle at 90% 15%, rgba(205,33,42,0.08), transparent 40%),
                    radial-gradient(circle at 50% 100%, rgba(0,140,69,0.06), transparent 45%),
                    #FFFBF3;
    }
 
    .block-container {
        padding-top: 1.5rem;
        max-width: 760px;
    }
 
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
 
    .tricolore-bar {
        height: 7px;
        width: 100%;
        border-radius: 6px;
        background: linear-gradient(90deg, #008C45 0%, #008C45 33%, #F4F5F0 33%, #F4F5F0 66%, #CD212A 66%, #CD212A 100%);
        margin-bottom: 1.1rem;
        box-shadow: 0 2px 6px rgba(0,0,0,0.12);
    }
 
    .app-title {
        font-family: 'Playfair Display', serif;
        font-weight: 900;
        font-size: 2.5rem;
        text-align: center;
        background: linear-gradient(90deg, #008C45, #444444 50%, #CD212A);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.1rem;
    }
 
    .app-subtitle {
        text-align: center;
        color: #6b5b4d;
        font-size: 1.05rem;
        margin-bottom: 0.3rem;
    }
 
    .deco-row {
        text-align: center;
        font-size: 1.5rem;
        letter-spacing: 6px;
        margin-bottom: 1.4rem;
        opacity: 0.85;
    }
 
    .level-caption {
        text-align: center;
        color: #8a7a6a;
        font-size: 0.95rem;
        margin-bottom: 1rem;
        font-style: italic;
    }
 
    .flashcard {
        border-radius: 22px;
        padding: 2.2rem 1.6rem;
        min-height: 260px;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        text-align: center;
        box-shadow: 0 10px 28px rgba(80, 50, 30, 0.14);
        border: 1px solid rgba(0,0,0,0.05);
        position: relative;
        overflow: hidden;
        margin-bottom: 1.1rem;
    }
    .flashcard::before {
        content: "";
        position: absolute;
        top: 0; left: 0; right: 0;
        height: 8px;
    }
    .card-l1 { background: linear-gradient(160deg, #FFFFFF, #EAF6EE); }
    .card-l1::before { background: #008C45; }
    .card-l2 { background: linear-gradient(160deg, #FFFFFF, #FBF4E8); }
    .card-l2::before { background: #C9A227; }
    .card-l3 { background: linear-gradient(160deg, #FFFFFF, #FBEAEA); }
    .card-l3::before { background: #CD212A; }
 
    .badge {
        display: inline-block;
        padding: 0.2rem 0.8rem;
        border-radius: 999px;
        font-size: 0.78rem;
        font-weight: 700;
        letter-spacing: 0.5px;
        margin-bottom: 0.9rem;
        text-transform: uppercase;
    }
    .badge-green { background: rgba(0,140,69,0.12); color: #007037; }
    .badge-red { background: rgba(205,33,42,0.12); color: #A81824; }
    .badge-gold { background: rgba(201,162,39,0.15); color: #8a6d10; }
 
    .verb-word {
        font-family: 'Playfair Display', serif;
        font-weight: 900;
        font-size: 2.6rem;
        color: #2e2620;
        margin-bottom: 0.3rem;
    }
    .verb-emoji {
        font-size: 4.5rem;
        margin-bottom: 0.4rem;
        line-height: 1.1;
    }
    .verb-sub {
        font-size: 1.15rem;
        color: #6b5b4d;
    }
    .detail-line {
        font-size: 1.05rem;
        color: #4a3f34;
        margin: 0.25rem 0;
    }
    .detail-label {
        font-weight: 700;
        color: #008C45;
    }
    .example-box {
        margin-top: 0.9rem;
        padding-top: 0.8rem;
        border-top: 1px dashed rgba(0,0,0,0.15);
        font-size: 0.98rem;
        color: #55483c;
    }
 
    .progress-text {
        text-align: center;
        color: #8a7a6a;
        font-size: 0.9rem;
        margin-bottom: 0.6rem;
    }
 
    .stats-row {
        text-align: center;
        font-size: 0.9rem;
        color: #6b5b4d;
        margin-top: 0.3rem;
    }
 
    div.stButton > button {
        border-radius: 12px;
        border: none;
        font-weight: 700;
        padding: 0.5rem 0.6rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)
 
# ==============================================================================
# INTESTAZIONE
# ==============================================================================
st.markdown('<div class="tricolore-bar"></div>', unsafe_allow_html=True)
st.markdown('<div class="app-title">Flashcards di Italiano</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="app-subtitle">Impara i verbi italiani!</div>',
    unsafe_allow_html=True,
)
st.markdown('<div class="deco-row">🍕 🏛️ 🍋 🚲 🎭 🍷 🎶</div>', unsafe_allow_html=True)
 
# ==============================================================================
# STATO
# ==============================================================================
def init_state(prefix: str) -> None:
    st.session_state.setdefault(f"{prefix}_order", list(range(N)))
    st.session_state.setdefault(f"{prefix}_idx", 0)
    st.session_state.setdefault(f"{prefix}_show", False)
    st.session_state.setdefault(f"{prefix}_know", 0)
    st.session_state.setdefault(f"{prefix}_review", 0)
    st.session_state.setdefault(f"{prefix}_dirs", [True] * N)  # True = IT->EN
 
 
def shuffle_deck(prefix: str, randomize_dirs: bool = False) -> None:
    order = list(range(N))
    random.shuffle(order)
    st.session_state[f"{prefix}_order"] = order
    st.session_state[f"{prefix}_idx"] = 0
    st.session_state[f"{prefix}_show"] = False
    if randomize_dirs:
        st.session_state[f"{prefix}_dirs"] = [random.choice([True, False]) for _ in range(N)]
 
 
def go_next(prefix: str) -> None:
    st.session_state[f"{prefix}_idx"] = (st.session_state[f"{prefix}_idx"] + 1) % N
    st.session_state[f"{prefix}_show"] = False
 
 
def go_prev(prefix: str) -> None:
    st.session_state[f"{prefix}_idx"] = (st.session_state[f"{prefix}_idx"] - 1) % N
    st.session_state[f"{prefix}_show"] = False
 
 
def flip_card(prefix: str) -> None:
    st.session_state[f"{prefix}_show"] = not st.session_state[f"{prefix}_show"]
 
 
def mark_known(prefix: str) -> None:
    st.session_state[f"{prefix}_know"] += 1
    go_next(prefix)
 
 
def mark_review(prefix: str) -> None:
    st.session_state[f"{prefix}_review"] += 1
    go_next(prefix)
 
 
def current_verb(prefix: str) -> dict:
    order = st.session_state[f"{prefix}_order"]
    idx = st.session_state[f"{prefix}_idx"]
    return VERBI[order[idx]]
 
 
def render_footer_controls(prefix: str, show_score: bool = True) -> None:
    idx = st.session_state[f"{prefix}_idx"]
    st.markdown(
        f'<div class="progress-text">Carta {idx + 1} di {N}</div>',
        unsafe_allow_html=True,
    )
 
    c1, c2, c3 = st.columns([1, 1.4, 1])
    with c1:
        st.button("⬅️ Indietro", key=f"{prefix}_prev", use_container_width=True,
                   on_click=go_prev, args=(prefix,))
    with c2:
        label = "🙈 Nascondi risposta" if st.session_state[f"{prefix}_show"] else "🔄 Mostra risposta"
        st.button(label, key=f"{prefix}_flip", use_container_width=True,
                   on_click=flip_card, args=(prefix,))
    with c3:
        st.button("Avanti ➡️", key=f"{prefix}_next", use_container_width=True,
                   on_click=go_next, args=(prefix,))
 
    if show_score and st.session_state[f"{prefix}_show"]:
        s1, s2 = st.columns(2)
        with s1:
            st.button("✅ Lo so già", key=f"{prefix}_know_btn", use_container_width=True,
                       on_click=mark_known, args=(prefix,))
        with s2:
            st.button("🔁 Da ripassare", key=f"{prefix}_review_btn", use_container_width=True,
                       on_click=mark_review, args=(prefix,))
 
    st.button("🔀 Mescola le carte", key=f"{prefix}_shuffle", use_container_width=True,
               on_click=shuffle_deck, args=(prefix,))
 
    know = st.session_state[f"{prefix}_know"]
    review = st.session_state[f"{prefix}_review"]
    if know or review:
        st.markdown(
            f'<div class="stats-row">✅ Sapute: <b>{know}</b> &nbsp;·&nbsp; 🔁 Da ripassare: <b>{review}</b></div>',
            unsafe_allow_html=True,
        )
 
 
# ==============================================================================
# SIDEBAR
# ==============================================================================
with st.sidebar:
    st.markdown("### 🇮🇹 Guida rapida")
    st.markdown(
        """
- **Livello 1 — Scheda verbo**
  Infinito, gruppo, coniugazione (io), traduzione e frase d'esempio.
- **Livello 2 — Traduzione**
  Italiano ⇄ Inglese: indovina la traduzione.
- **Livello 3 — Immagini**
  Indovina il verbo dalle emoji/immagine.
        """
    )
    st.markdown("---")
    direzione = st.radio(
        "Livello 2:",
        ["🇮🇹 ➜ 🇬🇧 Italiano prima", "🇬🇧 ➜ 🇮🇹 Inglese prima", "🔀 Mista"],
        index=0,
    )
    st.markdown("---")
    if st.button("♻️ Azzera tutte le statistiche", use_container_width=True):
        for p in ["L1", "L2", "L3"]:
            st.session_state[f"{p}_know"] = 0
            st.session_state[f"{p}_review"] = 0
        st.rerun()
 
# ==============================================================================
# TAB DEI 3 LIVELLI
# ==============================================================================
tab1, tab2, tab3 = st.tabs(["📖 Livello 1", "🔤 Livello 2", "🖼️ Livello 3"])
 
# ------------------------------------------------------------------ LIVELLO 1
with tab1:
    init_state("L1")
    st.markdown(
        '<div class="level-caption">Scopri il significato dei verbi</div>',
        unsafe_allow_html=True,
    )
    v = current_verb("L1")

    if not st.session_state["L1_show"]:
        st.markdown(
            f"""
            <div class="flashcard card-l1">
                <div class="badge badge-green">{v['gruppo']}</div>
                <div class="verb-word">{v['infinito']}</div>
                <div class="verb-emoji">{v['emoji']}</div>
                <div class="verb-sub">👇</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    else:
        sinonimi_html = ""
        if v.get("sinonimi"):
            sinonimi_html = (
                f'<div class="detail-line"><span class="detail-label">Sinonimi:</span> '
                f'{", ".join(v["sinonimi"])}</div>'
            )
        st.markdown(
            f"""
            <div class="flashcard card-l1">
                <div class="badge badge-green">{v['gruppo']}</div>
                <div class="verb-word">{v['infinito']}</div>
                <div class="detail-line"><span class="detail-label">Traduzione:</span> {v['eng']}</div>
                <div class="detail-line"><span class="detail-label">Io</span> → {v['io']}</div>{sinonimi_html}
                <div class="example-box">
                    🇮🇹 {v['frase_it']}<br>
                    🇬🇧 {v['frase_en']}
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    render_footer_controls("L1")
 
# ------------------------------------------------------------------ LIVELLO 2
with tab2:
    init_state("L2")
    st.markdown(
        '<div class="level-caption">Indovina la traduzione, poi capovolgi la carta</div>',
        unsafe_allow_html=True,
    )
    v = current_verb("L2")
    idx2 = st.session_state["L2_idx"]
 
    if direzione.startswith("🇮🇹"):
        it_to_en = True
    elif direzione.startswith("🇬🇧"):
        it_to_en = False
    else:
        it_to_en = st.session_state["L2_dirs"][idx2]

    fronte = v["eng"] if it_to_en else v["infinito"]
    retro = v["infinito"] if it_to_en else v["eng"]
    bandiera_fronte = "🇬🇧" if it_to_en else "🇮🇹"
    bandiera_retro = "🇮🇹" if it_to_en else "🇬🇧"
 
    if not st.session_state["L2_show"]:
        st.markdown(
            f"""
            <div class="flashcard card-l2">
                <div class="badge badge-gold">{bandiera_fronte} Da tradurre</div>
                <div class="verb-word">{fronte}</div>
                <div class="verb-sub">Come si dice in {"inglese" if it_to_en else "italiano"}?</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            f"""
            <div class="flashcard card-l2">
                <div class="badge badge-gold">{bandiera_retro} Traduzione</div>
                <div class="verb-word">{retro}</div>
                <div class="example-box">🇮🇹 {v['frase_it']}<br>🇬🇧 {v['frase_en']}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
 
    def shuffle_l2():
        shuffle_deck("L2", randomize_dirs=(direzione.startswith("🔀")))
 
    idx = st.session_state["L2_idx"]
    st.markdown(f'<div class="progress-text">Carta {idx + 1} di {N}</div>', unsafe_allow_html=True)
    c1, c2, c3 = st.columns([1, 1.4, 1])
    with c1:
        st.button("⬅️ Indietro", key="L2_prev", use_container_width=True, on_click=go_prev, args=("L2",))
    with c2:
        label2 = "🙈 Nascondi risposta" if st.session_state["L2_show"] else "🔄 Mostra risposta"
        st.button(label2, key="L2_flip", use_container_width=True, on_click=flip_card, args=("L2",))
    with c3:
        st.button("Avanti ➡️", key="L2_next", use_container_width=True, on_click=go_next, args=("L2",))
 
    if st.session_state["L2_show"]:
        s1, s2 = st.columns(2)
        with s1:
            st.button("✅ Lo so già", key="L2_know_btn", use_container_width=True, on_click=mark_known, args=("L2",))
        with s2:
            st.button("🔁 Da ripassare", key="L2_review_btn", use_container_width=True, on_click=mark_review, args=("L2",))
 
    st.button("🔀 Mescola le carte", key="L2_shuffle", use_container_width=True, on_click=shuffle_l2)
 
    know2, review2 = st.session_state["L2_know"], st.session_state["L2_review"]
    if know2 or review2:
        st.markdown(
            f'<div class="stats-row">✅ Sapute: <b>{know2}</b> &nbsp;·&nbsp; 🔁 Da ripassare: <b>{review2}</b></div>',
            unsafe_allow_html=True,
        )
 
# ------------------------------------------------------------------ LIVELLO 3
with tab3:
    init_state("L3")
    st.markdown(
        '<div class="level-caption">Guarda le immagini e indovina il verbo</div>',
        unsafe_allow_html=True,
    )
    v = current_verb("L3")
 
    if not st.session_state["L3_show"]:
        st.markdown(
            f"""
            <div class="flashcard card-l3">
                <div class="badge badge-red">Quale verbo è?</div>
                <div class="verb-emoji">{v['emoji']}</div>
                <div class="verb-sub">Pensa al verbo, poi rivela la risposta 👇</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            f"""
            <div class="flashcard card-l3">
                <div class="badge badge-red">Risposta</div>
                <div class="verb-emoji">{v['emoji']}</div>
                <div class="verb-word">{v['infinito']}</div>
                <div class="detail-line">{v['eng']}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
 
    render_footer_controls("L3")
 
st.markdown(
    '<div style="text-align:center; margin-top:1.5rem; opacity:0.6; font-size:0.85rem;">'
    'Fatto con il ❤️ per chi impara l\'italiano · 🇮🇹</div>',
    unsafe_allow_html=True,
)
 
