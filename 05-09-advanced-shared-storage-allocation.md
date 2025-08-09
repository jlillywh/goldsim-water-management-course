# Lesson 3: Advanced Shared Storage Allocation

## Learning Objectives

By the end of this lesson, you will be able to:
- Model multi-owner reservoir systems using GoldSim arrays to track individual storage accounts
- Implement priority-based water allocation using the `Allocator` element
- Understand water rights systems and their impact on shortage allocation
- Analyze the interaction between storage ownership and withdrawal priorities
- Configure and interpret complex multi-stakeholder reservoir models

## Context: From Single-User to Multi-Stakeholder Systems

In Lessons 1 and 2, we modeled reservoirs serving single purposes with unified management objectives. However, many real-world reservoirs serve multiple owners with competing interests, different legal rights, and varying priorities during shortages. Understanding how to model these complex **shared storage systems** is essential for professional water management.

**Shared reservoir systems** are commonplace in:
- **River basin management**: Multiple irrigation districts sharing storage in a federal reservoir
- **Municipal water banking**: Cities purchasing storage space in regional facilities
- **Multi-purpose projects**: Balancing flood control, water supply, hydropower, and environmental uses
- **Water markets**: Enabling trading of storage rights and water allocations
- **Drought management**: Implementing shortage sharing agreements among stakeholders

This lesson addresses the most challenging aspect of water management: **how to fairly and legally allocate limited water resources among competing users**. The techniques you'll learn form the foundation for water rights modeling, shortage management, and multi-stakeholder planning processes.

## Context / Overview

*This section is required by the specification but was missing. Please update.*
## Technical Content

### Conceptual Framework: The Reservoir as a Multi-Account Bank

The most intuitive way to understand shared storage is through a banking analogy. A shared reservoir operates like a bank with multiple account holders:

**The Physical Vault**: The total water volume in the reservoir represents the bank's vault—a single physical space containing all the water.

**Individual Accounts**: Each stakeholder (irrigation district, municipality, industrial user) has a separate "account" representing their legal ownership of a portion of the stored water.

**Deposits and Interest**: Inflows to the reservoir are distributed among account holders according to pre-defined ownership percentages. Evaporation losses are typically shared proportionally, like negative interest applied to all accounts.

**Withdrawal Rules**: Users can only withdraw water from their own accounts, but the actual water comes from the common physical pool.

**Overdraft Protection**: When an account balance reaches zero, that user cannot make additional withdrawals, even if other accounts have positive balances.

This accounting system enables precise tracking of water ownership while maintaining the operational and economic benefits of shared physical storage.

### Array-Based Storage Accounting

GoldSim's **array functionality** provides the ideal tool for modeling multi-owner storage systems. Instead of defining reservoir volume as a single scalar value, we can define it as a **vector** where each element represents a different owner's account.

#### Array Configuration

A three-owner reservoir might be configured as:
```
Reservoir_Volume[3] = {Owner_A_Volume, Owner_B_Volume, Owner_C_Volume}
```

Where:
- `Owner_A_Volume` tracks water belonging to the first stakeholder
- `Owner_B_Volume` tracks the second stakeholder's water
- `Owner_C_Volume` tracks the third stakeholder's water
- `Total_Volume = sum(Reservoir_Volume)` represents the physical water in the reservoir

#### Proportional Allocation of Gains and Losses

**Inflow Distribution**: New water entering the reservoir is typically allocated based on predetermined ownership percentages:
```
Owner_A_Inflow = Total_Inflow × Owner_A_Percentage
Owner_B_Inflow = Total_Inflow × Owner_B_Percentage
Owner_C_Inflow = Total_Inflow × Owner_C_Percentage
```

**Evaporation Sharing**: Evaporation losses are usually shared proportionally based on current account balances:
```
Owner_A_Evap = Total_Evaporation × (Owner_A_Volume / Total_Volume)
Owner_B_Evap = Total_Evaporation × (Owner_B_Volume / Total_Volume)
Owner_C_Evap = Total_Evaporation × (Owner_C_Volume / Total_Volume)
```

This proportional sharing ensures that all owners bear evaporation losses in proportion to their current storage holdings.

