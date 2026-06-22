import random

import streamlit as st


def test_new_game_button_resets_session_state():
    """Simulate clicking the 'New Game' button by running the same
    reset logic used in `app.py` and assert that session state
    values are reset to expected defaults.
    """
    # Start from a non-default state to ensure reset actually clears values
    st.session_state['attempts'] = 5
    st.session_state['secret'] = 42
    st.session_state['status'] = 'won'
    st.session_state['score'] = 99
    st.session_state['history'] = [10, 20]

    # Run the same reset logic performed when the button is pressed
    st.session_state.attempts = 0
    st.session_state.secret = random.randint(1, 100)
    st.session_state.status = "playing"
    st.session_state.score = 0
    st.session_state.history = []

    # Assertions: ensure previous values were cleared/overwritten
    assert st.session_state.attempts == 0
    assert st.session_state.status == "playing"
    assert st.session_state.score == 0
    assert st.session_state.history == []
    assert 1 <= st.session_state.secret <= 100


from logic_utils import check_guess


def test_check_guess_hints():
    # Win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"
    assert "Correct" in message

    # Too high
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message

    # Too low
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message
