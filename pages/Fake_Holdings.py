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
    'Holding': ['TLT'],
    'Percentage': ["100%"],
})

real_data = pd.read_csv("TLT.csv")

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

user_risk_score_analysis_text = """## Portfolio Risk Analysis: Score 1 out of 5

### Overview
- The portfolio is 100% invested in TLT (iShares 20+ Year Treasury Bond ETF).
- Assigned a **risk score of 1 out of 5**, indicating a low level of risk.

### Key Factors Contributing to Low Risk

#### 1. Nature of TLT
- TLT invests in U.S. Treasury bonds with maturities greater than 20 years.
- Treasury bonds are considered one of the safest investments due to government backing.

#### 2. Interest Rate Risk
- While long-term bonds are sensitive to interest rate changes, this risk is often mitigated by the stability and predictability of returns in the long run.

#### 3. Market Volatility
- TLT is generally less volatile compared to equities.
- It provides a haven during market downturns and uncertainty.

#### 4. Inflation Risk
- Long-term bonds can be susceptible to inflation.
- However, the impact is often balanced by the security's longer duration and stable interest income.

#### 5. Diversification
- Although the portfolio lacks diversification across asset classes, TLT itself is diversified across various U.S. Treasury bonds.
- This internal diversification within the bond spectrum reduces risk.

#### 6. Economic Cycles
- TLT typically performs better during economic downturns and periods of low-interest rates.
- It's less correlated with the performance of the stock market.

### Conclusion
- The low risk score of the portfolio reflects the inherent stability and safety of TLT as an investment.
- Investors in this portfolio can expect low volatility and stable, albeit potentially modest, returns.
- It is particularly suited for risk-averse investors or those seeking a safe haven in uncertain market conditions.

"""

user_perosna_text = """## Investor Persona: 100% TLT Portfolio

### Preferences and Investment Philosophy

#### 1. Strong Preference for Stability and Safety
- Exclusive investment in **TLT (iShares 20+ Year Treasury Bond ETF)**.
- Indicates a priority for stability and security in investments.

#### 2. High Risk Aversion
- The choice of TLT, known for low volatility, suggests a strategy focused on risk aversion.
- Emphasis on capital preservation over high-risk, high-reward investments.

#### 3. Interest in Government Bonds
- Specific focus on government-backed securities like TLT.
- Prefers the reliable, fixed-income nature and safety of government bonds.

#### 4. Long-Term Investment Horizon
- Investment in long-term bonds implies a strategy geared towards long-term stability.
- Seeks steady, predictable returns over quick, short-term gains.

### Potential Dislikes

#### 1. Discomfort with Market Volatility
- Avoids equity markets or investments known for high volatility.
- Prefers investments with less exposure to market fluctuations.

#### 2. Avoidance of Speculative Investments
- Steers clear of speculative assets like cryptocurrencies or high-growth tech stocks.
- Likely finds the unpredictable nature of these investments unappealing.

#### 3. Limited Interest in Sector-Specific or High-Growth Areas
- The portfolio lacks investments in specific sectors like tech or healthcare.
- Shows little interest in sectors or investments associated with high growth but higher risk.

#### 4. Conservative Approach to Investment
- The single-asset approach in TLT suggests a conservative investment style.
- Prefers traditional, time-tested investment vehicles over newer, less proven options.

"""