#### Account Balance Constraints

**Non-Negative Balances**: Individual accounts cannot go negative. If a withdrawal request would overdraw an account, the actual withdrawal is limited to the available balance.

**Physical Constraints**: The sum of all accounts cannot exceed the reservoir's physical capacity. When the reservoir is full, additional inflows become spill regardless of individual account balances.

### Water Rights and Priority-Based Allocation

When water supply is insufficient to meet all demands, **water rights systems** determine allocation priorities. The most common system in the western United States is **prior appropriation** ("first in time, first in right"), where earlier established rights have higher priority during shortages.

#### The Allocator Element Framework

GoldSim's `Allocator` element provides sophisticated tools for priority-based allocation:

**Supply Input**: The total amount of water available for allocation (limited by physical availability, operational constraints, or legal restrictions).

**Demand Inputs**: Withdrawal requests from each stakeholder, typically representing their full water needs or contractual entitlements.

**Priority Rankings**: A numerical or date-based system that determines allocation order during shortages.

**Allocation Outputs**: The actual water deliveries to each user, which may be less than their demands during shortage periods.

#### Priority System Implementation

**Date-Based Priorities**: Rights established earlier receive higher priority:
```
Priority_Rank = Date_of_First_Use (earlier dates = higher priority)
```

**Numerical Priorities**: Direct ranking system where lower numbers indicate higher priority:
```
Priority_Rank = 1, 2, 3, ... (1 = highest priority)
```

**Conditional Priorities**: Priority may change based on system conditions, water use types, or seasonal factors.

#### Shortage Allocation Logic

During shortages, the `Allocator` element implements a **"fill-the-senior-right-first"** approach:

1. **Highest Priority**: The most senior right receives their full demand or the entire available supply, whichever is smaller
2. **Remaining Rights**: Any remaining supply is allocated to the next most senior right
3. **Junior Rights**: The most junior rights are curtailed first and most severely

This creates a **non-linear shortage impact** where junior rights may be completely cut off while senior rights continue receiving full allocations.

### Integration of Storage Accounts and Allocation Priorities

The interaction between storage ownership and allocation priorities creates complex system dynamics:

#### Storage vs. Priority Conflicts

**High Storage, Low Priority**: A user with substantial stored water but junior rights may be unable to withdraw during shortages if the allocation system prioritizes releases for senior right holders.

**Low Storage, High Priority**: A senior right holder with minimal stored water may receive priority access to available water, even if other users have larger account balances.

#### Operational Strategies

**Conservative Storage Management**: Junior right holders may maintain higher storage levels to buffer against priority-based curtailments.

**Coordinated Operations**: Stakeholders may develop agreements that balance storage ownership with allocation priorities to improve overall system efficiency.

**Conditional Sharing**: Some systems modify allocation priorities based on storage levels, encouraging efficient use while protecting senior rights.

## Exercise: Exploring Multi-Owner Reservoir Dynamics

This exercise uses a sophisticated pre-built model to explore how storage allocation and water rights interact in complex multi-stakeholder systems.

### Exercise Overview

The `Shared_Reservoir.gsm` model represents a regional water supply reservoir serving three distinct user groups:
- **Municipal District**: Urban water supply with steady year-round demands
- **Irrigation District**: Agricultural user with seasonal demand patterns
- **Industrial User**: Manufacturing facility with constant process water needs

Each user has different storage ownership percentages, water right priorities, and demand patterns, creating realistic management challenges.

### Part 1: Model Exploration and Baseline Analysis

1. **Open and Examine the Model**
   - Open `Shared_Reservoir.gsm`
   - Navigate to the **"System Overview"** dashboard to understand model structure
   - Review the **"Inputs"** dashboard to see user-configurable parameters

2. **Understand the User Profiles**
   - **Municipal District**: 
     - Storage ownership: 50% of reservoir capacity
     - Steady demand: 0.6 m³/s year-round
     - Date of first use: 1925 (senior right)
   - **Irrigation District**:
     - Storage ownership: 35% of reservoir capacity  
     - Seasonal demand: 0.2-1.2 m³/s (peak in summer)
     - Date of first use: 1940 (intermediate right)
   - **Industrial User**:
     - Storage ownership: 15% of reservoir capacity
     - Constant demand: 0.3 m³/s
     - Date of first use: 1965 (junior right)

