# Global Educational Enrollment Analysis (2016 – 2019)

An interactive Power BI dashboard designed to analyze and compare student enrollment levels (Primary, Secondary, and Tertiary education) across selected global economies: **Jordan, Qatar, Oman, China, India, and Georgia** over a four-year period.

## Project Overview & Objectives
The purpose of this project is to transform complex World Bank Open Data into an intuitive, data-driven visual story. By cleaning and structuring multi-year education metrics, the dashboard uncovers critical regional enrollment trends, tracking structural and demographic shifts in global education infrastructure.


## Data Preprocessing & Engineering
To guarantee data quality and support dynamic, continuous time-series visualization, the following pipeline was executed:
* **Numeric Standardization:** Converted raw, inconsistent numerical columns into clean, uniform whole numbers.
* **Custom Regional Imputation:** Maintained geographical and historical integrity by handling missing data through row-wise, country-specific mean imputation.
* **Data Restructuring & Unpivoting:** Flattened and restructured multi-year columns into a unified, consolidated time-series format optimized for seamless DAX calculations and filtering in Power BI.


## Key Features & DAX Implementation
* **Dynamic Chart Titles:** Implemented custom **DAX Measures** that automatically update descriptive titles based on active slicer selections (Country, Year, Education Level), providing immediate context to the end-user.
* **Advanced Cross-Filtering Strategy:** Integrated multi-layered filtering page-by-page to control analysis boundaries while maintaining a smooth user experience across views.
* **Interactive Slicers:** Included responsive slicers for localized deep-dives by Country, Year, and Educational Series.

## Executive Insights
* **Global Footprint:** Total tracked student enrollment reached **2 Billion** across the target regions, heavily driven by primary education enrollment volumes.
* **Regional Dominance:** India dominates overall student enrollment metrics across the selected timeline, followed closely by China.
* **Higher Education Leaders:** Georgia and China command the highest proportional shares in higher education (Tertiary Enrollment) at approximately **20%**, signaling strong regional focus on advanced university education.
* **Infrastructure Shifts:** A sharp decline in primary enrollment was observed in India and Oman during 2016–2019, highlighting evolving demographic trends or structural educational shifts.
* 

## Directory Files
* `Final_Dashboard.pbix`: The core interactive Power BI application containing the data model, DAX measures, and visual components.
* `Dashboard report (1).docx`: Comprehensive text documentation detailing the project scope, dataset metadata, preprocessing logic, and analytical findings.

## Team & Contributions
* **Rahaf Ali (Data Engineering & Visualization Developer):** Responsible for executing data preprocessing, missing value imputation, unpivoting data structures, creating dynamic DAX measures, and designing the entire interactive visual layout.
*
