"""
Loop Analysis Engine
Analyzes Python code and creates step-by-step snapshots of loop execution
"""

import ast
import copy
import time
from typing import List, Dict, Any, Tuple
from utils import CodeExecutor, VariableTracker


class LoopAnalyzer:
    """Analyzes Python code with loops and generates visualization snapshots"""
    
    MAX_ITERATIONS = 10  # Safety limit to prevent infinite loops
    MAX_SNAPSHOTS = 10   # Maximum snapshots to capture
    
    def __init__(self):
        self.executor = CodeExecutor()
        self.tracker = VariableTracker()
        self.snapshots = []
        self.iteration_count = 0
    
    def analyze(self, code: str, initial_variables: Dict[str, Any] = None) -> Tuple[List[Dict], float]:
        """
        Analyze code and generate visualization snapshots
        
        Args:
            code: Python code containing a loop
            initial_variables: Initial variable values
            
        Returns:
            Tuple of (snapshots, execution_time)
        """
        start_time = time.time()
        self.snapshots = []
        self.iteration_count = 0
        
        try:
            # Parse the code
            tree = ast.parse(code)
            
            # Check if code contains loops
            if not self._has_loops(tree):
                raise ValueError("Code does not contain any loops (for/while)")
            
            # Execute code with tracing
            snapshots = self.executor.execute_with_tracing(
                code,
                initial_variables or {},
                max_iterations=self.MAX_ITERATIONS,
                max_snapshots=self.MAX_SNAPSHOTS
            )
            
            execution_time = time.time() - start_time
            return snapshots, execution_time
            
        except Exception as e:
            raise Exception(f"Analysis failed: {str(e)}")
    
    def _has_loops(self, tree: ast.AST) -> bool:
        """Check if AST contains for or while loops"""
        for node in ast.walk(tree):
            if isinstance(node, (ast.For, ast.While)):
                return True
        return False


class SnapshotCapture:
    """Captures a snapshot of variables at a specific point in execution"""
    
    def __init__(self, step: int, variables: Dict[str, Any]):
        self.step = step
        self.variables = copy.deepcopy(variables)
        self.timestamp = time.time()
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert snapshot to dictionary for JSON serialization"""
        return {
            'step': self.step,
            'variables': self._serialize_variables(self.variables)
        }
    
    @staticmethod
    def _serialize_variables(variables: Dict[str, Any]) -> Dict[str, Any]:
        """Serialize variables, handling complex types"""
        serialized = {}
        for name, value in variables.items():
            serialized[name] = SnapshotCapture._serialize_value(value)
        return serialized
    
    @staticmethod
    def _serialize_value(value: Any) -> Any:
        """Serialize a single value"""
        if value is None or isinstance(value, (bool, int, float, str)):
            return value
        elif isinstance(value, (list, tuple)):
            return [SnapshotCapture._serialize_value(v) for v in value]
        elif isinstance(value, dict):
            return {k: SnapshotCapture._serialize_value(v) for k, v in value.items()}
        else:
            return str(value)