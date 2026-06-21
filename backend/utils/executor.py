"""
Code Execution Engine with Tracing
Executes Python code while capturing variable state at each iteration
"""

import sys
import copy
from typing import List, Dict, Any
from io import StringIO


class CodeExecutor:
    """Executes Python code with iteration tracing"""
    
    def execute_with_tracing(
        self,
        code: str,
        initial_variables: Dict[str, Any],
        max_iterations: int = 10,
        max_snapshots: int = 10
    ) -> List[Dict[str, Any]]:
        """
        Execute code and capture snapshots at each loop iteration
        
        Args:
            code: Python code to execute
            initial_variables: Initial variable values
            max_iterations: Maximum iterations to allow (prevent infinite loops)
            max_snapshots: Maximum snapshots to capture
            
        Returns:
            List of snapshots with variable states
        """
        snapshots = []
        local_vars = copy.deepcopy(initial_variables)
        snapshot_counter = [0]  # Use list to allow modification in nested function
        iteration_counter = [0]  # Use list to allow modification in nested function
        
        # Create a custom trace function
        def trace_function(frame, event, arg):
            """Trace function to capture snapshots at loop iterations"""
            if event == 'line':
                # Capture snapshot periodically (every few line executions)
                if iteration_counter[0] % 3 == 0 and snapshot_counter[0] < max_snapshots:
                    snapshot = {
                        'step': snapshot_counter[0] + 1,
                        'variables': self._serialize_locals(frame.f_locals),
                        'iterationInfo': f'Line {frame.f_lineno}'
                    }
                    snapshots.append(snapshot)
                    snapshot_counter[0] += 1
                
                iteration_counter[0] += 1
                if iteration_counter[0] > max_iterations * 100:
                    raise RuntimeError(f"Execution limit exceeded (>{max_iterations * 100} iterations)")
            
            return trace_function
        
        try:
            # Execute code with tracing
            old_trace = sys.gettrace()
            sys.settrace(trace_function)
            
            exec(code, {'__builtins__': __builtins__}, local_vars)
            
            sys.settrace(old_trace)
            
            # If we didn't capture any snapshots, do a final capture
            if not snapshots:
                snapshots.append({
                    'step': 1,
                    'variables': self._serialize_locals(local_vars),
                    'iterationInfo': 'Execution completed'
                })
            
            return snapshots
            
        except Exception as e:
            sys.settrace(None)
            raise RuntimeError(f"Code execution failed: {str(e)}")
    
    def execute_simple(
        self,
        code: str,
        initial_variables: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Simple code execution without tracing
        Returns final variable state
        """
        local_vars = copy.deepcopy(initial_variables)
        
        try:
            exec(code, {'__builtins__': __builtins__}, local_vars)
            return self._serialize_locals(local_vars)
        except Exception as e:
            raise RuntimeError(f"Code execution failed: {str(e)}")
    
    @staticmethod
    def _serialize_locals(local_vars: Dict[str, Any]) -> Dict[str, Any]:
        """Serialize local variables, filtering out internal variables"""
        serialized = {}
        
        for name, value in local_vars.items():
            # Skip internal variables
            if name.startswith('__') or name == '_':
                continue
            
            serialized[name] = CodeExecutor._serialize_value(value)
        
        return serialized
    
    @staticmethod
    def _serialize_value(value: Any) -> Any:
        """Recursively serialize a value for JSON compatibility"""
        if value is None or isinstance(value, (bool, int, float, str)):
            return value
        elif isinstance(value, (list, tuple)):
            return [CodeExecutor._serialize_value(v) for v in value]
        elif isinstance(value, dict):
            return {str(k): CodeExecutor._serialize_value(v) for k, v in value.items()}
        elif isinstance(value, set):
            return list(value)
        else:
            # For other types, convert to string
            return str(value)