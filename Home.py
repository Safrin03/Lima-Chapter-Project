import streamlit as st
import plotly.express as px
import pandas as pd
import openai
import geopandas as gpd


# Page settings
st.set_page_config(
    page_title="ProsperaLima: Illuminating Pathways to Urban Excellence",
    page_icon="🏙️",
    layout="wide",
)


# Dataset
dataset_url = r"C:\Users\l\Downloads\Projects\Lima Chapter Project\Population.csv"


@st.cache_data
# read csv from a URL
def get_data() -> pd.DataFrame:
    return pd.read_csv(dataset_url)

data = gpd.read_file(r"C:\Users\l\Downloads\Projects\Lima Chapter Project\PER_adm\PER_adm3.shp")

df = get_data()
lima_data = data[data['NAME_1'].isin(['Lima Province'])]
# Convert population columns to numeric (remove commas)
df[['1993', '2007', '2017', '2022']] = df[['1993', '2007', '2017', '2022']].replace({',': ''}, regex=True).astype(int)


# Main Page ------------

# All information
population_info = {
    'Total Population': '10.1 million in the city and 11.3 million in the Lima Metropolitan Area',
    'Population Density': 'Around 3,200 people/km²',
    'Total Working-age Population': '8.45 million',
    'Economically Active Population in Lima': '5.58 million',
}
employment_info = {
    "Adequate employment rate": "53.8 %",
    "Underemployment rate": "39.7 % (7.8 % by hours, 31.9 % by income)",
    "Unemployment rate": "6.6 %",
    "Formal employment": "41.8 %",
    "Informal employment": "58.2 %",
}
salary_info = {
    "Minimum wage in Peru since May 2022": "S / 1025 per month",
    "Average monthly income in Lima": "S / 1, 924.70",
}


gdp_info = {
    "Total GDP of Lima": "$222.1 billion",
    "Contribution to Peru's GDP": "Lima contributes over two-thirds (approximately 66%) and "
                                  "Lima generates 45% of Peru's national GDP",
    "Contribution to Peru's industrial GDP": "Lima generates 60% of Peru's Industrial GDP",
}
gdp_data = {
    'GDP': 222.1,
    'Lima Share in Peru\'s GDP': 66,
    'Lima Share in Peru\'s National GDP': 45,
    'Lima Share in Industrial GDP': 60,
}

# creating column for homepage
col1, col2 = st.columns([2, 8])

# Create a session state
if "button_state" not in st.session_state:
    st.session_state.button_state = False

with col1:
    # Define your CSS style
    style = """
    <style>
        .rectangle {
            background-color: skyblue;
            display: flex;
            align-items: center;
            justify-content: center;
            border: 0.5px solid black;
            border-radius: 5px;
            margin-top: 10px;
            padding: 10px;
        }
    </style>
    """
    text1 = "Welcome to ProsperaLima, where data meets transformation! Our mission is to illuminate the path for Lima's prosperous future through data-driven insights and meaningful analytics. Discover the heartbeat of Lima's economy, population dynamics, and key focus areas that will shape the city's trajectory towards sustainable growth and enhanced quality of life."
    text2 = "Mission: ProsperaLima's mission is to transform data into actionable insights, fostering positive change, and driving Lima towards new heights of vitality and progress. By tapping into diverse datasets, including economic indicators, population dynamics, and infrastructure projects, we aim to provide a comprehensive understanding of Lima's current landscape and its untapped potential."
    text3 = "Why ProsperaLima? ProsperaLima stands as a beacon for informed decision-making and community engagement. By translating complex data into accessible narratives, we aim to inspire collaborative efforts towards a prosperous, inclusive, and resilient Lima. ProsperaLima is not just a dashboard; it's a dynamic narrative of Lima's evolution towards prosperity."
    text4 = "Join us on this transformative journey as we unlock the true potential of Lima, paving the way for a city that thrives in innovation, equity, and well-being."

    st.markdown(style, unsafe_allow_html=True)
    # Create a rectangle with text inside
    st.markdown(f'<div class="rectangle" style="width:{text1}px; height:auto;">{text1}</div>',
                unsafe_allow_html=True)
    st.markdown(f'<div class="rectangle" style="width:{text2}px; height:auto;">{text2}</div>',
                unsafe_allow_html=True)
    st.markdown(f'<div class="rectangle" style="width:{text3}px; height:auto;">{text3}</div>',
                unsafe_allow_html=True)
    st.markdown(f'<div class="rectangle" style="width:{text4}px; height:auto;">{text4}</div>',
                unsafe_allow_html=True)

