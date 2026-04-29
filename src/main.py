import os
import pathlib
import pandas as pd
import streamlit as st

#---------Paths & helpers

BASE_DIR = pathlib.Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
SCENARIOS_CSV = DATA_DIR / "scenarios.csv"

def ensure_data_dir():
    DATA_DIR.mkdir(parents=True, exist_ok=True)

def load_scenarios() -> pd.DataFrame:
    ensure_data_dir()
    if SCENARIOS_CSV.exists():
        return pd.read_csv(SCENARIOS_CSV)
    else:
        #Creates an empty data frame with the wanted columns
        cols =  [
            "name",
            "path_type",
            "years_in_school",
            "tuition_per_year",
            "loan_amount",
            "loan_interest_rate",
            "loan_term_years",
            "starting_salary",
            "salary_growth_rate",
            "monthly_expenses",
            "training_costs",
            "simulation_years",
        ]
        return pd.DataFrame(columns=cols)
    
def save_scenarios(df: pd.DataFrame) -> None:
    ensure_data_dir()
    df.to_csv(SCENARIOS_CSV, index=False)
    
    
#---------Streamlit app---------

st.set_page_config(page_title= "College vs Work Simulator", page_icon=":mortar_board:")

st.title("College vs Work - Scenario Manager (Starter)")
st.write