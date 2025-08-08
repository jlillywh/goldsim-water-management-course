# Lesson 7: Using Historical Records for Probabilistic Simulation

**Objective:** Learn how to use multi-year historical time series as a basis for running probabilistic simulations to analyze uncertainty and risk in water management systems.

## Introduction: Beyond Single Historical Replays

When you have a long historical record of climate or hydrologic data, running your model with that single historical sequence tells you only one story—what happened in the past. While this is valuable for understanding system behavior under known conditions, it doesn't help you understand the range of possible future outcomes.

The goal of this lesson is to move beyond a single historical replay and use the entire historical record to understand the **range of possible future outcomes**. We'll treat the historical record as a statistical "blueprint" for the future, allowing us to explore uncertainty and assess risk more comprehensively.

This approach is particularly powerful because it leverages real data patterns while generating new scenarios that haven't occurred historically but are statistically consistent with the observed record.

## Why Historical Records Make Excellent Statistical Blueprints

Historical climate and hydrologic records contain embedded patterns that are difficult to capture with simple statistical models:

- **Seasonal cycles** and their year-to-year variations
- **Persistence and autocorrelation** (wet years tend to follow wet years, dry periods can persist)
- **Extreme events** and their realistic frequencies
- **Multi-variable correlations** (temperature and precipitation relationships)

Rather than trying to model these complex relationships mathematically, we can use the historical record directly as a template for generating new scenarios.

## Core Technique: Bootstrapping

**Bootstrapping** is a statistical technique that creates new datasets by randomly sampling from an existing dataset **with replacement**. In the context of climate and hydrologic modeling, this means creating new time series by randomly selecting values, years, or blocks of data from your historical record.

### How Bootstrapping Works

1. **Take your original dataset** (e.g., 60 years of daily streamflow data)
2. **Randomly select** complete years, seasons, or blocks of days from this record
3. **Allow replacement**, meaning the same historical period can be selected multiple times
4. **Combine** the selected periods to create a new time series of your desired length

### Key Benefits of Bootstrapping

- **Preserves statistical character**: Seasonality, variability, and autocorrelation patterns are maintained
- **Generates realistic scenarios**: New combinations of real data create plausible future sequences
- **Requires no parameter estimation**: Uses the data directly without fitting statistical distributions
- **Handles complex patterns**: Captures relationships that would be difficult to model parametrically

## GoldSim Implementation: Bootstrap Sampling in Time Series Elements

GoldSim makes bootstrapping straightforward through the Time Series element's stochastic sampling options. Here's how to implement it:

### Setting Up Bootstrap Sampling

1. **Create or import your historical Time Series** containing the long-term record
2. **In the Time Series properties**, set the element to be used as a **Stochastic** 
3. **Select the sampling method** as **"Bootstrap"** from the dropdown options
4. **Configure the sampling parameters**:
   - **Sampling unit**: Choose whether to sample by individual values, days, months, or years
   - **Block size**: Specify how large each sampled block should be
   - **Series length**: Define the length of each generated scenario

### Practical Example: Reservoir Risk Analysis

Let's work through a concrete example:

**Scenario**: You have a 60-year daily streamflow record and want to analyze the risk of a reservoir running dry during a 5-year drought period.

**Implementation**:

1. **Import the 60-year daily streamflow record** into a Time Series element named "Historical_Streamflow"
2. **Set the Time Series as Stochastic** with Bootstrap sampling
3. **Configure sampling by complete years** to preserve seasonal patterns
4. **Set each realization to generate 5 years** of daily data
5. **Run 1,000 Monte Carlo realizations** to explore the full range of possible 5-year scenarios
6. **Analyze results** to determine:
   - Probability of reservoir depletion
   - Expected minimum storage levels
   - Duration and severity of low-storage periods

### Bootstrap Sampling Options

**Annual Sampling**: 
- Samples complete calendar or water years
- Best for preserving annual water balance patterns
- Good for multi-year drought analysis

**Seasonal Sampling**: 
- Samples complete seasons (e.g., 3-month blocks)
- Preserves seasonal characteristics while allowing more mixing
- Useful for seasonal supply and demand analysis

**Monthly Sampling**: 
- Samples individual months
- Provides more scenario variety but may break some persistence patterns
- Good for monthly planning studies

**Block Sampling**: 
- Samples custom-length blocks (e.g., 30-day periods)
- Balances preservation of short-term patterns with scenario diversity
- Flexible for various analysis needs

