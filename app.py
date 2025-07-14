# app.py - Enhanced Smart Lead Generation & Scoring Tool

import requests
from bs4 import BeautifulSoup
import pandas as pd
import streamlit as st
import altair as alt

st.set_page_config(page_title="Smart Lead Generator", layout="wide", page_icon="🚀")

st.title("🚀 Smart Lead Generation & Scoring Tool")

with st.sidebar:
    st.header("🔍 Lead Generation Settings")
    keyword = st.text_input("Enter Industry/Keyword:", value='SaaS')
    num_pages = st.slider("Number of Pages to Scrape:", 1, 5, 1)

# Dummy scraper function (replace with actual scraping logic)
def scrape_companies(keyword, num_pages=1):
    companies = []
    for i in range(5):
        companies.append({
            'Name': f'{keyword} Company {i+1}',
            'Website': f'https://www.{keyword.lower()}company{i+1}.com',
            'LinkedIn': f'https://www.linkedin.com/{keyword.lower()}company{i+1}',
        })
    return companies

# Scoring logic

def score_lead(company):
    score = 0
    if 'linkedin' in company['LinkedIn'].lower():
        score += 30
    if '.com' in company['Website']:
        score += 20
    if len(company['Name']) > 5:
        score += 50
    return score

if st.button("🚀 Scrape & Score Leads"):
    with st.spinner('Scraping data, please wait...'):
        leads = scrape_companies(keyword, num_pages)

        for lead in leads:
            lead['Score'] = score_lead(lead)

        df = pd.DataFrame(leads)

        st.success(f"✅ Scraped and scored {len(df)} leads.")

        # Display metric
        st.metric(label="Total Leads Scraped", value=len(df))

        # Data preview
        st.subheader("📊 Scored Leads")
        st.dataframe(df)

        # Visualization
        chart = alt.Chart(df).mark_bar().encode(
            x='Name',
            y='Score',
            color='Score',
            tooltip=['Name', 'Score']
        ).properties(title="Lead Score Distribution")

        st.altair_chart(chart, use_container_width=True)

        # Download button
        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button("📥 Download Leads as CSV", data=csv, file_name="qualified_leads.csv")

st.markdown("**Disclaimer:** This tool uses dummy data for demonstration. Replace the scraping logic for real-world use while adhering to ethical data collection practices.")
