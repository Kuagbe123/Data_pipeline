# Data_pipeline

# Data Ingestion Pipeline with Faker and MySQL( odotobri rural bank)

This repository contains a Python script to generate synthetic data using the Faker library and ingest it into a MySQL database. Additionally, it provides SQL queries to analyze the generated data and a diagram illustrating the pipeline.

## Table of Contents

- [Introduction](#introduction)
- [Requirements](#requirements)
- [Setup](#setup)
- [Usage](#usage)
- [Queries](#queries)
- [Pipeline Diagram](#pipeline-diagram)
- [Contributing](#contributing)
- [License](#license)

## Introduction

In this project, we leverage the Faker library to generate synthetic data representing demographics, transaction activity, customer preferences, and communication methods. This data is then ingested into a MySQL database using a Python script. Furthermore, SQL queries are provided to analyze the generated data.

## Requirements

To run the script and execute SQL queries, you need the following:

- Python 3.x
- MySQL server
- Required Python packages (`faker`, `mysql-connector-python`)

## Setup

1. **Clone the Repository**: 
   ```
   git clone https://github.com/yourusername/your-repository.git
   ```
   Replace `yourusername` with your GitHub username and `your-repository` with the name of your repository.

2. **Install Dependencies**: 
   ```bash
   pip install faker mysql-connector-python
   ```

3. **Database Setup**: 
   - Install MySQL server if not already installed.
   - Create a new database (e.g., `bank_data`) in MySQL.
   - Update the database connection details in the Python script (`ingest_data.py`).

## Usage

1. **Generate and Ingest Data**:
   - Open `ingest_data.py` in a text editor.
   - Adjust the number of records to be generated and the database connection details.
   - Run the script to generate and ingest data into the MySQL database:
     ```bash
     python ingest_data.py
     ```

2. **Execute Queries**:
   - Use a MySQL client or command-line interface to connect to your database.
   - Execute SQL queries from the provided file (`queries.sql`) to analyze the data.

## Queries

Ten example queries are provided in the `queries.sql` file. These queries cover various aspects of the generated data, such as counting records, finding customers with specific preferences, calculating averages, and more.

## Pipeline Diagram

A diagram illustrating the data ingestion pipeline is provided in the repository. It shows the flow of data from generation with Faker to ingestion into the MySQL database.

## Contributing

Contributions are welcome! If you have any suggestions, improvements, or additional features to propose, feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

---

