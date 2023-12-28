import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Function to load and apply a CSS file
def load_css(css_file):
    with open(css_file, "r") as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
        

# Set the page layout to wide mode
st.set_page_config(layout="wide")

# Load the CSS styling
load_css('style.css')

# Fake data creation for the graph
np.random.seed(23)
dates = pd.date_range(start='1/1/2018', periods=100, freq='M')


def calculate_allocation_changes(original_holdings, revised_holdings):
    changes = {}
    for row in original_holdings.itertuples():
        original_percentage = float(row.Percentage.strip('%'))
        revised_percentage = float(revised_holdings[revised_holdings['Holding'] == row.Holding]['Percentage'].values[0].strip('%')) if row.Holding in revised_holdings['Holding'].values else 0
        change = revised_percentage - original_percentage
        changes[row.Holding] = change
    return changes
# Create a DataFrame for the fake data


            
def custom_metric(label, value, delta, color):
        delta_sign = "+" if delta > 0 else ""
        delta_color = "green" if delta > 0 else "red"
        html = f"""
        <style>
            .metric-container {{
                display: flex;
                flex-direction: column;
                align-items: flex-start;
            }}
            .metric-label {{
                font-size: 16px;
                margin-bottom: 4px;
            }}
            .metric-value {{
                font-size: 20px;
                margin-bottom: 4px;
            }}
            .metric-delta {{
                font-size: 16px;
                color: {color};
            }}
        </style>
        <div class="metric-container">
            <div class="metric-label">{label}</div>
            <div class="metric-value">{value}</div>
            <div class="metric-delta">{delta_sign}{delta}%</div>
        </div>
        """
        st.markdown(html, unsafe_allow_html=True)

# Fake top 10 holdings data
holdings = pd.DataFrame({
    'Holding': ['Plus 500 LTD', 'Bitcoin', 'Uber Technologies Inc.', 'Global X Uranium ETF', 
                'AstraZeneca', 'Berkshire Hathaway Inc', 'Biogen Inc', 'GlaxoSmithKline', 
                'Palantir Technologies Inc.', 'Thermo Fisher Scientific Inc'],
    'Percentage': ["59.29%", "7.20%", "4.12%", "3.60%", "3.16%", "3.04%", "2.27%", "2.07%", "1.67%", "1.39%"],
})

real_data = pd.read_csv("C:/Users/user/PycharmProjects/Code/etoro/portfolio_returns_since_20200323.csv")

# Convert 'Dates' to datetime for plotting
real_data['Dates'] = pd.to_datetime(real_data['Dates'])
# Layout
st.title('Investment Portfolio Analysis')

# Metrics at the top
col1, col2, col3, col4 = st.columns(4)
col1.metric("Sharpe", "0.45")
col2.metric("YTD Return", "5.29%")
col3.metric("3 Years Return", "17.93%")
col4.metric("Since Inception Return", "41.79%")

# Main graph and holdings in two columns
graph_col, holdings_col = st.columns([2, 1])  # Adjust the ratio as needed

with graph_col:
    st.subheader('Portfolio Value Over Time')
    fig, ax = plt.subplots(figsize=(10, 5))  # Adjust the figsize as needed
    # Plotting the portfolio and benchmark lines using real data
    ax.plot(real_data['Dates'], real_data['Portolfio'], label='Portfolio', color='blue', linewidth=2)
    ax.plot(real_data['Dates'], real_data['Benchmark '], label='Benchmark', color='orange', linestyle='--', linewidth=2)
    # Formatting the x-axis as Month-Year
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))
    # Rotate date labels for better readability
    plt.setp(ax.xaxis.get_majorticklabels(), rotation=45, ha='right')
    # Adding gridlines, legend, and labels
    ax.grid(True)
    ax.legend()
    ax.set_xlabel('Date')
    ax.set_ylabel('Value')
    st.pyplot(fig)

with holdings_col:
    st.subheader('Top 10 Holdings')
    st.table(holdings)
