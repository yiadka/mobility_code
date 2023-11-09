#=

# set_options(ax, "x", "y", "data (N = $(length(X_obs)))")
=#

using PyPlot

# xを0から2πまでの範囲で0.1ずつ増える配列とする
x = range(0, 2π, step=0.1)
y = [[], [], [], []]

# 4つのグラフy[1]～y[4]のyの値を設定する
for i in x
    push!(y[1], sin(i))
    push!(y[2], cos(i))
    push!(y[3], i * 2)
    push!(y[4], 1 / i)
end


# サブプロット関数を呼び出し、figとaxesを取得する
# グラフの数は縦二つ、横二つ配置する
fig, axes = subplots(2, 2, constrained_layout=true)

# 複数のグラフから、横方向(行)→縦方向(列)の順にグラフを指定しアクシス(ax)を取得する。
# axに対してグラフの設定(plot)を行う。
i = 0
for row in 1:2, col in 1:2
    i += 1
    ax = axes[row, col]
    ax.plot(x, y[i])
end

fig.tight_layout()
plt.show()



