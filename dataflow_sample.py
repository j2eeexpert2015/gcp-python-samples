import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions

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
pipeline_options = PipelineOptions([
    '--runner=DataflowRunner',
    '--project=sanguine-anthem-393416',
    '--staging_location=gs://gcpsampleall/gcp_python/staging',
    '--temp_location=gs://gcpsampleall/gcp_python/temp',
    '--region=us-central1'
])

# Prepare the pipeline
with beam.Pipeline(options=pipeline_options) as p:
    (p | 'Create strings' >> beam.Create(strings)
       | 'Print strings' >> beam.Map(print_element))

print('Done')
