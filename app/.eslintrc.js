// https://eslint.org/docs/user-guide/configuring

module.exports = {
    root: true,
    parserOptions: {
        parser: 'babel-eslint'
    },
    env: {
        browser: true,
    },
    extends: [

        'plugin:vue/essential', 
        'standard'
    ],
    plugins: [
        'vue'
    ],
    // add your custom rules here
    rules: {
        'generator-star-spacing': 'off',
        'no-tabs': 0,
        'no-debugger': process.env.NODE_ENV === 'production' ? 'error' : 'off'
    }
}