plus500_analysis_text = """

#### Reasons to Invest Plus 500
1. **Growth and Expansion:** CAGR of 31% over the past decade, international expansion including the US market.
2. **High Margins:** Net income margins of about 45%, indicating efficient operations and effective cost management.
3. **Asset-Light Business Model:** No material debt, lower capital expenditure requirements, and quick adaptability.
4. **Technological Investment:** Significant investments in trading platform, especially enhancing mobile user experience.
5. **Multiple Revenue Streams:** Diverse trading options offering stability and variety in revenue sources.
6. **Healthy Cash Distribution:** History of rewarding shareholders with dividends and share buybacks.

#### Reasons to be Cautious or Not Invest:
1. **Market Dependence:** Revenues tied to trading volumes, susceptible to market volatility and downturns.
2. **Regulatory Risks:** Highly regulated industry; adverse changes can impact profitability and growth.
3. **Competitive Industry:** Requires ongoing investments in technology, products, and marketing.
4. **Customer Risk Exposure:** High percentage of retail investors lose money on CFDs, potential for tighter regulations.
5. **FX Risk:** Global revenues subject to changes in foreign exchange rates.
6. **Potential Overreliance on Bear Markets:** High FCF yield may not be sustainable in prolonged bear markets.

**Conclusion:** Plus500 offers compelling growth prospects and efficiency, balanced against risks in market dependence, regulation, and competition. Suitable for investors considering high-risk, high-reward investments within their risk tolerance and investment strategy.

"""
uber_anlysis_text="""
#### Reasons to Invest in Uber:

1. **Strong Year-to-Date Performance**: Uber's stock has surged significantly, indicating robust investor confidence and market performance.
   
2. **S&P 500 Inclusion**: This inclusion often leads to increased buying from funds that track the index, potentially boosting the stock price further.

3. **Solid Q3 Earnings**: Impressive growth in revenue and adjusted EBITDA, reflecting strong operational efficiency and market demand.

4. **Large Total Addressable Market (TAM)**: Uber's TAM is estimated at a substantial $5.7 trillion, suggesting significant growth potential.

5. **Diverse Business Segments**: Beyond ride-sharing, Uber is expanding into delivery, freight, and other services, diversifying its revenue sources.

6. **Strong Consumer Demand**: Consistent growth in active users and trips indicates solid demand for Uber’s services.

7. **Healthy Balance Sheet**: Despite ongoing acquisitions, Uber maintains a strong financial position.

8. **Potential for Share Buybacks**: Positive free cash flow and a healthy cash balance could lead to shareholder-friendly activities like share buybacks.

#### Reasons to be Cautious or Not Invest:

1. **High Valuation**: Compared to industry peers, Uber trades at a premium, which might concern value-focused investors.

2. **Macroeconomic Risks**: The potential economic downturn could reduce consumer spending on services like Uber.

3. **Regulatory Challenges**: Issues related to gig economy workers and international rulings could impact Uber’s profitability and operations.

4. **Competition**: The highly competitive nature of the mobility and delivery sectors could pressure margins and market share.

5. **Index Inclusion Effect**: While inclusion in the S&P 500 is positive, it can lead to short-term volatility and a potential pullback post-inclusion.

6. **Technological and Market Risks**: Challenges like the increasing scrutiny of autonomous vehicles and the need to continually innovate can impact long-term growth.

7. **Downgraded Ratings by Some Analysts**: Concerns over valuation and market conditions have led some analysts to downgrade Uber to a ‘Hold’ or even a ‘Sell’.

#### Conclusion:
Investing in Uber presents a case of weighing its strong market position, growth potential, and recent positive financial performance against concerns over valuation, regulatory challenges, and potential market volatility. As with any investment, it's crucial to consider both the growth prospects and the risks involved, aligning them with your investment strategy and risk tolerance."""
bitcoin_anlysis_Text="""#### Reasons to Invest in Bitcoin

##### Bullish Factors
1. **Halving Cycle Anticipation**: Historical patterns show Bitcoin rallying post-halving, suggesting potential for significant gains.
2. **Institutional Interest and Legitimacy**: BlackRock’s entry and potential ETF approvals indicate growing institutional interest, enhancing Bitcoin’s legitimacy.
3. **Diversification Potential**: Bitcoin offers portfolio diversification, demonstrating an inverse relationship with traditional equities at times.
4. **Technological Developments**: Innovations like NFTs and smart contract capabilities through protocols like Ordinals enhance Bitcoin's utility.
5. **Market Accessibility Improvement**: ETFs could provide easier access for institutional and non-professional investors.
6. **Rebound from Negative Sentiment**: Bitcoin's recovery from previous downturns reflects resilience and growing investor confidence.

##### Bearish Factors
1. **Regulatory Uncertainty**: Ongoing regulatory concerns, especially regarding market manipulation and the approval of spot ETFs.
2. **Market Volatility**: Bitcoin's price is highly volatile, posing risks for investors unaccustomed to such fluctuations.
3. **Decentralization Concerns**: BlackRock’s involvement could signify a move away from the ideal of decentralization in crypto.
4. **Risky for New Investors**: The complexity and technicalities of cryptocurrency can be daunting for new or amateur investors.
5. **Competition from CBDCs**: The rise of Central Bank Digital Currencies (CBDCs) might challenge Bitcoin's position as a digital currency.

##### Neutral/Consideration Factors
1. **Technological Adoption and Innovations**: While promising, the extent of mainstream adoption and success of new technologies in the blockchain and crypto space remains uncertain.
2. **Global Financial Sentiment**: Bitcoin's adoption and performance are influenced by global financial trends and investor sentiment towards traditional financial systems.
3. **Influence of External Factors**: Factors like inflation trends, global economic conditions, and changes in interest rates significantly impact Bitcoin's performance.

#### Conclusion
Investing in Bitcoin offers potential high-reward opportunities, especially considering its historical performance, technological advancements, and growing institutional interest. However, it comes with significant risks, including regulatory challenges, inherent market volatility, and uncertainties in technological adoption and global financial sentiment. Investors should weigh these factors carefully against their risk tolerance and investment goals before making decisions."""

