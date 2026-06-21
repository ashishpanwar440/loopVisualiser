import React from 'react';
import './Visualizer.css';

interface LoopSnapshot {
  step: number;
  variables: Record<string, any>;
  loopVar?: string;
  loopVarValue?: any;
  iterationInfo?: string;
}

interface VisualizerProps {
  snapshots: LoopSnapshot[];
  currentStepIndex: number;
  onStepChange: (index: number) => void;
}

const Visualizer: React.FC<VisualizerProps> = ({
  snapshots,
  currentStepIndex,
  onStepChange,
}) => {
  const currentSnapshot = snapshots[currentStepIndex];

  const handlePrevious = () => {
    if (currentStepIndex > 0) {
      onStepChange(currentStepIndex - 1);
    }
  };

  const handleNext = () => {
    if (currentStepIndex < snapshots.length - 1) {
      onStepChange(currentStepIndex + 1);
    }
  };

  return (
    <div className="visualizer">
      <div className="visualization-box">
        <h2>Step {currentSnapshot.step}</h2>
        {currentSnapshot.iterationInfo && (
          <div className="iteration-info">
            {currentSnapshot.iterationInfo}
          </div>
        )}

        <div className="variables-snapshot">
          <h3>Variable States</h3>
          <div className="variables-grid">
            {Object.entries(currentSnapshot.variables).map(([name, value]) => (
              <div key={name} className="variable-card">
                <span className="var-name">{name}</span>
                <div className="var-value-display">
                  {typeof value === 'object'
                    ? JSON.stringify(value, null, 2)
                    : String(value)}
                </div>
                <span className="var-type">
                  {Array.isArray(value)
                    ? 'list'
                    : typeof value}
                </span>
              </div>
            ))}
          </div>
        </div>
      </div>

      <div className="controls">
        <button
          className="nav-btn"
          onClick={handlePrevious}
          disabled={currentStepIndex === 0}
        >
          ← Previous
        </button>

        <div className="step-indicator">
          <span>{currentStepIndex + 1}</span>
          <span>/</span>
          <span>{snapshots.length}</span>
        </div>

        <button
          className="nav-btn"
          onClick={handleNext}
          disabled={currentStepIndex === snapshots.length - 1}
        >
          Next →
        </button>
      </div>

      <div className="progress-bar">
        <div
          className="progress-fill"
          style={{
            width: `${((currentStepIndex + 1) / snapshots.length) * 100}%`,
          }}
        />
      </div>
    </div>
  );
};

export default Visualizer;