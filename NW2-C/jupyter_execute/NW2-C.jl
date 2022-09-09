using DrWatson
@quickactivate

using CairoMakie

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
    x->  -(ℯ^(-x) -1) * 3,
    color = :green
)
text!(ax2, "Edukte", position = (1, 3), color = :red)
text!(ax2, "Produkte", position = (1, .8), color = :green)


fig

###### 
fig = Figure(resolution = (1200, 800))

u = 5
ts = 0:.01:u

endtherm = Axis(fig[1, 1],
    title = "Endotherme Reaktion",
    ylabel = "Freie Reaktionsenthalpie",
    xlabel = "Zeit"
)
exotherm = Axis(fig[1, 2],
    title = "Exotherme Reaktion",
    ylabel = "Freie Reaktionsenthalpie",
    xlabel = "Zeit"
)

lines!(endtherm,
    ts,
    t-> atan(8t-16)/π + .5 + ℯ^(-(1.75(t - 2))^2)
)
arrows!(endtherm,
    [2.15], [.01],
    [0],
    [1.69],
    color = :green
)
arrows!(endtherm,
    [2.2], [1.7],
    [0],
    [-.7],
    color = :red
)
text!(endtherm, 
    2.2, .6,
    text = "Aktivierungsenergie",
    color = :green
)
text!(endtherm, 
    2.2, .7,
    text = "ΔH\nfreie Reaktionsenthalpie",
    color = :red
)


lines!(exotherm,
    ts,
    t-> -(atan(8t-16)/π) + .5 + ℯ^(-(1.75(t - 2))^2)
)

arrows!(exotherm,
    [1.8], [1],
    [0],
    [.69],
    color = :green
)

arrows!(exotherm,
    [1.85], [1.7],
    [0],
    [-1.69],
    color = :red
)

text!(exotherm, 
    2.5, .6,
    text = "Aktivierungsenergie",
    color = :green
)

text!(exotherm, 
    2.5, .7,
    text = "ΔH\nfreie Reaktionsenthalpie",
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
