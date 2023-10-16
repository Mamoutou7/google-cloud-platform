def client_load_partitioned_table(table_id: str) -> None:
    # [START bigquery_load_table_partitioned]
    from google.cloud import bigquery

    # Construct a BigQuery client object.
    client = bigquery.Client()

    # TODO(developer): Set table_id to the ID of the table to create.
    # table_id = "your-project.your_dataset.your_table_name"

    job_config = bigquery.LoadJobConfig(
        schema=[
            bigquery.SchemaField("name", "STRING"),
            bigquery.SchemaField("post_abbr", "STRING"),
            bigquery.SchemaField("date", "DATE"),
        ],
        skip_leading_rows=1,
        time_partitioning=bigquery.TimePartitioning(
            type_=bigquery.TimePartitioningType.DAY,
            field="date",  # Name of the column to use for partitioning.
            expiration_ms=7776000000,  # 90 days.
        ),
    )
    uri = "gs://cloud-samples-data/bigquery/us-states/us-states-by-date.csv"

    load_job = client.load_table_from_uri(
        uri, table_id, job_config=job_config
    )  # Make an API request.

    load_job.result()  # Wait for the job to complete.

    table = client.get_table(table_id)
    print("Loaded {} rows to table {}".format(table.num_rows, table_id))
    # [END bigquery_load_table_partitioned]
