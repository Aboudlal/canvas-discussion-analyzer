project: canvas-discussion-analyzer
author: Abdellah Boudlal
repo: https://github.com/Aboudlal/canvas-discussion-analyzer

overview: >
  This project extracts structured CSV data from Canvas Discussions for Business Intelligence (BI).
  It removes irrelevant text (like "Why does this tool appeal...") and keeps only:
  - student name (normalized as First + Last initial)
  - activity_1, activity_2, activity_3
  - tool_not_now
  The output is a clean CSV, ready for analysis in Python or Power BI.

installation:
  prerequisites:
    - Python 3.10 or later
    - Git (optional, to clone repo)
  steps:
    - clone repo: git clone https://github.com/Aboudlal/canvas-discussion-analyzer.git
    - cd into project: cd canvas-discussion-analyzer
    - install dependencies: pip install -r requirements.txt

usage:
  step_1_prepare_input: >
    Copy the full Canvas discussion into a plain text file named "discussion.txt".
    Place it in the project root folder.
  step_2_run_parser:
    description: >
      Run the parser script to generate a clean CSV.
    windows: |
      python parse_discussion_minimal.py --in discussion.txt --out bi_discussion_submissions.csv
    linux: |
      python3 parse_discussion_minimal.py --in discussion.txt --out bi_discussion_submissions.csv
    macos: |
      python3 parse_discussion_minimal.py --in discussion.txt --out bi_discussion_submissions.csv
    note: >
      On Linux/macOS, use `python3` instead of `python` if both Python 2 and Python 3 are installed.
  step_3_open_notebook:
    description: >
      Explore the CSV with Jupyter Notebook:
    command: |
      jupyter notebook bi_discussion_analysis.ipynb
  step_4_optional_powerbi: >
    Import bi_discussion_submissions.csv into Power BI to create dashboards.
    Example DAX code is provided in the README for counting activities.

files:
  - parse_discussion_minimal.py: main parser script
  - bi_discussion_analysis.ipynb: notebook for data exploration
  - discussion.txt: raw input file (you provide)
  - bi_discussion_submissions.csv: clean output CSV
  - requirements.txt: Python dependencies
  - run.bat: one-click run for Windows
  - README.yaml: project documentation

requirements:
  - pandas >= 2.0
  - matplotlib >= 3.7
  - jupyter >= 1.0

example_commands:
  windows: python parse_discussion_minimal.py --in discussion.txt --out bi_discussion_submissions.csv
  linux: python3 parse_discussion_minimal.py --in discussion.txt --out bi_discussion_submissions.csv
  macos: python3 parse_discussion_minimal.py --in discussion.txt --out bi_discussion_submissions.csv
  notebook: jupyter notebook bi_discussion_analysis.ipynb

license: |
  MIT License (free to use, copy, modify, and share).
  Provided as-is without warranty.
  Copyright (c) 2025 Abdellah Boudlal
