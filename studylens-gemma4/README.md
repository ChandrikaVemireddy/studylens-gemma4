# 📚 StudyLens — AI-Powered Multimodal Study Assistant

StudyLens is an AI-powered study assistant that helps students understand learning material from images.

Users can upload notes, textbook pages, diagrams, or questions, and StudyLens uses the multimodal capabilities of **Gemma 4** to analyze the content and provide easy-to-understand explanations, key points, practice questions, and follow-up assistance.

Built for the **Hacktoberfest Hack Day Hyderabad × React Hyderabad** hackathon.

---

## ✨ Features

- 🖼️ **Image Understanding** — Upload notes, textbook pages, diagrams, or questions.
- 🤖 **Gemma 4 AI Analysis** — Uses Gemma 4's multimodal capabilities to understand visual content.
- 📖 **Simple Explanations** — Converts complex material into beginner-friendly explanations.
- 📝 **Key Points** — Extracts important information from uploaded material.
- 🧠 **Practice Quiz** — Generates questions to help reinforce learning.
- 💬 **Follow-up Questions** — Continue interacting with the uploaded study material.
- 🎓 **Student-Focused** — Designed to make learning more interactive and accessible.

---

## 🎯 Hackathon Challenge

### Best Use of Gemma 4

StudyLens demonstrates how Gemma 4's multimodal capabilities can transform static educational content into an interactive learning experience.

Instead of simply reading a page of notes, students can upload the material and interact with it through explanations, key points, quizzes, and follow-up questions.

---

## 🏗️ How It Works

```text
                 👨‍🎓 Student
                     │
                     ▼
             📸 Upload Study Image
                     │
                     ▼
            ⚛️ React Frontend
                     │
                     ▼
             🐍 FastAPI Backend
                     │
                     ▼
                🤖 Gemma 4
                     │
                     ▼
        ┌────────────┼────────────┐
        │            │            │
        ▼            ▼            ▼
   📖 Explanation  📝 Key Points  🧠 Quiz
                     │
                     ▼
              💬 Follow-up Chat
