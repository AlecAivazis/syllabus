// frontend build configuration using webpack
// reference: https://github.com/petehunt/webpack-howto

// the directories with source code
var path = require('path');
var current_location = path.resolve('.');
var asset_dir = path.join(current_location, 'syllabus', 'assets');
var src_dir = path.join(asset_dir, 'scripts');

// export the configuration
module.exports = {
    entry: './syllabus/assets/scripts/app.js',
    output: {
        path: './syllabus/assets/build/',
        publicPath: '/static/build/',
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
            { test: /\.(png|jpg)$/, loader: 'url-loader' }, // inline base64 URLs for <=8k images, direct URLs for the rest
            { test: /\.js$/, exclude: /node_modules/, loaders: ['babel-loader']},
            { test: /\.styl$/, loader: 'style-loader!css-loader!stylus-loader' },
        ]
    },
    resolve: {
        extensions: ['', '.js', '.styl', '.css'],
        root: [current_location, src_dir, asset_dir]
    },
    eslint: {
        configFile: '.eslintrc'
    }
};

// end of file