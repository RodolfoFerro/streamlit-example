# ==============================================================
# Author: Rodolfo Ferro
# Twitter: @rodo_ferro
#
# ABOUT COPYING OR USING PARTIAL INFORMATION:
# This script has been originally created by Rodolfo Ferro.
# Any explicit usage of this script or its contents is granted
# according to the license provided and its conditions.
# ==============================================================

# -*- coding: utf-8 -*-

from sklearn.datasets import load_iris
from sklearn import tree


def decision_tree(verbose=False):
    """Basic Decision Tree Classifier for Iris problem.
    Based on: http://scikit-learn.org/stable/modules/tree.html
    """

    # Load dataset:
    iris = load_iris()

    # Build and train classifier:
    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(iris.data, iris.target)

    # Visualize model:
    if verbose:
        tree.plot_tree(clf)

    return clf
