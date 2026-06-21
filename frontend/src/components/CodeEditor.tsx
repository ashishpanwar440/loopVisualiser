import React from 'react';
import './CodeEditor.css';

interface CodeEditorProps {
  code: string;
  onChange: (code: string) => void;
}

const CodeEditor: React.FC<CodeEditorProps> = ({ code, onChange }) => {
  return (
    <div className="code-editor">
      <label htmlFor="code-input">Python Code with Loop</label>
      <textarea
        id="code-input"
        className="code-input"
        value={code}
        onChange={(e) => onChange(e.target.value)}
        placeholder="Enter your Python code here..."
        spellCheck="false"
      />
      <div className="editor-info">
        <span>💡 Tip: Write simple loops with variable assignments</span>
      </div>
    </div>
  );
};

export default CodeEditor;