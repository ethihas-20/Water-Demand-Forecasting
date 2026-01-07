# Water Demand Forecasting Using Machine Learning

## Project Overview

This project develops a machine learning-based system for forecasting water demand in urban areas, specifically focusing on city and zone-wise predictions. Utilizing historical water consumption data, the system employs regression models to predict future demand, enabling better resource management and planning. The application includes a web interface for user interaction and an automated email alert system to notify stakeholders when demand thresholds are exceeded.

## Objectives

- To develop an accurate predictive model for water demand forecasting using machine learning techniques.
- To create a user-friendly web application for accessing predictions.
- To implement an automated alert system for demand threshold monitoring.
- To provide visualizations and reports for data-driven decision-making in water resource management.

## Machine Learning Approach

The project employs a regression-based machine learning approach using ensemble methods. Historical water demand data is preprocessed, including feature engineering and encoding of categorical variables. The model is trained using Scikit-learn's Random Forest Regressor, optimized through hyperparameter tuning. Model performance is evaluated using metrics such as Mean Absolute Error (MAE), Mean Squared Error (MSE), and R-squared. The trained model is serialized using Pickle for deployment in the Flask application.

## Project Structure

```
water-demand-project/
├── app.py                          # Flask web application
├── requirements.txt                # Python dependencies
├── data/
│   ├── raw/                        # Raw dataset files
│   └── processed/
│       └── FINAL_SCIENTIFIC_CITY_ZONE_WATER_DEMAND_DATASET.csv  # Processed dataset
├── src/
│   ├── train.py                    # Model training script
│   ├── predict.py                  # Prediction generation script
│   └── email_alert.py              # Email alert system
├── results/
│   ├── model.pkl                   # Trained model
│   ├── label_encoder_city.pkl      # City label encoder
│   ├── label_encoder_zone.pkl      # Zone label encoder
│   ├── std_residual.pkl            # Standard residual for alerts
│   ├── metrics.csv                 # Model evaluation metrics
│   └── predictions/
│       └── forecast.csv            # Generated predictions
└── img/
    └── forecast_*.png              # Visualization images
```

## Technologies Used

- **Programming Language**: Python 3.x
- **Data Processing**: Pandas, NumPy
- **Machine Learning**: Scikit-learn
- **Visualization**: Matplotlib
- **Web Framework**: Flask
- **Model Serialization**: Pickle
- **Email Service**: smtplib (Python standard library)

## Dataset Description

The dataset comprises historical water demand data aggregated at city and zone levels. The processed dataset (`FINAL_SCIENTIFIC_CITY_ZONE_WATER_DEMAND_DATASET.csv`) contains the following key features:

| Feature | Description | Type |
|---------|-------------|------|
| City | Name of the city | Categorical |
| Zone | Specific zone within the city | Categorical |
| Year | Year of the record | Numerical |
| Month | Month of the record | Numerical |
| Demand | Water demand in appropriate units | Numerical |

The dataset has been cleaned and preprocessed to handle missing values, outliers, and categorical encoding.

## Installation & Setup

1. **Create Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Prepare Data**:
   Ensure the processed dataset is placed in `data/processed/`.

## Model Training Steps

1. Navigate to the project directory.
2. Run the training script:
   ```bash
   python src/train.py
   ```
3. The script will:
   - Load and preprocess the data
   - Perform feature engineering
   - Train the regression model
   - Evaluate performance and save metrics
   - Serialize the model and encoders to the `results/` directory

## Prediction Steps

1. Ensure the trained model exists in `results/model.pkl`.
2. Run the prediction script:
   ```bash
   python src/predict.py
   ```
3. The script generates predictions for future periods and saves them as CSV files in `results/predictions/`.

## Running the Flask Application

1. Start the Flask server:
   ```bash
   python app.py
   ```
2. Access the web application at `http://localhost:5000`.
3. Input parameters (year, month, zone) to receive demand predictions.

## Email Alert System

The email alert system monitors predicted demand against predefined thresholds. When demand exceeds the threshold, automated emails are sent to configured recipients. The system uses SMTP for email delivery and is integrated into the prediction workflow.

To configure:
- Update email credentials and recipients in `src/email_alert.py`.
- Set appropriate thresholds based on historical data analysis.

## Output & Visualization

- **Predictions**: Stored in `results/predictions/forecast.csv` with columns for city, zone, date, and predicted demand.
- **Visualizations**: Generated plots saved in `img/` directory, including time series forecasts for different cities and zones.
- **Metrics**: Model performance metrics saved in `results/metrics.csv`.

## Results

The trained model achieves the following performance metrics (based on cross-validation):

- Mean Absolute Error (MAE): [Insert value]
- Mean Squared Error (MSE): [Insert value]
- R-squared: [Insert value]

Detailed results and visualizations demonstrate the model's ability to capture seasonal patterns and trends in water demand.

## Future Enhancements

- Integration with real-time data sources for dynamic forecasting.
- Implementation of deep learning models (e.g., LSTM) for improved accuracy.
- Expansion to include weather and demographic factors.
- Development of a mobile application interface.
- Incorporation of ensemble methods for better prediction robustness.

## Academic Relevance

This project serves as a comprehensive case study in applied machine learning for environmental engineering. It demonstrates the integration of data science techniques with domain-specific knowledge in water resource management. The methodology can be extended to other utility forecasting problems and provides a foundation for research in predictive analytics for sustainable urban planning.

## License

This project is licensed under the MIT License. See the LICENSE file for details.