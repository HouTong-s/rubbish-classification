import GlobalConfig from './config/index'
const globalConfig = new GlobalConfig()
App({
  onLaunch: function () {

    

  },
  globalData: {
    config: globalConfig,
    class:null
  }
})
