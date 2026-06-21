"""
Loop Visualiser Backend
Flask server for analyzing and visualizing Python loops
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
from analyzer import LoopAnalyzer
import os
from dotenv import load_dotenv
import traceback

load_dotenv()

app = Flask(__name__)
CORS(app)

# Configuration
DEBUG = os.getenv('FLASK_ENV') == 'development'
PORT = int(os.getenv('PORT', 5000))


@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({'status': 'healthy', 'service': 'loop-visualiser'}), 200


@app.route('/api/visualize', methods=['POST'])
def visualize():
    """
    Visualize Python loop execution
    
    Request body:
    {
        "code": "Python code string",
        "variables": {"var_name": value, ...}
    }
    
    Response:
    {
        "snapshots": [
            {
                "step": 1,
                "variables": {...},
                "iterationInfo": "Iteration 1",
                "loopVar": "i",
                "loopVarValue": 0
            },
            ...
        ],
        "executionTime": 0.123
    }
    """
    try:
        data = request.get_json()
        
        if not data or 'code' not in data:
            return jsonify({'error': 'Missing required field: code'}), 400
        
        code = data['code']
        initial_variables = data.get('variables', {})
        
        # Analyze and visualize the loop
        analyzer = LoopAnalyzer()
        snapshots, execution_time = analyzer.analyze(code, initial_variables)
        
        if not snapshots:
            return jsonify({
                'error': 'No loop found or code could not be analyzed',
                'snapshots': [],
                'executionTime': execution_time
            }), 400
        
        return jsonify({
            'snapshots': snapshots,
            'executionTime': execution_time
        }), 200
        
    except SyntaxError as e:
        return jsonify({
            'error': f'Syntax error in code: {str(e)}'
        }), 400
    except Exception as e:
        print(f"Error during visualization: {traceback.format_exc()}")
        return jsonify({
            'error': f'Failed to visualize loop: {str(e)}'
        }), 500


@app.route('/api/validate', methods=['POST'])
def validate_code():
    """
    Validate Python code for syntax errors
    
    Request body:
    {
        "code": "Python code string"
    }
    """
    try:
        data = request.get_json()
        code = data.get('code', '')
        
        compile(code, '<string>', 'exec')
        return jsonify({'valid': True, 'error': None}), 200
        
    except SyntaxError as e:
        return jsonify({
            'valid': False,
            'error': f'Syntax error: {str(e)}'
        }), 400


@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Endpoint not found'}), 404


@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Internal server error'}), 500


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=PORT,
        debug=DEBUG
    )