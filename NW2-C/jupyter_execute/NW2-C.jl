using DrWatson
@quickactivate

using DataFrames
using CairoMakie

d = Dict()

d[:n] = [1,2,3,4]
d[:Schale] = ["K", "L", "M", "N"]
d[:Nebenquantenzahl] = [
    [0],
    [0, 1],
    [0, 1, 2],
    [0, 1, 2, 3]
]

d[:m_L] = [
    [0],
    [-1, 0, 1],
    [-2, -1, 0, 1, 2],
    [-3, -2, -1, 0, 1, 2, 3]
]
d[:m_s] = ("± 1/2")
d[:e] = [
    [2],
    [2, 6],
    [2, 6, 10],
    [2, 6, 10, 14]
]
d[:orbital] = [
    ["s"],
    ["s", "p"],
    ["s", "p", "d"],
    ["s", "p", "d", "f"]
]

d |> DataFrame |> print

xs = 0:.1:5.5

fig = Figure(resolution =(1200, 300))

ax = Axis(fig[1, 1],
    xlabel = "Zeit/ Reaktionsverlauf",
    ylabel = "Konzentration"
)
lines!(ax, xs,
    x-> (ℯ^(-x)*2)+2,
    color = :red
)
lines!(ax, xs,
    x->  -(ℯ^(-x) -1)*2,
    color = :green
)
text!(ax, "Edukte", position = (1, 3), color = :red)
text!(ax, "Produkte", position = (1, .8), color = :green)

ax2 = Axis(fig[1, 2],
    xlabel = "Zeit/ Reaktionsverlauf",
    ylabel = "Konzentration"
)
lines!(ax2, xs,
    x-> (ℯ^(-x)*3)+1,
    color = :red
)
lines!(ax2, xs,
    x->  -(ℯ^(-x) -1) * 2.5,
    color = :green
)
text!(ax2, "Edukte", position = (1, 3), color = :red)
text!(ax2, "Produkte", position = (1, .8), color = :green)


fig

xs = -2:.01:2

fig = Figure()

ax = Axis(fig[1, 1],
    title = "Titration",
    xlabel = "NaOH / [ml]",
    ylabel = "pH-Wert"
)

ylims!(ax, 0,14)

lines!(ax, xs,
    x-> 12/(1 + ℯ^(-x*10)) + 1,
    color = :red
)
fig

xs = -2:.01:2

fig = Figure()

ax = Axis(fig[1, 1],
    title = "Titration",
    xlabel = "NaOH / [ml]",
    ylabel = "pH-Wert"
)

lines!(ax, xs,
    x-> 12/(1 + ℯ^(-x*10)) + 1,
    color = :red
)

lines!(ax, xs, 
    x-> tan(2.2x/π)/2 + 7
)

text!("Mit Puffer HA (pK_s = 7)", position=(-1.75, 7))
fig
