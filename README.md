# Data Cleaning Projects with Pandas

This repository contains a collection of Jupyter notebooks showcasing various data cleaning and dataset creation projects using Pandas and various Python libraries built for web scraping.

## Table of Contents

### Data Analysis Projects

-   [Project 1: Roller Coaster Data](https://github.com/benkaan001/pandas_and_beyond/blob/main/analyze_data/00_rollercoaster.ipynb)
-   [Project 2: FredAPI Unemployment Data](https://github.com/benkaan001/pandas_and_beyond/blob/main/analyze_data/01_unemployment.ipynb)
-   [Project 3: Social Security Registered Names Data](https://github.com/benkaan001/pandas_and_beyond/blob/main/analyze_data/02_registered_names.ipynb)
-   [Project 4: IMF Exchange Rate Data](https://github.com/benkaan001/pandas_and_beyond/blob/main/analyze_data/03_exchange_rates.ipynb)
-   [Project 5: Standford Open Policing Project](https://github.com/benkaan001/pandas_and_beyond/blob/main/analyze_data/04_standford_open_policing_project.ipynb)
-   [Project 6: TED Talks Dataset](https://github.com/benkaan001/pandas_and_beyond/blob/main/analyze_data/05_ted_talks.ipynb)

### Dataset Creation Projects
-   [Project 1: 100 Meter Olympics Dataset using readHtml](https://github.com/benkaan001/pandas_and_beyond/blob/main/generate_data/00_read_html.ipynb)
- [Project 2: ChatGPT Twitter Dataset using snscrape ](https://github.com/benkaan001/pandas_and_beyond/blob/main/generate_data/01_twitter.ipynb)
- [Project 3: Social Security Registered Names using wget](https://github.com/benkaan001/pandas_and_beyond/blob/main/generate_data/02_create_dataset_using_wget_dict.ipynb)
- [Project 4: IMF Exchange Rates Dataset using readHtml](https://github.com/benkaan001/pandas_and_beyond/blob/main/generate_data/03_exchange_rates.ipynb)


## File Organization
```
pandas_and_beyond/
├── analyze_data/
│   ├── __init__.py
│   ├── 00_project.ipynb
│   ├── 01_project.py
│   ├── ...
├── data/
│   ├── __init__.py
│   ├── external/
│   │   ├── external_data.csv
│   │   └── ...
│   └── generated/
│       ├── raw/
│       │   ├── raw_data.csv
│       │   └── ...
│       ├── cleaned/
│       │   ├── cleaned_data.csv
│       │   └── ...
│       └── ...
├── generate_data/
│   ├── __init__.py
│   ├── 00_create_dataset.ipynb
│   ├── 01_web_scrape.ipynb
│   ├── ...
│   └── using_csv/
│       ├── __init__.py
│       ├── 00_read_csv.ipynb
│       ├── ...
│       └── ...
├── helper/
│   ├── __init__.py
│   ├── helper_function.ipynb
│   ├── helper_module.py
│   └── ...
└── tests/
    ├── __init__.py
    ├── test_.py
    └── ...

```


## Requirements

-   Python 3.6 or higher
-   Pandas 1.0 or higher
-   Jupyter Notebook

## Getting Started

To get started with this repository, you will need to clone or download it to your local machine. Once you have done so, you can navigate to analyze data directory and open the corresponding Jupyter notebook.

## Contributing

This repository is a part of my continuous learning journey, which has been inspired by the valuable contributions made by various members of the Kaggle community. If you have a data cleaning project that you have implemented using Pandas and would like to contribute to this repository, please create a new branch and submit a pull request. Your contributions are highly appreciated and will help other learners who are looking to enhance their data cleaning skills using Pandas.