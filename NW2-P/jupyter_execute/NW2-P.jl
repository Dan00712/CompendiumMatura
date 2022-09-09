using DrWatson
@quickactivate
"Test"

using CairoMakie

@__DIR__

fig = Figure(resolution = (1200, 400))

acceleration = Axis(fig[1, 1],
    title = "Beschleunigung",
    xlabel = "Zeit",
)
speed = Axis(fig[1, 2],
    title = "Geschwindigkeit",
    xlabel = "Zeit"
)
distance = Axis(fig[1,3],
    title = "Weg",
    xlabel = "Zeit"
)

A = 2
v_0 = 5

a = (t)-> A
v = (t)-> (A * t) + v_0
s = (t)-> .5 * A * t^2 + v_0 * t

ts = 0:.1:8

lines!(acceleration, ts, a)
lines!(speed, ts, v)
lines!(distance, ts, s)

fig



fig = Figure()

ax = Axis(fig[1, 1])

vs = 0:.2:5
f_0 =  5_000
c = 340

# Sender Bewegent sich auf Quelle zu
lines!(ax,
    vs,
    v-> f_0 * (c)/(c + v),
    color = :green
)

fig

fig = Figure(resolution = (600*3, 800))

#isobar
ax1 = fig[1, 1] = Axis(fig,
	title = "Isobar",
	xlabel = "V",
	ylabel = "p"
)
xlims!(ax1, 0, 10)
ylims!(ax1, 0, 10)
lines!(ax1, [1, 6],
	V->1
)

# isochor
ax2 = fig[1, 2] = Axis(fig,
	title = "Isochor",
	xlabel = "V",
	ylabel = "p"
)
xlims!(ax2, 0, 10)
ylims!(ax2, 0, 10)
lines!(ax2, [1, 1], [1, 6])

# isoterm
ax3 = fig[1,3] = Axis(fig, 
	title = "Isoterm",
	xlabel = "V",
	ylabel = "p"
)
xlims!(ax3, 0, 10)
ylims!(ax3, 0, 10)
lines!(ax3, 0:0.1:10,
	V-> 1/(V-1) + 1
)
fig

fig = Figure()

Qs = [0, 1, 4, 5, 6, 7] .* 10
Ts = [-50, 0, 0, 100, 100, 100]

ax = Axis(fig[1, 1], 
	title = "Phasenübergänge",
	xlabel = "Innere Energie Q",
	ylabel = "Temperatur des Körpers"
)


lines!(ax, Qs, Ts)
text!(ax, 
	[
		(-5, -50),
		(25, 0),
		(55, 90)
	],
	text = [
		"Fest",
		"Flüssig",
		"Gasförmig"
	]
)
fig

fig = Figure()
ylims = [0,3]

create_blank = ax->begin
	ylims!(ax, ylims)
	hideydecorations!(ax, grid=false, label=false)
	hidexdecorations!(ax, grid=false)

	lines!(ax, 
		[0,4], [2,2],
		color = :black
	)
	lines!(ax, 
		[0,4], [1,1],
		color = :black
	)
end

ndot = Axis(fig[1, 1],
	title = "N-Dotieren",
	ylabel = "Leitungsband",
	xticks = yticks
)

create_blank(ndot)

lines!(ndot,
	[0, 4], [.5, .5],
	color = :green
)

arrows!(ndot,
	[.5, 1.5, 2.5], [.5, .5, .5],
	[.75, .75, .75], [.75, .75, .75],
	color = :green
)

nndot = Axis(fig[2,1],
	ylabel = "Valenzband"
)
create_blank(nndot)

pdot = Axis(fig[2, 2])
create_blank(pdot)
lines!(pdot,
	[0, 4], [2.5, 2.5],
	color = :orange
)

arrows!(pdot,
	[.5, 1.5, 2.5], [2.5, 2.5, 2.5],
	[.75, .75, .75], [-.75, -.75, -.75],
	color = :orange
)

ppdot = Axis(fig[1, 2],
	title = "P-Dotieren"
)
create_blank(ppdot)

fig
