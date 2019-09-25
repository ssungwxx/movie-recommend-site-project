module.exports = {
  publicPath: '/',
  devServer: {
    proxy: {
      '/api': {
        target: 'http://52.79.111.26/',
      },
      '/static/posters': {
        target: 'http://52.79.111.26/',
      },
    }
  }
}