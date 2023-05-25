"""
Utility methods and variables 
"""

import pathlib

# Output directory of esbuild
bundler_output_dir = pathlib.Path(__file__).parent / "static"

# Minimum npm package version
min_npm_version = "0.3.4"

# Allowed default values
allowed_defaults = [
    "marginTop",
    "marginRight",
    "marginBottom",
    "marginLeft",
    "margin",
    "width",
    "height",
    "aspectRatio",
    "style",
]

# List of existing plot methods
# Generated by tools/get_plot_methods.js
plot_methods = (
    "Area",
    "Arrow",
    "BarX",
    "BarY",
    "Cell",
    "Contour",
    "Density",
    "Dot",
    "Frame",
    "Geo",
    "Hexgrid",
    "Image",
    "Line",
    "Link",
    "Mark",
    "Raster",
    "Rect",
    "RuleX",
    "RuleY",
    "Text",
    "TickX",
    "TickY",
    "Tip",
    "Vector",
    "area",
    "areaX",
    "areaY",
    "arrow",
    "auto",
    "autoSpec",
    "axisFx",
    "axisFy",
    "axisX",
    "axisY",
    "barX",
    "barY",
    "bin",
    "binX",
    "binY",
    "boxX",
    "boxY",
    "cell",
    "cellX",
    "cellY",
    "centroid",
    "circle",
    "cluster",
    "column",
    "contour",
    "crosshair",
    "crosshairX",
    "crosshairY",
    "delaunayLink",
    "delaunayMesh",
    "density",
    "dodgeX",
    "dodgeY",
    "dot",
    "dotX",
    "dotY",
    "filter",
    "formatIsoDate",
    "formatMonth",
    "formatWeekday",
    "frame",
    "geo",
    "geoCentroid",
    "graticule",
    "gridFx",
    "gridFy",
    "gridX",
    "gridY",
    "group",
    "groupX",
    "groupY",
    "groupZ",
    "hexagon",
    "hexbin",
    "hexgrid",
    "hull",
    "identity",
    "image",
    "indexOf",
    "initializer",
    "interpolateNearest",
    "interpolateNone",
    "interpolatorBarycentric",
    "interpolatorRandomWalk",
    "legend",
    "line",
    "lineX",
    "lineY",
    "linearRegressionX",
    "linearRegressionY",
    "link",
    "map",
    "mapX",
    "mapY",
    "marks",
    "normalize",
    "normalizeX",
    "normalizeY",
    "plot",
    "pointer",
    "pointerX",
    "pointerY",
    "raster",
    "rect",
    "rectX",
    "rectY",
    "reverse",
    "ruleX",
    "ruleY",
    "scale",
    "select",
    "selectFirst",
    "selectLast",
    "selectMaxX",
    "selectMaxY",
    "selectMinX",
    "selectMinY",
    "shuffle",
    "sort",
    "sphere",
    "spike",
    "stackX",
    "stackX1",
    "stackX2",
    "stackY",
    "stackY1",
    "stackY2",
    "text",
    "textX",
    "textY",
    "tickX",
    "tickY",
    "tip",
    "transform",
    "tree",
    "treeLink",
    "treeNode",
    "valueof",
    "vector",
    "vectorX",
    "vectorY",
    "voronoi",
    "voronoiMesh",
    "window",
    "windowX",
    "windowY",
)
