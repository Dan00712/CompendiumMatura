# CompendiumMatura

This Project is used to store the notebooks to study for the A-Levels in the HTL-Braunau year 2023 
and also to manage the julia dependencies in one *Project.toml* file

## Using jupyter in this Collection

This code base is using the Julia Language and [DrWatson](https://juliadynamics.github.io/DrWatson.jl/stable/)
to make a reproducible scientific project named
> CompendiumMatura

To (locally) reproduce this project, do the following:

0. Download this code base. Notice that raw data are typically not included in the
   git-history and may need to be downloaded independently.
1. Open a Julia console and do:
   ```
   julia> using Pkg
   julia> Pkg.add("DrWatson") # install globally, for using `quickactivate`
   julia> Pkg.activate("path/to/this/project")
   julia> Pkg.instantiate()
   ```
2. To launch the jupyterlab browser window enter
   ```
   julia> inclue( joindir( srcdir("launchNb.jl")))
   ```
   Then press enter to instantiate the conda enviroment necessary for the notebooks

This will install all necessary packages for you to be able to run the scripts and
everything should work out of the box, including correctly finding local paths.