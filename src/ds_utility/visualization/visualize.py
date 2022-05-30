# Utils for plots


def plot_confusion_matrix(cm,
                          target_names,
                          title="Confusion matrix",
                          cmap=None,
                          normalize=True,
                          show=True,
                          dpi=50):
    """Given a sklearn confusion matrix (cm), make a nice plot.
    Args:
        cm:           confusion matrix from sklearn.metrics.confusion_matrix
        target_names: given classification classes such as [0, 1, 2]
                  the class names, for example: ["high", "medium", "low"]
        title:        the text to display at the top of the matrix
        cmap:         the gradient of the values displayed from matplotlib.pyplot.cm
                  see http://matplotlib.org/examples/color/colormaps_reference.html
                  plt.get_cmap("jet") or plt.cm.Blues
        normalize:    If False, plot the raw numbers
                      If True, plot the proportions
        show: Whether to call a plot.show()
    Usage
    .. code-block::
        plot_confusion_matrix(cm           = cm,                  # confusion matrix created by
                                                                  # sklearn.metrics.confusion_matrix
                              normalize    = True,                # show proportions
                              target_names = y_labels_vals,       # list of names of the classes
                              title        = best_estimator_name) # title of graph
    Citiation
    .. code-block::
        http://scikit-learn.org/stable/auto_examples/model_selection/plot_confusion_matrix.html
    """
    import matplotlib.pyplot as plt
    import itertools
    accuracy = np.trace(cm) / np.sum(cm).astype("float")
    misclass = 1 - accuracy
    if cmap is None:
        cmap = plt.get_cmap("Blues")
    plt.figure(figsize=(8, 6), dpi=dpi)
    plt.imshow(cm, interpolation="nearest", cmap=cmap)
    plt.title(title)
    plt.colorbar()
    if target_names is not None:
        tick_marks = np.arange(len(target_names))
        plt.xticks(tick_marks, target_names, rotation=0)
        plt.yticks(tick_marks, target_names)
    if normalize:
        # cm = cm.astype("float") / cm.sum(axis=1)[:, np.newaxis]
        cm = cm.astype("float") / cm.sum()
    thresh = cm.max() / 1.5 if normalize else cm.max() / 2
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        if normalize:
            plt.text(
                j,
                i,
                "{:0.2f} %".format(np.round(cm[i, j] * 100, 2)),
                horizontalalignment="center",
                color="orangered" if cm[i, j] > thresh else "orangered",
            )
        else:
            plt.text(
                j,
                i,
                "{:,}".format(cm[i, j]),
                horizontalalignment="center",
                color="orangered" if cm[i, j] > thresh else "orangered",
            )
    plt.tight_layout()
    plt.ylabel("True label")
    plt.xlabel("Predicted label\naccuracy={:0.4f}; misclass={:0.4f}".format(
        accuracy, misclass))
    if show:
        plt.show()