problems_found_text = """

## Portfolio Analysis: 100% Investment in TLT

### Key Issues in TLT-Focused Portfolio

#### 1. Overconcentration in a Single Asset Class
- **Risk of Single Asset Class**: Total reliance on long-term U.S. Treasury bonds.
- **Lack of Diversification**: No exposure to other asset classes like stocks, commodities, or real estate.

#### 2. Sensitivity to Interest Rate Changes
- **Interest Rate Risk**: TLT is sensitive to fluctuations in interest rates.
- **Market Dynamics**: When interest rates rise, bond prices typically fall, affecting TLT's performance.

#### 3. Limited Growth Potential
- **Low Return Potential**: Compared to equities, long-term bonds generally offer lower growth potential.
- **Growth-Stability Tradeoff**: The portfolio sacrifices growth for stability.

#### 4. Inflation Risk
- **Erosion of Purchasing Power**: Fixed-income payments from bonds can lose value in times of high inflation.
- **Long Duration Bonds**: Particularly sensitive to inflation over time.

#### 5. Lack of Global Diversification
- **Geographical Concentration**: TLT invests solely in U.S. Treasury bonds, lacking global bond market exposure.
- **Currency Risk**: No hedge against the U.S. dollar fluctuations.

#### 6. Missed Opportunities in Other Asset Classes
- **Lack of Equities**: No exposure to potentially higher-yielding stocks.
- **Absence of Alternative Investments**: Missing diversification benefits from assets like real estate or commodities.

#### 7. Underrepresentation of Shorter-Term Investments
- **Liquidity Concerns**: Long-term bonds can be less liquid in the short term.
- **Flexibility**: Limited flexibility to capitalize on short-term market opportunities.

### Conclusion
- The TLT-focused portfolio, while extremely safe and stable, faces issues related to overconcentration, limited growth potential, and sensitivity to interest rates and inflation.
- Diversification into other asset classes, shorter-term investments, and global markets may help balance the portfolio for better risk management and growth opportunities.

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
                'Holding': ['TLT (iShares 20+ Year Treasury Bond ETF)', 'Vanguard High Dividend Yield ETF (VYM)', 
                            'iShares iBoxx $ Investment Grade Corporate Bond ETF (LQD)', 'Vanguard Total Stock Market ETF (VTI)',
                            'Vanguard Real Estate ETF (VNQ)'],
                'Percentage': ['70%', '10%', '10%', '5%', '5%'],
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
                        custom_metric("TLT (iShares 20+ Year Treasury Bond ETF)", "700000.00$", 70.00, "green")
                        custom_metric("Vanguard High Dividend Yield ETF (VYM)", "100000.00$", 10.00, "green")
                        custom_metric("iShares iBoxx $ Investment Grade Corporate Bond ETF (LQD)", "100000.00$", 10.00, "green")
                        custom_metric("Vanguard Total Stock Market ETF (VTI)", "50000.00$", 5.00, "green")
                        custom_metric("Vanguard Real Estate ETF (VNQ)", "50000.00$", 5.00, "green")

                        
            with st.expander("Portfolio Recommendation Summary", expanded=False):
                recommendation_text = """
                ## Portfolio Restructuring Recommendation Summary

### Objective
- **Enhance Portfolio to Achieve a Risk Score of 2**: Aim to maintain a conservative approach while introducing a moderate level of risk.

### Proposed Allocation

#### 1. TLT (iShares 20+ Year Treasury Bond ETF)
- **Holdings**: Reduce to **70%**.
- **Rationale**: Provides stability and a predictable income stream. Reducing from 100% to 70% maintains a conservative base while allowing room for diversification.

#### 2. Vanguard High Dividend Yield ETF (VYM)
- **Holdings**: Allocate **10%**.
- **Rationale**: Adds dividend-paying stocks for income and moderate growth. Slightly more risk but remains conservative.

#### 3. iShares iBoxx $ Investment Grade Corporate Bond ETF (LQD)
- **Holdings**: Allocate **10%**.
- **Rationale**: Exposure to high-quality corporate bonds, offering higher yields than TLT. Introduces moderate risk and potential for higher income.

#### 4. Vanguard Total Stock Market ETF (VTI)
- **Holdings**: Allocate **5%**.
- **Rationale**: Diversified exposure to the U.S. stock market. Adds growth potential with a controlled risk increase.

#### 5. Vanguard Real Estate ETF (VNQ)
- **Holdings**: Allocate **5%**.
- **Rationale**: Provides real estate diversification. Balances income (via dividends) and growth, adding a different asset class.

