import { useEffect, useState } from 'react';
import LineChart from '../components/LineChart';

const Chart = () => {
  const [data, setData] = useState([]);

  useEffect(() => {
    fetchData();
  }, []);

  const fetchData = async () => {
    try {
      const response = await fetch('http://localhost:5000/data');  // Replace with your Flask API endpoint
      const jsonData = await response.json();
      // console.log('jsonData:', jsonData);
      setData(jsonData.result.rows);
    } catch (error) {
      console.error('Error fetching data:', error);
    }
  };

  return (
    <div>
      <h1 style={{margin: "auto",width:"fit-content",marginBottom:"20px",marginTop:"10px" }}>Line Chart</h1>
      {data.length > 0 ? (
        <LineChart data={data} />
      ) : (
        <p>Loading data...</p>
      )}
    </div>
  );
};

export default Chart;
