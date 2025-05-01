# Overview

> Human involvement is crucial to be in the loop. There is a desire to move away from quick, boilerplate-heavy code generation towards a more transparent and editable process.

# Dive Design Summary

## Dive Definition and Ambitions

- Dive is defined as a dynamically interactive virtual environment, a system for creating interactive environments that can be manipulated by AI agents.
- It enables the creation of complex dynamic environments for training and testing AI agents.
- Dive is explicitly not like “VIBE” coding experiences.
- It targets technical users frustrated with traditional software development tools.
- The ambition is to prototype a CLI tool called Submerge in Python.
- Submerge aims to slow down and reshape LLM interaction during coding.
- CLI expertise is becoming essential, and Submerge is designed as a CLI-first skill.
- Born from frustration, echoing Linus Torvalds' sentiment with existing tools.
- It enables step-by-step code generation, focusing on reproducibility.
- Encourages human-in-the-loop development over boilerplate-heavy automation.
- Prioritizes code quality and language tracing for transparency.
- It is currently a throwaway experiment to explore ideas.

## Chapter 2: Prompt Prompt Prompt

- Submerge is prototyped in Python.
- If successful, may be rewritten in C, Rust, or Zig.
- A .git-like folder named .dive will be created.
- .dive will track interaction history, defining and traversing a search space.
- Prompts are composable; many may be needed to achieve results.
- Process can be complex or simple depending on traversal.

### Analogies Used:

- RTS games (StarCraft) vs turn-based (chess, Heroes of Might and Magic).
- Graph traversal of all Turing programs.

- Aim to prevent nonsensical AI results when modifying creative prompts.
- Creative thinking is treated as a reproducible prompt sequence.
- Idea: Submerge might compile prompts, generating new versions from old ones.

## Chapter 3: Good Code Generation

- MVP: Submerge can self-generate via templated code.
- Good LLM-based generation requires very specific prompting.
- Proposes a project-specific vocabulary, similar to Agile practices.
- Clarity about files, classes, and structure is vital.
- Goal: Make specifying changes (e.g., fixing a line) easier than manual edits.

### Example:

- Python CLI with Typer for version reporting, debug mode, utilities.
- Logger with verbosity flags (-v, -vv).
- Configuration loaded from config.py.
- Project description stored and sourced from config.

## Chapter 4: Kind Of Config

- Uses a basic setup, not agent-mode or advanced chain-of-thought.
- Intention: make LLM interactions more interactive.
- Logger setup is boilerplate.
- Complains that code completion is bad.
- Goal: Make Python display the app callback.
- Project description is missing (a noted issue).
- Submerge to be installed via Poetry.
- Described as a composable prototype of Dive.
- Should support code completion features.
- Vision for submerge evolving into submerged apply (s and a).

### Additional Folders:

- doc/: documentation
- notes/: markdown-format research notes

- Folder structure = initial prompt, root of a tree.
- Considering using a DAG instead of a tree.

## Chapter 5: Like Prompt Json

- Introduces prompt.json instead of inline Python for prompts.
- Supports a meta-programming approach: Python generates Python.
- Documentation will be Markdown, the standard for LLM interaction.
- Markdown will be queryable and structured in a tree.
- Each tree node = prompt generation or history point.
- Path through deepest leaf determines project output.
- Project files will live outside .dive/.
- Plans to support YAML as a superset for JSON.
- Leverages chain-of-thought reasoning in prompts.
- Each prompt step = a tree traversal interaction.
- Capability to reference parts of the tree like a filesystem.
- Envisions setup like Version control + JIT + Obsidian.
- Possible fallback: store prompts in .py files.

## Chapter 6: Conclusion

- Introduce meta.json and metadata.json.

### metadata.json Includes:

- Active context
- Structured references

- Plan for parameters like a query transformer to:
  - Gather multiple sources
  - Compile to Markdown
  - Feed into LLM

- response.json mirrors LLM responses with:
  - User
  - Content

- Next step: generate *.json files to capture interaction behavior.