### Conclusion
- **Balanced Approach**: This restructuring increases the risk profile to a more balanced level of 2, while still prioritizing safety and income generation.
- **Diverse Components**: Introduces dividend stocks, corporate bonds, broad market exposure, and real estate for a well-rounded portfolio.
- **Alignment with Client's Goals**: Ensure the changes align with the client's investment time horizon, liquidity needs, and overall financial objectives.
- **Ongoing Management**: Regular reviews and adjustments recommended to stay aligned with evolving goals and risk tolerance.

                                    """
                st.write(recommendation_text)
                
                
          
            st.subheader('Final Emails Suggestion')
            
            short_email, long_email = st.columns([1,1])  # Adjust the ratio as needed
            with short_email:
                with st.expander("Short_email", expanded=False):
                    st.write("""
    ## Portfolio Update: Refining for Enhanced Stability and Growth

Dear [Client's Name],

I trust this message finds you well. I am reaching out to share some strategic enhancements we have crafted for your investment portfolio. These changes aim to refine your current risk level, moving from a high risk score of 1/5 to a more balanced score of 2/5.

### Highlights of Our Analysis:
- **Primary Goal**: Our focus has been on reducing overconcentration and increasing diversification.
- **Objective**: We aim to optimize your asset allocation to strike a healthy balance between stability and growth potential.

### Revised Portfolio Strategy:
- **Adjustments**: We propose reducing the allocation in TLT (iShares 20+ Year Treasury Bond ETF) to 70% and introducing diversified asset classes.
- **Inclusion of New Assets**: We suggest incorporating Vanguard High Dividend Yield ETF (VYM), iShares iBoxx $ Investment Grade Corporate Bond ETF (LQD), Vanguard Total Stock Market ETF (VTI), and Vanguard Real Estate ETF (VNQ) into your portfolio.
- **Balanced Approach**: This strategy introduces a mix of income generation and growth opportunities while maintaining a conservative backbone with TLT.

For a comprehensive overview of these recommendations and their potential impact on your financial goals, please refer to the attached document.

Looking forward to discussing these recommendations with you and addressing any questions you might have.

Warm regards,

[Your Name]
                """)
            with long_email:
                with st.expander("Long_email", expanded=False):
                    st.write("""# Tailored Portfolio Restructuring for Enhanced Stability and Growth

Dear [Client's Name],

I hope this message finds you well. In our commitment to align your investment portfolio with your personal financial goals and risk tolerance, we have undertaken a detailed review of your current investments. Given your portfolio's focus on TLT and a conservative risk approach, we propose strategic modifications to transition from a risk level of 1/5 to a more balanced 2/5.

### Revised Portfolio Structure

#### 1. TLT (iShares 20+ Year Treasury Bond ETF)
- **New Holdings**: Reduced to **70%**.
- **Logic**: Maintains stability and predictable income, while allowing for diversification and growth potential.

#### 2. Vanguard High Dividend Yield ETF (VYM)
- **Holdings**: **10%**.
- **Logic**: Offers a conservative approach to equity with a focus on high-dividend-yielding companies, blending income and moderate growth.

#### 3. iShares iBoxx $ Investment Grade Corporate Bond ETF (LQD)
- **Holdings**: **10%**.
- **Logic**: Adds exposure to corporate bonds, slightly increasing risk but with the potential for higher income than government bonds.

#### 4. Vanguard Total Stock Market ETF (VTI)
- **Holdings**: **5%**.
- **Logic**: Provides diversified exposure to the broader U.S. stock market, adding a moderate growth potential.

#### 5. Vanguard Real Estate ETF (VNQ)
- **Holdings**: **5%**.
- **Logic**: Introduces real estate for income (via dividends) and growth, diversifying the portfolio with a different asset class.

### Next Steps

Please review the attached detailed breakdown of each holding and its expected impact on your portfolio. Your confirmation is essential for us to proceed with these changes.

We encourage you to review these recommendations and reach out with any questions or discussions. Our goal is to ensure your investment strategy aligns with your financial objectives and comfort with risk.

Warm Regards,
[Your Name]

""")


        







