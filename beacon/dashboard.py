# import libraries
import time  
import numpy as np  
import pandas as pd  
import plotly.express as px 
import streamlit as st  

st.set_page_config(
    page_title="GitHub Repository Dataset",
    page_icon="🖥️",
    layout="wide",
)

st.title("GitHub Repository Dataset")
st.write("A dataset of 1,052 GitHub repositories along with their details.")

df = pd.read_csv("archive/github_dataset.csv")

st.title("Live Dashboard for Github Repositories")

df["language"] = df.language.fillna("Not specified")

lang_filter = st.selectbox("Select language", pd.unique(df["language"]))

placeholder = st.empty()

df = df[df["language"] == lang_filter]

for seconds in range(200):
    df["issues"] = df["issues_count"] * np.random.choice(range(1, 5)) # issues_count 
    df["pull_reqs"] = df["pull_requests"] * np.random.choice(range(1, 5)) # pull_requests
    avg_issues = np.mean(df["issues"])
    count_less_ten = int(df[(df["contributors"] > 8)]["contributors"].count() + np.random.choice(range(1, 30))) 
    pulls = np.mean(df["pull_reqs"])
    
    with placeholder.container():
        kpi1, kpi2, kpi3 = st.columns(3)

        kpi1.metric(label= "Issues Count ⚠️",
                    value= round(avg_issues),
                    delta= round(avg_issues) - 10,)
        
        kpi2.metric(label= "Repositories with 8 contributors or more 🧍‍",
                    value= int(count_less_ten),
                    delta= -10 + count_less_ten,)
        
        kpi3.metric(label= "Pull Requests 📩 ",
                    value= round(pulls), 
                    delta= round(pulls / count_less_ten),) # delta=-round(pulls / count_over_ten) * 100, 
    
        fig_col1, fig_col2 = st.columns(2)
        
        with fig_col1:
            st.markdown("### First Chart")
            fig = px.density_heatmap(data_frame=df, y="issues", x="contributors")
            st.write(fig)
            
        with fig_col2:
            st.markdown("### Second Chart")
            fig2 = px.histogram(data_frame=df, x="issues")
            st.write(fig2)
            
        st.markdown("### Detailed Data View")
        st.dataframe(df)
        time.sleep(1)
        
##############################################
################## END #######################
##############################################
        
