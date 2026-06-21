# Loop Visualiser - Backend

Flask-based Python server for analyzing and visualizing Python loop execution.

## Setup

### Prerequisites
- Python 3.8+
- pip

### Installation

```bash
pip install -r requirements.txt
```

### Configuration

Create a `.env` file in the backend directory:

```
FLASK_ENV=development
PORT=5000
DEBUG=true
```

### Running the Server

```bash
python app.py
```

The server will start on `http://localhost:5000`

## API Endpoints

### Health Check
```
GET /health
```

Response: `{ "status": "healthy", "service": "loop-visualiser" }`

### Visualize Loop
```
POST /api/visualize
```

**Request Body:**
```json
{
  "code": "for i in range(3):\n    x = i * 2",
  "variables": {
    "initial_var": 100
  }
}
```

**Response:**
```json
{
  "snapshots": [
    {
      "step": 1,
      "variables": {
        "i": 0,
        "x": 0
      },
      "iterationInfo": "Iteration 1"
    },
    {
      "step": 2,
      "variables": {
        "i": 1,
        "x": 2
      },
      "iterationInfo": "Iteration 2"
    }
  ],
  "executionTime": 0.123
}
```

### Validate Code
```
POST /api/validate
```

**Request Body:**
```json
{
  "code": "for i in range(3):\n    print(i)"
}
```

**Response:**
```json
{
  "valid": true,
  "error": null
}
```

## Project Structure

```
backend/
├── app.py              # Flask application
├── analyzer.py         # Loop analysis logic
├── utils/
│   ├── __init__.py
│   ├── executor.py     # Code execution engine
│   └── tracker.py      # Variable tracking
├── requirements.txt    # Python dependencies
└── README.md
```

## Features

### Execution Engine (`executor.py`)
- Safely executes Python code with tracing
- Captures variable states at each iteration
- Prevents infinite loops with iteration limits
- Serializes complex data types for JSON response

### Loop Analysis (`analyzer.py`)
- Detects loops in Python code
- Analyzes code structure using AST
- Generates visualization snapshots
- Handles errors gracefully

### Variable Tracking (`tracker.py`)
- Maintains history of variable changes
- Tracks variable values across iterations
- Provides variable change detection
- Supports querying specific variable history

## Safety & Limitations

- **Max Iterations**: 10 (configurable)
- **Max Snapshots**: 10 (for performance)
- **Restricted Builtins**: Only allows safe builtins
- **Timeout**: Implement timeout for long-running code

## Error Handling

The server returns appropriate HTTP status codes:
- `200` - Success
- `400` - Bad request (syntax error, missing fields)
- `404` - Endpoint not found
- `500` - Internal server error

## Future Improvements

- [ ] WebSocket support for real-time tracing
- [ ] Support for multiple loops and nested loops
- [ ] Advanced filtering and data structure visualization
- [ ] Performance profiling integration
- [ ] Breakpoint support