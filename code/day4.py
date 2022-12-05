# import libs
import pandas as pd
import numpy as np
from datetime import datetime

import streamlit as st

import plotly.graph_objects as go
import plotly.express as px

# load data
df_agg =  pd.read_csv('../data/ken_jee/Aggregated_Metrics_By_Video.csv').iloc[1:,:]
df_agg_sub = pd.read_csv('../data/ken_jee/Aggregated_Metrics_By_Country_And_Subscriber_Status.csv')
df_comments = pd.read_csv('../data/ken_jee/Aggregated_Metrics_By_Video.csv')
df_time = pd.read_csv('../data/ken_jee/Video_Performance_Over_Time.csv')
