//index.js
//获取应用实例
var app = getApp()
Page({
  data: {
    motto: 'Hello World',
    userInfo: {},
    screenData:'0',
    longitude:'0',

    defaultSize: 'default',
    primarySize: 'default',
    warnSize: 'default',
    disabled: false,
    plain: false,
    loading: false
  },
  //事件处理函数
  bindViewTap: function() {
    wx.navigateTo({
      url: '../logs/logs'
    })
  },
  onLoad: function () {
    console.log('onLoad')
    var that = this
    //调用应用实例的方法获取全局数据
    app.getUserInfo(function(userInfo){
      //更新数据
      that.setData({
        userInfo:userInfo
      })
    })

    this.getloca()
  },


  getloca: function () {
    var that = this
    var m = new Map();
    wx.getLocation({
      type: 'wgs84',
      success: function (res) {
        m.set('latitude', res.latitude);
        m.set('longitude', res.longitude);
        m.set('speed', res.speed);
        m.set('accuracy', res.accuracy);
        m.set('altitude', res.altitude);
        m.set('verticalAccuracy', res.verticalAccuracy);
        m.set('horizontalAccuracy', res.horizontalAccuracy);
        console.log(res.latitude)
        
        that.setData({
          screenData: res.latitude,
          longitude: res.longitude
        })
      }
    })
  },


    sx: function(){

      this.getloca()


    }
   
  
})
