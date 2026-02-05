#!/usr/bin/env bash
set -euo pipefail

pyinstaller --onefile --name book_builder_gui gui_app.py
