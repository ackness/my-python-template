---
name: maintain-toolchain
description: Maintain this repository's mise and uv toolchain, Python dependencies, GitHub Actions, and cross-language ignore rules. Use for requested upgrades or concrete tooling and CI fixes; do not upgrade dependencies during unrelated feature work.
---

# Maintain the project toolchain

Read [AGENTS.md](../../../AGENTS.md) and the current configuration before changing it.
Treat configuration and lockfiles as authoritative, not historical README version lists.
Commands below run from the project root.

## Choose the requested scope

- **uv and Python dependencies:** `mise run upgrade` upgrades uv, refreshes `uv.lock`,
  syncs the environment, and runs checks and builds. It does not update mise itself,
  the Python pin, build-backend requirement bounds, or Action versions. For one package,
  use `mise exec -- uv lock --upgrade-package PACKAGE` instead of refreshing everything.
- **Python:** use the current uv to inspect `uv python list --only-downloads`; choose a
  stable release unless previews were requested. Update `.python-version` with
  `mise exec -- uv python pin VERSION`. Review `requires-python` separately as the supported
  range, then sync and validate. Existing applications may need to preserve their older
  minimum supported version instead of raising it to the developer interpreter version.
- **mise itself:** follow its actual installation method (`mise self-update` or the owning
  package manager) only when included in the requested scope. For JS/TS, Go, or Rust,
  manage required tool versions in `mise.toml`; preserve that ecosystem's own dependency manager.
- **Build backend:** check the current `uv_build` release and compatibility policy before
  changing `[build-system]`. Keep a compatible upper bound. `uv.lock` does not pin isolated
  build requirements, so validate builds after changing them.
- **GitHub Actions:** query each used action's official repository for the latest suitable
  release; inspect breaking changes and runner requirements. Update the workflow and review
  `.github/dependabot.yml`. Keep an explicit tag or commit reference; `version: latest` on
  mise-action selects mise, not the version of the Action itself.

For a request for "latest", verify current releases from official registries and upstream
release pages. Do not promote a prerelease or switch type checkers silently. Routine locked
installs should continue to use `uv.lock`; upgrades are intentional changes to review and commit.

## CI, ignores, and validation

Keep local tasks and CI aligned through `mise.toml`. Maintain the existing OS matrix unless
the requested change requires a different support policy. Validate changed workflow syntax
with an available workflow validator; do not claim a remote run from static validation.

For ignore-rule changes, distinguish disposable outputs from shared build inputs.
Ignore generated environments, dependency caches, build artifacts, and local credentials;
retain shared lockfiles and secret-free configuration examples. Go's module cache is usually
outside the repository, while `vendor/` and `go.work` can be intentional project inputs.
Use `git check-ignore --no-index` with representative ignored and retained paths. Check tracked
files separately, since adding an ignore rule does not untrack an existing file.

Run `mise run check` for dependency or tooling changes and `mise run build` for packaging
changes or broad upgrades. Inspect lockfile and source changes for unintended package removals,
new registries, and machine-local paths. Update AGENTS or this skill if the workflow changed;
update product documentation only where its actual instructions became inaccurate.
