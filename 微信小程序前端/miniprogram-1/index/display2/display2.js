// index/display2/display2.js
Page({

  /**
   * 页面的初始数据
   */
  data: {
    class1:null,
    class2:null,
    list:[],
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    var that = this
    this.setData({
      class1:options.class1,
      class2:options.class2
    })
    wx.showLoading({
      title: '加载中',
    })
    wx.request({
      url: 'http://139.224.50.124:81/getPictures/',
      method:'POST',
      data:JSON.stringify({
        class1:this.data.class1,
        class2:this.data.class2,
      }),
      header: {
        "content-type": "application/json"
      },
      success (res) {
        wx.hideLoading({
          success: (res) => {},
        })
        //console.log(res.data)
        //console.log(res.data.data)
        console.log(res.data.data.length)
        that.setData({
          list:res.data.data
        })
        console.log(that.data.list.length)
      }
    })
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

  }
})