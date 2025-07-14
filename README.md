# Smart Lead Generation & Scoring Tool

A Streamlit web application for generating, scoring, and exporting business leads based on an industry keyword. This tool demonstrates a practical approach to lead generation aligned with Caprae Capital's AI-readiness mindset.

---

## 🚀 Features
- Input industry keyword to generate leads (dummy data simulation)
- Automated lead scoring based on company attributes
- Visual metrics and lead distribution charts
- Downloadable CSV export of scored leads
- Responsive and intuitive UI

---

## 🛠️ Setup Instructions

### 1. Create a Virtual Environment
```bash
python -m venv venv
# On Windows
source venv\Scripts\activate
```
### 2. Install Dependencies
```bash
pip install -r requirements.txt
```
### 4. Run the Streamlit App
```bash
streamlit run app.py
```
### 5. Open the App
Visit **http://localhost:8501** in your browser.

---
## 🖥️ Usage Instructions
1. Enter a keyword representing the desired industry (e.g., **Fintech**, **SaaS**).
2. Choose the number of pages to scrape (simulated).
3. Click **🚀 Scrape & Score Leads** to generate dummy data.
4. Review the generated leads, their scores, and download the CSV.
5. Explore the lead score distribution chart for insights.

---

## 📊 Technologies Used
- Python
- Streamlit
- Pandas
- BeautifulSoup4 (for scraping, dummy here)
- Altair (for data visualization)

---

## ⚠️ Disclaimer
This tool currently uses dummy data for demonstration. Replace the scraping logic with actual web scraping or API integrations while adhering to ethical data practices.

---

## ✅ Next Steps
- Integrate real-world scraping logic or APIs (e.g., LinkedIn, Crunchbase)
- Improve lead scoring with domain authority, contact verification
- Add CRM integrations or Zapier workflows

---

**Author:** Nitya Jain 
