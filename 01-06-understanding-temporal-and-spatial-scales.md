# Lesson 6: Understanding Temporal and Spatial Scales in Water Modeling

**Objective:** Recognize the importance of temporal and spatial scales in model design and how GoldSim handles them.

When building any water management model, one of the most fundamental decisions you'll make, often implicitly, concerns the temporal (time) and spatial (area/location) scales of your analysis. These choices impact the model's complexity, data requirements, computational efficiency, and ultimately, its ability to answer your specific questions.

A model designed to predict hourly flood peaks across a small urban catchment will look very different from one intended to assess annual water supply reliability for a large river basin over decades. Understanding how GoldSim allows you to define and manage these scales is crucial for effective model design.

## Temporal Scales

Temporal scale refers to the time step of your simulation and the overall duration of the simulation period. Water management models commonly utilize various time steps, such as hourly, daily, monthly, or annual intervals. The choice of time step directly impacts the model's accuracy, computational speed, and data requirements.

### Common Time Steps

**Hourly or sub-hourly time steps** are used for highly dynamic processes like flood routing or stormwater runoff, demanding high-resolution input data.

**Daily steps** are common for many hydrological and water balance models.

**Monthly or annual steps** are often reserved for long-term planning or climate change impact assessments where broader trends are the focus.

### Simulation Durations

Similarly, simulation durations can range from:

- **Short-term** (days to weeks for operational forecasting)
- **Medium-term** (months to a few years for seasonal planning)  
- **Long-term** (decades to centuries for climate change studies or mine closure plans)

The most common time settings we see in water management models built in GoldSim historically are **1-day time steps** and run for **multiple years**, sometimes up to about 100 years.

## Spatial Scales

Spatial scale, on the other hand, dictates how you represent the physical extent and geographical features of your water system within the model. This representation influences model complexity and data needs.

### Spatial Representation Approaches

**Point-based representation:** Focusing on a single location like a well or a gauge.

**Lumped catchment/system approach:** An entire watershed is treated as a single, homogenous unit, aggregating all inputs and outputs.

**Distributed or gridded approach:** Divides the area into cells, allowing for explicit representation of spatial variability like varying soil types or topography, though this is computationally intensive.

**Network-based approach:** Models the system as interconnected nodes and links, such as river or pipe networks, emphasizing flow paths between discrete locations.

## GoldSim's Approach to Scales

GoldSim is highly flexible in handling various temporal and spatial scales, allowing you to tailor your model to the specific needs of your problem.

### Temporal Flexibility

GoldSim provides multiple layers of temporal flexibility, allowing you to control how the model progresses through time and how its logic responds to the simulation clock.

- **Simulation Settings:** At the highest level, you define the overall simulation duration (e.g., 100 years) and the basic time step (e.g., 1 Day). This sets the primary rhythm for the simulation.

- **Advanced Timestep Options:** GoldSim's **Advanced...** button in the Time tab provides access to sophisticated temporal control features, including:
  - Adding shorter (magnified) timesteps over specified periods for increased precision during critical events
  - Defining Capture Times to save detailed results at specific moments for analysis
  - Controlling unscheduled updates and their inclusion in time history results
  - Dynamically controlling the timestep during simulation based on model conditions
  - Setting calendar preferences (first day of week, first month of year) for time-aware modeling

- **Adaptive Time-Stepping:** GoldSim's engine can automatically insert unscheduled steps to accurately capture critical moments. This includes state-based events (e.g., a reservoir filling) and probabilistic events. For example, a Timed Event element can trigger an event based on a statistical distribution, forcing the model to stop at that exact random moment.

- **Localized Time Steps:** You can define different time steps for different parts of your model. For complex components that change rapidly, you can instruct their parent Container to use a shorter time step (e.g., 1 hour) than the rest of the model (e.g., 1 day), providing both accuracy and computational efficiency.

- **Time Series Element:** This element is designed to import and manage historical data. It can handle data at various time intervals and includes settings to interpolate or handle mismatched data appropriately.

