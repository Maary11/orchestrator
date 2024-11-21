import streamlit as st
import ipaddress
from urllib.parse import urlparse

from src.ui import layout
from src.engine import orchestrate

def initialize_state():
    if "danger_level" not in st.session_state:
        st.session_state.danger_level = "starter"

def run_orchestrator(url):
    url_metrics = get_url_metrics(url)

    label, precision = orchestrate(url_metrics)

    set_danger_level(label, precision)

def get_url_metrics(url):
    metrics = []
    parts = urlparse(url)

    domain = parts.netloc
    tld_start = domain.rfind(".")

    metrics.append(url.count("."))
    metrics.append(url.count("-"))
    metrics.append(url.count("_"))
    metrics.append(url.count("/"))
    metrics.append(url.count("?"))
    metrics.append(url.count("="))
    metrics.append(url.count("@"))
    metrics.append(url.count("&"))
    metrics.append(url.count("!"))
    metrics.append(url.count(" "))
    metrics.append(url.count("~"))
    metrics.append(url.count(","))
    metrics.append(url.count("+"))
    metrics.append(url.count("*"))
    metrics.append(url.count("#"))
    metrics.append(url.count("$"))
    metrics.append(url.count("%"))
    metrics.append(len(domain) - tld_start - 1)
    metrics.append(len(url))
    metrics.append(domain.count("."))
    metrics.append(domain.count("-"))
    metrics.append(domain.count("_"))
    metrics.append(domain.count("/"))
    metrics.append(domain.count("?"))
    metrics.append(domain.count("="))
    metrics.append(domain.count("@"))
    metrics.append(domain.count("&"))
    metrics.append(domain.count("!"))
    metrics.append(domain.count(" "))
    metrics.append(domain.count("~"))
    metrics.append(domain.count(","))
    metrics.append(domain.count("+"))
    metrics.append(domain.count("*"))
    metrics.append(domain.count("#"))
    metrics.append(domain.count("$"))
    metrics.append(domain.count("%"))
    metrics.append(sum(domain.count(vowel) for vowel in "aeiouAEIOU"))
    metrics.append(len(domain))
    metrics.append(is_ip_address(domain))
    metrics.append(1 if any(keyword in domain for keyword in ["server", "client"]) else 0)

    return [metrics]

def is_ip_address(domain):
    try:
        ipaddress.ip_address(domain)
        return 1
    except ValueError:
        return 0

def set_danger_level(label, precision):
    if label == 0:
        if precision >= 0.9 and precision <= 0.985:
            st.session_state.danger_level = "safe"
        else:
            st.session_state.danger_level = "warning"
    else:
        if precision >= 0.9 and precision <= 0.985:
            st.session_state.danger_level = "dangerous"
        else:
            st.session_state.danger_level = "warning"
        
    st.rerun()
    
def run():
    initialize_state()
    layout(
        run_orchestrator
    )