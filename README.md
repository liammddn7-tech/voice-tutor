# Voice Tutor

A personal Socratic voice tutor. Claude (Anthropic API) teaches and keeps the study records; OpenAI handles speech to text and text to speech.

- The app is `index.html` (served by GitHub Pages). API keys and study records stay in the browser on each device; nothing personal is stored in this repository.
- Source: `src/app.html`. Run `python3 src/build.py` to rebuild (it inlines the bundled Anthropic SDK).
