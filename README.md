# pyobsplot

[![PyPI](https://img.shields.io/pypi/v/pyobsplot.svg?color=green)](https://pypi.org/project/pyobsplot)
[![Tests](https://github.com/juba/pyobsplot/actions/workflows/tests.yml/badge.svg)](https://github.com/juba/pyobsplot/actions/workflows/tests.yml)
[![Documentation](https://github.com/juba/pyobsplot/actions/workflows/publish.yml/badge.svg)](https://github.com/juba/pyobsplot/actions/workflows/publish.yml)

`pyobsplot` allows to use [Observable Plot](https://observablehq.com/@observablehq/plot?collection=@observablehq/plot) to create charts in Jupyter notebooks. Plots are produced as [widgets](https://ipywidgets.readthedocs.io/en/latest/index.html) from Python code with a syntax as close as possible to the JavaScript one.

It allows to do things like :

```python
import polars as pl
from pyobsplot import Obsplot, Plot

penguins = pl.read_csv("data/penguins.csv")

Obsplot({
    "grid": True,
    "color": {"legend": True},
    "marks": [
        Plot.dot(
            penguins, 
            {"x": "flipper_length_mm", "y": "body_mass_g", "fill": "species"}
        ),
        Plot.density(
            penguins, 
            {"x": "flipper_length_mm", "y": "body_mass_g", "stroke": "species"}
        )
    ]
})
```

![Sample plot screenshot](https://github.com/juba/pyobsplot/raw/main/doc/screenshots/readme_plot.png)


## Installation and usage

> **Warning**: this project is at a very early stage. There will be bugs, and please take a look at the limitations listed below.

`pyobsplot` can be installed with `pip`:

```sh
pip install pyobsplot
```

For usage instructions, see the [documentation website](https://juba.github.io/pyobsplot):

- See [getting started](https://juba.github.io/pyobsplot/getting_started.html) for a quick usage overview.
- See [usage](https://juba.github.io/pyobsplot/usage.html) for more detailed usage instructions.


## Features and limitations

**Features:**

- Syntax as close as possible to the JavaScript one
- Two renderers available: `widget`, which generates plots as Jupyter widgets, and `jsdom`, which generate SVG or HTML outputs
- [Pandas](https://pandas.pydata.org) and [polars](https://pola.rs) DataFrame and Series objects are serialized using [Arrow](https://arrow.apache.org) IPC format for improved speed and data type conversions
- Works offline, no iframe or dependency to Observable runtime
- Caching mechanism of data objects if they are used several times in the same plot
- Custom JavaScript code can be passed as strings with the `js` method
- Python `date` and `datetime` objects are automatically converted to JavaScript `Date` objects
- Plots can be defined with a dictionary, a call to a `Plot` mark function, or with `kwargs`. See [alternative syntaxes](usage.qmd#alternative-syntaxes).
- Works with Jupyter notebooks and Quarto HTML documents. Plots without legends are also supported in PDF and docx outputs with the `jsdom` renderer.

**Limitations:**

- Plots with legends don't work in Quarto in formats other than HTML.
- Some faceting operations produce warnings when used as top-level faceting (but the plots should be fine). This doesn't happen when you using mark-level faceting (with the `fx` and `fy` channels).



## Credits

- [Observable Plot](https://observablehq.com/@observablehq/plot?collection=@observablehq/plot), developed by [Mike Bostock](https://observablehq.com/@mbostock) and [Philippe Rivière](https://observablehq.com/@fil) among others.
- The widget is developed thanks to the [anywidget](https://anywidget.dev) framework.
- Some code from the `jsdom` renderer has been adapted from [altair_saver](https://github.com/altair-viz/altair_saver).
- The documentation website is generated by [Quarto](https://quarto.org) and the [bookup](https://github.com/juba/bookup-html) custom format.
