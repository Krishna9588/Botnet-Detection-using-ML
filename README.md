
## Botnet Detection using Machine Learning

A machine learning project to detect botnet-infected network traffic. 

Trained on the CTU-13 dataset and built using Python.

---
### Features and Project Description

- Clean & preprocess CTU-13 botnet data
- Train a Random Forest model
- Predict botnet traffic from test files
- Interactive Streamlit dashboard

---

### Setup 

1. **Clone the repo**
```
    git clone https://github.com/Krishna9588/Botnet-Detection-using-ML.git
```


2 **Install dependencies**

```bash
    pip install -r requirements.txt
```

3 **Download Dataset**
```bash
    git clone https://github.com/imfaisalmalik/CTU13-CSV-Dataset
    cd dataset
```

--- 

### About Dataset and dataset folder

In this project I have used CTU-13 Botnet Dataset. Which is available on Git Hub for public use.

1. [CTU13_Attack_Traffic](dataset/CTU13_Attack_Traffic.csv) - Dataset with Bot Attack
2. [CTU13_Normal_Traffic](dataset/CTU13_Normal_Traffic.csv) - Normal User Dataset
3. [prediction_output](dataset/prediction_output.csv) - Result dataset
4. [test_sample](dataset/test_sample.csv) - Sample dataset use for getting output

---

### Run this Project

1. Preprocess & Training the model
```bash
    python train_model.py
```

2. Detection
```bash
    python detector.py
```

3. Dashboard
```bash
    streamlit run streamlit_app.py
```

---

### Expected Output

```csv
SrcAddr, DstAddr, Proto, TotBytes, ..., Prediction, Prediction_Label
192.168.1.10, 8.8.8.8, TCP, 2400, ..., 0, NORMAL
10.0.0.5, 192.168.1.3, TCP, 5500, ..., 1, BOTNET
```

---
#### Next thing I am trying in this Project is to use my real-time traffic using the PyShark Python library as input to the model.

---





