# -*- coding:utf-8 -*-
import streamlit as st
import plotly.graph_objs as go
from plotly.subplots import make_subplots
import seaborn as sns

def main():
    st.title("Streamlit with Plotly")
    tips = sns.load_dataset('tips')
    m_tips = tips.loc[tips['sex'] == 'Male']
    f_tips = tips.loc[tips['sex'] == 'Female']

    fig = make_subplots(rows = 1,
                        cols = 2,
                        subplot_titles=('Male', 'Female'),
                        shared_yaxes=True,
                        shared_xaxes=True,
                        x_title='Total Bill($)'
                        )
    fig.add_trace(go.Scatter(x = m_tips['total_bill'], y = m_tips['tip'], mode='markers'), row=1, col=1)
    fig.add_trace(go.Scatter(x = f_tips['total_bill'], y = f_tips['tip'], mode='markers'), row=1, col=2)
    fig.update_yaxes(title_text="Tip($)", row=1, col=1)
    fig.update_xaxes(range=[0, 60])
    fig.update_layout(showlegend=False)

    # Display visualization
    st.plotly_chart(fig, use_container_width=True)

if __name__ == "__main__":
    main()
