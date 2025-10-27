project: 📊 Canvas Discussion Analyzer
author: Abdellah Boudlal
repo: https://github.com/Aboudlal/canvas-discussion-analyzer

overview: |
  This project extracts structured CSV data from Canvas Discussions for Business Intelligence (BI).
  It removes irrelevant text (like "Why does this tool appeal…") and keeps only:
    - 👤 Student name (First + Last initial)
    - 📝 Activity 1, Activity 2, Activity 3
    - 🛠️ Tool you don’t want to learn now
  The output is a clean CSV file ready for analysis with Python (pandas/matplotlib) or Power BI (DAX).

quick_start: |
  # Clone the repo
  git clone https://github.com/Aboudlal/canvas-discussion-analyzer.git
  cd canvas-discussion-analyzer

  # Install dependencies
  pip install -r requirements.txt

  # Run the parser (example)
  python parse_discussion_minimal.py --in discussion.txt --out bi_discussion_submissions.csv

installation:
  prerequisites:
    - Python 3.10 or later
    - Git (optional)
  steps:
    - git clone https://github.com/Aboudlal/canvas-discussion-analyzer.git
    - cd canvas-discussion-analyzer
    - pip install -r requirements.txt

usage:
  step_1_prepare_input: |
    Copy the full Canvas discussion into a plain text file named "discussion.txt".
    Place it in the project root folder.
  step_2_run_parser:
    windows: python parse_discussion_minimal.py --in discussion.txt --out bi_discussion_submissions.csv
    linux: python3 parse_discussion_minimal.py --in discussion.txt --out bi_discussion_submissions.csv
    macos: python3 parse_discussion_minimal.py --in discussion.txt --out bi_discussion_submissions.csv
    note: On Linux/macOS, use `python3` instead of `python` if Python 2 is also installed.
  step_3_open_notebook: |
    jupyter notebook bi_discussion_analysis.ipynb
  step_4_optional_powerbi: |
    Import bi_discussion_submissions.csv into Power BI to create dashboards.
    Example DAX queries are provided inside the notebook and README.

project_structure: |
  canvas-discussion-analyzer/
  ├─ parse_discussion_minimal.py     # parser script
  ├─ bi_discussion_analysis.ipynb    # Jupyter notebook for analysis
  ├─ discussion.txt                  # raw input file
  ├─ bi_discussion_submissions.csv   # clean output CSV
  ├─ requirements.txt                # Python dependencies
  ├─ run.bat                         # one-click run on Windows
  └─ README.yaml                     # documentation

requirements:
  - pandas >= 2.0
  - matplotlib >= 3.7
  - jupyter >= 1.0

example_commands:
  windows: 
  ### python parse_canvas_discussion.py --in discussion.txt --out bi_discussion_submissions.csv
  linux:
  ### python3 parse_canvas_discussion.py --in discussion.txt --out bi_discussion_submissions.csv
  macos: 
  ### python3 parse_canvas_discussion.py --in discussion.txt --out bi_discussion_submissions.csv
  notebook: jupyter notebook bi_discussion_analysis.ipynb













license: |
  MIT License

  Copyright (c) 2025 Abdellah Boudlal

  Permission is hereby granted, free of charge, to any person obtaining a copy
  of this software and associated documentation files (the "Software"), to deal
  in the Software without restriction, including without limitation the rights
  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
  copies of the Software, and to permit persons to whom the Software is
  furnished to do so, subject to the following conditions:

  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
  THE SOFTWARE.
