import argparse
import sys
import logging

import apache_beam as beam
from apache_beam.io import ReadFromText
from apache_beam.io import WriteToText
from apache_beam.options.pipeline_options import PipelineOptions
from apache_beam.options.pipeline_options import SetupOptions

logging.getLogger().setLevel(logging.INFO)

class CSVWrapper(beam.DoFn):
    def process(self, element):
        terms = element.split('\t')
        conv = []
        for term in terms:
            if ',' in term:
                conv.append('"' + term + '"')
        return ','.join(conv)

parser = argparse.ArgumentParser()
parser.add_argument('--input', dest='input', help='input file')
parser.add_argument('--output', dest='output', help='output-file')
known_args, pipeline_args = parser.parse_known_args(sys.argv)

pipeline_opts = PipelineOptions(pipeline_args)
pipeline_opts.view_as(SetupOptions).save_main_session = True
p = beam.Pipeline(options=pipeline_opts)

lines = p | 'read' >> ReadFromText(known_args.input)
lines = lines | beam.ParDo(CSVWrapper())
lines | 'write' >> WriteToText(known_args.output)

result = p.run()
result.wait_until_finish()