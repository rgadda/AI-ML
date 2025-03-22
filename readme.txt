AI-ML-Course/
├── README.md              # Overview of the repo and instructions
├── .gitignore             # Ignore Python caches, datasets, etc.
├── requirements.txt       # List of Python dependencies (e.g., numpy, pandas)
├── data/                  # Store datasets (if small; otherwise, link to external storage)
│   ├── raw/               # Unprocessed data
│   └── processed/         # Cleaned data
├── notebooks/             # Jupyter notebooks for exploration
│   ├── assignment1.ipynb  # Assignment 1 work
│   └── exploration.ipynb  # Scratch work
├── src/                   # Python source code (modular scripts)
│   ├── __init__.py        # Make it a package
│   ├── preprocessing.py   # Data cleaning functions
│   ├── models.py          # Model definitions
│   └── utils.py           # Helper functions
├── assignments/           # Organized by assignment
│   ├── assignment1/       # Assignment 1 folder
│   │   ├── main.py        # Main script
│   │   └── report.md      # Write-up or notes
│   └── assignment2/       # Assignment 2 folder
└── tests/                 # Unit tests (optional, if required)
    └── test_preprocessing.py