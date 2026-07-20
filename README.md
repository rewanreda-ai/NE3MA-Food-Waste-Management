# 🍏 NE3MA: AI-Powered Food Waste Management System

## 📌 Problem Statement
Large amounts of edible food are wasted daily in restaurants, hotels, university dormitories, and schools. Much of this food remains safe for consumption but is discarded due to the lack of an efficient decision-making system for redistribution and recycling.

## 💡 The Solution
**NE3MA** is an AI-powered food waste management platform that helps organizations reduce food waste by automatically identifying food items and recommending the most sustainable recycling pathway. 

The system combines **Computer Vision**, **Machine Learning**, and a **Mobile Application** to classify food and determine the best destination, including:
* 🧑‍🤝‍🧑 **Human Reuse & Donations**
* 🦙 **Animal Feed**
* ⚡ **Biogas Production**

---

## ⚙️ System Architecture
1. **Input:** User uploads a food image through the mobile application.
2. **Computer Vision:** A CV model identifies the food type.
3. **Data Collection:** Additional information is collected (Storage condition, Price, Number of Guests).
4. **Machine Learning:** An ML model predicts the optimal recycling category:
   * `1` - Repack for Human Consumption
   * `2` - Donation
   * `3` - Animal Feed
   * `4` - Biogas
5. **Routing:** The application automatically routes the food to the appropriate destination.

---

## 🛠️ Technologies Used
* **Machine Learning:** Python, Scikit-Learn, Random Forest Classifier
* **Computer Vision:** Food Image Classification Workflow
* **Data Visualization:** Power BI Dashboard
* **Mobile Application:** Flutter

---

## 👩‍💻 My Contribution
* ⚙️ **Built the complete Machine Learning pipeline** from scratch.
* 🧹 Performed extensive data preprocessing and feature engineering.
* 📊 Trained and evaluated the **Random Forest model**, achieving approximately **90% classification accuracy**.
* 📉 **Designed and developed the Power BI dashboard** to generate operational insights from restaurant food waste data.
* 🤝 Assisted in the integration of the Computer Vision workflow into the main system.
