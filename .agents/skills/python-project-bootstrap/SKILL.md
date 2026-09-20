---
name: python-project-bootstrap
description: Turn a fresh copy of this repository's Python template into a concrete application or CLI, including package naming, implementation, documentation, and validation. Use for starting or adopting the template, not routine feature edits or maintenance of the template itself.
---

# Bootstrap a Python project

Use the durable conventions in [AGENTS.md](../../../AGENTS.md). This skill must still
work after README has been replaced. All command paths below are relative to the project root.

## Establish the project

Read the requested outcome and the current source, `pyproject.toml`, `mise.toml`,
`.python-version`, and `.github/workflows/ci.yml`. Check Git status before editing.
Determine whether this is a fresh template or an existing application; preserve existing
behavior and user changes in the latter. Ask only for missing product choices that block
implementation, such as an unspecified purpose. Do not invent a product from the template.

## Adapt the skeleton

- Derive the distribution name, import package, and CLI command from the requested project.
  If a rename is needed, inspect the actual names and references rather than assuming
  the original template names still exist.
- Update project metadata, the `src/` package directory, imports, `[project.scripts]`,
  `__main__.py`, the mise run task, CLI tests, and any Ruff per-file rule naming an entry file.
  Search the tracked source and configuration for old identifiers after renaming; avoid
  blind replacements in lockfiles, caches, or unrelated text.
- Keep the distribution name and module name compatible with `uv_build`'s default mapping,
  or explicitly configure the backend for a justified different layout.
- Replace the greeting example with the requested behavior and meaningful tests.
  CLI entry functions should return `None` or an integer exit code, not a message string.
- Add only dependencies and other languages required by the user. Do not provision Docker,
  cloud resources, package publishing, or external repositories just because this is a new project.

## Make the project usable

Rewrite README for the actual product: purpose, installation, configuration, commands,
and examples. Add a secret-free environment example only if configuration is needed.
Retain this skill and AGENTS unless the user wants a different agent workflow; update any
instructions made inaccurate by the implementation. Avoid copying template maintenance
instructions into the product README.

For metadata or dependency changes, regenerate the lock with `mise exec -- uv lock`,
then run `mise run setup`, `mise run check`, and `mise run build` as relevant to the new project.
Exercise the actual entry point and its failure behavior. If packaging or CLI wiring changed,
install the built wheel in an isolated environment and run its command outside the checkout.
Resolve the wheel filename and command from build output and metadata, not fixed version strings.

Report the implemented behavior, how to run it, observed checks, and any concrete remaining
requirements. Local validation does not establish that GitHub Actions has run.
