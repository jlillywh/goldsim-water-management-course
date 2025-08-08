# Lesson 1: Working with Precipitation Data

**Objective:** Learn how to incorporate precipitation data into GoldSim models using Lookup Tables and Time Series elements, understanding the critical distinction between rates and quantities.

Climate factors such as precipitation and temperature play a crucial role in water management models. Understanding and accurately incorporating these variables into your model is essential for realistic and reliable simulations.

In this lesson, we will explore how to build a dynamic model using simple inputs and then refine it by transitioning to more detailed data.

## Why Precipitation Data Matters

Precipitation data is fundamental input that influences various water systems, including stormwater management, drinking water supplies, and mining operations. By mastering the techniques for working with climate data early on, you will be better prepared to build comprehensive and accurate models in subsequent units.

Additionally, it is crucial to avoid overcomplicating your models. Simple conceptual models for climate drivers can often be more effective and easier to manage. Each modeling project should be treated individually, based on its specific needs.

## Three Methods for Entering Precipitation Data

This lesson will walk through **3 different ways** to enter precipitation data into a GoldSim model:

1. **Lookup Tables** for monthly precipitation
2. **Time Series elements** with proper rate/quantity handling
3. **Manual rate/quantity conversions** using expressions

## Method 1: Using Lookup Tables for Monthly Precipitation

To set up monthly precipitation totals in a 1D lookup table, follow these steps:

1. Create a new **Data element** and give it a suitable name, such as "Precipitation_Table".
2. Define the **Display unit** for the precipitation data, such as inches or millimeters, based on your data.
3. Set the **Type** of the Data element as a **1D Lookup Table**.
4. In the Lookup Table Editor, define the **X-axis values** as the months of the year (January to December).
5. Enter the corresponding **precipitation values** for each month in the Y-axis column.
6. You can also add additional columns to the lookup table to include other relevant information, such as the average temperature or any other data you want to associate with the precipitation values.
7. Save the changes to the Data element.

By setting up the monthly precipitation totals in a 1D lookup table, you can easily access and analyze the precipitation data for different months throughout the year.

## Method 2: Understanding Rates vs. Quantities in Time Series

Climate data is sometimes recorded at time intervals that don't align with the model's time step. This discrepancy becomes particularly relevant when defining precipitation data, as it's essential to consider how it's represented.

### Critical Distinction: Rates vs. Quantities

Precipitation data is commonly represented in one of two ways:

- **Average precipitation rate** distributed over time intervals (units of length / time)
- **Total precipitation depth (quantity)** reported at the end of each time interval (units of length)

The Time Series element makes it easy to work with either type efficiently.

### Important Warning About Monthly Rates

**Be aware that monthly or annual rates must account for changing time periods and therefore, should be avoided.**

For example, let's say we have a monthly average precipitation rate for February defined as "10 in/mon". In GoldSim, this is the same as saying "10 inches per 30.4375 days" because the name "mon" is a constant unit defined as 30.4375 days.

If your expectation is that this would result in "10 inches per number of days in Feb," then you will get unexpected results.

Because this type of conversion can often lead to mistakes, it is recommended that **precipitation quantities should be defined** when working with time series with monthly and annual time intervals.

### Exercise: Setting Up Monthly Precipitation Time Series

The Time Series element simplifies the process of correctly defining time series data by providing built-in functionality to calculate rates of change when the user chooses to represent the data as "Change over previous/next time interval".

Follow these steps to define monthly precipitation time series data using a Time Series element:

1. Open the model created during Lesson 1 and save it as a new model named **"Monthly Precip TS.gsm"**.
2. Create a new **Time Series element** named "Precip_Monthly" with units of "mm".
3. Open the spreadsheet used in the previous lesson and navigate to the worksheet called "Monthly_Totals," which can also be downloaded from here: **Salt Lake City Weather Data.xlsx**
4. Copy and paste the monthly dates and values into the time series you just created.
5. Change the **Represents choice** to "Change over previous time interval".
6. Click on the **"More…"** button.
7. Check the box **"Enable Rate of Change output"**

![Time Series Element Properties](images/TimeSeriesProperties.png)

Now you can take advantage of a secondary property of the element "Rate of Change" will turns out to be the rate of precipitation automatically calculated.

## Method 3: Manual Conversion Between Rates and Quantities

Converting the precipitation between quantities and average rates can also be done using an Expression like this:

![Rate Calculation Expression](images/RateCalculationExpression.png)

The screen capture above shows how an Expression element is used to convert precipitation quantities to rates.

This lesson will help you understand how to use the functionality of the Time Series element to avoid any pitfalls related to changing time intervals.

## Observing Stair-Stepping Artifacts in Monthly Data

When you use monthly average data in a model with a time step shorter than one month (e.g., daily), the results will exhibit an artificial **stair-stepping effect**, as shown in the chart.

![Stair-Stepping Artifact](images/StairSteppingArtifact.png)

This occurs because the value for each month remains constant throughout that entire period, creating discrete jumps at the start of each new month.

This behavior is a direct consequence of the way the model references the monthly data. In this case, the temperature input (or other climate variable) is applied uniformly for each month, rather than varying continuously.

While this approach is sufficient for many purposes, it does introduce artifacts that might not accurately reflect natural, gradual transitions in the real world.

### How to Address This in Future Models

In the next lesson (Lesson 3: Working with Temperature Data), you will learn to address these stair-stepping artifacts using **interpolation methods**, such as:

- **Linear interpolation:** Creates straight-line transitions between monthly values.
- **Spline interpolation:** Produces smoother, more natural curves by fitting a continuous function to the data points.

These methods allow you to refine your model further and reduce artifacts, ensuring the results better represent continuous, dynamic systems.

For now, recognize this behavior as a natural limitation of using time-stepped simulations with discrete data, and keep it in mind when interpreting your results.

---

## Exercises

### Exercise 1: Data Element Comparison
Work with a Data element to simulate the average precip rate as constant over next and interpolated and compare the two using a Time History result plots.

### Exercise 2: Lookup Table Implementation
Use a lookup table to define monthly average precipitation for [example site location] then use an expression element to apply the monthly average values over the course of 1 calendar year.

### Exercise 3: Rate Conversion
Convert quantities to rates by dividing each monthly depth value by the time in each calendar month of the simulation.

---

## Required Assets

- **Salt Lake City Weather Data.xlsx** - Monthly precipitation data for exercises
- **Monthly Precip TS.gsm** - Example model file
- Various image assets for Time Series properties and rate calculations

