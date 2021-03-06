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

function getL2Data() {
    $.ajax({
        url: '/l2',
        success: function (data){
            console.log(data)
            left2Option.xAxis[0].data = data.day;
            left2Option.series[0].data = data.confirm_add;
            left2Option.series[1].data = data.suspect_add;
            left2Option.series[2].data = data.heal_add;
            left2Option.series[3].data = data.dead_add;
            ecLeft2.setOption(left2Option);
        }, error: console.error('请求l2数据失败')
    })
}
getL2Data();

function getR1Data() {
    $.ajax({
        url: '/r1',
        success: function (data){
            console.log(data)
            right1Option.xAxis[0].data = data.province;
            right1Option.series[0].data = data.confirm_add;
            ecRight1.setOption(right1Option);
        }, error: console.error('请求r1数据失败')
    })
}
getR1Data();

function getR2Data() {
    $.ajax({
        url: '/r2',
        success: function (data){
            console.log(data);
            wordCloudOption.series[0].data = data.keywords;
            ecWordCloud.setOption(wordCloudOption);
        }, error: console.error('请求r2数据失败')
    })
}
getR2Data();