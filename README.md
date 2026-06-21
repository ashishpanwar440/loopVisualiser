# Loop Visualiser

A web application for visualizing Python loops step-by-step to aid learning and understanding of loop execution.

## Features

- **Code Input Interface**: Write small Python code snippets with loops
- **Variable Initialization**: Set initial values for variables before execution
- **Step-by-Step Visualization**: Watch each iteration of loops with state changes
- **Multiple Visualizations**: Generate 5-10 snapshots showing loop progression
- **Educational Focus**: Clear, easy-to-understand visualization of loop mechanics

## Tech Stack

- **Frontend**: React.js with TypeScript
- **Backend**: Python with Flask
- **Visualization**: Interactive state snapshots with variable tracking
- **Code Execution**: Secure Python code analysis and execution

## Project Structure

```
loopVisualiser/
├── frontend/              # React.js application
│   ├── src/
│   │   ├── components/   # Reusable UI components
│   │   ├── pages/        # Page components
│   │   ├── services/     # API communication
│   │   └── types/        # TypeScript types
│   └── package.json
├── backend/              # Flask Python server
│   ├── app.py
│   ├── analyzer.py       # Loop analysis & execution
│   ├── requirements.txt
│   └── utils/
└── README.md
```

## Getting Started

### Frontend Setup
```bash
cd frontend
npm install
npm start
```

### Backend Setup
```bash
cd backend
pip install -r requirements.txt
python app.py
```

## How It Works

1. User writes Python code with a loop
2. User defines initial variable values
3. Backend analyzes and executes code step-by-step
4. Each loop iteration is captured as a state snapshot
5. Frontend displays interactive visualization of each step

## Usage Example

**Input Code:**
```python
for i in range(3):
    x = i * 2
    print(x)
```

**Initial Variables:** None required

**Output:** 3 visualization snapshots showing how `i` and `x` change in each iteration

---

For detailed documentation, see the respective README files in `frontend/` and `backend/` directories.