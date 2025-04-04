import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import altair as alt
from datetime import datetime, timedelta

# Set page config
st.set_page_config(
    page_title="Metric Drift Simulator",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: 700;
        color: #1E3A8A;
        margin-bottom: 1rem;
    }
    .sub-header {
        font-size: 1.5rem;
        font-weight: 600;
        color: #3B82F6;
        margin-top: 2rem;
        margin-bottom: 1rem;
    }
    .insight-box {
        background-color: #F3F4F6;
        padding: 1.5rem;
        border-radius: 0.5rem;
        margin-bottom: 1rem;
    }
    .insight-title {
        font-size: 1.25rem;
        font-weight: 600;
        color: #1F2937;
        margin-bottom: 0.5rem;
    }
    .team-label-finance {
        color: #047857;
        font-weight: 600;
    }
    .team-label-product {
        color: #4F46E5;
        font-weight: 600;
    }
    .team-label-marketing {
        color: #B91C1C;
        font-weight: 600;
    }
</style>
""", unsafe_allow_html=True)

# Title and introduction
st.markdown("<div class='main-header'>Metric Drift Simulator</div>", unsafe_allow_html=True)

st.markdown("""
This interactive tool demonstrates how the same metric can diverge across teams and contexts over time,
leading to what we call "metric drift." This phenomenon is a common challenge in data-centric organizations
where different teams may apply different transformations, filters, or interpretations to what is ostensibly
the same metric.
""")

# Sidebar for simulation parameters
st.sidebar.markdown("## Simulation Parameters")

# Time parameters
st.sidebar.markdown("### Time Range")
start_date = st.sidebar.date_input("Start Date", datetime.now() - timedelta(days=90))
end_date = st.sidebar.date_input("End Date", datetime.now())
time_granularity = st.sidebar.selectbox("Time Granularity", ["Daily", "Weekly", "Monthly"], index=1)

# Team parameters
st.sidebar.markdown("### Teams")
include_finance = st.sidebar.checkbox("Finance Team", value=True)
include_product = st.sidebar.checkbox("Product Team", value=True)
include_marketing = st.sidebar.checkbox("Marketing Team", value=True)

# Drift parameters
st.sidebar.markdown("### Drift Factors")
base_drift = st.sidebar.slider("Base Drift Factor", 0.0, 1.0, 0.2, 
                              help="Controls how much the base metric definition changes over time")
context_factor = st.sidebar.slider("Contextual Modifier", 0.0, 2.0, 1.0,
                                 help="Controls how much team-specific context affects the metric")
seasonality = st.sidebar.slider("Seasonality Effect", 0.0, 1.0, 0.3,
                              help="Controls the strength of seasonal patterns in the data")
noise_level = st.sidebar.slider("Random Noise", 0.0, 0.5, 0.1,
                              help="Controls the amount of random variation in the metric")

# Advanced parameters (collapsible)
with st.sidebar.expander("Advanced Parameters"):
    finance_modifier = st.slider("Finance Context Weight", 0.5, 1.5, 1.2, 
                               help="How much Finance team's context affects their metric definition")
    product_modifier = st.slider("Product Context Weight", 0.5, 1.5, 0.8,
                               help="How much Product team's context affects their metric definition")
    marketing_modifier = st.slider("Marketing Context Weight", 0.5, 1.5, 1.0,
                                 help="How much Marketing team's context affects their metric definition")
    
    show_annotations = st.checkbox("Show Event Annotations", value=True,
                                 help="Display key events that affected metric definitions")

# Generate time series data
def generate_dates(start_date, end_date, granularity):
    delta = (end_date - start_date).days
    if granularity == "Daily":
        return [start_date + timedelta(days=i) for i in range(delta + 1)]
    elif granularity == "Weekly":
        return [start_date + timedelta(days=i*7) for i in range(delta // 7 + 1)]
    else:  # Monthly
        result = []
        current = start_date
        while current <= end_date:
            result.append(current)
            # Add a month
            month = current.month + 1
            year = current.year
            if month > 12:
                month = 1
                year += 1
            # Handle edge cases for month lengths
            day = min(current.day, 28)  # Simplification to avoid month length issues
            current = current.replace(year=year, month=month, day=day)
        return result

# Simulate metric drift
def simulate_metric_drift(dates, base_drift, context_factor, seasonality, noise_level, 
                          finance_mod, product_mod, marketing_mod):
    # Convert dates to numeric for calculations
    date_nums = [(d - dates[0]).days for d in dates]
    max_days = date_nums[-1] if date_nums else 0
    
    # Base metric function (common starting point)
    def base_metric(t):
        # Base value with some growth
        base = 100 + 0.05 * t
        # Add seasonality (if enabled)
        if seasonality > 0:
            # Yearly seasonality pattern
            yearly_cycle = np.sin(2 * np.pi * t / 365) * 10 * seasonality
            # Weekly seasonality pattern (for higher frequency data)
            weekly_cycle = np.sin(2 * np.pi * t / 7) * 5 * seasonality
            base += yearly_cycle + weekly_cycle
        return base
    
    # Generate data for each team
    results = []
    
    # Key events that cause definition changes
    events = []
    if max_days >= 30:
        events.append({
            'day': min(30, max_days // 3),
            'description': "Finance team adds attribution window adjustment"
        })
    if max_days >= 60:
        events.append({
            'day': min(60, max_days // 2),
            'description': "Product team filters out test accounts"
        })
    if max_days >= 90:
        events.append({
            'day': min(90, max_days * 2 // 3),
            'description': "Marketing team changes channel grouping logic"
        })
    
    for i, d in enumerate(dates):
        t = date_nums[i]
        point = {"date": d, "day": t}
        
        # Calculate base value
        base_value = base_metric(t)
        
        # Add team-specific transformations
        
        # Finance team (tends to be conservative, focuses on recognized revenue)
        if include_finance:
            # Progressive drift based on finance-specific context
            finance_drift = base_drift * t * 0.15 * finance_mod
            # Step changes at specific events
            for event in events:
                if t >= event['day'] and "Finance" in event['description']:
                    finance_drift += 5 * context_factor * finance_mod
            
            # Add noise
            finance_noise = np.random.normal(0, base_value * noise_level * 0.5)
            
            # Final finance metric value
            finance_value = base_value * (1 + 0.1 * context_factor * finance_mod) - finance_drift + finance_noise
            point["Finance"] = max(0, finance_value)  # Ensure non-negative
        
        # Product team (focuses on user engagement and product usage)
        if include_product:
            # Progressive drift based on product-specific context
            product_drift = base_drift * t * 0.2 * product_mod
            # Step changes at specific events
            for event in events:
                if t >= event['day'] and "Product" in event['description']:
                    product_drift -= 8 * context_factor * product_mod  # Product team filters out data
            
            # Add noise
            product_noise = np.random.normal(0, base_value * noise_level * 0.7)
            
            # Final product metric value
            product_value = base_value * (1 - 0.05 * context_factor * product_mod) - product_drift + product_noise
            point["Product"] = max(0, product_value)  # Ensure non-negative
        
        # Marketing team (focuses on attribution and campaign performance)
        if include_marketing:
            # Progressive drift based on marketing-specific context
            marketing_drift = base_drift * t * 0.25 * marketing_mod
            # Step changes at specific events
            for event in events:
                if t >= event['day'] and "Marketing" in event['description']:
                    marketing_drift += 12 * context_factor * marketing_mod  # Marketing changes attribution
            
            # Add noise
            marketing_noise = np.random.normal(0, base_value * noise_level)
            
            # Final marketing metric value
            marketing_value = base_value * (1 + 0.15 * context_factor * marketing_mod) + marketing_drift + marketing_noise
            point["Marketing"] = max(0, marketing_value)  # Ensure non-negative
        
        # Add the data point
        results.append(point)
    
    return pd.DataFrame(results), events

# Generate dates based on parameters
dates = generate_dates(start_date, end_date, time_granularity)

# Run simulation
df, events = simulate_metric_drift(
    dates, 
    base_drift, 
    context_factor, 
    seasonality, 
    noise_level,
    finance_modifier,
    product_modifier,
    marketing_modifier
)

# Main content area
st.markdown("<div class='sub-header'>Metric Drift Visualization</div>", unsafe_allow_html=True)

# Create tabs for different visualizations
tab1, tab2, tab3 = st.tabs(["Time Series", "Divergence Analysis", "Data Table"])

with tab1:
    # Prepare data for visualization
    chart_data = df.melt(id_vars=['date', 'day'], var_name='Team', value_name='Metric Value')
    
    # Create the base chart
    chart = alt.Chart(chart_data).mark_line().encode(
        x=alt.X('date:T', title='Date'),
        y=alt.Y('Metric Value:Q', title='Metric Value'),
        color=alt.Color('Team:N', scale=alt.Scale(
            domain=['Finance', 'Product', 'Marketing'],
            range=['#047857', '#4F46E5', '#B91C1C']
        )),
        tooltip=['date:T', 'Team:N', 'Metric Value:Q']
    ).properties(
        width='container',
        height=400,
        title='Metric Values Across Teams Over Time'
    )
    
    # Add annotations if enabled
    if show_annotations and events:
        # Convert events to DataFrame for Altair
        event_df = pd.DataFrame([
            {'day': e['day'], 'date': dates[0] + timedelta(days=e['day']), 'description': e['description']}
            for e in events if e['day'] <= df['day'].max()
        ])
        
        # Create vertical rules for events
        event_rules = alt.Chart(event_df).mark_rule(
            color='gray',
            strokeDash=[5, 5],
            opacity=0.5
        ).encode(
            x='date:T'
        )
        
        # Create text annotations
        event_text = alt.Chart(event_df).mark_text(
            align='left',
            baseline='top',
            fontSize=12,
            angle=270,
            dx=5,
            dy=10
        ).encode(
            x='date:T',
            text='description:N',
            color=alt.value('gray')
        )
        
        # Combine charts
        chart = alt.layer(chart, event_rules, event_text)
    
    # Display the chart
    st.altair_chart(chart, use_container_width=True)
    
    # Add explanation
    st.markdown("""
    This chart shows how the same metric evolves differently across teams over time. 
    Notice how the values start relatively close but diverge as time progresses due to:
    
    1. Team-specific contextual adjustments
    2. Different business needs driving different transformations
    3. Incremental changes that compound over time
    4. Key events that trigger definition changes (shown as vertical lines)
    """)

with tab2:
    # Calculate divergence metrics
    if len(df.columns) > 2:  # Need at least one team
        # Create a copy for analysis
        analysis_df = df.copy()
        
        # Calculate team-to-team differences
        teams = [col for col in df.columns if col not in ['date', 'day']]
        
        if len(teams) >= 2:
            # Calculate pairwise differences
            for i in range(len(teams)):
                for j in range(i+1, len(teams)):
                    team1 = teams[i]
                    team2 = teams[j]
                    diff_col = f"{team1} vs {team2}"
                    analysis_df[diff_col] = (analysis_df[team1] - analysis_df[team2]).abs()
            
            # Calculate average divergence over time
            analysis_df['Avg Divergence'] = analysis_df[[f"{teams[i]} vs {teams[j]}" 
                                                      for i in range(len(teams)) 
                                                      for j in range(i+1, len(teams))]].mean(axis=1)
            
            # Plot the divergence
            divergence_data = analysis_df.melt(
                id_vars=['date', 'day'], 
                value_vars=[f"{teams[i]} vs {teams[j]}" for i in range(len(teams)) for j in range(i+1, len(teams))],
                var_name='Team Comparison', 
                value_name='Absolute Difference'
            )
            
            # Create divergence chart
            divergence_chart = alt.Chart(divergence_data).mark_line().encode(
                x=alt.X('date:T', title='Date'),
                y=alt.Y('Absolute Difference:Q', title='Absolute Difference'),
                color=alt.Color('Team Comparison:N'),
                tooltip=['date:T', 'Team Comparison:N', 'Absolute Difference:Q']
            ).properties(
                width='container',
                height=400,
                title='Metric Divergence Between Teams'
            )
            
            # Display the chart
            st.altair_chart(divergence_chart, use_container_width=True)
            
            # Add explanation
            st.markdown("""
            This chart shows the absolute difference between each pair of team metrics over time.
            Larger values indicate greater divergence in how teams are measuring the same concept.
            
            Key insights:
            - Initial differences are small but grow over time
            - Events and contextual changes accelerate divergence
            - Without governance, these metrics become increasingly incomparable
            """)
            
            # Calculate and display summary statistics
            st.markdown("<div class='sub-header'>Divergence Statistics</div>", unsafe_allow_html=True)
            
            # Calculate statistics for the last data point
            last_point = analysis_df.iloc[-1]
            
            # Create three columns for stats
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.metric(
                    "Max Team Divergence", 
                    f"{last_point[[f'{teams[i]} vs {teams[j]}' for i in range(len(teams)) for j in range(i+1, len(teams))]].max():.1f}",
                    delta=f"{last_point[[f'{teams[i]} vs {teams[j]}' for i in range(len(teams)) for j in range(i+1, len(teams))]].max() - analysis_df.iloc[0][[f'{teams[i]} vs {teams[j]}' for i in range(len(teams)) for j in range(i+1, len(teams))]].max():.1f}"
                )
            
            with col2:
                st.metric(
                    "Average Divergence", 
                    f"{last_point['Avg Divergence']:.1f}",
                    delta=f"{last_point['Avg Divergence'] - analysis_df.iloc[0]['Avg Divergence']:.1f}"
                )
            
            with col3:
                # Calculate percent change from start to end
                start_avg = analysis_df.iloc[0]['Avg Divergence']
                end_avg = last_point['Avg Divergence']
                pct_change = ((end_avg - start_avg) / start_avg * 100) if start_avg > 0 else 0
                
                st.metric(
                    "Divergence Growth", 
                    f"{pct_change:.1f}%",
                    delta=f"{pct_change:.1f}%"
                )
        else:
            st.info("Select at least two teams to see divergence analysis")
    else:
        st.info("Select at least one team to see divergence analysis")

with tab3:
    # Display the raw data
    st.dataframe(df)
    
    # Add download button
    csv = df.to_csv(index=False)
    st.download_button(
        label="Download Data as CSV",
        data=csv,
        file_name="metric_drift_simulation.csv",
        mime="text/csv",
    )

# Add insights section
st.markdown("<div class='sub-header'>Key Insights</div>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("<div class='insight-box'>", unsafe_allow_html=True)
    st.markdown("<div class='insight-title'>Why Metrics Drift Apart</div>", unsafe_allow_html=True)
    st.markdown("""
    * **Different Business Contexts**: Each team optimizes metrics for their specific needs
    * **Incremental Changes**: Small adjustments compound over time
    * **Lack of Documentation**: Changes aren't always communicated across teams
    * **Siloed Development**: Teams build transformations independently
    * **Temporal Effects**: Definitions evolve as business priorities change
    """)
    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    st.markdown("<div class='insight-box'>", unsafe_allow_html=True)
    st.markdown("<div class='insight-title'>Implications for Data Governance</div>", unsafe_allow_html=True)
    st.markdown("""
    * **Metrics Layer Limitations**: Traditional metrics layers enforce rigid definitions
    * **Flexibility Need**: Organizations need controlled adaptation for valid business reasons
    * **Transparency Requirement**: Changes must be visible and traceable
    * **Metrics Ecosystem**: A better approach combines governance with flexibility
    * **Version Control**: Metric definitions should be versioned like code
    """)
    st.markdown("</div>", unsafe_allow_html=True)

# Add team-specific explanations
if include_finance or include_product or include_marketing:
    st.markdown("<div class='sub-header'>Team-Specific Context</div>", unsafe_allow_html=True)
    
    if include_finance:
        st.markdown("<div class='team-label-finance'>Finance Team Perspective</div>", unsafe_allow_html=True)
        st.markdown("""
        The Finance team focuses on recognized revenue and financial reporting. Their metric adjustments typically:
        * Apply strict attribution windows aligned with financial periods
        * Include only fully processed transactions
        * Apply revenue recognition rules
        * Adjust for returns, refunds, and chargebacks
        * Align with external reporting requirements
        """)
    
    if include_product:
        st.markdown("<div class='team-label-product'>Product Team Perspective</div>", unsafe_allow_html=True)
        st.markdown("""
        The Product team focuses on user experience and product usage. Their metric adjustments typically:
        * Filter out internal test accounts and beta users
        * Focus on active users rather than all registered accounts
        * Apply product-specific segmentation
        * Track feature adoption and engagement
        * Normalize for A/B test variations
        """)
    
    if include_marketing:
        st.markdown("<div class='team-label-marketing'>Marketing Team Perspective</div>", unsafe_allow_html=True)
        st.markdown("""
        The Marketing team focuses on campaign performance and attribution. Their metric adjustments typically:
        * Apply marketing attribution models (first-touch, last-touch, multi-touch)
        * Group channels differently than other teams
        * Include view-through conversions
        * Adjust for marketing-specific seasonality
        * Focus on new customer acquisition metrics
        """)

# Add conclusion and call to action
st.markdown("<div class='sub-header'>Toward a Flexible & Governed Data Ecosystem</div>", unsafe_allow_html=True)
st.markdown("""
This simulation demonstrates why traditional metrics layers aren't enough for modern data-driven organizations. 
Instead, we need a metrics ecosystem that balances governance with flexibility:

1. **Base Metrics Layer**: Common definitions and transformations
2. **Composable Metrics**: Building blocks that can be assembled for different contexts
3. **Context-Aware Overrides**: Documented adjustments for specific business needs
4. **Robust Versioning & Lineage**: Track how metrics evolve over time
5. **Intelligent Discovery & Validation**: Help users find and understand the right metrics

By embracing this approach, organizations can maintain consistency where it matters while allowing 
for the necessary flexibility that different business contexts require.
""")

# Add reference to the full article
st.markdown("""
---
For a deeper exploration of these concepts, read the full article: 
[Why the Metrics Layer Still Isn't Enough: Toward a Flexible & Governed Data Ecosystem](https://teekag.github.io/portfolio-website/blog/metrics-ecosystem)
""")