user_risk_score_analysis_text = """## Portfolio Risk Analysis: Score 4 out of 5

### Overview
- The portfolio is assigned a **risk score of 4 out of 5**.
- This indicates a high level of risk.

### Key Risk Factors

#### 1. Diversification and Concentration Risk
- **Plus 500 LTD** dominates the portfolio with **59.29%**.
- High concentration in one stock increases risk significantly.

#### 2. Cryptocurrency Exposure
- **Bitcoin** makes up **7.20%** of the portfolio.
- Known for its high volatility, it adds to the risk profile.

#### 3. Sector-Specific Risks
- **Tech and Biotech, Financial Servise Exposure** while the holdings are good the conectrating to full equity expousre in those sector add risk and it  will be adviacle to alloacte some of the funds to other sectors.


#### 4. Market and Economic Sensitivity
- Stocks like **Uber** and **Berkshire Hathaway** are sensitive to economic cycles.

#### 5. Geographical Concentration
- Risk increases if most companies are based in the same region like the current portoflio.

#### 6. Lack of Fixed Income or Diversifying Assets
- No mention of fixed-income securities or diversifying assets that usually reduce risk.

### Conclusion
- The portfolio shows potential for high volatility and susceptibility to various risks.
- Continuous monitoring and possible rebalancing are essential.
"""

user_perosna_text = """Based on the composition of this user's portfolio, we can infer certain preferences, dislikes, and an overall investment philosophy:

#### Preferences and Investment Philosophy:
1. **High Interest in Technology and Healthcare:** A significant portion of the portfolio is invested in technology (like PLUS 500 LTD, Uber Technologies, Palantir Technologies) and healthcare companies (such as AstraZeneca, Biogen Inc, GlaxoSmithKline). This suggests a preference for industries that are innovative and potentially offer high growth.

2. **Diversification Across Industries:** The presence of companies from different industries (e.g., Financial Services, Cryptocurrency, Energy, Retail) indicates an understanding of the importance of diversification to reduce risk.

3. **Inclination Towards Established Companies:** Investments in companies like Berkshire Hathaway, Apple, and Microsoft suggest a preference for well-established businesses with proven track records, potentially indicating a more risk-averse approach.

4. **Interest in Emerging Markets or Sectors:** Investments in Bitcoin and Global X Uranium ETF show a willingness to invest in emerging markets or sectors, which can be more volatile but offer higher potential returns.

##### Potential Dislikes:
1. **Avoidance of Extremely High-Risk Investments:** The absence of highly speculative stocks or very small-cap companies suggests a discomfort with extremely high-risk investments.

2. **Limited Exposure to Certain Industries:** The portfolio shows limited exposure to certain volatile sectors like pure commodities trading or unproven tech startups.

3. **Conservative Approach to Financial Services:** The investment in PLUS 500 LTD, a platform for trading CFDs, is balanced by more stable, diversified holdings, indicating a cautious approach to the financial services sector."
"""

