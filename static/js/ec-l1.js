var ecLeft1 = echarts.init(document.getElementById('l1'));

const data = [[], []];
const dateList = data.map(function (item) {
    return item[0];
});

left1Option = {

    title: [
        {
            text: '全国累计趋势',
            left: 'left',
            textStyle: {
                color: 'white'
            }
        },

    ],
    tooltip: {
        trigger: 'axis',
        axisPointer: {
            type: 'line',
            lineStyle: {
                color: '#7171C6'
            }
        }
    },
    legend: {
        data: ['累计确诊', '现有疑似', '累计治愈', '累计死亡'],
        left: 'right',
        textStyle: {
            color: 'white'
        }
    },

    grid: {
        left: '4%',
        right: '6%',
        bottom: '4%',
        top: 50,
        containLabel: true
    },
    xAxis: [
        {
            type: 'category',
            data: []
        },
    ],
    yAxis: [
        {
            type: 'value',
            axisLabel: {
                show: true,
                color: 'white',
                fontSize: 12,
                formatter: function (value) {
                    if (value > 1000) {
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
        },
    ],
    series: [
        {
            name: '累计确诊',
            type: 'line',
            smooth: true,
            data: []
        },
        {
            name: '现有疑似',
            type: 'line',
            smooth: true,
            data: []
        },
        {
            name: '累计治愈',
            type: 'line',
            smooth: true,
            data: []
        },
        {
            name: '累计死亡',
            type: 'line',
            smooth: true,
            data: []
        },
    ]
};

left1Option && ecLeft1.setOption(left1Option);