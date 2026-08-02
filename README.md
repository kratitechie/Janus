# JANUS

An AI-powered multimodal notification routing system built for the WhatsApp Message Router Hackathon.

## Overview

JANUS intelligently classifies incoming WhatsApp messages and determines whether they should:

- Notify immediately
- Be added to the digest
- Be muted

Unlike traditional rule-based systems, JANUS reasons over multiple modalities including:

- Text messages
- Images
- Voice notes

using semantic retrieval and large language models.

---

## Features

- Semantic Retrieval (RAG)
- Context-aware Decision Agent
- Image Understanding
- Voice Transcription
- OCR Cache
- Audio Cache
- Decision Cache
- Chroma Vector Database
- Gemini 3.6 Flash
- Modular AI Architecture

---

## Architecture

Incoming Message

↓

Media Router

↓

Text / Image / Voice

↓

Normalized Text

↓

Context Builder

↓

Semantic Retrieval

↓

Decision Agent

↓

Structured JSON

↓

Output CSV

---

## Tech Stack

Python 3.11

Gemini 3.6 Flash

Gemini Embeddings (temporary)

ChromaDB

Pandas

---

## Folder Structure

src/

agents/

builders/

llm/

loaders/

media/

pipeline/

retrieval/

cache/

dataset/

---

## Status

🚧 Under active development.

Current progress:

- Text Routing ✅
- Image Understanding ✅
- Voice Transcription ✅
- Semantic Retrieval ✅
- Decision Agent ✅
- Batch Pipeline 🚧
- Deployment 🚧

---

## Authors

Krati Bhatia