# 📊 Data Analysis with PandasAI!

An intelligent data analysis web application that allows users to upload CSV files and query them using natural language.
Built with **Streamlit**, **PandasAI**, and **Google Gemini API**, this project combines rule-based logic with AI-powered insights.

---

## 🚀 Live Features

* 📂 Upload CSV files
* 💬 Ask questions in natural language
* 🧠 Hybrid query system (Rule-based + LLM fallback)
* 🔍 Automatic column detection
* ⚡ Instant calculations (sum, average, etc.)
* 🛡️ Graceful fallback when API fails
* 🎨 Clean and modern UI (custom styled)

---

## 🧠 How It Works

This project uses a **hybrid approach**:

1. **Rule-Based Engine (Fast & Accurate)**

   * Detects keywords like *total, average, mean*
   * Matches relevant columns dynamically
   * Performs direct Pandas operations

2. **LLM Integration (Gemini API)**

   * Handles complex natural language queries
   * Generates deeper insights and explanations

3. **Fallback System**

   * If API fails → switches to basic statistical analysis

---

## 🛠️ Tech Stack

* **Python**
* **Streamlit**
* **Pandas**
* **PandasAI**
* **Google Gemini API**
* **dotenv**

---

## 📸 Demo Screenshot

![App Screenshot](screenshot.png)

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/data-analysis-pandasai.git
cd data-analysis-pandasai
```

---

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

### 3️⃣ Setup environment variables

Create a `.env` file in the root directory:

```env
GOOGLE_API_KEY=your_api_key_here
```

---

### 4️⃣ Run the application

```bash
streamlit run main.py
```

---

## 💡 Example Queries

* "What is the total value?"
* "Show average sales"
* "Plot revenue trend"
* "Summarize the dataset"

---

## ⚠️ Notes

* If API quota is exceeded, the app automatically switches to fallback mode.
* Ensure your dataset contains numeric columns for calculations.

---

## 📂 Project Structure

```
├── main.py
├── llm_handler.py
├── data_handler.py
├── style.py
├── requirements.txt
├── README.md
├── .env.example
```

---

## 🚀 Future Improvements

* 📊 Automatic graph generation
* 💬 Chat history support
* 📄 Export analysis as PDF
* 🧠 Better NLP-based query understanding

---

## 👨‍💻 Author

**Advik Rathee**

---

## ⭐ If you found this useful, consider giving it a star!