3. **Run Baseline Scenario**
   - Execute the model with default settings
   - Navigate to **"Results"** dashboard
   - Examine key output plots:
     - **Storage by Owner**: Individual account balances over time
     - **Deliveries by Owner**: Actual water deliveries vs. demands
     - **Shortage Analysis**: Periods when demands exceed deliveries

### Part 2: Priority System Analysis

4. **Analyze Default Priority Impacts**
   - Identify periods when total demand exceeds available supply
   - Note which users experience the most severe curtailments
   - Observe how shortage allocation follows water rights seniority

5. **Test Priority Sensitivity**
   - Return to **"Inputs"** dashboard
   - Modify **"Date of First Use"** to reverse priorities:
     - Municipal: 1965 (make junior)
     - Irrigation: 1940 (keep intermediate)  
     - Industrial: 1925 (make senior)
   - Re-run model and compare results

6. **Equal Priority Scenario**
   - Set all three users to the same "Date of First Use" (e.g., 1945)
   - Analyze how allocation changes when priority differences are eliminated
   - Note the pro-rata sharing during shortage periods

### Part 3: Storage Ownership vs. Allocation Analysis

7. **Ownership Impact Assessment**
   - Return to default priorities
   - Modify storage ownership percentages:
     - Municipal: 20% (reduce from 50%)
     - Irrigation: 40% (increase from 35%)
     - Industrial: 40% (increase from 15%)
   - Analyze how ownership changes affect storage security and shortage vulnerability

8. **Extreme Scenario Testing**
   - Create a "worst-case" scenario:
     - Reduce total inflows by 30% (if model allows)
     - Increase all demands by 20%
   - Observe system behavior under severe stress conditions
   - Identify critical failure points and user impacts

### Part 4: Management Strategy Evaluation

9. **Conservation Impact Analysis**
   - Test demand reduction scenarios:
     - Reduce Municipal demand by 15% (conservation programs)
     - Reduce Irrigation demand by 25% (efficiency improvements)
   - Evaluate benefits to overall system reliability

10. **Storage Strategy Assessment**
    - Examine how different initial storage conditions affect outcomes
    - Consider seasonal timing of storage drawdown and recovery
    - Identify optimal storage management strategies for each user type

### Analysis Questions

After completing the exercise scenarios, address these critical questions:

**Priority System Impacts**:
1. How do water rights priorities affect shortage distribution among users?
2. What are the advantages and disadvantages of the prior appropriation system?
3. Under what conditions might alternative allocation methods be preferable?

**Storage vs. Allocation Interactions**:
4. How does storage ownership percentage interact with allocation priority?
5. Can a user with junior rights but large storage holdings maintain supply security?
6. What strategies might junior right holders adopt to manage shortage risk?

**System Optimization**:
7. How might the stakeholders modify operational agreements to improve overall efficiency?
8. What role could water markets or trading play in this system?
9. How do seasonal demand patterns affect optimal storage allocation strategies?

## Professional Application

Advanced shared storage allocation is essential for multiple aspects of professional water management:

**Water Rights Administration**: Accurate modeling of priority systems ensures compliance with legal requirements and supports water rights adjudication processes.

**Interstate Compact Management**: Many river systems are governed by compacts that specify storage and allocation arrangements among states, requiring sophisticated modeling capabilities.

**Water Banking and Markets**: Storage sharing arrangements enable water banking systems where users can store water in good years for use during droughts or sell storage space to other users.

**Drought Management**: Shared storage models help develop equitable drought response plans that balance legal requirements with practical operational constraints.

**Infrastructure Investment**: Understanding storage allocation dynamics helps stakeholders evaluate the benefits and costs of storage capacity expansions or operational improvements.

**Conflict Resolution**: Quantitative analysis of allocation alternatives provides an objective foundation for negotiating agreements among competing stakeholders.

## Key Takeaways

