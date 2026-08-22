# RemoteCare – AI-Powered Remote Work Burnout Detection

## 📌 About the Project

RemoteCare is a machine learning-based web application that predicts the burnout risk of remote employees. It uses employee work-related information to classify burnout risk as **Low, Medium, or High**.

## 🎯 Objective

The main objective is to identify possible burnout risk at an early stage and help improve employee well-being and work-life balance.

## 🛠️ Technologies Used

* Python
* Flask
* Scikit-learn
* NumPy
* HTML
* CSS
* Bootstrap
* Decision Tree Classifier

## ⚙️ How It Works

1. The user enters employee work-related details.
2. The data is processed using the saved scaler.
3. The trained Decision Tree model analyzes the input.
4. The system predicts the burnout risk.
5. The result is displayed on the web page.

## 📊 Input Features

* Work Hours
* Screen Time Hours
* Meetings Count
* Breaks Taken
* After Hours Work
* Sleep Hours
* Task Completion Rate
* Burnout Score
* Day Type

## 📁 Project Structure

```text
RemoteCare/
│
├── app.py
├── dtc.pkl
├── Scaler.pkl
│
├── templates/
│   ├── index.html
│   ├── about.html
│   └── predict.html
│
└── static/
    └── images/
```

## ▶️ How to Run

Install the required libraries:

```bash
pip install flask numpy scikit-learn
```

Run the application:

```bash
python app.py
```

Open the local Flask URL shown in the terminal.

## 🔮 Future Enhancements

* Improve the model using a larger dataset.
* Add employee wellness alerts.
* Improve the user interface.
* Develop a mobile version.

## 👩‍💻 Project

**RemoteCare – AI-Powered Remote Work Burnout Detection**
