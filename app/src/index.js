import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';


  // const driver = neo4j.driver(
  //   process.env.NEO4J.URI || '',
  //   neo4j.auth.basic(
  //     process.env.NEO4J_USER || '',
  //     process.env.NEO4J_PASSWORD || ''
  //   )
  // )

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  // <React.StrictMode>
    <App />
  // </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
