# Breast Cancer Prediction Using ANN

## 📌 Overview

This project uses an **Artificial Neural Network (ANN)** with a **Sequential model** to predict whether a breast tumor is **benign or malignant**. The model learns patterns from breast cancer diagnostic features and performs binary classification.

## 🧠 Model

* Algorithm: Artificial Neural Network (ANN)
* Framework: TensorFlow/Keras
* Architecture: Sequential Neural Network
* Activation: ReLU (hidden layers), Sigmoid (output layer)

## 📊 Dataset

The model uses breast cancer diagnostic features such as:

* Radius
* Texture
* Perimeter
* Area
* Smoothness
* Compactness
* Other cell characteristics

## ⚙️ Technologies

* Python
* TensorFlow/Keras
* NumPy
* Pandas
* Scikit-learn
* Matplotlib

## 📈 Performance
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>precision</th>
      <th>recall</th>
      <th>f1-score</th>
      <th>support</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1.000000</td>
      <td>0.946667</td>
      <td>0.972603</td>
      <td>75.000000</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0.906977</td>
      <td>1.000000</td>
      <td>0.951220</td>
      <td>39.000000</td>
    </tr>
    <tr>
      <th>accuracy</th>
      <td>0.964912</td>
      <td>0.964912</td>
      <td>0.964912</td>
      <td>0.964912</td>
    </tr>
    <tr>
      <th>macro avg</th>
      <td>0.953488</td>
      <td>0.973333</td>
      <td>0.961911</td>
      <td>114.000000</td>
    </tr>
    <tr>
      <th>weighted avg</th>
      <td>0.968176</td>
      <td>0.964912</td>
      <td>0.965287</td>
      <td>114.000000</td>
    </tr>
  </tbody>
</table>
</div>
<div>
ANN
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>precision</th>
      <th>recall</th>
      <th>f1-score</th>
      <th>support</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0.985915</td>
      <td>0.972222</td>
      <td>0.979021</td>
      <td>72.000000</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0.953488</td>
      <td>0.976190</td>
      <td>0.964706</td>
      <td>42.000000</td>
    </tr>
    <tr>
      <th>accuracy</th>
      <td>0.973684</td>
      <td>0.973684</td>
      <td>0.973684</td>
      <td>0.973684</td>
    </tr>
    <tr>
      <th>macro avg</th>
      <td>0.969702</td>
      <td>0.974206</td>
      <td>0.971863</td>
      <td>114.000000</td>
    </tr>
    <tr>
      <th>weighted avg</th>
      <td>0.973969</td>
      <td>0.973684</td>
      <td>0.973747</td>
      <td>114.000000</td>
    </tr>
  </tbody>
</table>
</div>
**Test Accuracy:** `0.9824561403508771`

The ANN model achieved high accuracy in classifying breast cancer cases.

	precision	recall	f1-score	support
0	0.985915	0.985915	0.985915	71.000000
1	0.976744	0.976744	0.976744	43.000000
accuracy	0.982456	0.982456	0.982456	0.982456
macro avg	0.981330	0.981330	0.981330	114.000000
weighted avg	0.982456	0.982456	0.982456	114.000000

