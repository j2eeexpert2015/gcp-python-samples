import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions, StandardOptions
import argparse

# A list of strings to output
strings = [
    'Hello, World!',
    'This is a minimalistic Dataflow job',
    'It simply logs these strings',
]

def print_element(element):
  print(element)


parser = argparse.ArgumentParser()
path_args, pipeline_args = parser.parse_known_args()
pipeline_options = PipelineOptions(pipeline_args)

# Prepare the pipeline
with beam.Pipeline(options=pipeline_options) as p:
    (p | 'Create strings' >> beam.Create(strings)
       | 'Print strings' >> beam.Map(print_element))

print('Done')
