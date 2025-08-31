# 🐍 Python‑Mastery – UV + Docker Starter

Welcome! This repo is **the ultimate learning resource** for mastering Python fundamentals through comprehensive, systematic practice.
Everything is wired for reproducible dev‑environments **without any tricky setup**:

- **uv** – ultra‑fast package & virtual‑env manager.
- **Docker + Compose** – optional Linux container that always mirrors your local setup.
- **6 foundational sections** with **111 systematic drills** covering "ALL the different ways" to use each concept.
- **7 organized mini-projects** with comprehensive templates and progressive versions.
- **FastAPI showcase webapp** integrating all your mini-projects for portfolio demonstration.

---

## ⚡ Choose your workflow

| Style                                                                   | When to use                                                 | One‑time setup             | Everyday commands                                                                                                                                              |
| ----------------------------------------------------------------------- | ----------------------------------------------------------- | -------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Local venv** <br>(fastest tests & lints)                              | You're happy running directly on macOS/Windows/Linux        | `uv venv`                  | ➊ `uv pip install -e ".[dev]"`<br>➋ `python 01_primitive_types/drills.py`<br>➌ `pytest -q`                                                                     |
| **Dev container** <br>(identical to Linux prod, no local Python needed) | You like VS Code _Dev Containers_ or you're on Windows Home | `docker compose build dev` | ➊ `docker compose up -d dev` _(start/refresh)_<br>➋ `docker compose exec dev bash` _(get a shell)_<br>➌ `python 01_primitive_types/drills.py`<br>➍ `pytest -q` |

> **Tip:** keep exactly **one** persistent container (`python-mastery-dev-1`).
> `docker compose run --rm …` gives disposable "scratch" shells, but beginners usually stick with `up + exec`.

---

## 📁 Complete Course Structure

```
.
├── 00_course_outline/          # 📚 Master learning roadmap & philosophy
├── 01_primitive_types/         # 🔤 Variables, strings, numbers (22 drills)
├── 02_control_flow/           # 🔄 Conditionals, loops (13 drills)
├── 03_functions/              # ⚙️  Code organization (12 drills)
├── 04_data_structures/        # 📊 Lists, dicts, sets (22 drills)
├── 05_exceptions/             # 🛡️  Error handling (20 drills)
├── 06_Classes_OOP/            # 🏗️  OOP, inheritance (22 drills)
├── Mini-Projects_hub/         # 🚀 7 organized project directories
│   ├── unit_converter/        #   ├── CLI interfaces & menu systems
│   ├── calculator/            #   ├── Function design & architecture
│   ├── password_toolkit/      #   ├── Security & string manipulation
│   ├── todo_manager/          #   ├── Data structures & CRUD
│   ├── number_guessing/       #   ├── Game logic & state management
│   ├── grades_analyzer/       #   ├── Data analysis & statistics
│   └── word_counter/          #   └── Text processing & algorithms
├── webapp/                    # 🔧 Portfolio showcase development
├── Dockerfile + docker-compose.yml
├── pyproject.toml             # Single source of deps & tool configs
├── REPORT.md                  # 📊 Comprehensive transformation report
└── PROGRESS.md                # 📈 Your achievement tracker
```

**Total Learning Path**: **111 systematic drills** + **7 comprehensive mini-projects** → **1 professional portfolio webapp**

---

## 🎯 **Learning Philosophy**

- **"ALL the Different Ways"**: Comprehensive coverage of every method, pattern, and approach for each concept
- **Progressive Mastery**: Each section builds only on previous concepts - zero forward references
- **Template-Driven Practice**: Copy clean templates with TODO markers, complete systematically
- **Muscle Memory**: Type every solution yourself to build coding fluency
- **Professional Standards**: Industry-grade patterns, error handling, and code organization
- **Real-world Integration**: All mini-projects become features in your portfolio webapp

---

## 🛠 What's inside the tool‑chain?

| Purpose            | Tool                 | Why beginners care                            |
| ------------------ | -------------------- | --------------------------------------------- |
| Package & env mgmt | **uv**               | one command to make venvs & install deps fast |
| Formatter          | **black**            | zero‑config code style                        |
| Linter             | **ruff**             | catches mistakes instantly                    |
| Tests              | **pytest**           | simple `assert`‑based testing                 |
| Container dev‑env  | **Docker + Compose** | mirrors Linux prod in one command             |

All dev‑tools live in **`pyproject.toml`** – no `requirements.txt` clutter.

---

## 🚀 **Getting Started**

### **1. Quick Start (Local Development)**

```bash
# Clone and setup
git clone <your-repo>
cd python-mastery-AOC
uv venv
uv pip install -e ".[dev]"

# Start with fundamentals (copy template, complete TODOs)
cd 01_primitive_types/
cp drills_template.py drills.py
python drills.py
```

### **2. Container Development**

```bash
# Build and start container
docker compose build dev
docker compose up -d dev
docker compose exec dev bash

# Inside container (copy template, complete TODOs)
cd 01_primitive_types/
cp drills_template.py drills.py
python drills.py
```

---

## 🔄 Adding / updating a dependency

1. **Local** (inside venv) **or** **container** shell:

```bash
uv pip add rich            # writes change into pyproject.toml
```

2. **Commit** the edited `pyproject.toml`.
3. **If you use Docker** rebuild once:

```bash
docker compose build dev
```

That's it – local & container stay in lock‑step.

---

## 🌐 **Final Showcase Webapp**

Your learning journey culminates in a FastAPI application featuring all 7 organized mini-projects:

```
🌐 Python Mastery Portfolio
├── 🧮 Unit Converter - Multi-category conversion tool
├── 🧮 Calculator - Professional mathematical operations
├── 🔐 Password Toolkit - Security and validation tools
├── 📝 Todo Manager - Task management with persistence
├── 🎮 Number Guessing - Interactive game logic
├── 📊 Grades Analyzer - Statistical data analysis
└── 📄 Word Counter - Text processing algorithms
```

**Run the showcase**:

```bash
docker compose exec dev bash
uvicorn webapp.main:app --reload --host 0.0.0.0 --port 8000
# Open http://localhost:8000
```

---

## 📈 Track your journey

- **REPORT.md** comprehensive transformation report documenting the entire learning system
- **PROGRESS.md** tracks every drill and mini-project completion
- **00_course_outline/** shows the complete learning roadmap and philosophy
- Each section has `notes_X.md` with systematic concept coverage and `drills_template.py` for practice
- Each mini-project directory contains templates, implementations, and project-specific guides
- Commit frequently to build momentum and showcase your growth

---

## 🎯 **Your Learning Path**

1. **Foundation**: `01_primitive_types/` → `06_Classes_OOP/` - Master core Python systematically
2. **Template Practice**: Copy `drills_template.py` → complete TODOs → build muscle memory
3. **Real Projects**: Explore `Mini-Projects_hub/` → copy templates → build professional applications
4. **Progressive Versions**: v1 (basic) → v2 (functions) → v2.1+ (production-ready)
5. **Portfolio Integration**: Combine all mini-projects into comprehensive webapp showcase

**Ready to master Python? Fire up your editor and start coding!** 🔥

> 💡 **Remember**: Type out every drill, don't copy‑paste. The goal is building muscle memory and deep understanding.
