Prompt: Build a Git-like Prompt Compiler and Human-in-the-Loop Code Generator

You are an assistant tasked with helping design and build a developer tool called Submerge. Submerge is a Git-inspired CLI tool and prompt compiler that enables modular, reproducible, and explainable code generation using large language models (LLMs).

The user has the following goals and requirements:

### ✅ Core Objectives

- **Centralized workspace**: `.dive/` folder acts like `.git/`, containing all prompt-related data, including:
  - `contracts/`: partial function stubs with docstrings as natural language specs.
  - `prompts/`: prompt variants (base + overlays) to guide generation.
  - `impls/`: generated outputs, organized by prompt variant name.
  - `reasoning.json`: agentic chain-of-thought describing the design process.
  - `response.json`: raw LLM responses, stored for audit/reproducibility.

### Command-line interface (submerge) should support:

- **plan**: show contract-to-prompt mappings.
- **generate**: compile prompt + contract → code + reasoning.
- **apply**: materialize selected implementation into the real project (e.g., `/src/`).
- **diff**: compare implementation variants across prompts.
- **trace**: show reasoning chain for each output.

### Prompt composition:

Prompt files are layered like `kustomize`, composed recursively based on a `kustomization.yaml` or folder conventions.

### File structure symmetry:

All generated implementations preserve original filenames, enabling `git diff` to work naturally. Variants are organized by folder, not filename.

### Human-in-the-loop:

The system does not apply changes automatically. It supports decision checkpoints, critique loops, and manual approvals.

### ⚙️ Example Workflow

1. Define a function in `generation/data_loader.py`:

```python
def load_user_data(path: str) -> pd.DataFrame:
    """Load user data from CSV or JSON and validate schema."""
    pass
```

2. Create prompt variants:

- `.dive/prompts/load_user_data/basic.md`
- `.dive/prompts/load_user_data/with_logging.md`

3. Run:

```bash
submerge generate
```

Submerge creates:

- `.dive/impls/basic/data_loader.py`
- `.dive/impls/basic/reasoning.json`
- `.dive/impls/basic/response.json`

4. You choose and:

```bash
submerge apply .dive/impls/basic/data_loader.py
```

### 🧠 Key Design Principles

- Mimics Git conventions (discovery, versioning, CLI UX)
- Separation of concerns (contracts, prompts, outputs, decisions)
- Supports Copilot and Obsidian workflows
- Allows LLMs to explain their reasoning step-by-step
- Enables semantic comparison of generated options
- Simplifies developer experience: no copy-pasting, no untracked context

### ✨ Bonus

- Future integration: VS Code extension, prompt linting, auto-testing
- Inspired by: Git, Kustomize, Copilot, LangChain (but simpler, more dev-focused)
- Prioritizes minimalism, transparency, reproducibility