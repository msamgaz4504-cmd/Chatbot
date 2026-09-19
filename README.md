# ENIAC Club Assistant

A rule-based conversational assistant developed for the ENIAC Club at ENSA Safi.

This project represents the first implementation of a conversational application developed during my learning journey in Natural Language Processing and Generative AI.

The objective of this version is to understand and implement the foundations of conversational systems before progressively improving the application as new concepts are introduced.

## Overview

ENIAC Club Assistant provides students with a conversational interface for accessing information related to the ENIAC Club.

The assistant currently covers topics such as:

* Club presentation and mission
* Training sessions and workshops
* Activities and events
* Membership and recruitment
* Club organization
* NEXUS: THE CODE HUNT
* Previous projects and achievements
* Participation information
* General club information

The current implementation is intentionally based on predefined conversational rules.

It does not use a Large Language Model, Retrieval-Augmented Generation system, or external generative AI API.

## Architecture

The application follows a rule-based conversational workflow:

```text
User message
     |
     v
Streamlit interface
     |
     v
NLTK Chat engine
     |
     v
Regular-expression matching
     |
     v
Predefined conversational pairs
     |
     v
Response
     |
     v
Streamlit interface
```

The chatbot compares each user message with a collection of predefined regular-expression patterns.

When a pattern matches, one of its associated responses is returned.

Example:

```python
[
    r"^(bonjour|salut|hello|coucou|bonsoir)[.! ]*$",
    [
        "Bonjour ! Bienvenue chez ENIAC. Comment puis-je vous aider ?",
        "Bonjour ! Que souhaitez-vous savoir sur le club ENIAC ?"
    ]
]
```

This architecture makes the behavior of the assistant predictable and easy to inspect, while also exposing the limitations of rule-based conversational systems.

## Current Capabilities

### Rule-Based Conversation Engine

The conversational logic is implemented with `NLTK Chat`, regular expressions, and predefined question-response pairs.

The current knowledge base contains more than 100 conversational rules organized around the main ENIAC-related topics.

### Custom French Reflections

The application includes a custom reflection dictionary used by the NLTK conversational engine.

Reflections allow captured expressions to be transformed when they are reused inside a response.

Examples include:

```text
je       -> vous
mon      -> votre
je veux  -> vous voulez
```

This mechanism allows certain dynamic responses to remain grammatically coherent.

### Web Interface

The user interface is implemented with Streamlit.

It currently provides:

* Interactive chat
* Conversation history
* Suggested questions
* Sidebar navigation
* Custom interface styling
* Session-based state management

### Authentication

The application includes a simple authentication layer before access to the chatbot.

Authentication values can be configured using environment variables:

```env
ENIAC_USERNAME= eniac
ENIAC_PASSWORD= Eniac@2026
```

This avoids relying exclusively on credentials written directly into the application logic.

### Fallback Strategy

The chatbot includes a final fallback rule for requests that do not match any known conversational pattern.

Instead of fabricating information, the assistant informs the user that the requested information is unavailable or needs confirmation.

This behavior was intentionally chosen to prioritize reliability over unsupported responses.

## Technology Stack

| Component             | Technology          |
| --------------------- | ------------------- |
| Programming language  | Python              |
| Conversational engine | NLTK                |
| Pattern matching      | Regular Expressions |
| Web interface         | Streamlit           |
| Version control       | Git                 |
| Repository hosting    | GitHub              |

## Project Structure

The current version keeps the implementation deliberately simple so that the conversational workflow remains easy to understand.

The main application contains the following logical components:

```text
Application
|
|-- Configuration
|
|-- Authentication
|
|-- French reflections
|
|-- Conversational pairs
|
|-- NLTK Chat engine
|
|-- Streamlit interface
|
`-- Session and conversation management
```

At this stage, the emphasis is on understanding the complete execution flow rather than introducing unnecessary architectural complexity.

## Running the Project Locally

### Clone the repository

```bash
git clone <repository-url>
cd <Chatbot>
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Configure authentication

The application supports environment variables for authentication:

```env
ENIAC_USERNAME=your_username
ENIAC_PASSWORD=your_password
```

### Start the application

```bash
streamlit run app.py
```

Streamlit will start the application and provide the local address used to access the interface from the browser.

## Current Limitations

This version intentionally relies on a rule-based architecture.

As a consequence, the assistant:

* depends on predefined patterns;
* cannot generate new knowledge independently;
* may fail when a request is expressed using an unsupported formulation;
* has limited tolerance for spelling mistakes and linguistic variations;
* does not perform semantic understanding of user requests;
* cannot currently analyze external documents;
* does not use a Large Language Model.

Increasing the number of conversational rules improves coverage, but does not fundamentally solve the limitations of the rule-based approach.

These limitations are important because they provide a clear baseline from which the application can be evaluated and progressively improved.

## Learning Outcomes

This project was developed as a practical implementation rather than only as a theoretical NLP exercise.

Through this first version, I worked on:

* Understanding the architecture of a conversational application
* Building a rule-based NLP system
* Designing regular-expression patterns
* Using NLTK conversational utilities
* Working with captured expressions and reflections
* Building an interactive application with Streamlit
* Managing conversational state
* Implementing basic authentication
* Designing fallback behavior
* Structuring domain-specific conversational knowledge
* Identifying the practical limitations of rule-based chatbots

The project also provided a practical comparison between deterministic conversational logic and more advanced AI-based conversational approaches.

## Further Development

This application is intended to evolve progressively as new NLP and AI concepts are studied and implemented.

Future work will focus on improving the assistant's ability to process information, handle more flexible user interactions, work with additional input formats, and provide more capable conversational behavior.

The objective is to evolve the project incrementally while preserving a clear understanding of each architectural and technical improvement.

## Author

**Meryem Samgaz**
Data Engineering and Artificial Intelligence Engineering Student — ENSA Safi

Areas of interest:

* Artificial Intelligence
* Data
* Natural Language Processing
* Generative AI

## Status

**Version 1 — Completed**

Current implementation:

```text
Rule-Based Conversational Assistant
Python + NLTK + Regular Expressions + Streamlit
```
