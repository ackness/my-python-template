# Project instructions

## Start here

This repository starts as a Python application / CLI template. Inspect the current
source and configuration before assuming it is still an unused template.
Implement the user's actual project; do not rerun initialization for ordinary changes.

`README.md` is user-facing product documentation and may be rewritten for the actual
application. Keep durable agent guidance here and optional procedures in
`.agents/skills/`. Neither should depend on the template README remaining intact.

## Toolchain and layout

- Use mise for tool installation and task entry points. Use uv for Python discovery,
  `.venv`, dependencies, locking, and builds; avoid a second Python version setting in mise.
- Read tool versions and task definitions from `mise.toml`, the development Python pin
  from `.python-version`, and supported Python versions and dependency requirements from
  `pyproject.toml`. `uv.lock` records resolved project dependencies. Action references and
  update schedules live in `.github/workflows/ci.yml` and `.github/dependabot.yml`.
  Do not treat versions mentioned in prose as current releases.
- Keep Python source under `src/` and tests under `tests/`. Derive the current package
  and CLI names from `pyproject.toml`; do not hardcode the original template name.
- Ruff handles lint and formatting; Pyrefly is the single type checker; pytest runs tests.
  Keep their configuration in `pyproject.toml`; Ruff and pytest caches belong under `.cache/`.
- Add runtime dependencies with `mise exec -- uv add PACKAGE` and development tools
  with `mise exec -- uv add --dev PACKAGE`. Commit the resulting `uv.lock` changes.
- Additional JS/TS, Go, or Rust tools belong in `mise.toml` when the project needs them.
  Add frameworks, services, containers, and extra directories only for actual requirements.

## Commands and validation

For a fresh checkout: `mise trust`, `mise install`, then `mise run setup`.
Use `mise exec -- uv ...` when shell activation is unavailable.

- `mise run run`: run the application.
- `mise run fmt`: apply safe fixes and formatting; `mise run lint`: check without edits.
- `mise run typecheck` / `mise run test`: focused type checks or tests.
- `mise run check`: lockfile, lint, formatting, types, and tests; the shared CI entry point.
- `mise run build`: wheel and source distribution; validate packaging changes with this.
- `mise run upgrade`: intentionally upgrade uv and project dependencies, then check and build.
  For scope and version-selection details, use the maintain-toolchain skill linked below.

Use relevant checks for the change. Documentation-only edits need link and diff review,
not a full application test run. Keep CI and local commands aligned in `mise.toml`.
CI runs setup, check, and build on Windows and Linux for main pushes, pull requests,
and manual dispatch. It does not publish packages or images. Report remote CI as unrun
unless the relevant commit's run was observed; an older green run does not validate new changes.

## Tracked and local files

Keep `AGENTS.md`, `.agents/skills/`, project configuration, and dependency lockfiles tracked.
Preserve `uv.lock` for the `--locked` workflow, and retain other ecosystems' shared
lockfiles when those ecosystems are used. Ignore environments, caches, build outputs,
credentials, and personal editor settings. Keep environment examples free of secrets.
Do not blanket-ignore Go `vendor/` or `go.work`; determine whether they are shared build inputs.

## On-demand skills

- [python-project-bootstrap](.agents/skills/python-project-bootstrap/SKILL.md): turn a
  fresh copy of this template into a concrete project, including renaming and product docs.
- [maintain-toolchain](.agents/skills/maintain-toolchain/SKILL.md): upgrade dependencies,
  Python, mise-managed tools, or GitHub Actions; maintain CI and ignore rules as requested.

Read a skill only when its workflow applies. If skill discovery is unavailable, open
its linked `SKILL.md` directly. Update these instructions and the affected skill when
the project's workflow changes; keep product-specific setup and usage in README.
