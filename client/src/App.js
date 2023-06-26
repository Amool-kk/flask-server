import './App.css';
import { Link, Routes, Route } from 'react-router-dom'
import Chart from './pages/Chart';

function App() {
  return (
    <Routes>
      <Route path="/" element={<Chart />} />
    </Routes>
  );
}

export default App;
