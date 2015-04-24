// frontend build configuration using webpack
// reference: https://github.com/petehunt/webpack-howto

module.exports = {
    entry: './src/app.js',
    output: {
        path: './assets',
        filename: 'app.js'
    },
    module: {
        preLoaders: [
            {
                test: /\.js$/,
                loader: "eslint-loader?{rules:[{semi:0}]}",
                exclude: /node_modules/
            },
        ],
        loaders: [
            { test: /\.css$/, loader: 'style-loader!css-loader' },
            { test: /\.(png|jpg)$/, loader: 'url-loader?limit=8192' }, // inline base64 URLs for <=8k images, direct URLs for the rest
            { test: /\.js$/, exclude: /node_modules/, loader: 'babel-loader' },
        ]
    },
    resolve: {
        extensions: ['', '.js', '.styl']
    },
    eslint: {
        configFile: '.eslintrc'
    }
};

// end of file