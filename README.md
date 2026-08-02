JANUS — AI Multimodal WhatsApp Notification Router
🚀 ## Overview

JANUS is an AI-powered notification routing system that intelligently prioritizes WhatsApp messages instead of treating every notification equally.

Rather than relying solely on keywords, JANUS combines multimodal understanding, semantic retrieval, user context, and LLM reasoning to determine whether a message should interrupt the user immediately, be shown later, or be muted.

The system supports:

Text messages
Image messages (OCR + scene understanding)
Voice notes (speech transcription)

## Problem

Modern messaging platforms generate excessive notifications.

Important messages such as OTPs, banking alerts, urgent work updates, and deadlines are often buried beneath promotions, forwarded spam, memes, and casual conversations.

JANUS solves this by routing every message into one of three actions:

🔔 Notify
📝 Digest
🔕 Mute

## Features

✅ Hybrid Rule Engine + LLM

✅ Multimodal Processing

OCR for posters/screenshots
Voice transcription

✅ Retrieval-Augmented Generation (RAG)

Semantic search over previous message history

✅ User Context Builder

User metadata
Groups
Business accounts
Events
Conversation history

✅ Local Embeddings

Sentence Transformers (all-MiniLM-L6-v2)

✅ ChromaDB Vector Database

✅ OCR Cache

✅ Voice Cache

✅ Decision Cache

## Architecture

Incoming Message
        │
        ▼
Context Builder
        │
 ┌──────┴────────┐
 │               │
Media Router     Metadata
 │
 ├── OCR
 ├── Voice
 └── Text
        │
        ▼
Semantic Retrieval (ChromaDB)
        │
        ▼
Rule Engine
        │
        ├── Notify
        ├── Digest
        └── Mute
        │
        ▼
Gemini Decision Agent
        │
        ▼
output.csv

## Tech Stack

Language

Python 3.11

LLM

Google Gemini 3.6 Flash

Embeddings

Sentence Transformers
all-MiniLM-L6-v2

Vector Database

ChromaDB

Libraries

pandas
torch
sentence-transformers
google-genai
python-dotenv

## Project Structure

Janus/

src/
    agents/
    builders/
    llm/
    media/
    retrieval/
    pipeline/
    loaders/

dataset/

cache/
    audio/
    ocr/
    chroma/
    decisions/

main.py
requirements.txt
README.md
output.csv

## Pipeline

Load dataset
Process media
Extract OCR / speech
Build user context
Retrieve similar historical messages
Apply Rule Engine
Use Gemini only for ambiguous cases
Generate routing decision
Export output.csv

## Output Schema

message_id

action

message_type

reason

confidence

evidence_message_ids

## Performance Optimizations

Local embeddings
Chroma vector search
OCR caching
Voice transcription caching
Decision caching
Rule-first routing to minimize LLM calls

## Authors

Krati Bhatia
Hackathon Submission – JANUS