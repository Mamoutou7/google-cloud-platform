
import typing

if typing.TYPE_CHECKING:
    from google.cloud import bigquery


def client_query_batch() -> "bigquery.QueryJob":
    # [START bigquery_query_batch]
    from google.cloud import bigquery

    # Construct a BigQuery client object.
    client = bigquery.Client()

    job_config = bigquery.QueryJobConfig(
        # Run at batch priority, which won't count toward concurrent rate limit.
        priority=bigquery.QueryPriority.BATCH
    )

    sql = """
        SELECT corpus
        FROM `bigquery-public-data.samples.shakespeare`
        GROUP BY corpus;
    """

    # Start the query, passing in the extra configuration.
    query_job = client.query(sql, job_config=job_config)  # Make an API request.

    # Check on the progress by getting the job's updated state. Once the state
    # is `DONE`, the results are ready.
    query_job = typing.cast(
        "bigquery.QueryJob",
        client.get_job(
            query_job.job_id, location=query_job.location
        ),  # Make an API request.
    )

    print("Job {} is currently in state {}".format(query_job.job_id, query_job.state))
    # [END bigquery_query_batch]
    return query_job
