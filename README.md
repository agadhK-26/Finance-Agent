<div align="center">

# 💹 Finance AI Agent

### Multi-Agent Financial Assistant powered by Agno + Groq

*Real-time market data, live news, and AI-driven investment insights — all in one conversational interface.*

[![Live Demo](https://img.shields.io/badge/🚀_Live_Demo-Streamlit-FF4B4B?style=for-the-badge)](https://finance-agent-mggjcmqhpp4emmermxc4az.streamlit.app/)
[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Agno](https://img.shields.io/badge/Agno-v2.6.22-6C5CE7?style=for-the-badge)](https://github.com/agno-agi/agno)
[![Groq](https://img.shields.io/badge/LLM-Groq-F55036?style=for-the-badge)](https://groq.com/)
[![License](https://img.shields.io/badge/License-MIT-brightgreen?style=for-the-badge)](#-license)

**[🔗 Try it live](https://finance-agent-mggjcmqhpp4emmermxc4az.streamlit.app/)**

</div>

---

## 📖 Overview

**Finance AI Agent** is a multi-agent financial assistant that ditches the "one giant LLM" approach in favor of a **hierarchical team of specialized agents** — each one an expert at a single job. A language-aware coordinator routes your query, specialist agents gather live financial data and news, an insight agent reasons over the results, and everything gets merged into one clean, structured answer.

Ask it to compare two stocks, explain a company's valuation, pull today's market news, or break down investment risk — and watch the agents work together to answer it.

---

## ✨ Key Features

| | |
|---|---|
| 🧠 **Hierarchical Multi-Agent System** | 2 leader agents coordinate 3 specialist agents |
| 📈 **Real-Time Market Data** | Live prices, fundamentals, and financial statements via Yahoo Finance |
| 📰 **Live News Search** | Up-to-the-minute financial news via Tavily Search |
| 💡 **AI-Powered Insights** | Bull/bear analysis, risk assessment, and financial reasoning |
| 🌍 **Multilingual Support** | Detects and responds in the user's language automatically |
| 💾 **Persistent Chat History** | SQLite-backed conversations, isolated per user via cookies |
| 🎨 **Modern Dark UI** | Clean, responsive Streamlit chat interface |

---

## 🏗️ Architecture

The app runs on a **5-agent hierarchical pipeline**:

```
                         👤 User
                            │
                    🌐 Language Leader
              (detects language, routes query)
                            │
                    🧭 Finance Leader
            (interprets intent, delegates tasks)
                            │
        ┌───────────────────┼───────────────────┐
        │                   │                   │
   📊 Finance Agent     📰 News Agent      💡 Insight Agent
  (Yahoo Finance data)  (Tavily search)   (analysis & reasoning)
        │                   │                   │
        └───────────────────┼───────────────────┘
                            │
                    🧭 Finance Leader
                    (merges & dedupes)
                            │
                    🌐 Language Leader
                    (translates response)
                            │
                         👤 User
```

<details>
<summary><b>Agent responsibilities (click to expand)</b></summary>

| Agent | Role |
|---|---|
| **Language Leader** | Entry point — detects user language, keeps conversation consistent, hands off to Finance Leader |
| **Finance Leader** | Orchestrator — analyzes intent, delegates to specialists, merges & deduplicates results |
| **Finance Agent** | Pulls stock prices, market cap, P/E, EPS, dividend yield, financials, analyst ratings |
| **News Agent** | Retrieves company news, earnings, market updates, M&A, regulatory events |
| **Insight Agent** | Performs comparisons, bull/bear cases, risk assessment, and financial reasoning |

</details>

---

## 🛠️ Tech Stack

| Category | Technology |
|---|---|
| **Language** | Python |
| **Agent Framework** | [Agno](https://github.com/agno-agi/agno) v2.6.22 |
| **Frontend** | Streamlit |
| **LLM Provider** | Groq |
| **Financial Data** | Yahoo Finance (YFinance Tools) |
| **Web Search** | Tavily Search API |
| **Database** | SQLite + SQLAlchemy |
| **Session Handling** | Streamlit Session State & Cookies |
| **Config** | python-dotenv |

---

## 🚀 Live Demo

> **[👉 finance-agent-mggjcmqhpp4emmermxc4az.streamlit.app](https://finance-agent-mggjcmqhpp4emmermxc4az.streamlit.app/)**

Try prompts like:
- `What is Apple's current stock price?`
- `Compare Apple and Microsoft.`
- `Show today's Tesla news.`
- `What are the risks of investing in Amazon?`
- `Compare TCS and Infosys.`

---

## ⚡ Getting Started

### Prerequisites
- Python 3.10+
- API keys for **Groq** and **Tavily**

### Installation

```bash
# Clone the repository
git clone https://github.com/<your-username>/finance-ai-agent.git
cd finance-ai-agent

# Create a virtual environment
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Configuration

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key_here
TAVILY_API_KEY=your_tavily_api_key_here
```

### Run Locally

```bash
streamlit run app.py
```

The app will be live at `http://localhost:8501`.

---

## 📂 Project Structure

```
finance-ai-agent/
├── agents/
│   ├── language_leader.py
│   ├── finance_leader.py
│   ├── finance_agent.py
│   ├── news_agent.py
│   └── insight_agent.py
├── db/
│   └── chat_history.db
├── utils/
│   └── session_manager.py
├── app.py
├── requirements.txt
├── .env.example
└── README.md
```

---

## 🗺️ Roadmap

- [ ] Add crypto & forex support
- [ ] Portfolio tracking dashboard
- [ ] Voice input for queries
- [ ] Export chat/analysis as PDF

---

## 🤝 Contributing

Contributions are welcome! Feel free to open an issue or submit a PR.

1. Fork the repo
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the **MIT License**.

---

<div align="center">

**Built with 🧠 multi-agent AI, ☕, and a lot of debugging**

[Live Demo](https://finance-agent-mggjcmqhpp4emmermxc4az.streamlit.app/) · [Report Bug](../../issues) · [Request Feature](../../issues)

</div>
