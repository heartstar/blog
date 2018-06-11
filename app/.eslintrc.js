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
        'html'
    ],
    // add your custom rules here 0:禁止  1:出现问题会有警告 2:出现问题会报错
    rules: {
        'generator-star-spacing': 'off',  //强制 generator 函数中 * 号周围使用一致的空格
        'no-tabs': 0,  //禁用 tab
        'no-debugger': 2, //禁用 debugger
        'no-mixed-spaces-and-tabs': 2, //禁止空格和 tab 的混合缩进
        'no-debugger': process.env.NODE_ENV === 'production' ? 'error' : 'off',
        'no-console': process.env.NODE_ENV === 'production' ? 'error' : 'off',
        'indent': [0, "tab"],
        "camelcase": [2, {"properties": "never"}],   //强制驼峰命名规则
        "no-extra-parens": 2,  //不允许出现多余的括号
        'no-dupe-args': 'error', // 禁止在函数参数中出现重复名称的参数
        'eol-last': 0, //要求或禁止文件末尾存在空行
        // 'semi': [2, "always"],  //以分号结尾
        'no-extra-semi': 2,  //不允许出现不必要的分号
    },
    "overrides": [
        {
            "files": ["*.vue"],
            "rules": {
                "indent": "off",
                "vue/script-indent": [0, 4, {"baseIndent": 1}]
            }
        }
    ]   
}
