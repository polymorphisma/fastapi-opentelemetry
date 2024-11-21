from fastapi import FastAPI
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from tracer import initialize_tracer

# Initialize the tracer
initialize_tracer()

app = FastAPI()

# Instrument FastAPI with OpenTelemetry
FastAPIInstrumentor.instrument_app(app)


@app.get("/")
def read_root():
    return {"Hello": "World"}
