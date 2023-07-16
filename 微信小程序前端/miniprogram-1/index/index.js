const app = getApp()

Page({
  data: {
    headerUrl:'',
    Url:'',
    classes:['可回收垃圾','干垃圾','湿垃圾','有害垃圾'],
    value:0,
    myclass:null,
    inputValue:null
  },
  onLoad: function (options) {
    // this.setData({
    //   headerUrl:options.img
    // })
  },
  upload (){
    var that = this;
   
    wx.chooseImage({
      count: 1,
      sizeType: ['compressed'],
      sourceType: ['album', 'camera'],
      success (res) {
        that.setData({
          Url:res.tempFilePaths[0]
        })
        const tempFilePaths = res.tempFilePaths
        wx.showLoading({
          title: '等待服务器返回',
        })
        wx.uploadFile({
          //http://139.224.50.124:80/uploadfile/
          url: 'http://classification.shop:80/uploadfile/', 
          filePath: tempFilePaths[0],
          name: 'file',
          success (res){
            const data = res.data
            console.log(data)
            const app =getApp()
            var js1 = JSON.parse(data)
            console.log(js1.class)
            app.globalData.class = js1.class
            wx.hideLoading({
              success: (res) => {},
            })
            wx.navigateTo({
              url: `./result/result?src=${tempFilePaths[0]}`,
            })
            //do something
          },
          fail (res){
            console.log(res)
            //do something
          },
        })
        
      }
    })
  },
  bindChange: function (e) {
    const val = e.detail.value
    console.log(val)
    
    this.setData({
      value: val,
    })
    console.log(this.data.value)
    //console.log(this.data.myclass)
  },
  search: function()
  {
    const myclass = this.data.classes[this.data.value]
    wx.navigateTo({
      url: `./display1/display1?src=${myclass}`,
    })
  },
  searchByKeyword:function()
  {
    console.log(this.data.inputValue)
    if(this.data.inputValue == '' || this.data.inputValue == null)
    {
    
      wx.showToast({
        title: '名称不能为空',
        icon: 'error'
      })
    }
    else
    {
      wx.request({
        url: 'http://139.224.50.124:81/searchByKeyword/',
        data:{
          keyword:this.data.inputValue
        },
        success(res)
        {
          console.log(res.data)
          wx.navigateTo({
            url: `./classresult/classresult?src=${res.data.class}`,
          })
        }
      })
    }
  },
  getInputValue(e){
    //console.log(e.detail)
    this.setData({
      inputValue: e.detail.value
    })
  }
})
