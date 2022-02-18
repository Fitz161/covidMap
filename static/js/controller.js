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

function getL1Data() {
    $.ajax({
        url: '/l1',
        success: function (data){
            console.log(data)
            left1Option.xAxis[0].data = data.day;
            left1Option.series[0].data = data.confirm;
            left1Option.series[1].data = data.suspect;
            left1Option.series[2].data = data.heal;
            left1Option.series[3].data = data.dead;
            ecLeft1.setOption(left1Option);
        }, error: console.error('请求l1数据失败')
    })
}
getL1Data();
