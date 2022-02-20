let ecWordCloud = echarts.init(document.getElementById('r2'));//, "dark");需下载dark主题

var data2 = [{}, {}];

var wordCloudOption = {
    title: [
        {
            text: '今日百度热搜',
            left: 'left',
            textStyle: {
                color: 'white'
            }
        }
    ],
    tootip: {
        show: false
    },
    series: [{
        type: 'wordCloud',
        gridSize: 1,
        sizeRange: [12, 55],
        rotationRange: [-45, 0, 45, 90],
        textStyle: {
            color: function () { //新版echarts随机颜色设置不用写在normal中，否则可能会失效
                return 'rgb(' + [
                    Math.round(Math.random() * 255),
                    Math.round(Math.random() * 255),
                    Math.round(Math.random() * 255)
                ].join(',') + ')'
            },
            emphasis: {
                shadowBlur: 10,
                    shadowColor: '#333'
            }
        },
        right: null,
        bottom: null,
        data: []
    }]
}

wordCloudOption && ecWordCloud.setOption(wordCloudOption);