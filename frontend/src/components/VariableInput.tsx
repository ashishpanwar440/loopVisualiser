import React, { useState } from 'react';
import './VariableInput.css';

interface VariableInputProps {
  variables: Record<string, any>;
  onChange: (variables: Record<string, any>) => void;
}

const VariableInput: React.FC<VariableInputProps> = ({
  variables,
  onChange,
}) => {
  const [varName, setVarName] = useState('');
  const [varValue, setVarValue] = useState('');

  const handleAddVariable = () => {
    if (varName.trim()) {
      try {
        // Try to parse the value as JSON/Python literal
        let parsedValue: any = varValue;
        if (varValue === 'True') parsedValue = true;
        else if (varValue === 'False') parsedValue = false;
        else if (varValue === 'None') parsedValue = null;
        else if (!isNaN(Number(varValue)) && varValue !== '')
          parsedValue = Number(varValue);
        else if (varValue.startsWith('[') || varValue.startsWith('{'))
          parsedValue = JSON.parse(varValue);

        onChange({
          ...variables,
          [varName]: parsedValue,
        });
        setVarName('');
        setVarValue('');
      } catch {
        // Keep as string if parsing fails
        onChange({
          ...variables,
          [varName]: varValue,
        });
        setVarName('');
        setVarValue('');
      }
    }
  };

  const handleRemoveVariable = (name: string) => {
    const newVariables = { ...variables };
    delete newVariables[name];
    onChange(newVariables);
  };

  const handleKeyPress = (e: React.KeyboardEvent) => {
    if (e.key === 'Enter') {
      handleAddVariable();
    }
  };

  return (
    <div className="variable-input">
      <label>Initial Variables (Optional)</label>
      <div className="input-group">
        <input
          type="text"
          placeholder="Variable name"
          value={varName}
          onChange={(e) => setVarName(e.target.value)}
          onKeyPress={handleKeyPress}
        />
        <input
          type="text"
          placeholder="Value (e.g., 10, 'hello', [1,2,3])"
          value={varValue}
          onChange={(e) => setVarValue(e.target.value)}
          onKeyPress={handleKeyPress}
        />
        <button onClick={handleAddVariable}>Add</button>
      </div>

      {Object.keys(variables).length > 0 && (
        <div className="variables-list">
          {Object.entries(variables).map(([name, value]) => (
            <div key={name} className="variable-item">
              <span className="var-name">{name}:</span>
              <span className="var-value">
                {JSON.stringify(value)}
              </span>
              <button
                className="remove-btn"
                onClick={() => handleRemoveVariable(name)}
              >
                ✕
              </button>
            </div>
          ))}
        </div>
      )}
    </div>
  );
};

export default VariableInput;