import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions
from apache_beam.options.pipeline_options import SetupOptions
#import config

# A list of strings to output
strings = [
    'Hello, World!',
    'This is a minimalistic Dataflow job',
    'It simply logs these strings',
]

def print_element(element):
  print(element)

# Create a pipeline executing on a direct runner (local machine).
# To change to DataflowRunner, you would change this line.
#pipeline_options = PipelineOptions(runner='DirectRunner')

# Now use the config to set the pipeline options:
"""
pipeline_options = PipelineOptions([
    '--runner=DataflowRunner',
    f'--project={config.project}',
    f'--staging_location={config.staging_location}',
    f'--temp_location={config.temp_location}',
    f'--region={config.region}',
])
"""

pipeline_options = PipelineOptions([
    '--runner=DataflowRunner',
    '--project=sanguine-anthem-393416',
    '--staging_location=gs://gcpsampleall/gcp_python/staging',
    '--temp_location=gs://gcpsampleall/gcp_python/temp',
    '--region=us-central1',
    '--flexrs_goal=COST_OPTIMIZED',  # Add this line
    #'--requirements_file=gs://gcpsampleall/gcp_python/dataflow/jobs/requirements.txt',
])


# Prepare the pipeline
with beam.Pipeline(options=pipeline_options) as p:
    (p | 'Create strings' >> beam.Create(strings)
       | 'Print strings' >> beam.Map(print_element))

print('Done')
