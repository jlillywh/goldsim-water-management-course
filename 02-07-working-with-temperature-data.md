# Lesson 5: Working with Temperature Data

**Objective:** Learn how to load and work with monthly temperature data using vectors, understand stair-stepping artifacts, and implement spline interpolation for smooth temperature transitions.

Air temperature can significantly influence water balance models through natural processes such as snowmelt, evapotranspiration, and water chemistry. Like daily precipitation time series discussed in Lesson 1, we can use Time Series elements to work with historical daily min and max temperatures, but rather than repeating those methods, we will now consider a different way to represent this data by using monthly averages defined in a Data element with a Vector data type.

## Data Element with a Vector Data Type

There are multiple ways to define monthly averages in GoldSim. For this lesson, we will use a **Data element with a vector data type** using an **Array Label Set** called "Months."

Before continuing with the lesson, you should take some time to acquaint yourself with Array Label Sets and how to work with vectors:

- **What are Arrays and Why Do We Need Them?** (GoldSim CT Module: Unit 2, Lesson 3)
- **Creating Vectors** (GoldSim CT Module: Unit 2, Lesson 4)  
- **Referencing Vectors and Manipulating Vectors Using Mathematical Operators** (GoldSim CT Module: Unit 2, Lesson 5)

## Create a New Model

You will need to create a new model to work through the exercises of this lesson. Follow the steps below to get started:

1. Start GoldSim to create a new model file.
2. Save the model with the name **"Monthly Avg Temp.gsm."**
3. Open the **Simulation Settings** and change the Time Basis to **Calendar Time**.
4. Set the start time to **1 Jan 2023** and the end time to **1 Jan 2025**
5. Set the Basic Step to **"Days"**.

## Load Temperature Data into the Model

For this lesson, we will work with monthly temperature **"normals,"** which are the daily measured temperatures averaged over each month for multiple years (see Table 1).

The data used in this lesson was measured at the **Salt Lake City International Airport from 1991-2020**, which can be downloaded from here.

### Table 1 - Average Daily Min/Max Temperatures at Salt Lake City Intl Airport (30-year avg)

| Month | Tmin (°F) | Tmax (°F) |
|-------|-----------|-----------|
| Jan   | 24.2      | 38.6      |
| Feb   | 28.6      | 44.7      |
| Mar   | 36.3      | 55.3      |
| Apr   | 41.8      | 61.9      |
| May   | 50.4      | 72.6      |
| Jun   | 59.1      | 84.1      |
| Jul   | 68.2      | 94.0      |
| Aug   | 66.6      | 91.7      |
| Sep   | 56.3      | 80.6      |
| Oct   | 43.6      | 65.5      |
| Nov   | 32.8      | 50.7      |
| Dec   | 25.3      | 39.0      |

Follow these steps to load the temperature data into the model:

1. Create a new **Data element**.
2. Name the element ID **"Tmin_Table"**.
3. Define the **Display unit** as "F" for Fahrenheit (or use a different unit of C or K if you are using different data for this lesson).

![Tmin Table Data Element](images/TminTableDataElement.png)

4. Assign the **Type** to be a **vector** with the **Array Label Set** of "Months."

![Data Type Dialog](images/DataTypeDialog.png)

5. Copy the data from the table above into a spreadsheet so it is easy to copy and paste into GoldSim.
6. Once the data is in a spreadsheet, copy and paste the **Tmin column** into the data table of the "Tmin_Table" Data element.

![Data Copy Process](images/DataCopyProcess.png)

7. **Repeat this process for Tmax** using another Data element.

Now that the data is loaded into the model, you are ready to start using the data to work through the exercises.

## Understanding the Stair-Stepping Artifact

When you use monthly average data in a model with a time step shorter than one month (e.g., daily), the results will exhibit an artificial **stair-stepping effect**, as shown in the chart.

![Stair-Stepping Artifact](images/TemperatureStairStepping.png)

This occurs because the value for each month remains constant throughout that entire period, creating discrete jumps at the start of each new month.

This behavior is a direct consequence of the way the model references the monthly data. In this case, the temperature input (or other climate variable) is applied uniformly for each month, rather than varying continuously.

While this approach is sufficient for many purposes, it does introduce artifacts that might not accurately reflect natural, gradual transitions in the real world.

## Introduction to Spline Interpolation

To address the stair-stepping artifact discussed above, we can use **interpolation methods** to create smooth transitions between monthly values. While several approaches exist, **spline interpolation** provides the most realistic representation for natural phenomena like temperature by producing smooth, continuous curves that better reflect how temperature changes gradually throughout the year.

**Cubic spline interpolation** fits a continuous function to the monthly data points, creating natural-looking curves that eliminate the artificial jumps between months. This approach is particularly well-suited for temperature data because it:

- Creates smooth transitions that mirror real-world temperature patterns
- Maintains the original monthly average values at the midpoints
- Produces realistic intermediate values throughout each month

In the following exercise, you will implement cubic spline interpolation using a pre-built GoldSim function to transform your stair-stepped temperature data into smooth, continuous curves.

## Alternative Approach: The Cosine Curve Method

While spline interpolation provides an excellent solution for smooth temperature transitions, there's another approach that leverages the **naturally cyclical nature of annual temperature patterns**: fitting a **cosine (or sinusoidal) curve** to represent the entire annual temperature cycle.

This method recognizes that temperature follows a predictable seasonal pattern that can be mathematically described as a sinusoidal wave. Rather than interpolating between discrete monthly values, we can derive the parameters of a continuous mathematical function that captures the annual temperature cycle.

