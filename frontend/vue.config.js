module.exports = {
    publicPath: "/",
    devServer: {
        proxy: {
            "/api": {
<<<<<<< HEAD
                target: "http://52.79.111.26:8000"
            },
            "/static/posters": {
                target: "http://52.79.111.26:8000"
=======
                target: "http://52.79.111.26:8000/"
            },
            "/static/posters": {
                target: "http://52.79.111.26:8000/"
>>>>>>> f19a2fdd81e2a010b7303aa23d76b556fadda99a
            }
        }
    }
};
