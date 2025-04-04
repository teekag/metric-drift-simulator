# Metric Drift Simulator

This interactive Streamlit application demonstrates how metrics can diverge across teams and contexts over time, leading to what we call "metric drift." This phenomenon is a common challenge in data-centric organizations where different teams may apply different transformations, filters, or interpretations to what is ostensibly the same metric.

## Features

- Interactive simulation of metric drift across Finance, Product, and Marketing teams
- Adjustable parameters to control drift factors, seasonality, and noise
- Visualization of metric values over time
- Analysis of divergence between team metrics
- Downloadable simulation data
- Explanations of why metrics drift and implications for data governance

## How to Run Locally

1. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

2. Run the Streamlit app:
   ```
   streamlit run app.py
   ```

## Deploying to Streamlit Cloud

1. Push this repository to GitHub
2. Sign up at [Streamlit Cloud](https://streamlit.io/cloud)
3. Create a new app pointing to this repository
4. Specify `app.py` as the main file

## Related Article

This simulator accompanies the article [Why the Metrics Layer Still Isn't Enough: Toward a Flexible & Governed Data Ecosystem](https://teekag.github.io/portfolio-website/blog/metrics-ecosystem), which explores the limitations of traditional metrics layers and proposes a more flexible metrics ecosystem approach.

## Parameters Explained

- **Base Drift Factor**: Controls how much the base metric definition changes over time
- **Contextual Modifier**: Controls how much team-specific context affects the metric
- **Seasonality Effect**: Controls the strength of seasonal patterns in the data
- **Random Noise**: Controls the amount of random variation in the metric
- **Team Context Weights**: How much each team's specific context affects their metric definition

## License

MIT
