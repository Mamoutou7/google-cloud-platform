def client_query_destination_table_clustered(table_id: str) -> None:
    # [START bigquery_query_clustered_table]
    from google.cloud import bigquery

    # Construct a BigQuery client object.
    client = bigquery.Client()

    # TODO(developer): Set table_id to the ID of the destination table.
    # table_id = "your-project.your_dataset.your_table_name"

    sql = "SELECT * FROM `bigquery-public-data.samples.shakespeare`"
    cluster_fields = ["corpus"]

    job_config = bigquery.QueryJobConfig(
        clustering_fields=cluster_fields, destination=table_id
    )

    # Start the query, passing in the extra configuration.
    query_job = client.query(sql, job_config=job_config)  # Make an API request.
    query_job.result()  # Wait for the job to complete.

    table = client.get_table(table_id)  # Make an API request.
    if table.clustering_fields == cluster_fields:
        print(
            "The destination table is written using the cluster_fields configuration."
        )
    # [END bigquery_query_clustered_table]
