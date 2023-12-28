import streamlit as st
import plotly.express as px
import pandas as pd
# import openai
import geopandas as gpd

# Page settings
st.set_page_config(
    page_title="ProsperaLima: Illuminating Pathways to Urban Excellence",
    page_icon="🏙️",
    layout="wide",
)

st.title("Navigating the Future: Insights and Strategies for Lima's Prosperity")

# Function to display content with shape and background color
def display_section(title, content, color="#f0f0f0"):
    st.write(
        f"""
        <div style="
            background-color: {color};
            padding: 15px;
            border-radius: 10px;
            margin-bottom: 20px;
        ">
            <h3>{title}</h3>
            {content}
        </div>
        """,
        unsafe_allow_html=True,
    )

# Income Insights Section
income_title = "Income Insights:"
income_content = """ 
**Key Findings:**
- San Juan de Miraflores and Pucusana contribute significantly to Lima's revenue.
- Diverse revenue sources, including property taxes and fines, showcase financial stability.
- Property taxes contribute approximately 45% to the total revenue.

**Recommendations:**
- Implement targeted tax incentives to stimulate economic activities.
- Strengthen property tax compliance through community engagement and awareness campaigns.
"""
display_section(income_title, income_content, color="#a6d6d6")

# Company Directory Section
company_title = "Company Directory:"
company_content = """
**Key Findings:**
- Manufacturing sector vital for Lima's economy.
- Concentration of large companies signifies economic robustness.
- Top three manufacturing sectors contributing to GDP: Textiles, Food, and Chemicals.

**Recommendations:**
- Foster collaboration between large companies and MSMEs for inclusive growth.
- Promote innovation in the manufacturing sector through research and development incentives.
- Introduce sector-specific investment forums to attract more businesses.
"""
display_section(company_title, company_content, color="#f0d6b4")

# Employment Insights Section
employment_title = "Employment Insights:"
employment_content = """ 
**Key Findings:**
- Informal employment poses a significant challenge, with over 58% of the population engaged in the informal sector.
- Adequate employment rate but underemployment remains high, especially in the service sector.
- Skill development programs can enhance employability and reduce underemployment.

**Recommendations:**
- Implement skill development programs with a focus on service sector needs.
- Encourage formalization through targeted policies and incentives.
- For districts with low workforce participation and pension scheme enrollment (e.g., SAN BARTOLO), consider targeted interventions.
- Develop industry-specific initiatives or incentives to encourage pension scheme enrollment based on the characteristics of each sector.
- Since public pension schemes have lower participation, collaborate with government agencies to promote public pension schemes and ensure workers are informed about all available options.

"""
display_section(employment_title, employment_content, color="#e3e3e3")

# Investment Projects Section
investment_title = "Investment Projects:"
investment_content = """
**Key Findings:**
- Provinces like Huaral, Huaura, and Cañete attract significant investments.
- Education and agriculture sectors receive notable attention.
- 60% of the investment projects are in the education sector.
- Units with a 100% success rate in project execution suggest these units effectively plan and formulate projects, ensuring successful execution.


**Recommendations:**
- Focus on sustainable and diversified investments, exploring opportunities in other sectors.
- Implement data-driven project selection criteria for optimal resource allocation.
- Promote knowledge sharing between successful formulating and executing units and those with lower success rates. Identify and implement best practices.
- Engage with stakeholders, including local communities, to gather insights on the impact of investments. This feedback can guide future project planning and execution.

"""
display_section(investment_title, investment_content, color="#c2d8c2")

# Future Strategies Section
future_title = "Future Strategies:"
future_content = """
**Key Insights:**
- Lima's economic growth is accompanied by challenges, including traffic congestion, air pollution, and social inequality.
- Continuous improvement culture is crucial for addressing disparities and fostering sustainable development.

**Strategies:**
- Embrace sustainable urban development practices to address rapid urbanization challenges.
- Prioritize social inclusivity in economic policies to reduce disparities.
- Implement data-driven decision-making processes for continuous improvement.
"""
display_section(future_title, future_content, color="#f9e4b7")

# Conclusion Section
conclusion_title = "Conclusion:"
conclusion_content = """
The prosperity of Lima lies in its ability to leverage diverse data insights for informed decision-making. Policymakers and city leaders must focus on fostering collaboration, promoting innovation, and implementing targeted policies to address challenges. By navigating the future with strategic initiatives, Lima can unlock its true potential, leading to a more prosperous and inclusive city.

"""
display_section(conclusion_title, conclusion_content, color="skyblue")

st.header("Empower Lima. Shape the Future.")
