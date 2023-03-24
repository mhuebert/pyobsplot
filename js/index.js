import * as Plot from "@observablehq/plot"
import * as d3 from "d3"
import * as arrow from "apache-arrow"


export function render(view) {
    let spec = () => view.model.get("spec");
    view.el.appendChild(generate_plot(spec()));
    view.model.on('change:spec', () => _onValueChanged(view, view.el));
}

function parse_spec(spec) {
    if (spec === null) {
        return null
    }
    if (Array.isArray(spec)) {
        return spec.map(d => parse_spec(d))
    }
    if (spec["ipyobsplot-type"] == "DataFrame") {
        return arrow.tableFromIPC(spec["value"])
    }
    if (typeof spec === 'string' || spec instanceof String) {
        return spec
    }
    if (Object.entries(spec).length == 0) {
        return spec
    }
    if (spec["ipyobsplot-type"] == "function") {
        let fun;
        switch (spec["module"]) {
            case "Plot":
                fun = Plot[spec["method"]]
                break;
            case "d3":
                fun = d3[spec["method"]]
                break;
            default:
                throw new Error(`Invalid module: ${spec["module"]}`)
        }
        if (fun === undefined) {
            throw new Error(`${spec["module"]}.${spec["method"]} is not defined`)
        }
        return fun.call(null, ...parse_spec(spec["args"]));
    }
    let ret = {}
    for (const [key, value] of Object.entries(spec)) {
        ret[key] = parse_spec(value)
    }
    return ret
}

function generate_plot(spec) {
    let plot = document.createElement("div");
    plot.classList.add("ipyobsplot-plot");
    let out
    try {
        out = parse_spec(spec);
        if (spec["ipyobsplot-type"] == "function") {
            if (!(out instanceof Element)) {
                out = svg.plot()
            }
        } else {
            out = Plot.plot(out)
        }
    } catch (error) {
        out = document.createElement("pre")
        out.classList.add("ipyobsplot-error")
        out.textContent = error
    }
    plot.appendChild(out)
    return plot
}

function _onValueChanged(view, el) {
    let plot = el.querySelector(".ipyobsplot-plot")
    el.removeChild(plot)
    let spec = () => view.model.get("spec");
    el.appendChild(generate_plot(spec()));

}

