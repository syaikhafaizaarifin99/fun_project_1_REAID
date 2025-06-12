import streamlit as st

# Inisialisasi session state
if "quiz_started" not in st.session_state:
    st.session_state.quiz_started = False

st.set_page_config(page_title="Find your Music Taste", page_icon="🎸")    

st.title("🎵 Fun Project 1.1: Music Taste Quiz")
st.header("Welcome to the Music Taste Quiz!")
st.write("This is a fun project to explore your music preferences.")

# Sidebar
st.sidebar.header("Quiz Navigation")
st.sidebar.write("Use the sidebar to navigate through the quiz.")

# Tombol
if st.sidebar.button("Start Quiz"):
    st.session_state.quiz_started = True

if st.sidebar.button("Results"):
    st.session_state.quiz_started = False
    st.session_state.show_result = True

if st.sidebar.button("About"):
    st.session_state.quiz_started = False
    st.session_state.show_result = False

# Tampilkan form jika quiz dimulai
if st.session_state.quiz_started:
    st.subheader("Let's begin the quiz!")
    st.write("Answer these questions to find out your music taste!")

    with st.form(key="music_form"):
        mood = st.radio(
            "1. What is your usual mood when listening to music?",
            ("Happy", "Sad", "Relaxed", "Energetic")
        )
        instrument = st.selectbox(
            "2. Which instrument do you enjoy most?",
            ("Guitar", "Piano", "Drums", "Synthesizer")
        )
        time = st.radio(
            "3. When do you usually listen to music?",
            ("Morning", "Afternoon", "Evening", "Late Night")
        )

        submit = st.form_submit_button("Submit")

    if submit:
        genre_score = {"Pop": 0, "Rock": 0, "Jazz": 0, "EDM": 0}

        if mood == "Happy":
            genre_score["Pop"] += 1
        elif mood == "Sad":
            genre_score["Jazz"] += 1
        elif mood == "Relaxed":
            genre_score["Jazz"] += 1
        elif mood == "Energetic":
            genre_score["Rock"] += 1
            genre_score["EDM"] += 1

        if instrument == "Guitar":
            genre_score["Rock"] += 1
        elif instrument == "Piano":
            genre_score["Jazz"] += 1
        elif instrument == "Drums":
            genre_score["Rock"] += 1
        elif instrument == "Synthesizer":
            genre_score["EDM"] += 2

        if time == "Morning":
            genre_score["Pop"] += 1
        elif time == "Afternoon":
            genre_score["Pop"] += 1
        elif time == "Evening":
            genre_score["Jazz"] += 1
        elif time == "Late Night":
            genre_score["EDM"] += 1

        result = max(genre_score, key=genre_score.get)
        st.session_state.quiz_result = result
        st.success(f"🎧 Your ideal music genre is: **{result}**!")
        
        if result == "Pop":
            st.image("pop.png", width=150, caption="Pop Vibes 🎶")
        elif result == "Rock":
            st.image("rock.png", width=150, caption="Rock On 🤘")
        elif result == "Jazz":
            st.image("jazz.png", width=150, caption="Smooth Jazz 🎷")
        elif result == "EDM":
            st.image("edm.png", width=150, caption="EDM Beats 🎧")

# About section
elif "show_result" in st.session_state and st.session_state.show_result:
    st.subheader("Results")
    if "quiz_result" in st.session_state:
        st.write(f"Your last result: **{st.session_state.quiz_result}**")
    else:
        st.info("You haven't submitted the quiz yet.")

# About section
elif "show_result" in st.session_state and not st.session_state.show_result:
    st.subheader("About This Project")
    st.write("""
        This is a fun Streamlit quiz project built to help users discover their music preferences.
        Created with ❤️ for learning and entertainment purposes.
    """)
