import os
import streamlit as st
from dotenv import load_dotenv
from pandasai.llm import GooglePalm

load_dotenv()

def create_llm_model():
    api_key = os.getenv("GOOGLE_API_KEY")

    if not api_key:
        return None

    return GooglePalm(api_key=api_key)


def handle_user_query(df, prompt):
    with st.spinner("Generating response..."):
        try:
            prompt_lower = prompt.lower()

            # 🔥 RULE-BASED LOGIC FIRST
            if "total" in prompt_lower:
                for col in df.columns:
                    if df[col].dtype != "object":
                        total = df[col].sum()
                        st.success(f"Total of '{col}': {total}")
                        return

            elif "average" in prompt_lower or "mean" in prompt_lower:
                for col in df.columns:
                    if df[col].dtype != "object":
                        avg = df[col].mean()
                        st.success(f"Average of '{col}': {avg}")
                        return

            # 🤖 LLM fallback
            response = df.chat(prompt)
            st.write(response)

        except Exception as e:
            st.warning("LLM failed, showing fallback analysis")
            st.write(df.describe())