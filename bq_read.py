import apache_beam as beam
from apache_beam.io.gcp.bigquery import ReadFromBigQuery
from apache_beam.options.pipeline_options import PipelineOptions, GoogleCloudOptions
import os
from apache_beam.options.pipeline_options import PipelineOptions, StandardOptions
import argparse

class PrintFn(beam.DoFn):
    def process(self, element):
        print(element)

if __name__ == "__main__":
    print("@@@@@@@@@@ BQReadDataflow main started @@@@@@@@@@")

    # Set up PipelineOptions
    pipeline_options = PipelineOptions()
    google_cloud_options = pipeline_options.view_as(GoogleCloudOptions)
    google_cloud_options.project = os.environ['PROJECT_ID']
    google_cloud_options.temp_location = f"gs://{os.environ['DATAFLOW_GCS_BUCKET_NAME']}/{os.environ['DATAFLOW_TEMP_FOLDER']}"
    pipeline_options.view_as(StandardOptions).runner = 'DataflowRunner'  # Set runner to DataflowRunner

    with beam.Pipeline(options=pipeline_options) as p:
        rows = (
            p
            | "ReadFromBigQuery" >> ReadFromBigQuery(
                query=f"SELECT * FROM `{os.environ['PROJECT_ID']}.{os.environ['DATASET_ID']}.{os.environ['GBQ_SOURCE_TABLE_NAME']}`",
                use_standard_sql=True
            )
            | "Print" >> beam.ParDo(PrintFn())
        )
