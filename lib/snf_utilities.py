import json
from snowflake.snowpark.session import Session

import streamlit as st


def create_session():
    if "snowpark_session" not in st.session_state:
        session = Session.builder.configs(json.load(open("../creds.json"))).create()
        st.session_state['snowpark_session'] = session

