import React from 'react';
import { Stage } from '../types/types';

// Icons for each stage type
const StageIcons = {
  'Raw Logs': (
    <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
    </svg>
  ),
  'Transform': (
    <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19.428 15.428a2 2 0 00-1.022-.547l-2.387-.477a6 6 0 00-3.86.517l-.318.158a6 6 0 01-3.86.517L6.05 15.21a2 2 0 00-1.806.547M8 4h8l-1 1v5.172a2 2 0 00.586 1.414l5 5c1.26 1.26.367 3.414-1.415 3.414H4.828c-1.782 0-2.674-2.154-1.414-3.414l5-5A2 2 0 009 10.172V5L8 4z" />
    </svg>
  ),
  'Normalize': (
    <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z" />
    </svg>
  )
};

interface Props {
  stages: Stage[];
}

export const TransformationPipeline = ({ stages }: Props) => (
  <div className="relative">
    {/* Vertical connector line */}
    <div className="absolute left-6 top-10 bottom-10 w-0.5 bg-blue-200 z-0" style={{ height: 'calc(100% - 80px)' }}></div>
    
    <div className="space-y-8 relative z-10">
      {stages.map((stage, index) => (
        <div key={index} className="relative">
          {/* Stage container with icon */}
          <div className="bg-white p-4 rounded shadow border-l-4 border-blue-500">
            <div className="flex items-center mb-2">
              {/* Icon based on stage label */}
              <div className="mr-2 text-blue-600">
                {StageIcons[stage.label as keyof typeof StageIcons] || 
                 <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                   <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M13 10V3L4 14h7v7l9-11h-7z" />
                 </svg>
                }
              </div>
              <h3 className="font-semibold text-blue-700">{stage.label}</h3>
            </div>
            <pre className="bg-gray-100 p-3 text-xs rounded mt-2 overflow-x-auto">{stage.content}</pre>
          </div>
          
          {/* Connector arrow */}
          {index < stages.length - 1 && (
            <div className="flex justify-center my-2 py-1">
              <div className="bg-white rounded-full p-1 shadow">
                <svg className="w-5 h-5 text-blue-500" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 14l-7 7m0 0l-7-7m7 7V3" />
                </svg>
              </div>
            </div>
          )}
        </div>
      ))}
    </div>
  </div>
);
