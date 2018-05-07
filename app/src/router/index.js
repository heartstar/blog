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
            {path: 'welcome', component: _import('welcome/index'), name: 'welcome', meta: {title: 'welcome', keepAlive: false}}
        ]
    },

    //文章
    {
        path: '/article', component: Layout,
        children: [
            {path: '', component: _import('article/articleList'), name: 'articleList', meta: {title: 'articleList', keepAlive: false}},
            {path: 'type/:id/', component: _import('article/articleList'), name: 'articleList', meta: {title: 'articleList', keepAlive: false}},
            {path: 'detail', component: _import('article/detail'), name: 'detail', meta: {title: 'detail', keepAlive: false}}
        ]
    },


    //admin管理后台
    {
        path: '/admin', component: _import('admin/index'),
        children: [
            //{path: 'admin', component: _import('admin/index'), name: 'welcome', meta: {title: 'welcome', keepAlive: false}}
        ]
    },
]

export default new Router({
    mode: 'history', //后端支持可开
    scrollBehavior: () => ({y: 0}),
    routes: asyncRouterMap,
})
