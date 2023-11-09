using Plots, GR
gr()

function RandonWalk(N, dTheta=π/100, R=1, xo=0, yo=0)
    X = zeros(N)
    Y = zeros(N)
    X[1] = xo
    Y[1] = yo
    for n in 1:N-1
        theta = rand(-pi: dTheta: pi)

        dx = R * cos(theta)
        dy = R * sin(theta)
        X[n+1] = X[n] + dx
        Y[n+1] = Y[n] + dy
    end
    gmax = maximum([maximum(X), maximum(Y)])
    gmin = minimum([minimum(X), minimum(Y)])
    print("max: ", gmax, "\n")
    print("min: ", gmin, "\n")
    println("Distance:", sqrt((X[end]-xo)^2 + (Y[end]-yo)^2))

    Plots.plot(X, Y, color="blue")
    Plots.plot(X[[1, end]], Y[[1, end]], color="red")
    
end
RandonWalk(50, pi/100)
