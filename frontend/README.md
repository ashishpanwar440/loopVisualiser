# Loop Visualiser - Frontend

React.js frontend for visualizing Python loop execution step by step.

## Setup

### Prerequisites
- Node.js 14+ and npm

### Installation

```bash
npm install
```

### Configuration

Create a `.env` file in the frontend directory:

```
REACT_APP_API_URL=http://localhost:5000
```

### Running the Application

Development mode:
```bash
npm start
```

Build for production:
```bash
npm run build
```

## Project Structure

```
src/
├── components/          # React components
│   ├── CodeEditor/      # Code input component
│   ├── VariableInput/   # Initial variables setter
│   └── Visualizer/      # Step visualization display
├── services/            # API client services
├── types/              # TypeScript type definitions
├── App.tsx             # Main app component
└── index.tsx           # React entry point
```

## Components

### CodeEditor
- Input field for Python code with loops
- Syntax highlighting support
- Example code templates

### VariableInput
- Add initial variable values
- Supports various types: numbers, strings, lists, dicts
- Remove variables functionality

### Visualizer
- Display current step information
- Show variable states as cards
- Navigation controls (Previous/Next)
- Progress indicator
- Step counter

## API Integration

The frontend communicates with the backend via:
- **Endpoint**: `POST /api/visualize`
- **Request**: 
  ```json
  {
    "code": "Python code string",
    "variables": { "var_name": value }
  }
  ```
- **Response**: 
  ```json
  {
    "snapshots": [
      {
        "step": 1,
        "variables": { ... },
        "iterationInfo": "Iteration 1"
      }
    ],
    "executionTime": 0.123
  }
  ```

## Features

- 🎨 Beautiful gradient UI
- 📱 Responsive design
- ⚡ Real-time variable tracking
- 🔄 Step-by-step navigation
- 📊 Visual state representation