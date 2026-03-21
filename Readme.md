# 🎙️ Voice & Text to Image — Whisper + DALL-E Pipeline

![Python](https://img.shields.io/badge/Python-3.11-blue?style=flat-square&logo=python)
![OpenAI](https://img.shields.io/badge/OpenAI-Whisper_+_DALL--E-green?style=flat-square&logo=openai)
![Streamlit](https://img.shields.io/badge/UI-Streamlit-red?style=flat-square&logo=streamlit)
![Internship](https://img.shields.io/badge/Built_At-Enloomed_India-blue?style=flat-square)
![Input Reduction](https://img.shields.io/badge/Input_Time_Reduced-60%25-brightgreen?style=flat-square)
![Status](https://img.shields.io/badge/Stage-Complete-green?style=flat-square)

---

🏢 **Built At:** Enloomed India Pvt. Ltd., Kanpur — AI/ML Developer Intern
📅 **Duration:** December 2023 – February 2024
👤 **Author:** [Ashutosh — GitHub](https://github.com/Ashutosh-AIBOT) · [LinkedIn](https://www.linkedin.com/in/ashutosh1975271/)
💼 **Portfolio:** [ashutosh-portfolio-kappa.vercel.app](https://ashutosh-portfolio-kappa.vercel.app/)

---

## 📋 Table of Contents

- [What This Does](#-what-this-does)
- [Internship Impact](#-internship-impact)
- [Architecture](#-architecture)
- [What I Built](#-what-i-built)
- [Pipeline Deep Dive](#-pipeline-deep-dive)
- [Quick Start](#-quick-start)
- [Environment Variables](#-environment-variables)
- [Tech Stack](#-tech-stack)
- [Project Status](#-project-status)
- [Links](#-links)
- [Author](#-author)

---

## 🧠 What This Does

A real production pipeline built during an AI/ML internship
at Enloomed India Pvt. Ltd. that converts voice or text input
into AI-generated images — reducing user input time by 60%.

1. **Problem** — Users at Enloomed needed to generate images
   from descriptions but typing long prompts was slow,
   error-prone, and created friction in the workflow
2. **Solution** — Speak your prompt instead of typing it.
   OpenAI Whisper transcribes speech in real time.
   DALL-E generates the image from the transcription.
   Full pipeline runs in under 10 seconds.
3. **For** — AI/ML Engineer / GenAI Developer hiring managers
   looking for real production AI pipeline proof from
   an actual internship, not just a personal project

---

## 📈 Internship Impact

| Metric | Value |
|--------|-------|
| User Input Time Reduction | **60%** |
| Company | Enloomed India Pvt. Ltd. |
| Location | Kanpur, UP |
| Duration | Dec 2023 – Feb 2024 |
| Role | AI/ML Developer Intern |
| Pipeline Type | Voice → Transcription → Image Generation |
| Dashboard | Real-time Streamlit performance dashboard |
| Data Processed | Unstructured audio datasets |

---

## 🏗️ Architecture
```
User Input
  ├── Voice → Microphone (SoundDevice)
  └── Text  → Direct text input (Streamlit)
        ↓
Audio Capture (SoundDevice)
  → Records audio in real time
  → Saves to .wav file (Wavio)
        ↓
OpenAI Whisper API
  → Transcribes audio to text
  → Handles accents, noise, pacing
  → Returns clean text prompt
        ↓
Prompt Processing
  → Clean and format transcription
  → Add style modifiers if needed
  → Prepare for DALL-E input
        ↓
OpenAI DALL-E API
  → Generates image from text prompt
  → Returns image URL / base64
  → Supports multiple image sizes
        ↓
Analytics Pipeline
  → Audio dataset cleaning and preprocessing
  → Performance metrics logging
  → Company-level insights and analysis
```

---

## 🔨 What I Built

### 1. Voice Capture Module
- SoundDevice library captures real-time microphone input
- Configurable sample rate and duration
- Wavio saves captured audio as clean `.wav` file
- Handles microphone permission and device selection
- Error handling for no-input and low-quality audio

### 2. OpenAI Whisper Integration
- Whisper API transcribes `.wav` file to text
- Handles multiple accents and background noise
- Returns clean, punctuated transcription
- Reduced manual typing input time by **60%**
- Supports real-time streaming transcription mode

### 3. Prompt Processing Layer
- Cleans raw transcription for DALL-E compatibility
- Removes filler words and transcription artifacts
- Optionally appends style modifiers for better outputs
- Validates prompt length against DALL-E limits

### 4. DALL-E Image Generation
- OpenAI DALL-E API generates image from processed prompt
- Supports 256×256, 512×512, 1024×1024 output sizes
- Returns image URL displayed directly in Streamlit
- Saves generated images locally for session history

### 5. Streamlit Performance Dashboard
- Real-time display of generated images
- Shows transcription text alongside image
- Logs pipeline latency per step (capture → transcribe → generate)
- KPI cards: total generations, avg latency, success rate
- Built to support company-level insight monitoring

### 6. Audio Dataset Cleaning Pipeline
- Preprocessed unstructured audio datasets for company use
- Standardized audio file formats and sample rates
- Removed corrupted and duplicate audio files
- Prepared clean datasets to support analytics workflows

---

## 🔍 Pipeline Deep Dive
```
Step 1 — Voice Capture (avg ~2 seconds)
  User speaks: "A futuristic city at night with neon lights"
  SoundDevice records → Wavio saves → audio.wav

Step 2 — Whisper Transcription (avg ~1.5 seconds)
  audio.wav → Whisper API
  Output: "A futuristic city at night with neon lights"

Step 3 — Prompt Processing (avg ~0.1 seconds)
  Clean text → validate → format
  Final prompt: "A futuristic city at night with neon lights,
                 digital art, highly detailed, 4K"

Step 4 — DALL-E Generation (avg ~5 seconds)
  Prompt → DALL-E API → image URL
  Image displayed in Streamlit

Total pipeline time: ~8.6 seconds
vs manual typing workflow: ~22 seconds
Time saved: 60% reduction
```

---

## ⚡ Quick Start

**Prerequisites:** Python 3.11+, Git, OpenAI API key
```bash
# 1. Clone the repo
git clone https://github.com/Ashutosh-AIBOT/voice-text-to-image-pipeline.git
cd voice-text-to-image-pipeline

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Set up environment variables
cp .env.example .env
# Add your OpenAI API key to .env

# 5. Run the app
streamlit run app.py

# 6. Open browser
# http://localhost:8501
# Click Record → Speak your prompt → See the image
```

---

## 🔑 Environment Variables

| Variable | What It Is | Where To Get |
|----------|-----------|-------------|
| `OPENAI_API_KEY` | OpenAI API key for Whisper + DALL-E | [platform.openai.com](https://platform.openai.com/) |
| `IMAGE_SIZE` | DALL-E output size | `256x256`, `512x512`, or `1024x1024` |
| `APP_ENV` | Environment flag | `development` or `production` |

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3.11 | Core language |
| OpenAI Whisper API | Speech to text transcription |
| OpenAI DALL-E API | Text to image generation |
| SoundDevice | Real-time microphone audio capture |
| Wavio | Audio file saving (.wav format) |
| Streamlit | Interactive dashboard and UI |
| Pandas + NumPy | Audio dataset cleaning and analysis |
| Matplotlib | Performance metrics visualization |
| Git | Version control |

---

## 📁 Repository Structure
```
voice-text-to-image-pipeline/
│
├── app.py                          # Main Streamlit app
│
├── pipeline/
│   ├── __init__.py
│   ├── capture.py                  # SoundDevice audio capture
│   ├── transcribe.py               # Whisper API integration
│   ├── process.py                  # Prompt cleaning + formatting
│   ├── generate.py                 # DALL-E image generation
│   └── analytics.py                # Performance logging + KPIs
│
├── data/
│   └── audio/                      # Captured audio files (session)
│
├── outputs/
│   └── images/                     # Generated images (session)
│
├── .env.example                    # Environment variable template
├── requirements.txt
└── README.md
```

---

## 📊 Project Status

| Deliverable | Status |
|-------------|--------|
| Voice Capture Module | ✅ Complete |
| Whisper Transcription | ✅ Complete |
| Prompt Processing Layer | ✅ Complete |
| DALL-E Image Generation | ✅ Complete |
| Streamlit Dashboard | ✅ Complete |
| Audio Dataset Cleaning | ✅ Complete |
| Performance Analytics | ✅ Complete |
| 60% Input Time Reduction | ✅ Achieved |

---

## 🌐 Links

| Resource | URL |
|----------|-----|
| 💼 Portfolio | [ashutosh-portfolio-kappa.vercel.app](https://ashutosh-portfolio-kappa.vercel.app/) |
| 🐙 GitHub | [github.com/Ashutosh-AIBOT](https://github.com/Ashutosh-AIBOT) |
| 🔗 LinkedIn | [linkedin.com/in/ashutosh1975271](https://www.linkedin.com/in/ashutosh1975271/) |

---

## 👤 Author

**Ashutosh**
B.Tech Electronics Engineering  · Batch 2026
AI/ML Developer Intern — Enloomed India Pvt. Ltd. (Dec 2023 – Feb 2024)
[GitHub](https://github.com/Ashutosh-AIBOT) · [LinkedIn](https://www.linkedin.com/in/ashutosh1975271/) · [Portfolio](https://ashutosh-portfolio-kappa.vercel.app/)

---

> *"Speak it. See it. 60% faster.*
> *Built at a real company. Shipped to real users."*
>
> — Ashutosh, building this from zero.
```
