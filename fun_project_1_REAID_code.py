import streamlit as st

# Inisialisasi session state
if "quiz_started" not in st.session_state:
    st.session_state.quiz_started = False

if "quiz_result" not in st.session_state:
    st.session_state.quiz_result = None

st.set_page_config(page_title="Find your Music Taste", page_icon="🎸")

st.title("🧠 What's Your Tech Role?")
st.write("Temukan apakah kamu lebih cocok jadi **Programmer**, **Designer**, atau **Data Scientist** berdasarkan pilihan kamu!")

# Sidebar
st.sidebar.header("Quiz Navigation")
if st.sidebar.button("Start Quiz"):
    st.session_state.quiz_started = True
    st.session_state.quiz_result = None

if st.sidebar.button("Results"):
    st.session_state.quiz_started = False

if st.sidebar.button("About"):
    st.session_state.quiz_started = False
    st.session_state.quiz_result = "about"

# Tampilkan pertanyaan jika kuis dimulai
if st.session_state.quiz_started:
    st.subheader("📝 Jawab pertanyaan berikut ini:")

    with st.form("tech_quiz"):
        q1 = st.radio("1. Apa kegiatan favoritmu saat di depan komputer?", 
                      ("Menulis kode", "Mendesain tampilan", "Menganalisis data"))
        
        q2 = st.radio("2. Software mana yang paling ingin kamu kuasai?", 
                      ("Visual Studio Code", "Figma", "Jupyter Notebook"))
        
        q3 = st.radio("3. Apa yang paling kamu sukai dari sebuah proyek?", 
                      ("Logika & struktur", "Tampilan visual", "Wawasan dari data"))

        q4 = st.radio("4. Kamu lebih tertarik ke bidang apa?", 
                      ("Pengembangan aplikasi", "Desain UI/UX", "Statistik dan machine learning"))
        
        submit = st.form_submit_button("Lihat Hasil")

    if submit:
        # Skoring
        score = {"Programmer": 0, "Designer": 0, "Data Scientist": 0}

        for answer in [q1, q2, q3, q4]:
            if answer in ["Menulis kode", "Visual Studio Code", "Logika & struktur", "Pengembangan aplikasi"]:
                score["Programmer"] += 1
            elif answer in ["Mendesain tampilan", "Figma", "Tampilan visual", "Desain UI/UX"]:
                score["Designer"] += 1
            elif answer in ["Menganalisis data", "Jupyter Notebook", "Wawasan dari data", "Statistik dan machine learning"]:
                score["Data Scientist"] += 1

        # Menentukan hasil
        result = max(score, key=score.get)
        st.session_state.quiz_result = result
        st.success(f"Hasil kamu adalah: **{result}**!")

# Tampilkan hasil (jika user klik Results atau submit quiz)
elif st.session_state.quiz_result and st.session_state.quiz_result != "about":
    st.subheader("🎯 Hasil Kuis")

    role = st.session_state.quiz_result
    if role == "Programmer":
        st.image("https://cdn-icons-png.flaticon.com/512/1055/1055687.png", width=150)
        st.write("🧠 Kamu cocok menjadi **Programmer**! Kamu menyukai logika, menyusun sistem, dan berpikir teknis.")
    elif role == "Designer":
        st.image("https://cdn-icons-png.flaticon.com/512/2721/2721205.png", width=150)
        st.write("🎨 Kamu cocok menjadi **Designer**! Kamu punya rasa estetik yang tinggi dan menyukai tampilan yang menarik.")
    elif role == "Data Scientist":
        st.image("https://cdn-icons-png.flaticon.com/512/3887/3887811.png", width=150)
        st.write("📊 Kamu cocok menjadi **Data Scientist**! Kamu tertarik pada data, insight, dan analisis mendalam.")

# About section
elif st.session_state.quiz_result == "about":
    st.subheader("ℹ️ Tentang Proyek Ini")
    st.write("""
    Kuis ini dibuat menggunakan **Streamlit** sebagai proyek pembelajaran.
    """)
