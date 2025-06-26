
# 🐍 Python‑Mastery – UV + Docker Starter

Welcome! This repo is a **beginner‑friendly playground** for relearning Python.
Everything is wired for reproducible dev‑environments **without any tricky setup**:

* **uv** – ultra‑fast package & virtual‑env manager.
* **Docker + Compose** – optional Linux container that always mirrors your local setup.
* Clean, numbered section folders (`01_primitive_types/`, `02_control_flow/`, …) so you never wonder where to save a drill.

---

## ⚡ Choose your workflow

| Style                                                                   | When to use                                                 | One‑time setup             | Everyday commands                                                                                                                                                |
| ----------------------------------------------------------------------- | ----------------------------------------------------------- | -------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Local venv** <br>(fastest tests & lints)                              | You’re happy running directly on macOS/Windows/Linux        | `uv venv`                  | ➊ `uv pip install -e ".[dev]"`<br>➋ `python 01_primitive_types/drills.py`<br>➌ `pytest -q`                                                                       |
| **Dev container** <br>(identical to Linux prod, no local Python needed) | You like VS Code *Dev Containers* or you’re on Windows Home | `docker compose build dev` | ➊ `docker compose up -d dev`  *(start/refresh)*<br>➋ `docker compose exec dev bash`  *(get a shell)*<br>➌ `python 01_primitive_types/drills.py`<br>➍ `pytest -q` |

> **Tip:** keep exactly **one** persistent container (`python-mastery-dev-1`).
> `docker compose run --rm …` gives disposable “scratch” shells, but beginners usually stick with `up + exec`.

---

## 📁 Folder map

```
.
├── 00_course_outline/        # high‑level TOC
├── 01_primitive_types/       # ← first chapter: drills.py + README.md
├── 02_control_flow/
├── webapp/                   # later: FastAPI + HTMX showcase site
├── Dockerfile + docker-compose.yml
├── pyproject.toml            # single source of deps & tool configs
└── PROGRESS.md               # tick‑box tracker
```

---

## 🛠 What’s inside the tool‑chain?

| Purpose            | Tool                 | Why beginners care                            |
| ------------------ | -------------------- | --------------------------------------------- |
| Package & env mgmt | **uv**               | one command to make venvs & install deps fast |
| Formatter          | **black**            | zero‑config code style                        |
| Linter             | **ruff**             | catches mistakes instantly                    |
| Tests              | **pytest**           | simple `assert`‑based testing                 |
| Container dev‑env  | **Docker + Compose** | mirrors Linux prod in one command             |

All dev‑tools live in **`pyproject.toml`** – no `requirements.txt` clutter.

---

## 🔄 Adding / updating a dependency

1. **Local** (inside venv) **or** **container** shell:

```bash
uv pip add rich            # writes change into pyproject.toml
```

2. **Commit** the edited `pyproject.toml`.
3. **If you use Docker** rebuild once:

```bash
docker compose build dev
```

That’s it – local & container stay in lock‑step.

---

## 🌐 Running a mini‑project that serves HTTP

```bash
docker compose exec dev bash
uvicorn mini_api:app --reload --host 0.0.0.0 --port 8000
```

* The code is live‑reloaded because it watches the bind‑mount.
* Port **8000** inside the container is mapped to **8000** on your host, so open [http://localhost:8000](http://localhost:8000).

---

## 📈 Track your journey

Update **PROGRESS.md** every time you finish a drill or mini‑project – future you (and any recruiters) will see the concrete timeline of your growth.

Happy coding — and remember: type out every drill, don’t copy‑paste! 🔥
