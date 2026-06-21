import React, { useState } from 'react';
import CodeEditor from './components/CodeEditor';
import VariableInput from './components/VariableInput';
import Visualizer from './components/Visualizer';
import { visualizeLoop } from './services/api';
import './App.css';

interface LoopSnapshot {
  step: number;
  variables: Record<string, any>;
  loopVar?: string;
  loopVarValue?: any;
  iterationInfo?: string;
}

const App: React.FC = () => {
  const [code, setCode] = useState<string>('for i in range(3):\n    x = i * 2');
  const [variables, setVariables] = useState<Record<string, any>>({});
  const [snapshots, setSnapshots] = useState<LoopSnapshot[]>([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [currentStepIndex, setCurrentStepIndex] = useState(0);

  const handleVisualize = async () => {
    setLoading(true);
    setError(null);
    setCurrentStepIndex(0);

    try {
      const result = await visualizeLoop(code, variables);
      setSnapshots(result.snapshots);
    } catch (err) {
      setError(
        err instanceof Error ? err.message : 'Failed to visualize loop'
      );
      setSnapshots([]);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="app">
      <header className="app-header">
        <h1>🔄 Loop Visualiser</h1>
        <p>Learn how loops work step by step</p>
      </header>

      <div className="app-container">
        <div className="input-section">
          <CodeEditor code={code} onChange={setCode} />
          <VariableInput
            variables={variables}
            onChange={setVariables}
          />
          <button
            className="visualize-btn"
            onClick={handleVisualize}
            disabled={loading}
          >
            {loading ? 'Analyzing...' : 'Visualize Loop'}
          </button>
        </div>

        {error && <div className="error-message">{error}</div>}

        {snapshots.length > 0 && (
          <Visualizer
            snapshots={snapshots}
            currentStepIndex={currentStepIndex}
            onStepChange={setCurrentStepIndex}
          />
        )}
      </div>
    </div>
  );
};

export default App;