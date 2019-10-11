module.exports = {

    publicPath: "/",
    devServer: {
        proxy: {
            "/api": {

                //target: "http://127.0.0.1:8000"
                target: "http://52.79.111.26:8000"
            },
            "/static/posters": {
                //target: "http://127.0.0.1:8000"
                target: "http://52.79.111.26:8000"

        
            }
        }
    }
};
