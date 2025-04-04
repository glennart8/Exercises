import pandas as pd
import dlt
from pathlib import Path
import os

# used for extracting data from source, in this case a local csv file
@dlt.resource(write_disposition="replace")
def load_csv_resource(file_path: str, **kwargs):
    df = pd.read_csv(file_path, **kwargs)
    yield df


if __name__ == "__main__":
    # Set working directory to the directory where the script is located
    working_directory = Path(__file__).parent  # This will get the directory of the current .py file

    # Construct the path to the CSV file in the data folder
    csv_path = working_directory / "data" / "NetflixOriginals.csv"
    
    # Load the CSV data using the correct encoding
    data = load_csv_resource(csv_path, encoding="latin1")
    print(data)
    
    # Set up the DLT pipeline
    pipeline = dlt.pipeline(
        pipeline_name='movies',
        destination=dlt.destinations.duckdb("movies.duckdb"),
        dataset_name='staging'
    )
    
    # Run the pipeline and load the data into the DuckDB database
    load_info = pipeline.run(data, table_name="netflix")

    # Pretty print the information on data that was loaded
    print(load_info)