### The Cosine Function for Temperature

The basic form of a cosine function for temperature is:

**T(t) = T_avg + A × cos(2π × (t - t_shift) / 365)**

Where:
- **T_avg** = Annual average temperature
- **A** = Amplitude (half the difference between maximum and minimum annual temperatures)  
- **t** = Day of year (1-365)
- **t_shift** = Phase shift (day of year when temperature is at its peak)

### Deriving the Parameters

To implement this method, you need to calculate three key parameters from your monthly data:

1. **Annual Average (T_avg):** The mean of all 12 monthly values
2. **Amplitude (A):** Half the difference between the highest and lowest monthly values
3. **Phase Shift (t_shift):** The day of year corresponding to the peak temperature month

For example, with Salt Lake City data where July (day ~196) has the highest temperature:
- If the annual range is 70°F (94°F max - 24°F min), the amplitude would be 35°F
- The phase shift would be approximately 196 days (mid-July)

### Building the Expression in GoldSim

Once you have the parameters, you can create a GoldSim Expression element that calculates temperature for any day of the year:

```
T_avg + Amplitude * cos(2*pi() * (elapsed_days - phase_shift) / 365)
```

This single expression provides a smooth, continuous temperature curve that naturally captures the seasonal cycle without requiring interpolation between discrete points.

### Advantages of the Cosine Method

- **Physically realistic:** Mimics the natural sinusoidal pattern of seasonal temperature variation
- **Mathematically elegant:** Single continuous function covers the entire year
- **Computationally efficient:** No need for interpolation calculations
- **Predictable behavior:** Smooth, symmetric seasonal transitions

### 💭 Food for Thought

Consider how you would implement the parameter calculations using GoldSim's vector functions:

- How would you use the `vavg()` function to calculate the annual average from your monthly temperature vector?
- What combination of `vmax()` and `vmin()` functions would give you the amplitude?
- How might you determine the phase shift if you know that July corresponds to array index 7 in your monthly data vector?
- Could you create a more sophisticated version that accounts for the fact that peak temperature often occurs slightly after the summer solstice?

Think about whether this approach would work better for certain geographic locations or climate types compared to spline interpolation.

---

## Exercises

### Exercise 1: Basic Temperature Referencing
1. Create a new Expression element called **"Tmin_Monthly"** with Display Units of Celsius ("C").
2. Write an equation that references the Data element "Tmin_Table" and returns a value corresponding to the current calendar month as the simulation progresses through time.
3. This requires the use of the built-in run property called **"Month"**.
   - For more information about GoldSim's run properties, please refer to: [Using Run Properties to Explicitly Reference Time](https://support.goldsim.com)
4. Run the model and plot a time history of the Expression output "Tmin" to produce a chart like that shown in the screen capture below.

![Monthly Temperature Output](images/MonthlyTemperatureOutput.png)

### Exercise 2: Combined Temperature Display
Repeat the above exercise for Tmax and include both outputs in a single **Time History Result element**.

### Exercise 3: Spline Interpolation Implementation
1. Create a new Container named **"Interpolation_Functions."** This will contain the interpolation functions needed to smooth the temperature data.

2. Access the **"Spline Interpolation for Monthly Data"** model from the GoldSim Help Center's online library at [Spline Interpolation for Monthly Data](https://support.goldsim.com/hc/en-us/articles/360023299754-Spline-Interpolation-for-Monthly-Data). Search for "spline interpolation" to find the example model.

3. Open the model from the Help Center, locate the **"Cubic_Spline_For_Monthly_Data"** container, copy it, and paste it into your **Interpolation_Functions** container.

4. Rename the pasted container to **"Tmin_Spline."**

5. Inside the **Tmin_Spline** container, locate the **"Input_Table"** element and link it to your **Tmin_Table** element.
   - **Important:** You must cast off the temperature units by modifying the input expression to be: `Tmin_Table / 1 F` (or use your model's temperature unit). The spline function operates on unitless values.

6. Navigate to the **"Output"** element inside the **Tmin_Spline** container and assign it the correct Display Unit of **'F'** (or your model's temperature unit).

7. **Repeat steps 3-6 for Tmax** by creating a second copy of the spline container:
   - Copy the **Cubic_Spline_For_Monthly_Data** container again and paste it into **Interpolation_Functions**
   - Rename this copy to **"Tmax_Spline"**
   - Link its **Input_Table** to your **Tmax_Table** using the same unit casting approach: `Tmax_Table / 1 F`
   - Set the **Output** element's Display Unit to **'F'**

8. Create a new **Time History Result** element to plot the **Output** from both the **Tmin_Spline** and **Tmax_Spline** containers, showing the smooth interpolated temperature curves.

You should be able to produce a chart like this:

![Interpolated Temperature Output](images/InterpolatedTemperatureOutput.png)

### Exercise 4: Temperature Range Analysis
1. Create an **Extrema element** to calculate the maximum difference between Tmax and Tmin.
   - Refer to [Using the Extrema Element](https://support.goldsim.com) to learn more about this element.
2. **What is the peak difference between Tmax and Tmin in Celsius?**
   - Hint: The units for temperature differentials are defined using a different unit (Cdeg or Fdeg), as described in our Help Documentation: [Dealing with Temperature Units](https://support.goldsim.com)

---

## Required Assets

- **Salt Lake City Temperature Data.xlsx** - Monthly temperature normals data
- **Monthly Avg Temp.gsm** - Base model file for exercises
- Access to **GoldSim Help Center** online library for spline interpolation examples
- Various images showing data loading, stair-stepping artifacts, and interpolated results
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
