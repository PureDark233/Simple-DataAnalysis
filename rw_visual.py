import matplotlib.pyplot as plt
from random_walk import RandomWalk

while True:
    # initailize
    rw = RandomWalk()
    rw.fill_walk()

    plt.figure(dpi=128, figsize=(10, 10))

    # save for changing color
    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,
                edgecolor='none', s=1)

    # the color of the beginning and end
    plt.scatter(0, 0, c='green', edgecolor='none', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolor='none', s=100)
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)
    plt.show()

    keep_running = input("Again?(y/n): ")
    if keep_running == 'n':
        break
