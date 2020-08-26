# Pose Estimation with TensorFlow Lite 🚶🏻‍♂️

<!-- Project description -->
This repository contains a trained version of PoseNet that runs directly with TensorFlow Lite.

The trained model returns a set of `(x, y)` paired keypoints containing the ouput of inference. All keypoints are indexed by an ID. You can see the IDs and parts in the following table:

| ID | PART       |
| -- | ---------- |
|  0 | NOSE       |
|  1 | L_EYE      |
|  2 | R_EYE      |
|  3 | L_EAR      |
|  4 | R_EAR      |
|  5 | L_SHOULDER |
|  6 | R_SHOULDER |
|  7 | L_ELBOW    |
|  8 | R_ELBOW    |
|  9 | L_WRIST    |
| 10 | R_WRIST    |
| 11 | L_HIP      |
| 12 | R_HIP      |
| 13 | L_KNEE     |
| 14 | R_KNEE     |
| 15 | L_ANKLE    |
| 16 | R_ANKLE    |


## Prerequisities

Before you begin, ensure you have met the following requirements:

* You have a _Windows/Linux/Mac_ machine running [Python 3.6+](https://www.python.org/).
* You have installed the latest versions of [`pip`](https://pip.pypa.io/en/stable/installing/) and [`virtualenv`](https://virtualenv.pypa.io/en/stable/installation/) or `conda` ([Anaconda](https://www.anaconda.com/distribution/)).


## Setup

To install the dependencies, you can simply follow this steps.

Clone the project repository:
```bash
git clone https://github.com/RodolfoFerro/streamlit-example.git
cd streamlit-example
```

To create and activate the virtual environment, follow these steps:

**Using `conda`**

```bash
$ conda create -n streamlit python=3.7

# Activate the virtual environment:
$ conda activate streamlit

# To deactivate (when you're done):
(streamlit)$ conda deactivate
```

**Using `virtualenv`**

```bash
# In this case I'm supposing that your latest python3 version is 3.7
$ virtualenv streamlit --python=python3

# Activate the virtual environment:
$ source streamlit/bin/activate

# To deactivate (when you're done):
(streamlit)$ deactivate
```

To install the requirements using `pip`, once the virtual environment is active:
```bash
(streamlit)$ pip install -r requirements.txt
```

#### Running the script

Finally, if you want to run the main script:
```bash
$ streamlit run app.py
```

This will start your camera and open a window with the output.

#### Modify parameters

If you want to change the parameters of the viewer, the model used, etc., you can directly modify the specs from the `run.py` script.

## Output file

The generated output file is modified in real time. An example of the generated output is the following:

```json
[
    {
        "ID": 0,
        "part": "NOSE",
        "x": 143,
        "y": 155
    },
    {
        "ID": 1,
        "part": "L_EYE",
        "x": 164,
        "y": 138
    },
    {
        "ID": 2,
        "part": "R_EYE",
        "x": 126,
        "y": 136
    },
    {
        "ID": 3,
        "part": "L_EAR",
        "x": 187,
        "y": 152
    },
    {
        "ID": 4,
        "part": "R_EAR",
        "x": 102,
        "y": 147
    },
    {
        "ID": 6,
        "part": "R_ELBOW",
        "x": 58,
        "y": 251
    },
    {
        "ID": 9,
        "part": "L_HIP",
        "x": 156,
        "y": 221
    },
    {
        "ID": 10,
        "part": "R_HIP",
        "x": 152,
        "y": 219
    }
]
```
