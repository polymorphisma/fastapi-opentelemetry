from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.sdk.resources import Resource
# from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.trace.export import ConsoleSpanExporter  # Optional for debugging


SERVICE_NAME = 'fastapi'
OTLP_COLLECTOR_ENDPOINT = "http://localhost:4317"


# Initialize OpenTelemetry Tracer once globally
def initialize_tracer():
    # Create a resource with service information
    resource = Resource.create({"service.name": SERVICE_NAME})

    # Create an OpenTelemetry TracerProvider
    tracer_provider = TracerProvider(resource=resource)

    # Set up OTLP Exporter (send traces to OTLP endpoint, e.g., OpenTelemetry Collector)
    otlp_exporter = OTLPSpanExporter(endpoint=f"{OTLP_COLLECTOR_ENDPOINT}")
    span_processor = BatchSpanProcessor(otlp_exporter)
    tracer_provider.add_span_processor(span_processor)

    # Optional: Set up a console exporter for debugging
    console_processor = BatchSpanProcessor(ConsoleSpanExporter())
    tracer_provider.add_span_processor(console_processor)

    # Set the global TracerProvider so that it's available throughout the application
    trace.set_tracer_provider(tracer_provider)


# Initialize the tracer once when the module is loaded
initialize_tracer()


# Function to get the OpenTelemetry Tracer
def get_tracer():
    return trace.get_tracer(SERVICE_NAME)
