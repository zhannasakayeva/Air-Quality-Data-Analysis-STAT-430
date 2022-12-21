from shiny import App, render, ui
import matplotlib.pyplot as plt
import numpy as np
import statsmodels.api as sm
import pandas as pd

app_ui = ui.page_fluid(
  # App title
  ui.panel_title("Regression Model Prediction"),

  # Sidebar layout container
  ui.layout_sidebar(

    # Sidebar inputs 
    ui.panel_sidebar(
      ui.input_slider("O3", "AQI_O3_4hr", 0, 150, 1),
      ui.input_slider("PM10", "AQI_PM10", 0, 1000, 5),
    ),

    # Output display region 
    ui.output_text_verbatim("txt"),
    
  ),
)

    # Part 2: server ----
def server(input, output, session):
  @output
  @render.text

  def txt():
    OLS2 = sm.load("OLS2.pickle")
    a = pd.DataFrame({'const': [1],  
              'AQI_O3_4hr': [input.O3()], 
              'AQI_PM10': [input.PM10()]})
    return f"The prediction of AQI_PM2.5 concentration is {OLS2.predict(a)[0]}"

app = App(app_ui, server)
