import React from 'react';
import ReactDOM from 'react-dom/client';
import './styles/globals.css';
import IndexPage from './pages/index';

const root = ReactDOM.createRoot(
  document.getElementById('root') as HTMLElement
);
root.render(
  <React.StrictMode>
    <IndexPage />
  </React.StrictMode>
);