with col2:
    st.title("Homepage: Overview of Lima Metropolitan Area ")
    # Create a button to display population data
    button1 = st.button("Population Data")
    if button1:
        # Toggle the button state
        st.session_state.button_state = not st.session_state.button_state

    # Display the sample of the population data if the button is pressed
    if st.session_state.button_state:
        # Display the sample of the population data
        st.subheader("Population Dataset of Lima Province:")
        st.dataframe(df[['District', '1993', '2007', '2017', '2022']])
    else:
        # Convert to GeoDataFrame
        merged_df = pd.merge(lima_data, df, left_on='NAME_3', right_on='District', how='right')
        gdf = gpd.GeoDataFrame(merged_df, geometry='geometry_x')

        # Create a GeoJSON-like object
        geojson_data = gdf.to_crs(epsg=4326).__geo_interface__

        # Create a choropleth map
        fig_map = px.choropleth_mapbox(
            df,
            geojson=geojson_data,
            locations=df.District,
            featureidkey="properties.District",
            color=df["District"],
            hover_name='District',
            labels={'District': 'Districts'},
            mapbox_style="carto-positron",
            center={"lat": -12.0464, "lon": -77.0428},
            zoom=7.8,
        )

        fig = px.choropleth_mapbox(
            df,
            geojson=geojson_data,
            locations=df.District,
            featureidkey="properties.District",
            color=df["2022"],
            hover_name='District',
            color_continuous_scale="spectral",
            labels={'2022': 'Population', 'District': 'District'},
            mapbox_style="carto-positron",
            center={"lat": -12.0464, "lon": -77.0428},
            zoom=7.8,
        )

        # Create a line chart for population over the years
        fig_line = px.line(
            df,
            x='District',
            y=['1993', '2007', '2017', '2022'],
            labels={'value': 'Population', 'variable': 'Year'},
            # line_shape = 'linear',
            # line_dash_sequence=['solid', 'dash', 'dot', 'dashdot'],
            # markers=True,
            # template='plotly_dark'
        )

        # Create a pie chart
        fig_gdp = px.pie(
            names=list(gdp_data.keys()),
            values=list(gdp_data.values()),
        )

        tab1, tab2, tab3, tab4 = st.tabs(["Demographics", "Population", "GDP Contribution", "Social Indicators"])

        with tab1:
            st.header("Geographic Distribution of Lima Province")
            st.plotly_chart(fig_map)
            st.write("Lima Province, situated on Peru's central western coast, features diverse geography and encompasses 43 districts, "
                     "blending urban, suburban, and rural landscapes. The capital city, Lima, functions as the country's political, "
                     "cultural, and economic center, positioned along the Pacific Ocean, impacting its climate and lifestyle. Moving inland, "
                     "the province extends to higher elevations, yielding a mix of climates from coastal deserts to cooler mountainous regions."
                     "\n The eastern part of Lima Province showcases more mountainous terrain, hosting districts like La Molina and San Borja at elevated altitudes. "
                     "This geographical variety contributes to the province's unique climatic and topographical characteristics.")

            st.image(r"Images/Lima City Picture 2.jpeg", width=750, caption = "Plaza Mayor de Lima")
            # GitHub Logo
            github_logo = r"Images/Github logo.jpeg"
            st.image(github_logo,width=50)
            github_link = "https://github.com/OmdenaLimaChapter/1.First-project_Lima_Peru_Open_Data/tree/main/Datasets/economy-and-finance/Province%20of%20Lima"
            # Display GitHub logo with link
            github_html = f'<a href="{github_link}" target="_blank"><img src="data:image/jpeg;base64,{github_logo}" width="100"></a>'
            st.markdown(github_html, unsafe_allow_html=True)
            # Omdena Logo
            omdena_logo = r"Images/Omdena Logo.jpeg"
            st.image(omdena_logo,width=40)
            omdena_link = "https://omdena.com/chapter-challenges/analyzing-open-data-to-drive-positive-change-in-lima/#"
            omdena_html = f'<a href="{omdena_link}" target="_blank"><img src="data:image/jpeg;base64,{omdena_logo}" width="100"></a>'
            st.markdown(omdena_html, unsafe_allow_html=True)


        with tab2:
            st.header("Population Info")
            for key, value in population_info.items():
                st.write(f"**{key}:** {value}")
            # Display the choropleth map
            st.subheader("District-wise Population for the Year 2022")
            st.plotly_chart(fig)
            with st.container():
                st.subheader("Population Growth Over the Years")
                st.plotly_chart(fig_line)
            st.write("The population of Lima has more than doubled since 1993, growing from 5.7 million to over 10 million in 2022")

        with tab3:
            st.header("Lima's Contribution to Peru's GDP")
            st.markdown("Peruvian currency :1 USD = 3.775741 PEN")
            for key, value in gdp_info.items():
                st.write(f"**{key}:** {value}")
            st.plotly_chart(fig_gdp)
            st.write("Lima's GDP includes significant contributions from the industrial, financial, and retail sectors.")

        with tab4:
            st.header("Employment:")
            for key, value in employment_info.items():
                st.write(f"**{key}:** {value}")
            st.header("Salary:")
            for key, value in salary_info.items():
                st.write(f"**{key}:** {value}")
            st.header("Poverty:")
            st.write("26.5% of Lima's population lives in poverty \n 2% of Lima's population lives in extreme poverty")


        # with data_container:
        #     button1, expander1 = st.columns(2)
        #     with button1:
        #         st.button(button1)
        #     with expander1:
        #         st.expander(expander1, use_container_width=True)


