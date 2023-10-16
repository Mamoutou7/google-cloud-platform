def client_query_add_column(table_id: str) -> None:
    # [START bigquery_add_column_query_append]
    from google.cloud import bigquery

    # Construct a BigQuery client object.
    client = bigquery.Client()

    # TODO(developer): Set table_id to the ID of the destination table.
    # table_id = "your-project.your_dataset.your_table_name"

    # Retrieves the destination table and checks the length of the schema.
    table = client.get_table(table_id)  # Make an API request.
    print("Table {} contains {} columns".format(table_id, len(table.schema)))

    # Configures the query to append the results to a destination table,
    # allowing field addition.
    job_config = bigquery.QueryJobConfig(
        destination=table_id,
        schema_update_options=[bigquery.SchemaUpdateOption.ALLOW_FIELD_ADDITION],
        write_disposition=bigquery.WriteDisposition.WRITE_APPEND,
    )

    # Start the query, passing in the extra configuration.
    query_job = client.query(
        # In this example, the existing table contains only the 'full_name' and
        # 'age' columns, while the results of this query will contain an
        # additional 'favorite_color' column.
        'SELECT "Timmy" as full_name, 85 as age, "Blue" as favorite_color;',
        job_config=job_config,
    )  # Make an API request.
    query_job.result()  # Wait for the job to complete.

    # Checks the updated length of the schema.
    table = client.get_table(table_id)  # Make an API request.
    print("Table {} now contains {} columns".format(table_id, len(table.schema)))
    # [END bigquery_add_column_query_append]
