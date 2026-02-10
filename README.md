# Litestar Test

A starter repository for the [Litestar](https://litestar.dev/) ASGI framework - a modern, high-performance Python web framework.

## Features

- ✨ Modern async Python web framework
- 🚀 Fast and type-safe API development
- 📝 Automatic OpenAPI documentation
- 🧪 Comprehensive test suite with pytest
- 🐳 Docker support for easy deployment
- 🔧 Development tools (Black, Ruff)

## Project Structure

```
litestarTest/
├── app/
│   ├── __init__.py
│   ├── main.py              # Main application entry point
│   ├── controllers/         # API route handlers
│   │   ├── __init__.py
│   │   ├── health.py       # Health check endpoints
│   │   └── items.py        # Item CRUD endpoints
│   └── models/             # Data models
│       ├── __init__.py
│       └── item.py         # Item model
├── tests/                  # Test suite
│   ├── __init__.py
│   ├── test_main.py
│   └── test_items.py
├── .env.example           # Environment variables template
├── Dockerfile             # Docker configuration
├── docker-compose.yml     # Docker Compose configuration
├── pyproject.toml         # Project configuration
├── requirements.txt       # Production dependencies
└── requirements-dev.txt   # Development dependencies
```

## Getting Started

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- (Optional) Docker and Docker Compose

### Installation

1. Clone the repository:
```bash
git clone https://github.com/Aleks901/litestarTest.git
cd litestarTest
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. (Optional) Install development dependencies:
```bash
pip install -r requirements-dev.txt
```

5. Copy the environment file:
```bash
cp .env.example .env
```

### Running the Application

#### Using Python directly:

```bash
uvicorn app.main:app --reload
```

The application will be available at `http://localhost:8000`

#### Using Docker:

```bash
docker-compose up
```

### API Documentation

Once the application is running, you can access:
- Interactive API documentation (Swagger UI): `http://localhost:8000/schema/swagger`
- Alternative API documentation (ReDoc): `http://localhost:8000/schema/redoc`
- OpenAPI schema: `http://localhost:8000/schema/openapi.json`

## API Endpoints

### Root
- `GET /` - Welcome message

### Health Check
- `GET /health` - Check application health status

### Items (CRUD)
- `GET /items` - List all items
- `GET /items/{item_id}` - Get a specific item
- `POST /items` - Create a new item
- `PUT /items/{item_id}` - Update an item
- `DELETE /items/{item_id}` - Delete an item

## Running Tests

Run the test suite:
```bash
pytest
```

Run tests with coverage:
```bash
pytest --cov=app
```

## Development

### Code Formatting

Format code with Black:
```bash
black .
```

### Linting

Lint code with Ruff:
```bash
ruff check .
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Resources

- [Litestar Documentation](https://docs.litestar.dev/)
- [Litestar GitHub](https://github.com/litestar-org/litestar)
- [ASGI Specification](https://asgi.readthedocs.io/)

## License

This project is a starter template and can be used freely for any purpose.