problems_found_text = """

## Key Issues in Client's Portfolio

### Overconcentration in Plus 500 LTD
- **High Volatility**: Excessive reliance on a single stock increases portfolio volatility.
- **Sector-Specific Risks**: Heightened exposure to sector-specific and market fluctuations.

### Limited Diversification
- **Asset Class Spread**: Inadequate diversification across various asset classes.
- **Geographical Reach**: Overemphasis on specific markets, lacking global exposure.

### Underrepresentation of Safer Asset Classes
- **Gold and Bonds**: Insufficient allocation to assets that hedge against inflation and market downturns.
- **Stability Factors**: Missed opportunities in balancing portfolio with stable income-generating assets.

### High Allocation to High-Volatility Assets (e.g., Bitcoin)
- **Disproportionate Investment**: Over-investment in assets with high volatility.
- **Risk Misalignment**: Inconsistent with the client's moderate risk tolerance level.

### Overall Portfolio Imbalance
- **Risk Skew**: Portfolio excessively tilted towards high-risk investments.
- **Growth-Stability Balance**: Lack of equilibrium between growth potential and stability, crucial for long-term investment objectives.
"""

user_json = {
    "userPersona": user_perosna_text,
    "problemsFound": problems_found_text,
    "TopHoldingsAnalysis": {
        "Plus500 Ltd.": plus500_analysis_text,
        "Uber Inc": uber_anlysis_text,
        "Bitcoin": bitcoin_anlysis_Text,
    }
}

company_names = list(user_json['TopHoldingsAnalysis'].keys())
if 'analysis_done' not in st.session_state:
    st.session_state.analysis_done = False
if 'selected_company' not in st.session_state:
    st.session_state.selected_company = company_names[0]

# Function to handle company selection change
def update_selected_company():
    st.session_state.selected_company = st.session_state['company_select']

# Function to handle analyze button click
def perform_analysis():
    st.session_state.analysis_done = True
    
def pereform_recommendation():
    st.session_state.recommendation_done = True
    
# Analyze button and results
st.subheader('Analysis')
if st.button('Analyze', on_click=perform_analysis):
    pass


