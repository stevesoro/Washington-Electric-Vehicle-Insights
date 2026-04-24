# Electric Vehicle Population Analysis

## Overview
This project analyzes electric vehicle (EV) adoption using a public dataset from Data.gov.
The objective is to uncover **market trends, geographic patterns, and product positioning insights** that can inform **business strategy, pricing, and policy decisions**.

---

## Objectives
This analysis answers the following key questions:

- How fast is EV adoption growing?
- Which manufacturers dominate the market?
- Where is EV adoption most concentrated?
- What is the relationship between **price and electric range**?
- How do policy incentives influence EV characteristics?

---

## Dataset
- Source: Electric Vehicle Population Data (Data.gov) https://catalog.data.gov/dataset/electric-vehicle-population-data
- Records: ~280K+ vehicles
- Key fields:
  - `Model Year`
  - `Make` / `Model`
  - `Electric Range`
  - `Base MSRP`
  - `EV Type`
  - `Location (City, State)`

---

## Data Preparation
To ensure data reliability and consistency, the following steps were performed:

- Removed duplicate records
- Standardized categorical variables (e.g., manufacturer names)
- Converted numeric fields (`Model Year`, `Electric Range`, `Base MSRP`)
- Handled missing values
- Extracted latitude/longitude from location data for spatial analysis

---

## Analysis & Insights

### EV Adoption Over Time
- EV adoption shows a **strong upward trend**, with clear acceleration after 2020  
- Indicates increasing consumer demand and policy support  

**Insight:** The market is transitioning from early adoption to rapid growth.

---

### Market Share by Manufacturer
- Tesla holds a dominant share of EV registrations  
- Other players (Nissan, Chevrolet, Ford) are gaining traction  

**Insight:** The market is still concentrated, but competition is intensifying.

---

### Geographic Distribution
- EV adoption is highly concentrated in **urban areas**
- A small number of cities account for a large proportion of vehicles  

**Insight:** Adoption is driven by infrastructure, income levels, and urban density.

---

### EV Type Distribution
- Battery Electric Vehicles (BEVs) dominate over Plug-in Hybrid EVs (PHEVs)

**Insight:** The market is moving toward **fully electric solutions**, reflecting improved technology and infrastructure.

---

### Electric Range Analysis
- Significant variation in electric range across vehicles
- Premium manufacturers offer a higher average range  

**Insight:** Range is a key competitive differentiator.

---

### Price vs Range Relationship
- Strong positive relationship between **price and electric range**

**Insight:** Higher range vehicles are positioned as **premium products**, indicating a trade-off between affordability and performance.

---

## Advanced Analysis

### Manufacturer Growth Trends
- Tesla shows sustained growth across model years  
- Legacy manufacturers are gradually increasing market share  

**Insight:** The market is shifting from dominance to competitive expansion.

---

### Policy Impact (CAFV Eligibility)
- Incentive-eligible vehicles cluster around certain range levels  

**Insight:** Policy incentives influence both consumer choices and product design.

---

### Market Segmentation
Using clustering (price vs range), EVs can be grouped into:

- Entry-level: low price, low range  
- Mid-range: balanced price and performance  
- Premium: high price, high range  

**Insight:** The EV market exhibits **clear segmentation**, supporting targeted pricing strategies.

---

## Key Takeaways

- EV adoption is **rapidly accelerating**
- Tesla dominates, but competition is increasing
- Adoption is **geographically concentrated** in urban areas
- Higher range is strongly associated with **higher price**
- The market shows **clear segmentation**, indicating increasing maturity
- Policy incentives play a measurable role in shaping the market

---

## Business Implications

### For Manufacturers
- Opportunity to compete in the **mid-range segment**
- Range optimization remains a critical differentiator

### For Policymakers
- Focus infrastructure investment in **urban centers**
- Incentives effectively influence adoption and innovation

### For Analysts & Investors
- EV market is entering a **high-growth phase**
- Competitive dynamics are evolving rapidly

---

## Tools & Technologies
- Python (Pandas)
- Data Visualization (Matplotlib)

---

## Next Steps
- Build an **interactive Power BI dashboard**:
  - EV adoption trends  
  - Market share by manufacturer  
  - Geographic distribution (map)  
  - Price vs range analysis  

- Enrich analysis with additional datasets:
  - Charging infrastructure
  - Demographics (income, population)
  - Fuel price trends

---

## Repository Structure

EV-Population-Analysis
|- WA EV Insights Py Code.py
|- README.md

---

## Key Value of This Project
This project demonstrates:

- Strong **data cleaning and preprocessing**
- Structured **analytical thinking**
- Ability to translate data into **business insights**
- End-to-end analytics workflow from raw data to strategic recommendations

---

## Contact
If you'd like to discuss this project or collaborate, feel free to reach out.
