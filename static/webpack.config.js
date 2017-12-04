/**
 * Webpack config files that tell webpack where to find the
 * JS files and where to place their bundled output
 *
 * Author: Philip Bedward
 * Date: 11/8/17
 */
const webpack = require('webpack');
const config = {
    entry:  __dirname + '/js/index.jsx',
    output: {
        path: __dirname + '/dist',
        filename: 'bundle.js',
    },
    resolve: {
        extensions: ['.js', '.jsx', '.css']
    },
    module: {
      rules: [
          {
              test: /\.jsx?$/,
              exclude: /node_modules/,
              loader: 'babel-loader',
              query: {
                  presets: ['react']
              }
          },
          {
              test: /\.css$/,
              loader: [ 'style-loader', 'css-loader' ]
          },
          {
              test: /\.(png|woff|woff2|eot|ttf|svg)$/,
              loader: 'url-loader?limit=100000'
          },
      ]
    }
};
module.exports = config;