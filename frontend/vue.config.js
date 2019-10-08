module.exports = {

    publicPath: "/",
    devServer: {
        proxy: {
            "/api": {
<<<<<<< HEAD
                target: "http://localhost:8000/"
            },
            "/static/posters": {
                target: "http://localhost:8000"
=======
                target: "http://52.79.111.26:8000"
            },
            "/static/posters": {
                target: "http://52.79.111.26:8000"
>>>>>>> develope
            }
        }
    }
};