- **Shared storage systems require dual accounting** for physical water volumes and individual ownership accounts
- **GoldSim arrays enable efficient modeling** of multi-owner storage systems within single reservoir elements  
- **Water rights priorities create non-linear shortage impacts** where junior users may be completely curtailed while senior users receive full allocations
- **The Allocator element provides sophisticated tools** for implementing complex priority-based allocation systems
- **Storage ownership and allocation priorities interact** in complex ways that require careful analysis and management
- **Realistic multi-stakeholder models** must account for different demand patterns, priorities, and operational strategies among users
- **Scenario analysis reveals system vulnerabilities** and helps identify strategies for improving overall system performance

## Exercise / Activities

*This section is required by the specification but was missing. Please update.*
## Key Takeaways / Summary

*This section is required by the specification but was missing. Please update.*
## Quiz

Test your understanding of advanced shared storage allocation concepts:

1. **Array-Based Storage Modeling**: What is the primary advantage of using GoldSim arrays to model multi-owner reservoir storage?
   - A) Arrays reduce computational time for large models
   - B) Arrays enable tracking individual owner accounts within a single reservoir element
   - C) Arrays automatically enforce water rights priorities
   - D) Arrays eliminate the need for separate inflow calculations

2. **Priority-Based Allocation**: In a prior appropriation water rights system, during a shortage, which user receives water first?
   - A) The user with the largest storage account
   - B) The user with the highest current demand
   - C) The user with the earliest date of first use (senior right)
   - D) The user with the largest ownership percentage

3. **Evaporation Loss Sharing**: How are evaporation losses typically allocated among multiple reservoir owners?
   - A) Equally among all owners regardless of storage levels
   - B) Proportionally based on current individual account balances
   - C) Only charged to the owner with the largest account
   - D) Based on each owner's historical average storage

4. **Allocator Element Function**: When total water supply is less than total demand, how does the GoldSim Allocator element distribute available water?
   - A) Pro-rata to all users based on their demand percentages
   - B) Equally among all users regardless of demand or priority
   - C) According to priority rankings, filling higher-priority demands first
   - D) Based on storage account balances, with larger accounts receiving more

**Answers**: 1-B, 2-C, 3-B, 4-C

## Assets Needed

### GoldSim Model Files
- `Shared_Reservoir.gsm`: Comprehensive multi-owner reservoir model with interactive dashboard for exploring storage allocation and priority systems
- `Simple_Allocation_Demo.gsm`: Simplified two-user model for understanding basic allocation concepts

### Data Files Required
- `Multi_User_Demands.xlsx`: Demand time series for different user types (municipal, irrigation, industrial) with realistic seasonal patterns
- `Shortage_Analysis_Data.xlsx`: Historical shortage periods for calibrating and validating allocation model behavior

### Images Required
- `shared-storage-concept-diagram.png`: Conceptual illustration showing reservoir as multi-account bank with individual user accounts
- `array-based-modeling-screenshot.png`: GoldSim screenshot showing array configuration for multi-owner reservoir storage
- `allocator-element-configuration.png`: Screenshot of Allocator element setup with priority rankings and demand inputs
- `priority-allocation-flowchart.png`: Flowchart illustrating how priority-based allocation works during shortage conditions
- `storage-vs-priority-interaction.png`: Diagram showing complex interactions between storage ownership and allocation priorities

### Dashboard Components
- `Multi_Owner_Dashboard.png`: Screenshot of comprehensive results dashboard showing storage accounts, deliveries, and shortage analysis
- `Priority_Comparison_Charts.png`: Example charts comparing allocation outcomes under different priority scenarios

### Supporting Documents
- `Water_Rights_Primer.pdf`: Brief introduction to water rights systems and their modeling implications
- `Shared_Storage_Best_Practices.pdf`: Guidelines for implementing multi-owner reservoir models in practice
- `Allocation_Troubleshooting_Guide.pdf`: Common issues and solutions when working with complex allocation systems

*Note: This lesson represents the culmination of reservoir operations modeling, integrating physical storage, operational rules, and complex legal/institutional frameworks. The concepts learned here are directly applicable to the most challenging water management scenarios encountered in professional practice.*
