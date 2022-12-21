from typing import List

from shiny import *
from shiny.types import NavSetArg
from shiny.ui import h4
import skimage
import numpy as np
from PIL import Image, ImageOps
from pathlib import Path
from shiny import App, render, ui
from shiny.types import FileInfo, ImgData, SilentException

def nav_controls(prefix: str) -> List[NavSetArg]:
    return [
        ui.nav("Time Series", "Time series visualization from year 2020: ", ui.img(src="timeseries.png", style="width: 800px;")),
        ui.nav("First 5 observations", "First five observations from the whole dataset: ", ui.img(src="five.png", style="width: 800px;")),
        ui.nav("PM2.5 By Month", "Boxplot of PM2.5 by month in year of 2020: ", ui.img(src="box2020.png", style="width: 800px;")),
        ui.nav("PM2.5 Change"," How PM2.5 has changed on average over the years from 2015 to 2022: ", ui.img(src="byyear.png", style="width: 800px;")),
        ui.nav("Heatmap", "Correlation matrix for the dataset: ", ui.img(src="heatmap.png", style="width: 800px;")),
        ui.nav("Month Trend", "The monthly seasonal trend: ", ui.img(src="month_trend.png", style="width: 800px;")),

        ui.nav_spacer(),
        
    ]

app_ui = ui.page_navbar(
    title="EDA",
    bg="#0062cc",
    inverse=True,
    id="navbar_id",
    footer=ui.div(
        {"style": "width:80%;margin: 0 auto"},
        ui.tags.style(
            """
            h4 {
                margin-top: 3em;
            }
            """
        ),
        h4("EDA"),
        ui.navset_tab(*nav_controls("navset_tab()")),
        
    )
)


def server(input, output, session):
    @output
    @render.ui
    def images() -> ui.Tag:
        img = ui.img(src="heatmap.png", style="width: 400px;")
        return img
    
www_dir = Path(__file__).parent / "www"
app = App(app_ui, server, static_assets=www_dir)  
