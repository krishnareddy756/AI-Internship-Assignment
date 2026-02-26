## Importing libraries and files
from crewai import Task

from agents import financial_analyst, verifier, investment_advisor, risk_assessor

## Creating a task to help solve user's query
analyze_financial_document = Task(
    description="Analyze the financial document provided and answer the user's query: {query}. \
Carefully examine the financial statements, key metrics, and performance indicators. \
Identify important trends, ratios, and financial health indicators. \
Summarize key findings and their implications for investment decisions. \
Use relevant data from the document to support your analysis.",

    expected_output="""Provide a comprehensive financial analysis including:
- Executive Summary of key financial metrics
- Balance Sheet Analysis (assets, liabilities, equity trends)
- Income Statement Review (revenue, profitability, margins)
- Cash Flow Assessment (operating, investing, financing activities)
- Financial Ratios (liquidity, profitability, efficiency ratios)
- Key Findings and Trends
- Investment Implications
- Risk Factors to Consider
- Data sources and references""",

    agent=financial_analyst,
    async_execution=False,
)

## Creating an investment analysis task
investment_analysis = Task(
    description="Based on the financial document analysis provided, develop professional investment recommendations addressing: {query}. \
Evaluate the company's market position, competitive advantages, and growth prospects. \
Assess valuation metrics relative to peers. \
Consider sector trends and macro economic factors. \
Provide specific, actionable investment recommendations with clear rationale.",

    expected_output="""Investment recommendations including:
- Company Overview and Current Valuation
- Valuation Analysis (P/E, P/B, DCF estimates)
- Competitive Position and Market Dynamics
- Growth Prospects and Opportunities
- Key Risks and Concerns
- Investment Rating (Buy/Hold/Sell) with justification
- Target Price and Investment Thesis
- Time Horizon for the recommendation
- Suitable for what investor profile
""",

    agent=investment_advisor,
    async_execution=False,
)

## Creating a risk assessment task
risk_assessment = Task(
    description="Conduct comprehensive risk assessment based on the financial document: {query}. \
Identify financial, operational, market, and compliance risks. \
Assess the company's ability to manage these risks. \
Analyze sensitivity to market changes, competitive threats, and regulatory changes. \
Quantify risk levels where possible and recommend mitigation strategies.",

    expected_output="""Complete risk assessment including:
- Executive Summary of Risk Profile
- Financial Risk Analysis (liquidity, solvency, debt ratios)
- Operational Risk Assessment (supply chain, key person risk)
- Market Risk (competitive position, industry disruption)
- Regulatory and Compliance Risk
- External Risk Factors (macro, geopolitical)
- Risk Rating (Low/Medium/High) with explanation
- Recommended Risk Mitigation Strategies
- Sensitivity Analysis Results
- Risk-Adjusted Valuation Impact
""",

    agent=risk_assessor,
    async_execution=False,
)

    
verification = Task(
    description="Verify the authenticity and completeness of the financial document: {query}. \
Assess whether the document is a legitimate financial report. \
Check for required financial statement components. \
Validate data consistency and format compliance. \
Identify any missing or concerning information.",

    expected_output="""Verification report including:
- Document Authenticity Assessment
- Financial Report Type Identification (10-K, Annual Report, etc.)
- Required Components Check (Balance Sheet, Income Statement, Cash Flow)
- Data Quality and Consistency Review
- Red Flags or Concerns Identified
- Verification Status (Approved/Needs Review/Rejected)
- Recommendations for Analysis
- Data collection date and report period confirmation
""",

    agent=verifier,
    async_execution=False
)