- **Time-Aware Logic with Run Properties:** GoldSim includes built-in variables called run properties that make your model "aware" of the current time. This allows you to create expressions that change behavior based on the date (Month, Day) or elapsed time (Etime).

More advanced features, such as embedding entire Submodels with independent clocks or using looping Containers to add iterative dimensions, provide even greater control but are topics for a more advanced course.

### Spatial Flexibility

GoldSim is not inherently spatially aware. It does not have a built-in physical grid like specialized tools such as MODFLOW. Instead, GoldSim provides you with a blank slate, allowing you to define spatial relationships and discretizations explicitly within your model structure.

- **Containers and Hierarchical Modeling** enable you to represent different spatial units (e.g., sub-catchments, individual reservoirs) as modular components within your model.

- **Arrays and Lookups** can represent spatially varying parameters. For example, you can use a vector of values to define different soil properties for a series of sub-catchments or a Lookup Table to define rainfall intensity that varies by location.

- **A Note on Array-Based Networks:** While arrays (vectors and matrices) are powerful for defining distributed properties, they are generally not suitable for modeling complex flow networks that involve feedback (e.g., interconnected ponds where the flow from A affects B, and the level of B affects the flow from A). Attempting to do so often leads to impractical logic and circular reference errors.

- **Dedicated Flow Elements** such as Reservoirs, Pipes, and Aquifers are the proper tools for defining physical components and their spatial relationships within a network. These elements are designed to be linked together and, when necessary, can use specialized solvers to handle the complex feedback inherent in these systems.

You build the spatial representation that is most appropriate for your problem, rather than being constrained by a predefined grid.

## When to Simplify vs. Add Detail

A critical aspect of effective modeling is knowing when to simplify and when to add detail regarding temporal and spatial scales.

### You Should Simplify When:

- The problem's objectives do not require fine-scale detail
- High-resolution data is unavailable
- Computational resources are limited
- You are developing a conceptual understanding

### You Should Add Detail When:

- Precise timing or localized effects are crucial
- Accurate high-resolution data is available
- Rapidly changing processes are dominant
- Regulatory requirements dictate a specific level of granularity

The overarching goal is always to create the **simplest model that can still reliably answer your specific questions**, avoiding unnecessary complexity that might increase data demands, simulation times, and potential for errors without adding significant analytical value.

---

## Exercises

### Question 1
Which of the following best describes the primary impact of choosing a finer time step (e.g., hourly instead of daily) in a GoldSim water management model?

**A)** It generally simplifies the model's complexity and reduces data requirements.

**B)** It allows for a more precise representation of dynamic processes but demands more data and computational power.

**C)** It restricts the model to only annual or monthly simulation durations.

**D)** It makes the model inherently spatially aware, like MODFLOW.

**Correct Answer:** B) It allows for a more precise representation of dynamic processes but demands more data and computational power.

### Question 2
GoldSim is described as having a "blank slate" approach to spatial representation. What does this imply about GoldSim compared to tools like MODFLOW?

**A)** GoldSim has a built-in physical grid that automatically discretizes the spatial domain.

**B)** GoldSim is designed to only model single points in space, without any ability to represent areas or networks.

**C)** You define the spatial relationships and discretizations explicitly within your GoldSim model structure using elements like Containers, rather than being constrained by a predefined grid.

**D)** GoldSim automatically handles all spatial processes without any user input.

**Correct Answer:** C) You define the spatial relationships and discretizations explicitly within your GoldSim model structure using elements like Containers, rather than being constrained by a predefined grid.

### Question 3
You are developing a GoldSim model to assess the long-term water supply reliability of a large river basin over the next 50 years. Which combination of temporal and spatial scales would generally be a suitable starting point for this objective, prioritizing efficiency and relevant detail?

**A)** Hourly time step with a highly distributed (gridded) spatial representation.

**B)** Daily time step with a point-based spatial representation at a single gauge.

**C)** Monthly or annual time step with a lumped catchment spatial representation for major sub-basins.

**D)** Sub-hourly time step with a network-based representation of individual household pipes.

**Correct Answer:** C) Monthly or annual time step with a lumped catchment spatial representation for major sub-basins.
