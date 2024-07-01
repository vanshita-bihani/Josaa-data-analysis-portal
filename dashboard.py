def load_dashboard():
    @st.cache_data
    def get_data():
        df = pd.read_csv("./all data/2016allrounds.csv")
        return df

    try:
        df = get_data()
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return

    st.sidebar.header("Please Filter Here:")

    # Multiselect widgets for filtering
    Branch = st.sidebar.multiselect("Select The Branch:", options=df["Branch"].unique())
    Gender = st.sidebar.multiselect("Select The Gender:", options=df["Gender"].unique())
    Quota = st.sidebar.multiselect("Select The Quota:", options=df["Quota"].unique())
    Round = st.sidebar.multiselect("Select The Round:", options=df["round"].unique())
    Caste = st.sidebar.multiselect("Select The Caste:", options=df["Caste"].unique())

    # Initialize filters as True (select all)
    branch_filter = df["Branch"].isin(Branch) if Branch else pd.Series(True, index=df.index)
    gender_filter = df["Gender"].isin(Gender) if Gender else pd.Series(True, index=df.index)
    quota_filter = df["Quota"].isin(Quota) if Quota else pd.Series(True, index=df.index)
    round_filter = df["round"].isin(Round) if Round else pd.Series(True, index=df.index)
    caste_filter = df["Caste"].isin(Caste) if Caste else pd.Series(True, index=df.index)

    try:
        # Apply filters to the dataframe
        df_selection = df.loc[branch_filter & gender_filter & quota_filter & round_filter & caste_filter]
        
        if df_selection.empty:
            st.warning("No data matches the selected filters.")
            return

        st.title("Dashboard")
   
        # KPIs
        avg_opening_rank = int(round(df_selection["Opening Rank"].mean(), 0))
        avg_closing_rank = int(round(df_selection["Closing Rank"].mean(), 0))
        max_opening_rank = int(round(df_selection["Opening Rank"].min(), 0))
        min_closing_rank = int(round(df_selection["Closing Rank"].max(), 0))
        
        left_col, middle_col, right_col = st.columns(3)
       
        with left_col:
            st.subheader("Average Opening Rank: ")
            st.subheader(f"{avg_opening_rank:,}")

        with middle_col:
            st.subheader("Average Closing Rank: ")
            st.subheader(f"{avg_closing_rank:,}")

        with right_col:
            st.subheader("Minimum Opening Rank: ")
            st.subheader(f"{max_opening_rank:,}")
            st.subheader("Maximum Closing Rank: ")
            st.subheader(f"{min_closing_rank:,}")  # Fixed this line

        st.markdown("----")

        # Rest of your code for plots and dataframe display
        # ...

    except Exception as e:
        st.error(f"An error occurred: {e}")
        st.write("Debug info:")
        st.write("Data shape:", df.shape)
        st.write("Columns:", df.columns)
        st.write("Data types:", df.dtypes)