# Create an Expander to display population information
# expander1 = st.expander(label="Population Information", expanded=False)

# District_filter = st.selectbox("Select the Province", pd.unique(df["District"]))
# # creating a single-element container
# placeholder = st.empty()
# # dataframe filter
# df = df[df["District"] == District_filter]

# Chatbox in the sidebar
## chatgpt api
openai.api_key = st.secrets["OPEN_API_KEY"]
if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"

with st.sidebar:
    st.write("Get Started: Embark on a journey of discovery. Click, explore, and empower Lima's future with ProsperaLima.")
    st.sidebar.title("ChatGPT like Clone")

    # with st.expander("Chat with Assistant"):
    #     with st.chat_message(name="assistant"):
    #         st.write("Hello!")

    ## Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    ## Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message['role']):
            st.markdown(message['content'])

    ## React to user input
    prompt = st.text_input("Hello, Do you have any questions?")
    if prompt:
        # Display user message in chat message container
        with st.chat_message("user"):
            st.markdown(prompt)
        # Add user message to chat history
        st.session_state.messages. append({'role': 'user', 'content': prompt})

        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            full_response = ""
            for response in openai.ChatCompletion.create(
                model=st.session_state["openai_model"],
                messages=[
                    {"role": m["role"], "content": m["content"]}
                    for m in st.session_state.messages
                ],
                stream=True,
            ):
                full_response += response.choices[0].delta.get("content", "")
                message_placeholder.markdown(full_response + "┃")
            message_placeholder.markdown(full_response)
        st.session_state.messages.append({"role": "assistant", "content": full_response})


