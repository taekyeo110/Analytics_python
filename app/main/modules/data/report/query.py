from google.cloud import bigquery
# from app.main.config.api_config import BIG_QUERY_KEY


# Construct a BigQuery client object.
client = bigquery.Client()

# TODO(developer): Set table_id to the ID of the destination table.
table_id = "lws-cloocus.ustest.ustable"

job_config = bigquery.QueryJobConfig(destination=table_id)

sql = 'SELECT * FROM `bigquery-public-data.covid19_weathersource_com.postal_code_day_history` LIMIT 34230421'

# Start the query, passing in the extra configuration.
query_job = client.query(sql, job_config=job_config)  # Make an API request.
query_job.result()  # Wait for the job to complete.

print("Query results loaded to the table {}".format(table_id))