## Practical Exercise: Streamflow Risk Analysis

### Step-by-Step Instructions

1. **Prepare your data**: Use a long-term daily streamflow record (at least 20-30 years for robust statistics)

2. **Create the Time Series element**:
   - Import your historical streamflow data
   - Name it "Bootstrap_Streamflow"
   - Set units appropriately (e.g., m³/s or cfs)

3. **Configure bootstrap sampling**:
   - Check "Use as Stochastic"
   - Select "Bootstrap" as the sampling method
   - Choose "Annual" sampling to preserve yearly patterns
   - Set scenario length to your analysis period (e.g., 10 years)

4. **Build your water system model**:
   - Connect the Bootstrap_Streamflow to your reservoir inflows
   - Include demands, losses, and operational rules
   - Add appropriate result elements to track storage levels

5. **Run probabilistic simulation**:
   - Set Monte Carlo realizations to 500-1000
   - Run the model to generate multiple scenarios

6. **Analyze results**:
   - Plot storage probability distributions
   - Calculate risk metrics (probability of shortfall)
   - Identify critical low-flow sequences

## Advanced Bootstrap Techniques

### Conditional Sampling

You can enhance bootstrap sampling by conditioning on specific criteria:

- **Climate state**: Sample preferentially from El Niño, La Niña, or neutral years
- **Antecedent conditions**: Weight sampling based on initial system state
- **Seasonal conditions**: Focus on wet, dry, or average seasonal patterns

### Multi-variate Bootstrapping

When working with multiple correlated variables (temperature, precipitation, streamflow), sample complete time periods to preserve correlations:

- Sample entire years to maintain annual temperature-precipitation relationships
- Use block sampling to preserve short-term correlations
- Consider spatial correlations when dealing with multiple stations

## When to Use Bootstrap vs. Parametric Generation

**Use Bootstrap sampling when**:
- You have a long, high-quality historical record (20+ years)
- Complex patterns exist that are difficult to model parametrically  
- You need to preserve exact historical event characteristics
- Computational efficiency is important

**Use parametric generation when**:
- Historical records are short or incomplete
- You need to explore conditions outside the historical range
- You want to incorporate climate change projections
- You need to model specific statistical properties precisely

## Model Documentation and Interpretation

### Document Your Approach

When using bootstrap sampling, clearly document:

- **Data source and period** of the historical record
- **Sampling method** and block size used
- **Number of realizations** and scenario length
- **Assumptions about stationarity** (is the historical record representative of future conditions?)

### Interpret Results Appropriately

- **Bootstrap scenarios represent variability within the historical record**—they don't account for non-stationarity or climate change
- **Results are conditional on the historical period**—different periods might yield different risk assessments  
- **Extreme events beyond the historical record** won't appear in bootstrap scenarios

## Conclusion: Leveraging Historical Data for Robust Analysis

Bootstrap sampling allows you to leverage long historical records to perform robust risk and uncertainty analysis without needing complex statistical models. By treating your historical data as a statistical blueprint, you can:

- **Generate thousands of realistic scenarios** from a single historical record
- **Preserve complex data patterns** that are difficult to model parametrically
- **Assess risks and probabilities** more comprehensively than single-scenario analysis
- **Make informed decisions** based on the full range of historical variability

This technique forms a bridge between simple historical analysis and fully synthetic weather generation. In cases where historical records are too short or unavailable, the next step is to move to fully synthetic weather generation techniques (such as using tools like PrecipGen), which can create statistically realistic weather sequences for any location based on limited historical data or climate model outputs.

## Additional Exercises

### Exercise 1: Drought Risk Assessment
Use a 30+ year precipitation record to assess the probability of consecutive dry years affecting agricultural water supply.

### Exercise 2: Flood Frequency Analysis  
Bootstrap daily streamflow data to estimate flood return periods and compare with traditional frequency analysis methods.

### Exercise 3: Multi-site Correlation
Sample simultaneously from multiple correlated streamflow stations to preserve spatial correlation patterns in a regional water system model.

---

## Required Assets

- **Long-term daily streamflow dataset** (minimum 20 years recommended)
- **Bootstrap_Example.gsm** - Example model demonstrating bootstrap setup
- **Risk_Analysis_Template.gsm** - Template for reservoir risk analysis
- Various screenshots showing Time Series bootstrap configuration options