if st.session_state.analysis_done:
    # Display the analysis layout after the button is pressed
    st.subheader('Analysis Results')

    # Layout for analysis results
    with st.expander("Risk Score Analysis"):
        st.write(user_risk_score_analysis_text)
    
    with st.expander("User Persona"):
            st.write(user_json['userPersona'])

    with st.expander("Problems Found"):
        st.write(user_json['problemsFound'])

    with st.expander("Top Holdings Analysis"):
        # Selectbox for choosing the company
        st.selectbox(
            "Select a Company for Analysis",
            options=company_names,
            index=company_names.index(st.session_state.selected_company),
            key='company_select',
            on_change=update_selected_company
        )

        # Display the selected company's analysis
        st.write(user_json['TopHoldingsAnalysis'][st.session_state.selected_company])

    def perform_recommendation():
        st.session_state.recommendation_done = True

    # Recommendation button
    if st.button('Generate Recommendation', on_click=perform_recommendation):
        pass

    # Recommendation results
        if st.session_state.recommendation_done:
            st.subheader('Recommendation')
            
            holdings_col_old, holdings_col_new,metrics_col = st.columns([1,1,1])  # Adjust the ratio as needed
            

            with holdings_col_old:
                with st.expander("Portfolio Holdings Old", expanded=False):
                    st.table(holdings)

            revised_holdings = pd.DataFrame({
    'Holding': ['Plus 500 LTD', "Interactive Brokers", "Charles Schwab", "Vanguard Total Stock Market ETF", 
                "U.S. Treasury Long-Term Bonds (TLT)", "International Hedged Quality Dividend Growth Fund", 
                "Robinhood", "Gold (ETFs like GLD)", "Commodities Basket (ETFs like DBC)", 
                "U.S. Treasury Intermediate-Term Bonds(IEI)" ,"Uber Technologies Inc","Global X Uranium ETF" ,"AstraZeneca","Berkshire Hathaway Inc","Bitcoin"],
    'Percentage': ["20%", "12%", "10%", "15%", "15%", "10%", "5%", "5%", "5%", "5%","4.12%","3.60%","3.16%","3.04%", "3%"],
})
            

            with holdings_col_new:
                with st.expander("Portfolio Holdings New", expanded=False):
                    st.table(revised_holdings)
    
        # Function to render a metric with custom styling
                with metrics_col:
        # Function to render a metric with custom styling
                    def custom_metric(label, value, delta, color):
                        delta_sign = "+" if delta > 0 else "" if delta == 0 else "-"  # Handle the case when delta is 0
                        delta_color = "green" if delta > 0 else "red" if delta < 0 else "black"  # Use black color for delta = 0
                        html = f"""
                        <style>
                            .metric-container {{
                                display: flex;
                                flex-direction: column;
                                align-items: flex-start;
                            }}
                            .metric-label {{
                                font-size: 16px;
                                margin-bottom: 4px;
                            }}
                            .metric-value {{
                                font-size: 20px;
                                margin-bottom: 4px;
                            }}
                            .metric-delta {{
                                font-size: 16px;
                                color: {delta_color};
                            }}
                        </style>
                        <div class="metric-container">
                            <div class="metric-label">{label}</div>
                            <div class="metric-value">{value}</div>
                            <div class="metric-delta">{delta_sign}{abs(delta)}%</div>
                        </div>
                        """
                        st.markdown(html, unsafe_allow_html=True)

                    # Display custom metrics
                    with st.expander("Portfolio Changes", expanded=False):
                        custom_metric("Plus500 (PLSQF)", "-565316.68$", -39.29, "red")
                        custom_metric("Bitcoin (BTC)", "-60431.74$", -4.20, "red")
                        custom_metric("Interactive Brokers (IBKR)", "172662.12$", 12.00, "green")
                        custom_metric("Charles Schwab (SCHW)", "143885.10$", 10.00, "green")
                        custom_metric("Vanguard Total Stock Market ETF (VTI)", "215827.65$", 15.00, "green")
                        custom_metric("U.S. Treasury Long-Term Bonds (TLT)", "215827.65$", 15.00, "green")
                        custom_metric("International Hedged Quality Dividend Growth Fund", "143885.10$", 10.00, "green")
                        custom_metric("Robinhood (HOOD)", "71942.55$", 5.00, "green")
                        custom_metric("Gold (ETFs like GLD)", "71942.55$", 5.00, "green")
                        custom_metric("Commodities Basket (ETFs like DBC)", "71942.55$", 5.00, "green")
                        custom_metric("U.S. Treasury Intermediate-Term Bonds (IEI)", "71942.55$", 5.00, "green")
                        
            with st.expander("Portfolio Recommendation Summary", expanded=False):
                recommendation_text = """
                ## In-Depth Financial Strategy Analysis for Portfolio Restructuring of [Client's Name]

                ### Executive Summary
                This document presents a detailed analysis of the strategic adjustments recommended for [Client's Name]'s investment portfolio. The focus is on achieving a balance between risk mitigation and growth potential, in line with a revised risk tolerance of 3/5.

                ### Strategic Investment Decisions

                #### De-Risking Through Diversification

                ##### Plus 500 LTD: Managing Concentration Risk
                - **Previous Position:** Over-concentration
                - **Adjusted Allocation:** 20%
                - **Deep Analysis:** The performance of Plus 500 LTD has been outstanding, but its over-representation in the portfolio posed a significant single-stock risk. The reduction to 20% is a move to mitigate this idiosyncratic risk. By diversifying away from this concentration, the portfolio is less vulnerable to company-specific events, aligning with modern portfolio theory which advocates for diversification to reduce unsystematic risk.

                #### Rebalancing Equity Holdings for Stability

                ##### Selection of IBKR and SCHW Over HOOD
                - **Allocations:** IBKR (12%), SCHW (10%), HOOD (5%)
                - **Analytical Logic:** Interactive Brokers and Charles Schwab represent more stable investments due to their established market presence and diversified revenue streams, as opposed to the highly volatile and growth-oriented Robinhood. This decision reflects a preference for value and stability, resonating with the principles of value investing - seeking undervalued, established players with strong fundamentals.

                #### Inclusion of Non-Correlated Assets

                ##### Gold and Commodities for Hedging
                - **Allocations:** Gold (5%), Commodities (5%)
                - **Strategic Insight:** The inclusion of gold and commodities is rooted in their historical performance of being less correlated with stock and bond markets. Gold is recognized for its inverse correlation with equities during market downturns, providing a hedge against inflation and currency devaluation. Commodities offer exposure to different economic cycles, potentially enhancing returns and reducing overall portfolio volatility.

                #### Fixed Income Strategy for Downside Protection

                ##### Diversified Bond Holdings
                - **Allocations:** TLT (15%), IEI (5%)
                - **Rationale:** Allocating towards a mix of long-term (TLT) and short-term (IEI) U.S. Treasury Bonds is a strategic move to cushion against market volatility. Long-term bonds (TLT) offer higher yield potential and are sensitive to interest rate changes, providing an inflation hedge. Short-term bonds (IEI) offer lower volatility and are less sensitive to interest rate changes, providing liquidity and stability. This bond ladder approach is a fundamental risk management strategy in fixed-income investing.

                #### Broad Market Exposure for Consistent Growth

                ##### Vanguard Total Stock Market ETF (VTI)
                - **Allocation:** 15%
                - **Investment Philosophy:** VTI offers comprehensive exposure to the entire U.S. equity market, including small-, mid-, and large-cap stocks. This aligns with the concept of total market investing, which is based on the efficient market hypothesis. It posits that it's challenging to beat the market consistently through active management, hence the strategy to own a representative sample of the entire market for diversified exposure and risk spreading.

                #### Global Diversification for Risk Reduction

                ##### International Hedged Quality Dividend Growth Fund (IHDG)
                - **Allocation:** 10%
                - **Global Investment Strategy:** Incorporating IHDG addresses home country bias and introduces diversification into high-quality, dividend-paying international stocks. This fund employs a currency-hedged approach, reducing the portfolio's vulnerability to foreign exchange volatility. It's a manifestation of the modern portfolio theory, which suggests that international diversification can potentially reduce portfolio risk without compromising returns.

                #### Cryptocurrency Allocation: Balancing Innovation and Risk

                ##### Bitcoin
                - **Adjusted Allocation:** 3%
                - **Futuristic Approach:** The reduced but maintained allocation in Bitcoin acknowledges its potential as an emerging asset class, while aligning with a more conservative risk profile. This decision is influenced by the recognition of cryptocurrencies as a high-risk, high-reward investment, and a nod to portfolio theory's suggestion to include 'alternative investments' for diversification and potential outsized returns in a small portion of the portfolio.

                ### Conclusion
                The recommendations for [Client's Name]'s portfolio restructuring are grounded in a balance of traditional investment principles and modern financial theories. The aim is to navigate market uncertainties, optimize returns, and align with the client's revised risk tolerance.

                ---
                *This strategic analysis is designed to align [Client's Name]'s investment strategy with their long-term financial objectives and comfort with risk exposure.*

                                    """
                st.write(recommendation_text)
                
                
          
            st.subheader('Final Emails Suggestion')
            
            short_email, long_email = st.columns([1,1])  # Adjust the ratio as needed
            with short_email:
                with st.expander("Short_email", expanded=False):
                    st.write("""
    ## Portfolio Update: Strategic Enhancements for Optimal Balance

    Dear [Client's Name],

    I hope you are doing well. Following a thorough analysis of your investment portfolio, aligned with your financial goals and risk preferences, we propose a strategic shift. Our recommendation is to adjust your risk level from 4/5 to a more moderate 3/5.

    ### Highlights of Our Analysis
    - **Key Focus:** Reducing volatility and enhancing diversification.
    - **Objective:** Optimizing asset allocation to balance growth with stability.

    ### Revised Portfolio Strategy
    - **Adjustments:** Changes in key holdings like Plus 500 LTD, Interactive Brokers, and Charles Schwab.
    - **Diversification:** Strategic investments in gold, commodities, and bonds.
    - **Exposure:** Broad market and geographical diversification.
    - **High-Standard Assets:** Adjusted Bitcoin allocation for a moderate risk profile.

    For a detailed breakdown of these recommendations, please refer to the attached PDF.

    Warm regards,

    [Your Name]
                    """)
            with long_email:
                with st.expander("Long_email", expanded=False):
                    st.write("""## Personalized Portfolio Restructuring Plan for [Client's Name]: Balancing Growth with Stability

Dear [Client's Name],

I hope this message finds you in good spirits. As part of our commitment to aligning your investment portfolio with your personal goals and comfort level with risk, we've undertaken a comprehensive review of your investments. Given your initial risk tolerance of 4/5 and the considerable scale of your portfolio, we're suggesting a more balanced approach, moving towards a risk level of 3/5.

### Your Revised Top 10 Holdings:

1. **Plus 500 LTD:** 
- Holdings: 20%
- Logic: We recognize the robust performance of Plus 500 in your portfolio. However, its concentration in your portfolio adds unnecessary volatility. The reduction balances this risk with minimal expected effect on returns.

2. **Interactive Brokers (IBKR, SCHW, HOOD):**
- Holdings: 
    - IBKR: 12%
    - SCHW: 10%
    - HOOD: 5%
- Logic: We favor established firms like IBKR and SCHW for their proven business models and lower risk profiles, as opposed to the more speculative nature of Robinhood, while maintaining exposure to the Plus 500 sector.

3. **Asset Class Diversification and Safe Havens**
- **Gold (ETFs like GLD):**
    - Holdings: 5%
    - Logic: Gold remains an effective uncorrelated hedge against inflation and market fluctuations, adding a layer of security to your investments. In addition, gold is considered a safe haven and usually goes up in deep crises.

- **Commodities Basket (ETFs like DBC):**
    - Holdings: 5%
    - Logic: This diversifies your exposure beyond traditional stocks and bonds, tapping into the potential of various commodities with uncorrelated returns.

- **Bonds (ETFs like BND, TLT):**
    - Holdings: 
    - TLT: 15%
    - IEI: 5%
    - Logic: These bonds add a stable income stream and act as a buffer in market downturns (10% in long-term TLT and 5% in short-term IEI). In addition, U.S. bonds are considered go-to safe havens and usually go up in deep crises.

4. **Broader Market Exposure**
- **Vanguard Total Stock Market ETF (VTI):**
    - Holdings: 15%
    - Logic: VTI's broad market exposure makes it an essential part of every well-rounded portfolio.

5. **Geographical Diversification**
- **International Hedged Quality Dividend Growth Fund:**
    - Holdings: 10%
    - Logic: By incorporating international equities with a focus on quality dividend-paying stocks and growth factors, IHDG brings stability, income, and growth potential from non-U.S. developed markets.

6. **Highly Volatile Assets**
- **Bitcoin:**
    - Adjusted to 3%
    - Logic: While maintaining your interest in the dynamic cryptocurrency market, this reduced allocation aligns better with a moderate risk profile.

### Next Steps:

To implement this personalized portfolio restructuring, please use the following link:
[Automatic Portfolio Adjustment Link]

I encourage you to review these changes at your earliest convenience. Do not hesitate to reach out for any clarifications or further discussions. Our goal is to ensure your investment strategy is not only aligned with your financial objectives but also comfortable for you in terms of risk exposure.

Warm Regards,
[Your Name]
""")


        







