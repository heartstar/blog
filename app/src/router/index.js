import Vue from 'vue'
import Router from 'vue-router'

const _import = require('./_import_' + process.env.NODE_ENV)

Vue.use(Router)

/* Layout */
import Layout from '../views/layout/Layout'

export const asyncRouterMap = [
    //首页
    {
        path: '', component: Layout, redirect: 'welcome',
        children: [
            {path: 'welcome', component: _import('welcome/index'), name: 'welcome', meta: {title: 'welcome', noCache: true}}
        ]
    },
]

export default new Router({
    mode: 'history', //后端支持可开
    scrollBehavior: () => ({y: 0}),
    routes: asyncRouterMap,
})
