/// <reference types="react-scripts" />

declare module 'react';
declare module 'react/jsx-runtime';
declare module 'react-dom/client';

declare namespace JSX {
  interface IntrinsicElements {
    [elemName: string]: any;
  }
}
