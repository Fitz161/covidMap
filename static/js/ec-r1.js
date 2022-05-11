var ecRight1 = echarts.init(document.getElementById('r1'));

right1Option = {

    title: [
        {
            text: '省份/地区新增确诊TOP5',
            left: 'left',
            textStyle: {
                color: 'white'
            }
        },

    ],
    color: ['#3398DB'],
    tooltip: {
        trigger: 'axis',
        axisPointer: {
            type: 'shadow',
        }
    },

    xAxis: [
        {
            type: 'category',
            data: [],
            axisLabel: {
                color: 'white',
            }
        },
    ],
    yAxis: [
        {
            type: 'value',
            axisLabel: {
                color: 'white',
                formatter: function (value) {
                    if (value >= 1000) {
                        value = value / 1000 + 'k';
                    }
                    return value;
                }
            },
            axisLine: {
                show: true
            },
            splitLine: {
                show: true,
                lineStyle: {
                    color: '#17273B',
                    width: 1,
                    type: 'solid'
                }
            }
        }
    ],
    series: [
        {
            type: 'bar', //条形图
            barMaxWidth: '50%',
            data: []
        }
    ]
};

right1Option && ecRight1.setOption(right1Option);