import matplotlib.pyplot as plt
import pandas as pd

def plot_random(X, Y, xcol, title_col, nplots = 9, ncols = 3, sample_rate = 125):
    rnd_samples = np.random.choice(np.arange(X.shape[1] - 1), nplots)
    
    fig, axes = plt.subplots(nrows=np.int32(np.ceil(nplots/ncols)),
                             ncols = ncols,
                             figsize = (ncols * 5, np.int32(np.ceil(nplots/ncols) * 4)))
    axes = axes.flatten()

    for idx, ax in zip(rnd_samples, axes):
        yvals = X.iloc[:, idx]
        xvals = np.arange(yvals.shape[0]) * (1/sample_rate)
        ax.plot(xvals, yvals)
        ax.legend().remove()
#         X.plot(x = xcol, y = idx, kind = "line", ax = ax, legend = False)
        ax.set_title("".join([str(idx),": ", Y.loc[idx, title_col]]))
        ax.set_xlabel("time(s)")

    plt.subplots_adjust(hspace=0.5)