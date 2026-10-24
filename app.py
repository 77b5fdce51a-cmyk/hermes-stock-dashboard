import streamlit as st
from subsystems.subsystem_1 import render as render_1
from subsystems.subsystem_2 import render as render_2
from subsystems.subsystem_3 import render as render_3
from subsystems.subsystem_4 import render as render_4
from subsystems.subsystem_5 import render as render_5
from subsystems.subsystem_6 import render as render_6
from subsystems.subsystem_7 import render as render_7
from subsystems.subsystem_8 import render as render_8
from subsystems.subsystem_9 import render as render_9
from subsystems.subsystem_10 import render as render_10

st.set_page_config(page_title="Hermes Stock Dashboard", layout="wide")
st.title("📦 Hermes Stock Dashboard")

tabs = st.tabs([
    "sys.1", "sys.2", "sys.3", "sys.4", "sys.5",
    "sys.6", "sys.7", "sys.8", "sys.9", "sys.10",
])

with tabs[0]:
    render_1()
with tabs[1]:
    render_2()
with tabs[2]:
    render_3()
with tabs[3]:
    render_4()
with tabs[4]:
    render_5()
with tabs[5]:
    render_6()
with tabs[6]:
    render_7()
with tabs[7]:
    render_8()
with tabs[8]:
    render_9()
with tabs[9]:
    render_10()
