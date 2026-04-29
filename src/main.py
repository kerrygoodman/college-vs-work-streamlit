import os
import pathlib
import pandas as pd
import streamlit as st

#---------Paths & helpers

BASE_DIRE = pathlib.Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIRE / "data"
SCENARIOS_CSV = DATA_DIR / "scenarios.csv"

def ensure_data_dir():
    DATA_DIR.mkdir(parents=True, exist_ok=True)

def load_scenarios():
    ensure_data_dir()
    if SCENARIOS_CSV.exsists():
        return
    