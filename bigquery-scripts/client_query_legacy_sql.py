def client_query_legacy_sql() -> None:
    # [START bigquery_query_legacy]
    from google.cloud import bigquery

    # Construct a BigQuery client object.
    client = bigquery.Client()

    query = (
        "SELECT name FROM [bigquery-public-data:usa_names.usa_1910_2013] "
        'WHERE state = "TX" '
        "LIMIT 100"
    )

    # Set use_legacy_sql to True to use legacy SQL syntax.
    job_config = bigquery.QueryJobConfig(use_legacy_sql=True)

    # Start the query, passing in the extra configuration.
    query_job = client.query(query, job_config=job_config)  # Make an API request.

    print("The query data:")
    for row in query_job:
        print(row)
    # [END bigquery_query_legacy]
