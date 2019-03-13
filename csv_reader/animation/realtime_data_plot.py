import numpy as np
import time
import matplotlib
matplotlib.use('GTKAgg')
from matplotlib import pyplot as plt
import random

def randomwalk(dims=(256, 256), n=20, sigma=5, alpha=0.95, seed=1):
    """ A simple random walk with memory """

    r, c = dims
    gen = np.random.RandomState(seed)
    #pos = gen.rand(2, n) * ((r,), (c,))
    old_delta = gen.randn(2, n) * sigma
    pos=[[]]
    while True:
        #delta = (1. - alpha) * gen.randn(2, n) * sigma + alpha * old_delta
        #pos += delta
        #for ii in xrange(n):
        #    if not (0. <= pos[0, ii] < r):
        #        pos[0, ii] = abs(pos[0, ii] % r)
        #    if not (0. <= pos[1, ii] < c):
        #        pos[1, ii] = abs(pos[1, ii] % c)
        #old_delta = delta
        a=random.randint(1,1000)
        b=random.randint(1,1000)

        pos.append(a)
        yield (a ,b)#pos
        #yield pos


def run(niter=10000, doblit=True):
    """
    Display the simulation using matplotlib, optionally using blit for speed
    """

    fig, ax = plt.subplots(1, 1)
    ax.set_aspect('equal')
    ax.set_xlim(0, 255)
    ax.set_ylim(0, 255)
    ax.hold(True)
    #rw = randomwalk()
    #x, y = randomwalk()#rw.next()
    a=random.randint(1,1000)
    b=random.randint(1,1000)
    x=[]
    y=[]
    x.append(a)#random.randint(1,1000)
    y.append(b)#random.randint(1,1000)

    plt.show(False)
    plt.draw()

    if doblit:
        # cache the background
        background = fig.canvas.copy_from_bbox(ax.bbox)

    points = ax.plot(x, y, 'o')[0]
    #ax.add_artist(points)
    fig.canvas.draw()

    tic = time.time()

    for ii in range(niter):

        # update the xy data
        #x, y = rw.next()
        a=random.randint(1,1000)
        b=random.randint(1,1000)
        x.append(a)
        y.append(b)
        points.set_data(x, y)

        if doblit:
            # restore background
            fig.canvas.restore_region(background)

            # redraw just the points

            ax.draw_artist(points)

            # fill in the axes rectangle
            fig.canvas.blit(ax.bbox)

        else:
            # redraw everything
            fig.canvas.draw()

    plt.close(fig)
    print ("Blit = %s, average FPS: %.2f" % (
        str(doblit), niter / (time.time() - tic)))

if __name__ == '__main__':
    run(doblit=False)
    run(doblit=True)
