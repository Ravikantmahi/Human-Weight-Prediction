# 🧠 Weight Prediction App using Flask & Machine Learning

---

## 📌 About the Project

This is a simple **Flask web application** that predicts a person's **weight (in kg)** based on their **height and gender** using a **Linear Regression model**.

---

## 🔗 Project Links
🔗 [Live Demo](https://human-weight-prediction.glitch.me/)
- **GitHub Repository:** [https://github.com/Ravikantmahi/Iris-Flower-Prediction](https://github.com/Ravikantmahi/Human-Weight-Prediction)


## ⚙️ How It Works

1. The user inputs their **gender** and **height**.
2. The app uses a preloaded CSV dataset (`weight-height.csv`) to:
   - Train a **Linear Regression** model.
   - Predict the user's weight.
3. The result is displayed on a separate result page.

---

## 📁 Dataset Used

The app uses a dataset `weight-height.csv` with the following columns:

- `Gender` (Male/Female)
- `Height` (in inches)
- `Weight` (in pounds)

> The gender is converted to numeric for model training:  
> `Male = 1`, `Female = 0`.

---

## 🧪 Technologies Used

- 🐍 Python 3
- 🔥 Flask
- 📊 Pandas
- 📈 Scikit-learn (Linear Regression)
- 🌐 HTML (Jinja2 templates)

---

## 🚀 How to Run This Project

### 🔧 Prerequisites

- Python installed
- pip (Python package manager)

### 📥 Step-by-Step Setup

1. **Clone the Repository**  
   ```bash
   git clone https://github.com/your-username/weight-predictor-flask.git
   cd weight-predictor-flask
   pip install -r requirements.txt
   ```
2.If requirements.txt is not present, install manually:
  ```
    pip install flask pandas scikit-learn
   ```
3.Add Dataset
 Make sure weight-height.csv is placed in the project folder.

4.Run the App
```
python app.py
```
5.Visit in Browser
```
Open http://localhost:5000 in your browser.
```
🧾 File Structure
```
├── app.py                 # Main Flask application
├── weight-height.csv      # Dataset
├── templates/
│   ├── index.html         # Input form page
│   └── result.html        # Result page
```
💡 Example Prediction
Input:
Gender: Male
Height: 70 inches

Output:
Predicted Weight: ~755.2 hg

🧠 Concepts Learned
Data preprocessing (mapping categorical to numeric)

Model training inside a web app

Handling form data in Flask

Rendering templates using Jinja2

Using sklearn’s LinearRegression

🙌 Acknowledgements
Dataset Source: public-datasets

Inspired by beginner Flask + ML tutorials

**📬 Contact**

Ravi Kant
