import pandas as pd
import plotly.express as px
import streamlit as st
from streamlit_option_menu import option_menu
import logging


def load_dashboard():
        
    # st.set_page_config(page_title="Josaa Data Analysis", layout="wide")

    # Load the data
    @st.cache_data
    def get_data():

        df = pd.read_csv("./all data/2016allrounds.csv")
        return df


    df=get_data()



    # st.set_page_config(page_title="Josaa Data Analysis", layout="wide")

    st.sidebar.header("Please Filter Here:")

    # Multiselect widgets for filtering
    Branch = st.sidebar.multiselect(
        "Select The Branch:", options=df["Branch"].unique())

    Gender = st.sidebar.multiselect(
        "Select The Gender:", options=df["Gender"].unique())

    Quota = st.sidebar.multiselect(
        "Select The Quota:", options=df["Quota"].unique())

    Round = st.sidebar.multiselect(
        "Select The Round:", options=df["round"].unique())

    Caste = st.sidebar.multiselect(
        "Select The Caste:", options=df["Caste"].unique())

    # Initialize filters as True (select all)
    branch_filter = df["Branch"].isin(Branch) if Branch else True
    gender_filter = df["Gender"].isin(Gender) if Gender else True
    quota_filter = df["Quota"].isin(Quota) if Quota else True
    round_filter = df["round"].isin(Round) if Round else True
    caste_filter = df["Caste"].isin(Caste) if Caste else True


    # branch_filter = df["Branch"].isin(Branch) if Branch else df["Branch"].notna()
    # gender_filter = df["Gender"].isin(Gender) if Gender else df["Gender"].notna()
    # quota_filter = df["Quota"].isin(Quota) if Quota else df["Quota"].notna()
    # round_filter = df["round"].isin(Round) if Round else df["round"].notna()
    # caste_filter = df["Caste"].isin(Caste) if Caste else df["Caste"].notna()


    #df_selection = df[branch_filter & gender_filter & quota_filter & round_filter & caste_filter]
    df_selection={}
    try:
    # Apply filters to the dataframe
        df_selection = df.loc[branch_filter & gender_filter & quota_filter & round_filter & caste_filter]
    except Exception as e:
        st.error("An error occurred: {}".format(e))

    st.title("Dashboard ")

   
    #kpis making
    avg_opening_rank=int(round(df_selection["Opening Rank"].mean(),0))
    avg_closing_rank=int(round(df_selection["Closing Rank"].mean(),0))
    max_opening_rank=int(round(df_selection["Opening Rank"].min(),0))
    min_closing_rank=int(round(df_selection["Closing Rank"].max(),0))



    left_col,middle_col,right_col=st.columns(3)

    with left_col:
        st.subheader("Average Opening Rank: ")
        st.subheader(f"{avg_opening_rank:,}")


    with middle_col:
        st.subheader("Average Closing Rank: ")
        st.subheader(f"{avg_closing_rank:,}")


    with right_col:
        st.subheader("Minimum Opening Rank: ")
        st.subheader(f"{max_opening_rank:,}")
        st.subheader("Maximum closing Rank: ")
        st.subheader(f"{max_opening_rank:,}")




    st.markdown("----")



    opencollegewise_display = df_selection.groupby(by=["College"])[["Opening Rank"]].mean().reset_index()
    closecollegewise_display = df_selection.groupby(by=["College"])[["Closing Rank"]].mean().reset_index()


    # Create a bar plot
    figure1 = px.bar(
        opencollegewise_display,
        x="Opening Rank",
        y="College",
        orientation="h",
        title="<b>Opening Ranks by College</b>",
        color_discrete_sequence=["#0083B8"] * len(opencollegewise_display),
        template="plotly_white",
    )

    figure2 = px.bar(
        closecollegewise_display,
        x="Closing Rank",
        y="College",
        orientation="h",
        title="<b>Closing Ranks by College</b>",
        color_discrete_sequence=["#0083B8"] * len(closecollegewise_display),
        template="plotly_white",
    )

    # letcol,rigcol=st.columns(2)
    # letcol.plotly_chart(figure1,use_container_width=True)
    # rigcol.plotly_chart(figure2,use_container_width=True)

    hide_st_style= """
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                header {visibility:hidden;}
                </style>
            """

    st.markdown(hide_st_style, unsafe_allow_html=True)

    st.plotly_chart(figure1)
    st.plotly_chart(figure2)


    st.dataframe(df_selection)

    # Display filtered dataframe
    # st.dataframe(df_selection)
