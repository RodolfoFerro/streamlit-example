# Example of an ML web app using Streamlit 🌱
![GitHub last commit](https://img.shields.io/github/last-commit/RodolfoFerro/streamlit-example?logo=github&style=for-the-badge)
![GitHub repo size](https://img.shields.io/github/repo-size/RodolfoFerro/streamlit-example?logo=github&style=for-the-badge)
![GitHub](https://img.shields.io/github/license/RodolfoFerro/streamlit-example?label=LICENSE&logo=github&style=for-the-badge) <br>
[![Twitter](https://img.shields.io/twitter/follow/rodo_ferro?label=Twitter&logo=twitter&logoColor=fff&style=for-the-badge)](https://twitter.com/rodo_ferro/)
[![LinkedIn](https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&logoColor=fff&colorB=555)](https://www.linkedin.com/in/rodolfoferro/) <br>
[![Slides](https://img.shields.io/static/v1?label=Slides&message=Google%20Slides&color=tomato&logo=google&logoColor=fff&style=for-the-badge)](https://docs.google.com/presentation/d/e/2PACX-1vTBfub0FyiWLf_4NEnH7Ob6BHJtQaSsr1iqSC5C8deVtXWEbx9-o8i_03FS-qf6mk0jhKdUno1KtqAs/pub?start=false&loop=false&delayms=3000)

<!-- Project description -->
This repository contains code to build a Streamlit web app that serves an Iris classifier.


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
(streamlit)$ streamlit run app.py
```

#### Extend code!

Please feel free to use this repo as a template to extend code!
