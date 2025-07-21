# 🐍 Python‑Mastery – UV + Docker Starter

Welcome! This repo is a **comprehensive learning playground** for mastering Python fundamentals through hands-on practice.
Everything is wired for reproducible dev‑environments **without any tricky setup**:

- **uv** – ultra‑fast package & virtual‑env manager.
- **Docker + Compose** – optional Linux container that always mirrors your local setup.
- **12 progressive sections** (`01_primitive_types/`, `02_control_flow/`, …) with 140+ drills and 26 mini-projects.
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
├── 00_course_outline/          # 📚 Master learning roadmap
├── 01_primitive_types/         # 🔤 Variables, strings, numbers (15 drills)
├── 02_control_flow/           # 🔄 Conditionals, loops (13 drills)
├── 03_functions/              # ⚙️  Code organization (12 drills)
├── 04_data_structures/        # 📊 Lists, dicts, sets (23 drills)
├── 05_exceptions/             # 🛡️  Error handling (7 drills)
├── 06_classes/                # 🏗️  OOP, inheritance (22 drills)
├── 07_modules/                # 📦 Code packaging (8 drills)
├── 08_stdlib/                 # 🏛️  Standard library (17 drills)
├── 09_packaging/              # 📋 Pip, venv, publishing (10 drills)
├── 10_packages/               # 🌐 External libraries (12 drills)
├── 11_web_apis/               # 🚀 FastAPI, CRUD (8 drills)
├── 12_webapp/                 # 🎨 Portfolio showcase
├── webapp/                    # 🔧 Development workspace
├── Dockerfile + docker-compose.yml
├── pyproject.toml             # Single source of deps & tool configs
└── PROGRESS.md                # 📈 Your achievement tracker
```

**Total Learning Path**: 147 micro-drills + 26 mini-projects → **1 comprehensive portfolio webapp**

---

## 🎯 **Learning Philosophy**

- **Progressive Mastery**: Each section builds only on previous concepts - no forward references
- **Muscle Memory**: Type every solution yourself, no copy-paste
- **Real-world Integration**: All mini-projects become features in your final webapp
- **Portfolio Ready**: Showcase professional Python development skills

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

# Start with fundamentals
python 01_primitive_types/drills.py
```

### **2. Container Development**

```bash
# Build and start container
docker compose build dev
docker compose up -d dev
docker compose exec dev bash

# Inside container
python 01_primitive_types/drills.py
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

Your learning journey culminates in a FastAPI application featuring:

```
🌐 Python Mastery Portfolio
├── 🧮 Calculators (Unit converter, Functions, Banking)
├── 🎮 Games (Number guessing, Logic puzzles)
├── 📊 Data Tools (CSV analyzer, JSON validator)
├── 📁 File Management (Log viewer, Config editor)
├── 🌤️ External APIs (Weather, Email sender)
├── 👥 User System (Registration, Profiles)
└── 📈 Admin Dashboard (Usage stats, System health)
```

**Run the showcase**:

```bash
docker compose exec dev bash
uvicorn webapp.main:app --reload --host 0.0.0.0 --port 8000
# Open http://localhost:8000
```

---

## 📈 Track your journey

- **PROGRESS.md** tracks every drill and mini-project completion
- **00_course_outline/** shows the complete learning roadmap
- Each section README has detailed drill prompts and mini-project specs
- Commit frequently to build momentum and showcase your growth

---

## 🎯 **Your Learning Path**

1. **Start**: `01_primitive_types/` - Master variables, strings, numbers
2. **Progress**: Follow numbered sections in order
3. **Practice**: Complete all drills + mini-projects in each section
4. **Build**: Integrate mini-projects into final webapp
5. **Showcase**: Deploy your comprehensive Python portfolio

**Ready to master Python? Fire up your editor and start coding!** 🔥

> 💡 **Remember**: Type out every drill, don't copy‑paste. The goal is building muscle memory and deep understanding.
