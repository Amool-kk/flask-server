import { useEffect, useRef } from 'react';
import * as echarts from 'echarts';

const LineChart = ({ data }) => {
  const chartRef = useRef(null);

  let date = [];
  let months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Nov', 'Dec'];
  for (let i = 0; i < data.length; i++) {
    var temp = new Date(data[i].transaction_date);
    date.push([temp.getFullYear(), temp.getMonth()+1, temp.getDate()].join('/'));
  }

  useEffect(() => {
    const chart = echarts.init(chartRef.current, 'dark');
    const options = {
      title: {
        left: 'center',
        text: "Monthly Ative Addresses",
      },
      tooltip: {
        trigger: 'axis',
        position: function (pt) {
          return [pt[0], '10%'];
        },
      },
      toolbox: {
        feature: {
          datazoom: {
            yAxisIndex: 'none',
          },
          restore: {},
        },
      },
      grid: {
        top: "13%",
        left: '3%',
        right: '4%',
        bottom: '3%',
        containLabel: true
      },
      xAxis: {
        type: 'category',
        boundaryGap: false,
        data: date,
      },
      yAxis: {
        type: 'value',
        boundaryGap: [0, '100%'],
      },
      datazoom: [
        {
          type: 'inside',
          start: 0,
          end: 10,
        },
        {
          start: 0,
          end: 10,
        }
      ],
      series: [{
        name: 'Average Transactions Per Block',
        type: 'line',
        symbol: 'none',
        sampling: 'lttb',
        areaStyle: {},
        data: data.map(item => item.average_transactions_per_block),
      }],
    };

    chart.setOption(options);

    return () => {
      chart.dispose();
    };
  }, [data]);

  return <div ref={chartRef} style={{ width: '100%', height: '400px' }} />;
};

export default LineChart;
