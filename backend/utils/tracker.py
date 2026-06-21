"""
Variable Tracking Utility
Tracks variable changes across iterations
"""

import copy
from typing import List, Dict, Any


class VariableTracker:
    """Tracks variable values and changes across iterations"""
    
    def __init__(self):
        self.snapshots: List[Dict[str, Any]] = []
        self.current_step = 0
    
    def capture_state(self, variables: Dict[str, Any], step_info: str = "") -> None:
        """
        Capture current variable state
        
        Args:
            variables: Current variable values
            step_info: Information about current step
        """
        snapshot = {
            'step': self.current_step + 1,
            'variables': copy.deepcopy(variables),
            'iterationInfo': step_info,
            'timestamp': None
        }
        self.snapshots.append(snapshot)
        self.current_step += 1
    
    def get_snapshots(self) -> List[Dict[str, Any]]:
        """Get all captured snapshots"""
        return self.snapshots
    
    def clear(self) -> None:
        """Clear all snapshots"""
        self.snapshots = []
        self.current_step = 0
    
    def get_variable_history(self, var_name: str) -> List[Any]:
        """
        Get history of a specific variable across all snapshots
        
        Args:
            var_name: Name of the variable
            
        Returns:
            List of values for that variable in each snapshot
        """
        history = []
        for snapshot in self.snapshots:
            if var_name in snapshot['variables']:
                history.append(snapshot['variables'][var_name])
            else:
                history.append(None)
        return history
    
    def get_variable_changes(self, var_name: str) -> List[tuple]:
        """
        Get changes for a specific variable
        
        Returns:
            List of (step, old_value, new_value) tuples
        """
        changes = []
        history = self.get_variable_history(var_name)
        
        prev_value = None
        for step, value in enumerate(history):
            if step == 0 or value != prev_value:
                changes.append((step + 1, prev_value, value))
            prev_value = value
        
        return changes