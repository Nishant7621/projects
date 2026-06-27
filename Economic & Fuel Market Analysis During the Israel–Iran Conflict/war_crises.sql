create database war_crisis;

use war_crisis;

select*from fuel_crisis;

-- 1. How many records are in the dataset?
SELECT COUNT(*) AS Total_Records
FROM fuel_crisis;


-- 2. How many countries are analyzed?
SELECT COUNT(DISTINCT Country) AS Total_Countries
FROM fuel_crisis;


-- 3. What is the date range of the crisis?
SELECT
MIN(Date) AS Start_Date,
MAX(Date) AS End_Date
FROM fuel_crisis;

-- Fuel Crisis Analysis
-- 4. Which countries have the highest average fuel prices?
SELECT
Country,
ROUND(AVG(Fuel_Price_Local),2) AS Avg_Fuel_Price
FROM fuel_crisis
GROUP BY Country
ORDER BY Avg_Fuel_Price DESC;

-- 5. Which countries experienced the largest fuel price increase?
SELECT
Country,
ROUND(AVG(Fuel_Price_Change_Percent),2) AS Avg_Fuel_Change
FROM fuel_crisis
GROUP BY Country
ORDER BY Avg_Fuel_Change DESC;


-- Oil Market Analysis
-- 6. Average WTI, Brent and OPEC prices
SELECT
ROUND(AVG(WTI_Crude_USD_per_barrel),2) AS Avg_WTI,
ROUND(AVG(Brent_Crude_USD_per_barrel),2) AS Avg_Brent,
ROUND(AVG(OPEC_Basket_USD_per_barrel),2) AS Avg_OPEC
FROM fuel_crisis;


-- 7. Highest oil price day
SELECT
Date,
WTI_Crude_USD_per_barrel
FROM fuel_crisis
ORDER BY WTI_Crude_USD_per_barrel DESC
LIMIT 10;

-- Inflation Analysis
-- 8. Which countries were most affected by inflation?
SELECT
Country,
ROUND(AVG(Inflation_Rate_Percent),2) AS Avg_Inflation
FROM fuel_crisis_data
GROUP BY Country
ORDER BY Avg_Inflation DESC;

-- 9. Global average inflation rate
SELECT
ROUND(AVG(Inflation_Rate_Percent),2) AS Global_Avg_Inflation
FROM fuel_crisis_data;


-- Shipping & Logistics Analysis
-- 10. Countries with highest shipping costs
SELECT
Country,
ROUND(AVG(Shipping_Cost_Index),2) AS Avg_Shipping_Cost
FROM fuel_crisis_data
GROUP BY Country
ORDER BY Avg_Shipping_Cost DESC;


-- 11. Maximum freight rate increase
SELECT
MAX(Freight_Rate_Change_Percent) AS Max_Freight_Increase
FROM fuel_crisis_data;

-- Crisis Impact Analysis
-- 12. Countries with highest crisis intensity
SELECT
Country,
ROUND(AVG(Crisis_Intensity_Index),2) AS Avg_Crisis
FROM fuel_crisis_data
GROUP BY Country
ORDER BY Avg_Crisis DESC;


-- 13. Daily crisis trend
SELECT
Date,
ROUND(AVG(Crisis_Intensity_Index),2) AS Crisis_Level
FROM fuel_crisis_data
GROUP BY Date
ORDER BY Date;

-- Stock Market Analysis
-- 14. Which countries suffered the biggest stock market decline?
SELECT
Country,
ROUND(AVG(Stock_Market_Index_Change),2) AS Avg_Market_Change
FROM fuel_crisis_data
GROUP BY Country
ORDER BY Avg_Market_Change ASC;

-- 15. Energy sector performance by country
SELECT
Country,
ROUND(AVG(Energy_Stock_Change),2) AS Avg_Energy_Stock_Change
FROM fuel_crisis_data
GROUP BY Country
ORDER BY Avg_Energy_Stock_Change DESC;

-- News Sentiment Analysis
-- 16. Average sentiment score by country
SELECT
Country,
ROUND(AVG(News_Sentiment_Score),2) AS Avg_Sentiment
FROM fuel_crisis_data
GROUP BY Country
ORDER BY Avg_Sentiment;

-- 17. Most negative sentiment days
SELECT
Date,
News_Sentiment_Score
FROM fuel_crisis_data
ORDER BY News_Sentiment_Score ASC
LIMIT 10;

-- Trading Volume Analysis
-- 18. Countries with highest oil trading volume
SELECT
Country,
ROUND(SUM(Trading_Volume_Million_Barrels),2) AS Total_Volume
FROM fuel_crisis_data
GROUP BY Country
ORDER BY Total_Volume DESC;


-- Advanced Analytics Queries

-- 19. Top 5 countries most affected by the crisis
SELECT
Country,
ROUND(AVG(Crisis_Intensity_Index),2) AS Crisis,
ROUND(AVG(Inflation_Rate_Percent),2) AS Inflation,
ROUND(AVG(Fuel_Price_Change_Percent),2) AS Fuel_Change
FROM fuel_crisis_data
GROUP BY Country
ORDER BY Crisis DESC, Inflation DESC
LIMIT 5;

-- 20. Overall Economic Stress Score
SELECT
Country,
ROUND(
AVG(
(Inflation_Rate_Percent +
Fuel_Price_Change_Percent +
Freight_Rate_Change_Percent)/3
),2
) AS Economic_Stress
FROM fuel_crisis_data
GROUP BY Country
ORDER BY Economic_Stress DESC;