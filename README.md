# 🧠 Metric Normalization Explorer

An interactive tool to visualize how different teams transform raw logs into modeling-ready metrics—like MAU. Compare logic, see outputs, and understand metric drift across functions.

## 🔍 What It Solves
- Metric ambiguity (same name, different logic)
- Invisible transformation pipelines
- Metric drift across teams
- Poor documentation of feature inputs

## 🚀 Features
- Raw → Transform → Normalize pipeline viewer
- Team-specific metric pipelines (Product, Finance, Marketing)
- SQL or logic previews for each step
- Output chart comparison
- Explanatory panel per context

## 📦 Tech Stack
- React + TypeScript
- Tailwind CSS
- Recharts
- (Optional) OpenAI API for explanations

## 📁 Structure
```
src/
├── components/
├── data/
├── pages/
└── types/
```

## 📌 Future Enhancements
- LLM-powered assistant to explain logic differences
- Metric versioning viewer (Git-style diffs)
- Real data integration or import

## 💡 Inspired by
- MetricLayer frameworks
- Real-world metric drift in data-centric orgs
