# Overview
This project will give songs recommendation based on person's mood with **KNN** algorithm
## How it works
we got the spotify dataset from [kaagle](https://kaagle.com) which contains energy and valence values. we will get valence values by scanning person face and energy values by asking some questions. using **KNN** algorithm dataset is trained and tested with 97% accuracy. 
This project make use of [Google Vision](https://cloud.google.com/vision) api to get valence values.
## Building the project
* This project require python to be installed. Get it from [here](https://www.python.org/downloads/).
* Jupyter Notebook is recommended to train and test dataset. Get it from [here](https://docs.jupyter.org/en/latest/install/notebook-classic.html).
* Before running the application you need to have google vision api. Get it from [here](https://cloud.google.com/vision).
* Get JSON key from your account and paste it in your directory and rename it to **vision.json**
* Now run application with command ```python3 main.py```
## Output
**Image contents** <br>
![one](https://github.com/shanureddy4/Songs-Recommendation/blob/master/screenshots/onne.png) <br>
**Songs recommended** <br>
![two](https://github.com/shanureddy4/Songs-Recommendation/blob/master/screenshots/two.png)
