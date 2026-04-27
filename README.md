# 🏪 Marketplace Insights Dashboard: Data-Driven Strategic Growth

<div align="center">

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.29+-FF4B4B.svg)
![Plotly](https://img.shields.io/badge/Plotly-Interactive-3f4f75.svg)
![Pandas](https://img.shields.io/badge/Pandas-Data_Processing-150458.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

**Uncovering non-obvious, actionable insights from e-commerce marketplace data to drive strategic product & growth decisions.**

[🌐 Live Project Demo](https://marketplace-insights-dashboard-3vmpxsc3bmrqxg9ezxqtkg.streamlit.app/) • [💼 Portfolio](https://charan-karthik-nayakanti-14.netlify.app) • [🔗 LinkedIn](https://www.linkedin.com/in/charankarthiknayakanti/) • [🐙 GitHub](https://github.com/mrkarthik14)

</div>

---

## 📌 Executive Overview

This project exemplifies **senior-level product analytics and data science** by transforming raw e-commerce marketplace data into strategic, high-ROI business recommendations. Rather than just reporting metrics, this interactive dashboard acts as an exploratory tool to uncover deep product insights—bridging the gap between data analytics and product strategy.

### 🎯 Core Objectives
- **Data-Driven Product Management:** Transition from reactive metric tracking to proactive insight generation.
- **Actionable Strategic Impact:** Deliver specific, quantifiable business recommendations (e.g., ~$556K in incremental annual revenue).
- **Interactive Exploration:** Build a robust, scalable Streamlit application for stakeholders to interact with complex datasets intuitively.

---

## 📸 Dashboard Gallery

### 1. Executive Summary
*High-level overview of the marketplace's health and primary strategic insights.*
<div align="center">
  <img src="Screenshots/Marketplace%20Analytics%20Dashboard.png" alt="Executive Summary Page" width="800"/>
</div>

### 2. The Platinum Paradox
*Deep dive into seller tiers and the hidden value of premium sellers.*
<div align="center">
  <img src="Screenshots/Platinum%20Paradox.png" alt="Platinum Paradox Insight Page" width="800"/>
</div>

### 3. The Weekend Effect
*Analyzing purchasing temporal patterns to optimize marketing spend.*
<div align="center">
  <img src="Screenshots/weekend%20effect.png" alt="Weekend Effect Insight Page" width="800"/>
</div>

### 4. The Response Multiplier
*Understanding the cascading ROI of seller engagement on product ratings.*
<div align="center">
  <img src="Screenshots/response%20multiplier.png" alt="Response Multiplier Insight Page" width="800"/>
</div>

### 5. VIP Customer Opportunity & Shipping Premium
*Segmentation strategies for maximizing high-LTV customers and fulfillment optimization.*
<div align="center">
  <img src="Screenshots/VIP%20oppurtinity.png" alt="VIP Insight Page" width="800"/>
  <br><br>
  <img src="Screenshots/Shipping%20Premium.png" alt="Shipping Premium Insight Page" width="800"/>
</div>

---

## 💻 Under The Hood: Code Architecture

The architecture is designed for modularity, clean data separation, and performant caching. 

### Data Ingestion & Caching Strategy
*Efficiently loading and joining 10k+ rows using Streamlit's robust caching mechanisms.*
<div align="center">
  <!-- TODO: Upload code screenshot and replace image path below -->
  <img src="images/code_snippet_caching.png" alt="Data Caching Code Snippet" width="700"/>
</div>

### Dynamic UI Rendering
*Generating dynamic, interactive UI components using custom CSS and Plotly.*
<div align="center">
  <!-- TODO: Upload code screenshot and replace image path below -->
  <img src="images/code_snippet_ui.png" alt="UI Rendering Code Snippet" width="700"/>
</div>

---

## 🔬 Analytical Methodology & Dataset

1. **Synthetic Data Generation Strategy:** Engineered a complex dataset reflecting real-world distributions (log-normal pricing, Poisson-distributed shipping times) to simulate a live production environment. The generated `.csv` files are tracked in this repository for reproducibility.
2. **Exploratory Data Analysis (EDA):** Leveraged Pandas for advanced multi-dimensional aggregation, temporal analysis, and cohort segmentation.
3. **Insight Distillation:** Filtered noise to identify the top 5 statistically significant patterns.
4. **Business Translation:** Mapped data correlations to concrete product recommendations, estimating GMV impact via conservative conversion multipliers.

---

## 📈 Strategic Business Impact

The analysis uncovered five core levers for growth, projecting an estimated **$556K** in incremental annual revenue based on current GMV baselines.

| Strategic Lever | Primary KPI Addressed | Expected Impact | Est. Annual Revenue Lift |
|:---|:---|:---|:---|
| **Platinum Sellers** | High-Value Customer Retention | +15-20% Retention | +$140K |
| **Weekend Campaigns** | Weekend GMV | +8-12% GMV | +$46K |
| **Seller Responsiveness**| Product Conversion Rate | +12% Conversion | +$111K |
| **VIP Segmentation** | Customer LTV (Lifetime Value) | +10% VIP Conversion | +$92K |
| **Fulfillment Speed** | Conversion & Return Rates | +18% Conv. / -2.5% Returns | +$167K |

---

## ⚙️ Local Development & Deployment

### Prerequisites
- Python 3.9+
- Git

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/mrkarthik14/marketplace-insights-dashboard.git
cd marketplace-insights-dashboard

# 2. Install dependencies (Crucial step to avoid ModuleNotFoundError on Streamlit Cloud)
pip install -r requirements.txt

# 3. Generate the data
python generate_marketplace_data.py

# 4. Launch the application
streamlit run marketplace_dashboard.py
```

> **Note for Streamlit Cloud Deployments:** 
> Ensure `requirements.txt` is successfully pushed to the remote repository main branch. If `plotly.express` throws a `ModuleNotFoundError`, it indicates the dependencies were not built successfully during the cloud deployment pipeline.

---

## 🧠 Future Roadmap & Iterations

- **Predictive Analytics:** Implement ML models for Churn Prediction and LTV Forecasting.
- **A/B Testing Simulator:** Create a module to probabilistically model the impact of strategic recommendations before live deployment.
- **Live API Integration:** Transition from synthetic data generation to live Snowflake/BigQuery pipeline connections.
- **Advanced Cohort Analysis:** Integrate full RFM (Recency, Frequency, Monetary) modeling capabilities.

---
*Built with product-led growth principles in mind. Designed for scale, impact, and clarity.*
