# 🍽️ Restaurant Analytics Dashboard

## 📌 Project Overview
An end-to-end data analytics project analyzing **11+ million restaurant orders** across multiple branches in Egypt. The project covers data ingestion, SQL transformation, and interactive Power BI dashboards.

## 🛠️ Tech Stack
- **SQL Server** — Data storage & transformation
- **Python (pandas, pyodbc)** — Data ingestion (CSV + JSON)
- **Power BI** — Interactive dashboards & DAX measures

## 📊 Dashboard Pages
| Page | Description |
|------|-------------|
| Overview | High-level KPIs: Revenue, Orders, Customers, Rating |
| Financial Performance | Net Revenue, Discount Impact, Revenue by Branch & Category |
| Customer Behavior | Peak Hours, Weekday vs Weekend, Order Type distribution |
| Branch & Operations | Branch comparison, Peak Hours, Avg Order Value |
| Customer Satisfaction | Rating distribution, trends, and order type analysis |
## 📸 Dashboard Preview
![Overview](images/overview.png)
![Financial Performance](images/financial.png)

## 🔍 Key Insights
- **القاهرة** is the highest revenue branch with **0.47bn EGP**
- **Cash** is the dominant payment method at **40.53%**
- **عصير مانجو** is the most ordered item
- Only **1.9%** of ratings are below 3 — indicating high customer satisfaction
- **Weekday orders (2.15M)** slightly outperform Weekend orders (1.94M)

## 📁 Project Structure
├── SQL/
│   ├── 01_create_table.sql
│   └── 02_alter_table.sql
├── Dashboard/
│   └── Restaurant_Dashboard.pbix
└── README.md
## 🚀 How to Run
1. Run SQL scripts in order (`01` → `02`)
2. Load data using Python scripts
3. Open `.pbix` file in Power BI Desktop
4. Connect to your SQL Server instance
