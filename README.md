# AI Customer Requirements Analyst - voice-of-customer

### Transforming Community Discussions into Actionable Product Intelligence using Local LLM model

🚀 **Live Demo:** https://voice-of-customer-ai-agent.streamlit.app/

📂 **GitHub Repository:** https://github.com/yashodharhajare-wq/voice-of-customer-ai-agent

---

<img width="1916" height="1019" alt="image" src="https://github.com/user-attachments/assets/9bd51970-6061-4652-b213-ca3fce7b2d61" />

---

# Overview

This project is an AI-powered Voice of Customer (VoC) Intelligence Platform that analyzes Reddit community discussions and converts unstructured conversations into structured business insights.

Online customer discussions are highly noisy and contain a mixture of:

* Product complaints
* Feature requests
* Buying advice
* Product showcases
* Technical troubleshooting
* Community conversations
* Humor and memes

Manually identifying meaningful customer requirements from thousands of discussions is extremely time-consuming for product managers and research teams.

This system automates that process using local Large Language Models (LLMs), semantic extraction pipelines, and analytics dashboards.

The platform helps answer business-critical questions such as:

* What problems are customers repeatedly facing?
* Which features are most requested?
* What benefits do users appreciate most?
* Which discussions contain actionable product insights?
* Which customer personas appear frequently?
* What themes dominate customer conversations?

Instead of manually reading thousands of comments, teams can directly explore structured insights through an interactive dashboard.

---

# Key Highlights

* AI-powered customer requirements analysis
* Fully local LLM deployment using Ollama
* Open-source and API-free workflow
* Automated Voice-of-Customer intelligence extraction
* Prompt-engineered structured insight generation
* Modular and scalable processing pipeline
* KPI-driven product intelligence dashboard
* Product insight filtering from noisy Reddit discussions

---

# Problem Statement

Online communities contain valuable customer feedback, but extracting meaningful insights manually is difficult due to the unstructured and noisy nature of conversations.

A single discussion thread may contain:

* Genuine complaints
* Product praise
* Technical support requests
* Feature suggestions
* User recommendations
* Humor and memes
* Showcase posts

Most discussions are not directly useful for product decision-making.

The challenge is identifying which conversations actually contain actionable customer intelligence and converting them into structured product insights.

This project solves that problem using AI-driven classification, extraction, normalization, and aggregation pipelines.

---

# Dataset

## Source

Mechanical Keyboards Reddit Community
(Can be extended using Reddit APIs)

## Dataset Size

* 9,042 Reddit comments
* Multiple discussion threads
* User-generated product feedback

## Data Fields

* Discussion Title
* Comment Text
* Comment Score
* Post URL
* Discussion Metadata

---

# System Architecture

```text
Reddit Discussions
        │
        ▼
Discussion Grouping
        │
        ▼
LLM Classification
        │
        ▼
Product Insight Extraction
        │
        ▼
Theme Normalization
        │
        ▼
Insight Aggregation
        │
        ▼
Interactive Dashboard
```

---

# Technology Stack

## AI / LLM

* Ollama
* Qwen 2.5 7B
* Prompt Engineering
* Structured JSON Extraction

## Data Processing

* Python
* Pandas
* NumPy

## Visualization

* Streamlit
* Plotly

## Development

* Git
* GitHub

---

# Why Local LLMs?

The entire AI pipeline runs locally using Ollama and open-source models.

Benefits:

* No paid API dependency
* Offline capability
* Better data privacy
* Full model control
* Lower operational costs
* Reproducible experimentation

This project demonstrates how production-style AI systems can be built entirely with open-source infrastructure.

---

# Pipeline

## 1. Discussion Grouping

Raw Reddit comments are grouped into discussion-level records.

Generated Metrics:

* Comment Count
* Average Score
* Maximum Score
* Discussion Metadata

Output:

```text
discussions.pkl
```

---

## 2. Discussion Classification

A local LLM classifies each discussion into categories such as:

* Complaint
* Praise
* Feature Request
* Buying Advice
* Technical Support
* Showcase
* Humor / Meme
* Community Discussion

Additional outputs:

* Contains Product Insights
* Confidence Score
* Classification Reason

This stage filters noisy discussions and identifies conversations that actually contain actionable product intelligence.

Output:

```text
classified_discussions.pkl
```

---

## 3. Product Insight Extraction

The LLM extracts only explicitly mentioned customer insights.

Extracted Categories:

* Pain Points
* Gains
* Personas
* Must-Have Features
* Nice-To-Have Features
* Feature Requests

Design Goals:

* No hallucinations
* JSON-only responses
* Explicit evidence extraction
* Conservative generation behavior
* Structured outputs

Output:

```text
discussion_insights.pkl
```

---

# Prompt Engineering Strategy

A major focus of the project was prompt engineering and output reliability.

Multiple prompting strategies were tested to:

* Reduce hallucinations
* Improve JSON consistency
* Enforce schema compliance
* Improve reasoning quality
* Avoid fabricated insights
* Increase extraction precision

The system prioritizes conservative extraction behavior over aggressive generation.

---

## 4. Theme Normalization

Similar insights are merged into standardized themes.

Example:

