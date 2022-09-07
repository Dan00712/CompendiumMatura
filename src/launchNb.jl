using DrWatson
@quickactivate

using IJulia
path = joinpath(@__DIR__, "..", "notebooks")
@info "path: $path"
jupyterlab(dir = path, detached = true)