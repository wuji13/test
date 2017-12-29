// pages/cal/cal.js
Page({

  /**
   * 页面的初始数据
   */
  data: {
    id1:"back",
    id2: "clear",
    id3: "negative",
    id4: "+",
    id5: "1",
    id6: "2",
    id7: "3",
    id8: "-",
    id9: "4",
    id10: "5",
    id11: "6",
    id12: "×",
    id13: "7",
    id14: "8",
    id15: "9",
    id16: "÷",
    id17: "0",
    id18: ".",
    id19: "history",
    id20: "=",
    screenData: "0",


  
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
  
  },

  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady: function () {
  
  },

  /**
   * 生命周期函数--监听页面显示
   */
  onShow: function () {
  
  },

  /**
   * 生命周期函数--监听页面隐藏
   */
  onHide: function () {
  
  },

  /**
   * 生命周期函数--监听页面卸载
   */
  onUnload: function () {
  
  },

  /**
   * 页面相关事件处理函数--监听用户下拉动作
   */
  onPullDownRefresh: function () {
  
  },

  /**
   * 页面上拉触底事件的处理函数
   */
  onReachBottom: function () {
  
  },

  /**
   * 用户点击右上角分享
   */
  onShareAppMessage: function () {
  
  },

  clickButton: function(event){
    console.log(event.target.id);
    var sd = this.data.screenData;
    var data;
    if(sd==0)
    {
      data = event.target.id;
    }

    else{
      data = sd + event.target.id;
    }   
    this.setData({screenData:data});
  }


})