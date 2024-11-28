import pandas as pd
import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import matplotlib.pyplot as plt

# Title
st.title("Mental Health Tracker Dashboard")

# Function to fetch data from Google Sheets
def fetch_google_sheets_data():
    # Define the scope for Google Sheets and Drive
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    
    # Replace 'path/to/credentials.json' with your actual credentials file path
    creds = ServiceAccountCredentials.from_json_keyfile_name("mental-health-tracker-442920-8ac8936827c8.json", scope)
    client = gspread.authorize(creds)
    
    # Replace 'Mental Health Tracker Responses' with the name of your Google Sheet
    sheet = client.open("Mental Health Tracker Responses").sheet1
    
    # Fetch all records from the sheet
    data = sheet.get_all_records()
    
    # Convert to DataFrame
    return pd.DataFrame(data)

# User input: Select data source
data_source = st.radio(
    "How would you like to load your data?",
    ("Google Sheets", "Upload CSV")
)
# Load data based on user selection
data = None
if data_source == "Google Sheets":
    try:
        st.info("Fetching data from Google Sheets...")
        data = fetch_google_sheets_data()
        st.success("Data successfully fetched from Google Sheets.")
    except Exception as e:
        st.error(f"An error occurred while fetching data: {e}")
        st.info("Ensure your credentials and Google Sheet name are correct.")
elif data_source == "Upload CSV":
    uploaded_file = st.file_uploader("Upload your data (CSV)", type="csv")
    if uploaded_file:
        try:
            # Try reading with UTF-8 encoding
            data = pd.read_csv(uploaded_file, encoding='utf-8')
            st.success("CSV file successfully uploaded.")
        except UnicodeDecodeError:
            # Fallback to Latin-1 encoding
            data = pd.read_csv(uploaded_file, encoding='latin1')
            st.success("CSV file successfully uploaded with fallback encoding.")
        except Exception as e:
            st.error(f"An error occurred while reading the CSV: {e}")

# Add validation for required columns
if data is not None:
    required_columns = ["Date", "Mood", "Exercise"]
    missing_columns = [col for col in required_columns if col not in data.columns]

    if missing_columns:
        st.error(f"The following required columns are missing from the dataset: {missing_columns}")
    else:
        # Process data as expected
        data["Date"] = pd.to_datetime(data["Date"], errors="coerce")  # Convert Date column to datetime
        if data["Date"].isnull().any():
            st.warning("Some dates could not be parsed. Ensure the Date column is formatted as YYYY-MM-DD.")

# If data is loaded, display features
if data is not None:
    st.subheader("Your Data")
    st.write(data)
    
    # Ensure the Date column is properly formatted
    if "Date" in data.columns:
        try:
            data["Date"] = pd.to_datetime(data["Date"])
        except Exception:
            st.warning("Date column could not be converted to datetime. Ensure it follows the YYYY-MM-DD format.")
    
    # Bar Chart: Average Scores
    st.subheader("Average Scores for Each Variable")
    if st.button("Show Averages"):
        avg_scores = data.select_dtypes(include=["float", "int"]).mean().sort_values(ascending=False)
        st.bar_chart(avg_scores)

    # Line Chart: Mood Over Time
    st.subheader("Mood Over Time")
    if "Mood" in data.columns and "Date" in data.columns:
        st.line_chart(data.set_index("Date")["Mood"])
    else:
        st.warning("Mood data or Date column is missing in the dataset.")

    # Scatter Plot: Exercise vs. Mood
    st.subheader("Scatter Plot: Exercise vs. Mood")
    if "Exercise" in data.columns and "Mood" in data.columns:
        fig, ax = plt.subplots()
        ax.scatter(data["Exercise"], data["Mood"])
        ax.set_xlabel("Exercise")
        ax.set_ylabel("Mood")
        ax.set_title("Exercise vs. Mood")
        st.pyplot(fig)
    else:
        st.warning("Exercise or Mood column is missing in the dataset.")

    # Heatmap: Correlation Matrix
    st.subheader("Heatmap: Correlation Matrix")
    if st.button("Show Correlation Heatmap"):
        numeric_data = data.select_dtypes(include=["float", "int"])
        if not numeric_data.empty:
            corr = numeric_data.corr()
            st.write(corr)
            fig, ax = plt.subplots(figsize=(8, 6))
            cax = ax.matshow(corr, cmap="coolwarm")
            fig.colorbar(cax)
            ax.set_xticks(range(len(corr.columns)))
            ax.set_xticklabels(corr.columns, rotation=90)
            ax.set_yticks(range(len(corr.columns)))
            ax.set_yticklabels(corr.columns)
            st.pyplot(fig)
        else:
            st.warning("No numeric data available for correlation heatmap.")

    # Weekly Averages Line Chart
    st.subheader("Weekly Averages")
    if "Date" in data.columns:
        data.set_index("Date", inplace=True)
        weekly_avg = data.resample("W").mean()
        st.line_chart(weekly_avg)
    else:
        st.warning("Date column is missing or not in the correct format.")
else:
    st.info("Please select a data source to get started.")