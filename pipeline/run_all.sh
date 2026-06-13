#!/usr/bin/env bash
# Run the deterministic pipeline (acquire + digest) for many subjects, unattended.
# This is PLAIN PYTHON — no Claude / no LLM / no tokens. Just run it in a terminal.
#
#   ./run_all.sh                 # run the default subject list below
#   ./run_all.sh history biology # run a specific list
#   nohup ./run_all.sh &         # detach and let it run in the background
#
# Logs go to _data/reports/run-<subject>.log so you can check progress without watching.
set -euo pipefail
cd "$(dirname "$0")"

SUBJECTS=("${@:-history}")
[ $# -eq 0 ] && SUBJECTS=(history english biology business geography maths chemistry pe)

mkdir -p _data/reports
for subj in "${SUBJECTS[@]}"; do
  echo "=== $subj  ($(date '+%H:%M:%S')) ==="
  # --headful off by default so it runs without a visible browser
  python run.py "$subj" 2>&1 | tee "_data/reports/run-$subj.log"
  echo
done
echo "All done. Digests in _data/digest/, manifests + logs in _data/reports/."
