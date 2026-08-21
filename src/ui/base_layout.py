import streamlit as st


def style_background_home():

    st.markdown(
        """
        <style>
            .stApp {
                background: #5865F2 !important;
            }

            .stApp div[data-testid="stColumn"] {
                background-color: #E0E3FF !important;
                padding: 2.5rem !important;
                border-radius: 5rem !important;
            }
        </style>
        """,
        unsafe_allow_html=True
    )


def style_background_dashboard():

    st.markdown(
        """
        <style>
            .stApp {
                background: #E0E3FF !important;
            }
        </style>
        """,
        unsafe_allow_html=True
    )


def style_base_layout():

    st.markdown(
        """
        <style>

        @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis:YEAR@1979&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis:YEAR@1979&family=Outfit:wght@100..900&display=swap');


        /* =========================
           HIDE STREAMLIT UI
        ========================= */

        #MainMenu,
        footer,
        header {
            visibility: hidden;
        }


        /* =========================
           MAIN CONTAINER
        ========================= */

        .block-container {
            padding-top: 1.5rem !important;
        }


        /* =========================
           TEXT COLORS
        ========================= */

        h1,
        h2,
        h3,
        h4,
        h5,
        h6,
        p,
        label {
            color: #000000 !important;
        }


        /* =========================
           HEADINGS
        ========================= */

        h1 {
            font-family: "Climate Crisis", sans-serif !important;
            font-size: 3.5rem !important;
            line-height: 1.1 !important;
            margin-bottom: 0rem !important;
            color: #000000 !important;
        }

        h2 {
            font-family: "Climate Crisis", sans-serif !important;
            font-size: 2rem !important;
            line-height: 0.9 !important;
            margin-bottom: 0rem !important;
            color: #000000 !important;
        }

        h3,
        h4,
        h5,
        h6,
        p {
            font-family: "Outfit", sans-serif !important;
            color: #000000 !important;
        }


        /* =========================
           BUTTONS
        ========================= */

        button {
            border-radius: 1.5rem !important;
            background-color: #5865F2 !important;
            color: #FFFFFF !important;
            padding: 10px 20px !important;
            border: none !important;
            transition: transform 0.25s ease-in-out !important;
        }


        /* SECONDARY BUTTON */

        button[kind="secondary"] {
            border-radius: 1.5rem !important;
            background-color: #EB459E !important;
            color: #FFFFFF !important;
            padding: 10px 20px !important;
            border: none !important;
            transition: transform 0.25s ease-in-out !important;
        }


        /* TERTIARY BUTTON */

        button[kind="tertiary"] {
            border-radius: 1.5rem !important;
            background-color: #000000 !important;
            color: #FFFFFF !important;
            padding: 10px 20px !important;
            border: none !important;
            transition: transform 0.25s ease-in-out !important;
        }


        /* =========================
           BUTTON HOVER
        ========================= */

        button:hover {
            transform: scale(1.05) !important;
        }

        </style>
        """,
        unsafe_allow_html=True
    )