# AutoSuggest Search Engine

Prefix-based search engine using Trie and Min-Heap ranking.

---

## 🚀 Description

This project provides auto-suggestion of words based on user-input prefixes. It uses a **Trie** data structure for fast prefix lookup and a **Min-Heap** to rank suggestions by frequency or relevance. Ideal for search bars, input assistance, and auto-completion features.

---

## 📑 Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Folder Structure](#folder-structure)
- [Contributing](#contributing)
- [License](#license)
- [Author](#author)

---

## 🛠️ Installation

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

## 📌 Usage
Start typing a prefix in the search bar and get top-ranked word suggestions in real time.

## ✨ Features
Fast prefix search using Trie

Top-k suggestions using Min-Heap

Easy integration with web-based UIs

Scalable and customizable

## 🧰 Tech Stack
Python – core logic

Flask – backend server (optional)

HTML/CSS/JavaScript – frontend

Trie & Min-Heap – custom data structures

## 📁 Folder Structure

```
AutoSuggest-Search-Engine/
├── backend/
│   ├── triestructure.py         
│   └── build_trie.py           
├── frontend/
│   ├── index.html               
│   └── style.css                
├── requirements.txt             
├── README.md                    

```

## 📄 License
This project is open-source and available under the [MIT License](LICENSE).  
© 2025 Sruthi Pulipati

## 👤 Author
**Sruthi Pulipati**

This is a personal project built to explore and implement efficient search algorithms like Trie and Min-Heap for real-time auto-suggestion functionality.

