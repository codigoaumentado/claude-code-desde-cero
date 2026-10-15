#!/usr/bin/env bash
# Hook PostToolUse: formatea con ruff cada archivo .py que Claude edita o crea.
# Claude Code envía por stdin un JSON con tool_input.file_path.
raiz="$(cd "$(dirname "$0")/../.." && pwd)"
archivo=$(jq -r '.tool_input.file_path // empty')

if [[ "$archivo" == *.py ]]; then
  "$raiz/.venv/bin/ruff" format --quiet "$archivo"
fi
