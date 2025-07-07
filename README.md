# AutoSuggest Search Engine

Prefix-based search engine using Trie and Min-Heap ranking.

---
## Description

This project provides auto-suggestion of words based on user-input prefixes. It uses a **Trie** data structure for fast prefix lookup and a **Min-Heap** to rank suggestions by frequency or relevance. Ideal for search bars, input assistance, and auto-completion features. 

---

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Applications](#applications)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Folder Structure](#folder-structure)
- [License](#license)
- [Author](#author)

---

## Installation

1. **Clone the repository:**

```
git clone https://github.com/SruthiPuli/Auto-Complete-Search-Engine.git
cd Auto-Complete-Search-Engine
```

#### 2. Install Dependencies :
```
pip install -r requirements.txt
```

#### 3. Run the Project :
```
python manage.py runserver
```

## Usage

 ## 1: Typing a Few Letters to Save Time
User Input: rec
#### Suggestions:
- recipe
- record
- recovery

### Usage Purpose:
The user saves time by not typing the full word and selects from ranked options.

## 2: Correcting or Guiding Ambiguous Input
User Input: resu
#### Suggestions:

- resume
- result
- resurface

#### Usage Purpose:
The system disambiguates what the user might mean, guiding them toward correct or intended input.

## 3: Discovering Relevant Alternatives
User Input: mac
#### Suggestions:

- macbook
- mac os
- mac address

#### Usage Purpose:
The user may only know part of the term — suggestions help them discover other meaningful completions.

## 4: Handling Incomplete or Partial Words
User Input: prog
#### Suggestions:

- programming
- progress
- programmer

#### Usage Purpose:
User types a fragment, and the system completes it based on frequency or context.

## 5: Prioritized Suggestions Based on Frequency
User Input: da
#### Suggestions:

- data (most frequent)
- dashboard
- database

#### Usage Purpose:
The top-k results help the user pick the most commonly used terms with minimal effort.

## Applications

### 1. Search Engines (e.g., Google, Bing)

When a user starts typing a query like how to, the search engine suggests top queries like:

##### Uses prefix search with a Trie and top-k ranking based on popularity (click-through rates, frequency).

### 2. E-commerce Product Search (e.g., Amazon, Flipkart)
Typing lap shows suggestions like:
##### Uses Trie for fast lookup and Min-Heap or similar structure to rank products by search frequency, user interest, or reviews.

### 3. Dictionary/Language Apps (e.g., Merriam-Webster, Duolingo)
Search language words
##### Uses prefix search to help users quickly find words, with ranking based on word popularity or usage frequency.

### 4. Code Editors / IDEs (e.g., VS Code, IntelliJ)
code words suggestions like print(), private, printf()
Performs context-aware prefix matching and ranks suggestions based on usage history, scope, and language syntax.


## Features
### Fast Prefix Search using Trie

- Utilizes a Trie (Prefix Tree) data structure for efficient word lookup
- Enables real-time search suggestions as the user types
- Optimized for fast insertion and prefix-based retrieval of words

### Top-K Suggestions using Min-Heap
- Integrates a Min-Heap to rank and retrieve the most relevant or frequent suggestions
- Maintains the top-k matches dynamically based on usage frequency or ranking score
- Ensures that the most relevant results are always returned efficiently

### Easy Integration with Web-Based UIs
- Designed to plug seamlessly into any frontend built with HTML/CSS/JavaScript
- Works with Django APIs or other web frameworks for smooth client-server interaction
- Provides instant feedback in the UI for a responsive and interactive user experience

### Scalable and Customizable
- Supports large datasets with thousands of searchable words
- Easily configurable to adjust the number of suggestions, scoring methods, or ranking logic
- Flexible enough to adapt to different domains like e-commerce, search engines, or text editors


## Tech Stack
### Core Technologies
#### Python
- Constructing the Trie and Min-Heap data structures
- Inserting words with associated ranks into the heap
- Performing prefix-based search queries efficiently
- Saving the model data to enable fast retrieval without rebuilding the structure every time

#### Django
- Acting as the bridge between the frontend and backend
- Receiving input words from the user via API calls
- Passing those inputs to the backend search model
- Returning auto-suggest results (from Trie & Min-Heap logic) back to the frontend in real-time

#### HTML / CSS / JavaScript
- Creating a clean, user-friendly interface for the search bar
- Capturing the user’s typed input dynamically
- Displaying live suggestions as the user types

### Data Structures

#### Trie (Prefix Tree) 
The Trie is used to store all words for fast prefix-based lookup.
Each character in a word is stored as a node, enabling O(length) search for any prefix.
It supports efficient insertion and retrieval of words during the build phase.
When a user inputs a prefix, the Trie quickly finds all words starting with that prefix.
These matched words are then passed to the Min-Heap for ranking based on frequency or relevance.
#### Min-Heap 
Min-Heap is used to efficiently rank and retrieve the top suggestions based on frequency or relevance.
Each node in the heap stores a word and its corresponding frequency.
When a prefix is searched, all matching words from the Trie are pushed into the Min-Heap.
The heap maintains the top-k suggestions with the highest frequency by discarding lower-ranked entries.

## Folder Structure

```
AutoSuggest-Search-Engine/
├── Search/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── SearchApp/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│   ├── backend/
│   │   ├── __init__.py
│   │   ├── build_trie.py
│   │   ├── query.py
│   │   ├── trie.pkl
│   │   ├── triestructure.py
│   │   └── words.txt
│   ├── migrations/
│   └── Templates/
│       └── index.html
├── Snapshots/
│   └── (snapshot files)
├── db.sqlite3
├── manage.py
├── requirements.txt
├── LICENSE
└── README.md           

```

## License
This project is open-source and available under the [MIT License](LICENSE).  
© 2025 Sruthi Pulipati

## Author
**Sruthi Pulipati**

This is a personal project built to explore and implement efficient search algorithms like Trie and Min-Heap for real-time auto-suggestion functionality.