```text
Bluetooth Issues
Bluetooth Connectivity Problems
Bluetooth Reliability Problems

↓
Bluetooth Reliability
```

Output:

```text
normalized_insights.pkl
```

---

## 5. Insight Aggregation

Normalized insights are aggregated to identify:

* Most Common Pain Points
* Most Requested Features
* Top User Personas
* Most Appreciated Benefits

This stage converts raw discussions into business-level KPIs.

---

# Importance of Comment Signals

Customer intent is often revealed deeper inside comment sections rather than post titles.

The system evaluates:

* Comment frequency
* Discussion engagement
* Comment scores
* Repeated complaints
* Feature request intensity
* Community reactions

High-engagement discussions often indicate stronger customer demand or more impactful product problems.

This improves the reliability of extracted insights.

---

# LLM Evaluation & Benchmarking

Multiple local models were benchmarked before selecting the final production model.

| Model       | Result   |
| ----------- | -------- |
| Gemma 3 4B  | Rejected |
| Qwen 3 8B   | Rejected |
| Qwen 2.5 7B | Selected |

## Evaluation Criteria

* JSON Reliability
* Schema Compliance
* Hallucination Rate
* Prompt Controllability
* Extraction Accuracy
* Inference Stability

## Final Selection

### Qwen 2.5 7B via Ollama

Reasons:

* Consistent structured outputs
* Strong schema adherence
* Lower hallucination rate
* Better prompt controllability
* Reliable extraction behavior

---

# Dashboard Features

## KPI Overview

Displays:

* Total Discussions Analyzed
* Pain Point Discussions
* Gains Discussions
* Feature Request Discussions
* Persona Coverage
* Average Confidence Score

---

## Interactive Filters

Users can filter by:

* Discussion Type
* Minimum Confidence
* Minimum Comment Count
* Theme Frequency
* Keyword Search

---

## Analytics Tabs

### Pain Points

Visualizes recurring customer problems.

### Gains

Highlights product benefits users appreciate.

### Personas

Identifies recurring customer segments.

### Feature Requests

Displays the most requested product improvements.

### Discussion Explorer

Allows exploration of individual discussions including:

* Discussion Type
* Engagement Metrics
* Confidence Score
* Reddit Link
* Extracted Insights

---

# Modular System Design

The system was intentionally designed with a modular architecture.

Each stage operates independently:

* Classification
* Extraction
* Normalization
* Aggregation
* Dashboard Visualization

Advantages:

* Easier debugging
* Better resource management
* Partial pipeline reruns
* Improved maintainability
* Scalability for larger datasets
* Reduced hardware pressure on local systems

This design allows efficient execution even on limited local hardware resources.

---

# AI-Assisted Development

AI tools were used during development to accelerate experimentation, debugging, and prompt refinement.

AI assistance was utilized for:

* Prompt experimentation
* Architecture refinement
* Debugging support
* Pipeline optimization ideas
* Dashboard improvement suggestions

All core implementation, business logic, evaluation methodology, and system architecture decisions were independently designed and validated.

---

# Key Skills Demonstrated

## AI Engineering

* Local LLM Deployment
* Prompt Engineering
* Hallucination Reduction
* JSON Schema Enforcement
* Structured Information Extraction

## Data Engineering

* Pipeline Design
* Data Transformation
* Data Aggregation
* Feature Engineering

## Analytics

* Voice-of-Customer Analysis
* Product Intelligence
* Customer Insight Discovery
* KPI Generation

## Software Engineering

* Modular Architecture
* Reproducible Workflows
* Dashboard Development

---

# Repository Structure

```text
voice-of-customer-ai-agent/

├── dashboard/
│   └── app.py
│
├── src/
│   ├── run_classifier.py
│   ├── run_extractor.py
│   ├── normalize_themes.py
│   ├── analyze_insights.py
│
├── outputs/
│   └── normalized_insights.pkl
│
├── screenshots/
│
├── requirements.txt
│
└── README.md
```

---

# Results

The platform successfully transformed over 9,000 Reddit comments into structured product intelligence.

Generated insights include:

* Customer pain points
* Product strengths
* User personas
* Must-have features
* Feature requests
* Recurring discussion themes

The resulting dashboard enables rapid exploration of customer behavior and product opportunities.

---

# Future Scope

## End-to-End Automation

The platform can evolve into a fully automated customer intelligence system where users simply:

1. Upload raw discussion data
2. Run automated processing
3. Receive structured dashboards and insights instantly

No manual analysis would be required.

---

## Enterprise Knowledge Integration

The same architecture can be adapted for internal company datasets such as:

* Customer support tickets
* Product reviews
* CRM notes
* Survey responses
* Community forums
* Internal feedback systems

This could significantly reduce manual research workload while enabling direct visibility into customer behavior and business KPIs.

---

## Advanced Product Intelligence

Potential future capabilities:

* Sentiment Analysis
* Trend Forecasting
* Topic Evolution Tracking
* Automated Product Recommendations
* Multi-platform Customer Intelligence
* Competitive Insight Analysis

---

# Running Locally

## Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/voice-of-customer-ai-agent.git
cd voice-of-customer-ai-agent
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Launch Dashboard

```bash
streamlit run dashboard/app.py
```

---

# Author

**Yashodhar Hajare**
