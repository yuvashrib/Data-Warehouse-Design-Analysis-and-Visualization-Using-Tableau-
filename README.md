# UK Airport Punctuality Analysis - 2023

## Problem Statement
The dataset comprises punctuality statistics for selected UK airports, with data for each month of 2023. The goal is to utilize this data to design a data warehouse and create visualizations using Tableau for analyzing airport performance trends, enabling actionable insights for researchers and policymakers.

## Tools and Technologies Used
- **Data Warehouse Design:** Star Schema
- **Database Management System:** Oracle Apex
- **Data Manipulation and Preparation:** Python
- **Visualization:** Tableau
- **Data Format:** CSV files
- **Data Source:** UK Airport punctuality statistics (12 monthly files)

## Objectives
1. **Design a Data Warehouse:** Create a star schema to support efficient querying and reporting.
2. **Database Implementation:** Write SQL scripts to create and populate tables.
3. **Data Preparation:** Clean, transform, and organize the data for database loading.
4. **Visualizations:** Develop insightful Tableau dashboards to analyze trends.

## Star Schema Design
The star schema consists of:
- **Fact Table:** `FlightDelay_Fact`
  - Measures: Arrival delays, departure delays, etc.
  - Foreign Keys: Links to dimension tables.
- **Dimension Tables:**
  - `Airport_Dimension`: Airport names and codes.
  - `Airline_Dimension`: Airline names.
  - `City_Dimension`: City names and associated country IDs.
  - `Country_Dimension`: Country names.
  - `Period_Dimension`: Time-based attributes like year, month, and quarter.

### Justification for Design
- **Simplicity:** Direct links between the fact table and dimension tables ensure easy querying.
- **Performance:** Reduced joins enhance query execution speed.
- **Scalability:** New dimensions can be added with minimal schema changes.
- **Maintenance:** Changes in dimension data only impact the respective table.

## Data Preparation  

### Steps:  
1. **Data Conversion:** Transformed Excel files into CSV format.  
2. **Data Cleaning:**  
   - Removed duplicates.  
   - Addressed missing values.  
3. **Data Transformation:**  
   - Split data into dimension and fact components.  
   - Assigned unique IDs to each entity (e.g., `airport_id`, `period_id`).  
4. **Data Integration:** Merged data into structured files using Python.  
5. **Database Loading:** Uploaded CSVs into Oracle Apex and populated tables with SQL scripts.
6. **Data Visualizations:** Vizualized the data to derive key insights using Tableau.

### Challenges:  
- **Data Consistency:** Ensured accurate foreign key relationships.  
- **Normalization:** Reduced redundancy by maintaining clean, structured tables.  

---

## Tableau Visualizations  
Visualizations have been created using the dimension and fact tables established earlier. These visualizations are intended to aid in data analysis and derive key insights crucial for business strategy formulation and decision-making.

Tableau, a business intelligence tool, was utilized to craft these visualizations. The following steps outline the process undertaken to generate select visualizations, along with their respective aims, creation steps, and key insights.


---

## Conclusion  

This project showcases the potential of a well-designed star schema and Tableau visualizations in analyzing airport punctuality data. The derived insights can support operational enhancements and policy formulation, ultimately improving passenger experiences and airport efficiency.  

