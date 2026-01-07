import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import sys
sys.path.append('src')
from predict import predict_demand
from email_alert import send_alert_email

# Alert thresholds
LOW_THRESHOLD = 300.0   # MLD
HIGH_THRESHOLD = 800.0  # MLD

# Title
st.title('Water Demand Forecasting for Urban Planning (Tamil Nadu)')

# Load dataset to get cities and zones
df = pd.read_csv('data/processed/FINAL_SCIENTIFIC_CITY_ZONE_WATER_DEMAND_DATASET.csv')
df['date'] = pd.to_datetime(df['date'])
cities = df['city'].unique()

# Dropdown for city selection
city = st.selectbox('Select City', cities)

# Dropdown for zone selection, filtered by city
zones = df[df['city'] == city]['zone'].unique()
zone = st.selectbox('Select Zone', zones)

# Date picker
date = st.date_input('Select Date for Prediction')

# Alert rules
st.subheader("Alert Rules:")
st.write("- Below 300 MLD → Low water alert")
st.write("- Above 800 MLD → High water alert")

# Predict button
if st.button('Predict Demand'):
    try:
        result = predict_demand(city, zone, date.strftime('%Y-%m-%d'))
        st.subheader('Prediction Results')
        st.write(f"**City:** {city}")
        st.write(f"**Zone:** {zone}")
        st.write(f"**Selected Date:** {date.strftime('%Y-%m-%d')}")
        st.write(f"**Expected Water Demand:** {result['expected']:.2f} MLD")
        st.write(f"**Lower Bound:** {result['lower']:.2f} MLD")
        st.write(f"**Upper Bound:** {result['upper']:.2f} MLD")
        st.write(f"**Shock Adjusted Demand:** {result['shock_adjusted']:.2f} MLD")
        if result['shock_detected']:
            st.warning("External shock detected: Forecast has been adjusted.")

        # Generate forecast graph
        try:
            # Filter historical data
            filtered_df = df[(df['city'] == city) & (df['zone'] == zone)].copy()
            filtered_df = filtered_df.sort_values('date')
            # Get last 30 days for context
            historical_df = filtered_df.tail(30)

            # Prepare predicted data
            pred_date = pd.to_datetime(date)
            pred_data = pd.DataFrame({
                'date': [pred_date],
                'expected': [result['expected']],
                'lower': [result['lower']],
                'upper': [result['upper']]
            })

            # Plot
            fig, ax = plt.subplots(figsize=(10, 6))
            ax.plot(historical_df['date'], historical_df['water_demand_mld'], label='Historical Demand', color='blue', linewidth=2)
            ax.scatter(pred_date, result['expected'], color='red', label='Predicted Expected', s=100, zorder=5)
            ax.scatter(pred_date, result['lower'], color='orange', label='Predicted Lower Bound', s=100, zorder=5)
            ax.scatter(pred_date, result['upper'], color='green', label='Predicted Upper Bound', s=100, zorder=5)
            # Connect bounds with vertical line
            ax.plot([pred_date, pred_date], [result['lower'], result['upper']], color='black', linestyle='--', linewidth=2, label='Prediction Range')
            ax.set_xlabel('Date')
            ax.set_ylabel('Water Demand (MLD)')
            ax.set_title(f'Water Demand Forecast for {city} - {zone}')
            ax.legend()
            ax.grid(True, alpha=0.3)
            # Rotate x-axis labels for better readability
            plt.xticks(rotation=45)
            st.pyplot(fig)
        except Exception as e:
            st.error(f"Error generating graph: {str(e)}")

        # Apply alert logic
        predicted_value = result["expected"]
        if predicted_value < LOW_THRESHOLD:
            alert_type = "LOW"
        elif predicted_value > HIGH_THRESHOLD:
            alert_type = "HIGH"
        else:
            alert_type = "NORMAL"

        if alert_type in ["LOW", "HIGH"]:
            send_alert_email(city, zone, date.strftime('%Y-%m-%d'), predicted_value, alert_type, LOW_THRESHOLD, HIGH_THRESHOLD)
            st.success("📧 Alert email sent successfully")
        else:
            st.info("✅ Water demand within safe limits")
    except Exception as e:
        st.error(f"Error in prediction: {str(e)}")