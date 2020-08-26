import plotly as py
import plotly.graph_objs as go


def plotly_figure_1(data):
    """Creates a nice figure."""

    t1_box = go.Box(
        name='Largo del sépalo (cm)',
        y=data['sepal length (cm)'],
        marker=dict(color='rgba(160,160,50,0.7)')
    )

    t2_box = go.Box(
        name='Ancho del sépalo (cm)',
        y=data['sepal width (cm)'],
        marker=dict(color='rgba(50,160,150,0.7)')
    )

    t3_box = go.Box(
        name='Largo del pétalo (cm)',
        y=data['petal length (cm)'],
        marker=dict(color='rgba(160,60,150,0.7)')
    )

    t4_box = go.Box(
        name='Ancho del pétalo (cm)',
        y=data['petal width (cm)'],
        marker=dict(color='rgba(150,160,150,0.7)')
    )

    fig_box = [t1_box, t2_box, t3_box, t4_box]

    return fig_box


def plotly_figure_2(data):
    # Iris-setosa
    trace_setosa = go.Scatter3d(
        x = data['sepal length (cm)'][:50],
        y = data['sepal width (cm)'][:50],
        z = data['petal length (cm)'][:50],
        mode = 'markers',
        opacity = 0.7,
        name = "Iris-setosa",
        marker = dict(
                    size = 5,
                    color = 'rgba(255,102, 255,0.8)'
        )
    )

    # Iris-versicolor
    trace_versicolor = go.Scatter3d(
        x = data['sepal length (cm)'][50:100],
        y = data['sepal width (cm)'][50:100],
        z = data['petal length (cm)'][50:100],
        mode = 'markers',
        opacity = 0.7,
        name = "Iris-versicolor",
        marker = dict(
                    size = 5,
                    color = 'rgba(102, 255, 51, 0.8)'
        )
    )

    # Iris-virginica
    trace_virginica = go.Scatter3d(
        x = data['sepal length (cm)'][100:],
        y = data['sepal width (cm)'][100:],
        z = data['petal length (cm)'][100:],
        mode = 'markers',
        opacity = 0.7,
        name = "Iris-virginica",
        marker = dict(
                    size = 5,
                    color = 'rgba(51, 102, 255, 0.8)'
        )
    )

    list_3d = [trace_setosa, trace_versicolor, trace_virginica]

    fig_3d = go.Figure(data=list_3d)
    return fig_3d