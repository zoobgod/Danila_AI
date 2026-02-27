# Danila_AI (Python API + TypeScript UI)

Danila_AI is a document translation app for:
- Medical / Pharmacopeia documents
- Judicial / Business documents

Core workflow:
1. Extract text from PDF and image-like files (OCR fallback supported).
2. Show extracted source text for user review.
3. Translate to Russian with OpenAI API (English or Chinese source).
4. Export a structured, formatted `.docx` using the app's built-in layout.

Custom glossary upload is supported (`.txt/.csv/.tsv/.json/.md`) and can include EN->RU and ZH->RU terminology.

## Architecture

```text
frontend (React + TS + Tailwind)
  -> /api/extract
  -> /api/translate
  -> /api/generate-doc
backend (FastAPI)
  -> modules/pdf_extractor.py
  -> modules/translator.py
  -> modules/doc_generator.py
```

## API Endpoints

- `GET /api/health`
- `GET /api/capabilities`
- `POST /api/extract` (multipart: `file`)
- `POST /api/translate` (JSON: includes `source_language`, `domain_profile`)
- `POST /api/generate-doc` (JSON, streams `.docx`)
- `POST /api/process` (single-call pipeline, multipart)

## Translation Modes

- `source_language`: `auto`, `en`, `zh`
- `domain_profile`: `combined`, `medical`, `judicial_business`

## DOCX Output Policy

Danila_AI always uses its own fixed document structure for output.
User-provided Word structure templates are intentionally disabled.

## Local Development

### 1) Python backend

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python backend/run.py
```

Backend: `http://localhost:8000`

For a fuller local OCR/table stack:

```bash
pip install -r requirements.full.txt
```

### 2) Frontend

```bash
cd frontend
npm install
npm run dev
```

Frontend: `http://localhost:5173`

## Deploying on Vercel

This repo includes `vercel.json` configured for:
- Python API entrypoint: `api/index.py`
- Static frontend build from `frontend/`

### Environment Variables

- `CORS_ALLOW_ORIGINS` (optional, comma-separated). Default: `*`
- Frontend optional: `VITE_API_BASE_URL` (if API is hosted elsewhere)

## OCR Notes

For scanned documents, server runtime should provide Tesseract.

`packages.txt` currently lists:
- `tesseract-ocr`
- `tesseract-ocr-eng`
- `ghostscript`
- `default-jre-headless`
