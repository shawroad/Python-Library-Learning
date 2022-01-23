var ec_left = echarts.init(document.getElementById("left"), "dark");

option_left = {
  xAxis: {
    type: 'category',
    data: []
  },
  yAxis: {
    type: 'value'
  },
  series: [
    {
      data: [],
      type: 'line'
    }
  ]
};
ec_left.setOption(option_left);