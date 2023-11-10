using Plots
using Distributions
gr()
using LinearAlgebra
using QuadGK

# Define the model
ρ(a, α, β) = a^(α - 1)*(1 - a)^(β - 1) / Distributions.beta(α, β)

# plot the model
a = 0:0.01:1
α = [0.02, 0.5, 1, 2, 4, 5, 10]
β = [0.01, 0.5, 1, 2, 4, 5, 8]

Plots.plot(a, ρ.(a, α[1], β[1]), label = "α = $(α[1]), β = $(β[1])", lw = 2)

# ρを積分する
ρ_int(a, α, β) = QuadGK.quadgk(ρ, 0, a, (α, β))[1]

# plot the model
Plots.plot!(a, ρ_int.(a, α[1], β[1]), label = "α = $(α[1]), β = $(β[1])", lw = 2)