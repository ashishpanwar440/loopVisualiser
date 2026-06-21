import axios from 'axios';

const API_BASE_URL = process.env.REACT_APP_API_URL || 'http://localhost:5000';

const apiClient = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

interface LoopSnapshot {
  step: number;
  variables: Record<string, any>;
  loopVar?: string;
  loopVarValue?: any;
  iterationInfo?: string;
}

interface VisualizeResponse {
  snapshots: LoopSnapshot[];
  executionTime: number;
}

export const visualizeLoop = async (
  code: string,
  initialVariables: Record<string, any> = {}
): Promise<VisualizeResponse> => {
  try {
    const response = await apiClient.post<VisualizeResponse>('/api/visualize', {
      code,
      variables: initialVariables,
    });
    return response.data;
  } catch (error) {
    if (axios.isAxiosError(error)) {
      throw new Error(error.response?.data?.error || 'Failed to visualize loop');
    }
    throw error;
  }
};

export default apiClient;