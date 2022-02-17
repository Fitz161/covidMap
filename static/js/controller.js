function getC1Data() {
    $.ajax({
        url: '/c1',
        success: function (jsonData) {
            //分别选中各个元素并填充内容
            console.log(jsonData);
            $('.num h1').eq(0).text(jsonData.confirm);
            $('.num h1').eq(1).text(jsonData.confirm_add);
            $('.num h1').eq(2).text(jsonData.heal);
            $('.num h1').eq(3).text(jsonData.dead);
        }, error: console.error('请求c1数据失败')
  })
}
getC1Data();

function getC2Data() {
    $.ajax({
        url: '/c2',
        success: function (jsonData) {
            console.log(jsonData);
            mapOption.series[0].data = jsonData.keyData;
            echartsMap.setOption(mapOption);
        }, error: console.error('请求c2数据失败')
    })
}
getC2Data();
