# FastAPI with OpenTelemetry Integration

This repository demonstrates how to integrate OpenTelemetry into a FastAPI application for basic observability. The setup enables you to collect and export telemetry data, including traces, to an OpenTelemetry Collector for monitoring and debugging.

---

## Features

- **Tracing**: Automatically instrument FastAPI routes to capture incoming requests.
- **Exporters**: Export telemetry data to OpenTelemetry-compatible backends (e.g., Jaeger, Zipkin, cloud platforms).
- **Extensibility**: Easily add metrics and logs to enhance observability.

---

## Prerequisites

Before you begin, ensure you have the following:

- **Python 3.8+**
- **Poetry** for dependency management. [Poetry Documentation](https://python-poetry.org/docs/)

---

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/<username>/fastapi-opentelemetry.git
   cd fastapi-opentelemetry
   ```

2. **Install dependencies**:
   ```bash
   poetry install
   ```

3. **Run the OpenTelemetry Collector**:
   Use Docker to run a local OpenTelemetry Collector instance:
   ```bash
   docker run --name otel-collector -p 4317:4317 -v $(pwd)/otel-config.yaml:/etc/otel/config.yaml otel/opentelemetry-collector --config /etc/otel/config.yaml
   ```

---

## Running the Application

1. **Start the FastAPI app**:
   ```bash
   poetry run uvicorn main:app --host 0.0.0.0 --port 8000 --workers 1
   ```

2. **Test the endpoint**:
   Open your browser or use `curl` to test the application:
   ```bash
   curl http://localhost:8000/
   ```

   You should see:
   ```json
   {"message": "Hello, World!"}
   ```

---

## Implementation Details

### Directory Structure

```
.
├── main.py                 # FastAPI application
├── tracer.py               # OpenTelemetry tracer setup
├── otel-config.yaml        # OpenTelemetry Collector configuration
├── pyproject.toml          # Poetry configuration
└── README.md               # Project documentation
```

### Key Components

- **OpenTelemetry Packages**:
  - `opentelemetry-api`: Core API for OpenTelemetry.
  - `opentelemetry-sdk`: SDK implementation of OpenTelemetry.
  - `opentelemetry-exporter-otlp`: Exporter for sending telemetry data to an OTLP-compatible backend.
  - `opentelemetry-instrumentation-fastapi`: Automatically instruments FastAPI routes.

- **Tracing Initialization**:
  Tracing setup is handled in `tracer.py`, including configuration for:
  - `TracerProvider`: Root of the OpenTelemetry tracing system.
  - `OTLPSpanExporter`: Sends telemetry data to the OpenTelemetry Collector.
  - `ConsoleSpanExporter`: Optional exporter for local debugging.

- **Instrumentation**:
  FastAPI is instrumented using `FastAPIInstrumentor.instrument_app(app)`.

---

## Extending Observability

As your application grows, consider adding:

- **Metrics**: Use `opentelemetry-metrics` to monitor performance metrics like latency, throughput, etc.
- **Logs**: Capture application logs for deeper insights into runtime behavior.

---

## References

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [OpenTelemetry Python Documentation](https://opentelemetry.io/docs/instrumentation/python/)
- [Poetry Documentation](https://python-poetry.org/docs/)
- [Database Migrations with Alembic and FastAPI](https://alembic.sqlalchemy.org/)

---

## Contributing

Feel free to open issues or submit pull requests to improve this project.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Happy Coding! 🚀
