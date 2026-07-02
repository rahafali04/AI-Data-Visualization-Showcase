# Smart Parking Recommendation System

An interactive, ML-powered smart parking assistant that predicts parking space availability and provides geospatial mapping to recommend optimal parking locations based on live occupancy data, time, and day constraints.

---

## Project Overview & Objectives
Finding available parking spaces in crowded urban areas is a significant challenge. This project solves this by using Machine Learning to predict parking status (Available, Busy, or Full) and deploying an interactive dashboard that guides drivers to the best available spots in real-time.

---

## Technical Features & Engineering
* Machine Learning Integration: Integrates a trained classification model and data scaler to process input variables like zone, hours, and days, returning live prediction scores.
* Geospatial Visualization: Deploys dynamic map markers that visually locate parking zones using coordinate datasets.
* Real-time Status Alerts: Renders responsive user interface containers and visual progress bars that change styles and colors according to the predicted parking occupancy risk.

---

## Directory Files
* app.py: The primary Streamlit application file housing the layout logic, form input handlers, and map integration.
* parking_model.pkl: The trained machine learning model file utilized for live occupancy status classification.
* parking_scaler.pkl: The preprocessing scaler file used to normalize incoming user inputs prior to model inference.
* final_merged_dataset.csv: The baseline tabular dataset containing regional tracking data, used to populate spatial coordinates.

---

## Team & Contributions
* Rahaf Ali (Data Visualization & UI/UX Developer): Designed and implemented the interactive Streamlit user interface, handled the integration of real-time mapping visualization using Folium and streamlit_folium, and engineered customized dynamic status alerts based on ML model predictions.
