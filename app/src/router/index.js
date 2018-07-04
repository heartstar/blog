import Vue from 'vue'
import Router from 'vue-router'
/* Layout */
import Layout from '../views/layout/Layout'

const _import = require('./_import_' + process.env.NODE_ENV)

Vue.use(Router)

export const asyncRouterMap = [

	{
		path: '/blog',
		component: Layout,
		redirect: '/blog',
		children: [
            {path: '', component: _import('welcome/index'), name: 'welcome', meta: {title: 'welcome',keepAlive: false}},
            {path: 'article', component: _import('article/articleList'), name: 'articleList', meta: {title: 'articleList',keepAlive: false},
                children: [
                    {path: 'type/:id/', component: _import('article/articleList'), name: 'articleList', meta: {title: 'articleList',keepAlive: false}},
                    {path: 'detail', component: _import('article/detail'), name: 'detail', meta: { title: 'detail', keepAlive: false}}
                ]
            },
            {path: 'tools', component: _import('tools/toolset'), name: 'toolset', meta: {title: 'toolset', keepAlive: false}},
            {path: 'movie', component: _import('movie/movies'), name: 'movies', meta: {title: 'movies', keepAlive: false}},
            {path: 'games', component: Layout},
            {path: 'admin', component: _import('admin/index'), name: 'movies', meta: {title: 'movies', keepAlive: false},
                children: [
                    {path: 'login', component: _import('admin/login'), name: 'login', meta: {title: 'login', keepAlive: false}}
                ]
            },
        ]
	},
	
]

export default new Router({
	mode: 'history', // 后端支持可开
	scrollBehavior: () => ({
		y: 0
	}),
	routes: asyncRouterMap
})