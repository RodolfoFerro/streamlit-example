from sklearn.datasets import load_iris
from sklearn import tree


def iris_classifier(verbose=False):
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
        dot_data = tree.export_graphviz(clf, out_file=None,
                                        feature_names=iris.feature_names,
                                        class_names=iris.target_names,
                                        filled=True, rounded=True,
                                        special_characters=True)
        graph = graphviz.Source(dot_data)
        graph.render("iris")

    return clf