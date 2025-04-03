import React, { useState } from 'react';
import { Header } from '../components/Header';
import { MetricSelector } from '../components/MetricSelector';
import { TeamContextSelector } from '../components/TeamContextSelector';
import { TransformationPipeline } from '../components/TransformationPipeline';
import { ChartView } from '../components/ChartView';
import { ExplanationPanel } from '../components/ExplanationPanel';
import { pipelines } from '../data/pipelines';
import { chartData } from '../data/chartOutputs';
import { TeamType } from '../types/types';

const IndexPage = () => {
  const [selectedTeam, setSelectedTeam] = useState('product' as TeamType);
  const pipelineStages = pipelines[selectedTeam].stages;
  const outputData = chartData[selectedTeam];

  return (
    <div className="min-h-screen bg-gray-50 text-gray-800 p-6">
      <Header />
      <MetricSelector />
      <TeamContextSelector selected={selectedTeam} setSelected={setSelectedTeam} />

      <div className="grid grid-cols-1 md:grid-cols-2 gap-6 mt-8">
        <TransformationPipeline stages={pipelineStages} />
        <ChartView data={outputData} selectedTeam={selectedTeam} />
      </div>

      <div className="mt-10">
        <ExplanationPanel selectedTeam={selectedTeam} />
      </div>
    </div>
  );
};

export default IndexPage;
