---
title: MentalHealthDashboard
emoji: 👁
colorFrom: pink
colorTo: blue
sdk: streamlit
sdk_version: 1.40.2
app_file: app.py
pinned: false
license: mit
short_description: An interactive dashboard to track and analyze mental health
---

Check out the configuration reference at https://huggingface.co/docs/hub/spaces-config-reference

MENTAL HEALTH TRACKER DASHBOARD

OVERVIEW

The Mental Health Tracker Dashboard allows users to track and visualize mental health indicators such as Diet, Exercise, Sleep, and Mood. Data can be uploaded as a CSV or fetched directly from a linked Google Sheet.

FEATURES

	•	VISUALIZE MOOD TRENDS: Line chart for tracking changes over time.
	•	EXPLORE RELATIONSHIPS: Correlation heatmap and scatter plots.
	•	VIEW WEEKLY AVERAGES: Aggregated trends for simplified analysis.
	•	FILE UPLOAD OR GOOGLE SHEETS INTEGRATION: Upload CSV files or fetch live data from Google Sheets.

DATA COLLECTION

	•	USE GOOGLE FORMS: Collect data with a simple form linked to a Google Sheet.
	•	TRACK VARIABLES: Diet, Exercise, Social Connection, Screen Time, Sleep, Mood, and Job Satisfaction (1–5 scale).

INSTALLATION

	1.	CLONE REPOSITORY:

git clone <repository-url>  
cd mental-health-tracker  

	2.	INSTALL DEPENDENCIES:

pip install -r requirements.txt  

	3.	RUN LOCALLY:

streamlit run app.py  

USAGE

	1.	EXPORT DATA AS CSV: Download responses from Google Sheets.
	2.	UPLOAD DATA: Use the app to upload CSVs or fetch data directly from Google Sheets.
    3.  VISIT https://forms.gle/j6x29a34Xy8jp3tu6 to enter data to track mental health metrics

TECHNOLOGIES USED

	•	STREAMLIT: Dashboard framework.
	•	PANDAS: Data manipulation.
	•	MATPLOTLIB: Visualizations.
	•	GOOGLE SHEETS API: Live data integration.

FUTURE IMPROVEMENTS

	•	ADD USER AUTHENTICATION for personalized tracking.
	•	DAILY REMINDERS for data submission.
	•	DEPLOY TO HUGGING FACE SPACES for public access.
