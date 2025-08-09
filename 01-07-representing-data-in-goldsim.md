# Lesson 7: Representing Data in GoldSim

**Objective:** Learn how to use GoldSim's core data elements to represent the three most common types of data used in water management models: time series, functional relationships, and scalar parameters.

## Introduction

Every water management model is built upon data. The key to building an effective model in GoldSim is knowing how to translate real-world information into the appropriate GoldSim elements. This lesson provides a practical guide to the three most common data structures you will use.

## 1. Time Series Data → The Time Series Element

Time series are sequences of data points recorded over time. In water management, this is the most common data type you will encounter.

**Common Examples:** Historical daily rainfall, measured streamflow from a gauge, projected monthly temperatures.

**GoldSim Element:** The Time Series element is purpose-built for this. <img src="images\01_06_TimeSeriesElement.png" alt="Time Series Element" width="20%" align="right">

It allows you to import data from files or paste it in directly. Crucially, it lets you define how GoldSim should interpret the data (e.g., as instantaneous values or as constant values over the time step) and how to interpolate between points.

## 2. Functional Relationships → The Lookup Table Element

Often, one variable in a system is a direct function of another. This relationship is not a simple equation but is defined by a set of paired data points.

**Common Examples:** A reservoir's surface area as a function of its water level (a stage-storage curve), a pump's flow rate as a function of the pressure it's working against (a pump curve).

**GoldSim Element:** The Lookup Table element is the ideal tool for this. <img src="images\01_06_LookupTableElement.png" alt="Lookup Table Element" width="10%" align="right">

It allows you to define a one-to-one or many-to-one relationship between two or more variables. GoldSim then uses this table to look up the appropriate output value based on the current input value during the simulation.

## 3. Parameter Sets: Scalars, Vectors, and Matrices

While many model parameters are single values (scalars), GoldSim's real power comes from its ability to handle organized sets of data using vectors (1D arrays) and matrices (2D arrays). You define these using GoldSim's core input elements.

**Scalars:** A scalar is a single, fixed value that defines a property or constant. <img src="images\01_06_DataElement.png" alt="Data Element" width="20%" align="right">

**Common Examples:** A total catchment area in square kilometers; the initial volume of a pond.

**Vectors (1D Arrays):** A vector is an ordered list of values. This is useful when a parameter has different values for a set of related items.

**Common Example:** A list of runoff coefficients for different land use types (e.g., forest, urban, agricultural) within a catchment.

**Matrices (2D Arrays):** A matrix is a two-dimensional grid of values, ideal for representing parameters that vary spatially.

**Common Example:** A grid representing varying initial soil moisture levels or hydraulic conductivity values across a study area.

### Learning the Mechanics of Arrays

This lesson focuses on making you aware of the types of data you can represent. The detailed mechanics of creating, referencing, and manipulating vectors and matrices are covered extensively in other dedicated resources. For step-by-step instructions, refer to:

- **The GoldSim Help System: Using Vectors and Matrices:** The official documentation for array functionality.

- **The Contaminant Transport Course (Unit 2):** This unit provides a comprehensive, hands-on guide to working with vectors and matrices in GoldSim.

## Conclusion

Understanding this mapping is fundamental. By representing real-world data with the correct GoldSim element, you create a model that is transparent, robust, and easy to understand. As we progress through the course, you will see these three elements—Time Series, Lookup Tables, and Data—used repeatedly as the primary inputs for our models.

---

## Exercises

### Question 1
You have a 30-year record of historical daily streamflow from a USGS gauge that you need to use as an inflow to a reservoir. Which GoldSim element is the most appropriate for this data?

**A)** A Lookup Table element  
**B)** A Data element  
**C)** A Time Series element  
**D)** An Expression element

**Correct Answer:** C) A Time Series element

### Question 2
To model evaporation from a pond, you need to calculate the pond's surface area based on its current water level. A survey has provided a table of corresponding water levels and surface areas. What is the best GoldSim element to represent this relationship?

**A)** A Time Series element  
**B)** A Lookup Table element  
**C)** A Stochastic element  
**D)** A Data element

**Correct Answer:** B) A Lookup Table element
## Learning Objectives

*This section is required by the specification but was missing. Please update.*
## Context / Overview

*This section is required by the specification but was missing. Please update.*
## Technical Content

*This section is required by the specification but was missing. Please update.*
## Exercise / Activities

*This section is required by the specification but was missing. Please update.*
## Key Takeaways / Summary

*This section is required by the specification but was missing. Please update.*
