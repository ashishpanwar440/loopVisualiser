# Contributing to Loop Visualiser

We love your input! We want to make contributing to Loop Visualiser as easy and transparent as possible.

## Development Setup

### Frontend Development
```bash
cd frontend
npm install
npm start
```

### Backend Development
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

### Full Stack with Docker
```bash
docker-compose up
```

## Making Changes

1. Create a new branch for your feature
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. Make your changes and commit with clear messages
   ```bash
   git commit -m "Add feature: description"
   ```

3. Push to your branch
   ```bash
   git push origin feature/your-feature-name
   ```

4. Open a Pull Request

## Code Style

### Frontend (React/TypeScript)
- Use functional components
- Follow React best practices
- Add TypeScript types for props
- Keep components focused and reusable

### Backend (Python)
- Follow PEP 8 style guidelines
- Use type hints where applicable
- Write docstrings for functions and classes
- Keep functions small and focused

## Testing

Before submitting a PR, please test your changes:

### Frontend
```bash
cd frontend
npm test
```

### Backend
```bash
cd backend
# Add test files and run with pytest
pytest
```

## Reporting Issues

- Use clear and descriptive titles
- Describe the current behavior and expected behavior
- Provide code examples or screenshots
- Include your environment details

## Feature Requests

- Describe the use case and why this feature would be useful
- Provide example code if applicable
- Discuss alternatives you've considered

## Pull Request Process

1. Update documentation if needed
2. Add or update tests as appropriate
3. Ensure all tests pass
4. Update CHANGELOG if applicable
5. Wait for review and feedback

## License

By contributing, you agree that your contributions will be licensed under the same license as the project.