import Vue from 'vue'
import Router from 'vue-router'
/* Layout */
import Layout from '../views/layout/Layout'

const _import = require('./_import_' + process.env.NODE_ENV)

Vue.use(Router)

export const asyncRouterMap = [
	// 首页
	{
		path: '',
		component: Layout,
		redirect: 'home',
		children: [{
			path: 'home',
			component: _import('welcome/index'),
			name: 'welcome',
			meta: {
				title: 'welcome',
				keepAlive: false
			}
		}]
	},

	// 文章
	{
		path: '/article',
		component: Layout,
		children: [{
				path: '',
				component: _import('article/articleList'),
				name: 'articleList',
				meta: {
					title: 'articleList',
					keepAlive: false
				}
			},
			{
				path: 'type/:id/',
				component: _import('article/articleList'),
				name: 'articleList',
				meta: {
					title: 'articleList',
					keepAlive: false
				}
			},
			{
				path: 'detail',
				component: _import('article/detail'),
				name: 'detail',
				meta: {
					title: 'detail',
					keepAlive: false
				}
			}
		]
	},

	// 小工具
	{
		path: '/',
		component: Layout,
		children: [{
			path: '/tools',
			component: _import('tools/toolset'),
			name: 'toolset',
			meta: {
				title: 'toolset',
				keepAlive: false
			}
		}]
	},

	// 电影
	{
		path: '',
		component: Layout,
		children: [{
			path: '/movie',
			component: _import('movie/movies'),
			name: 'movies',
			meta: {
				title: 'movies',
				keepAlive: false
			}
		}]
	},

	// 小游戏
	{
		path: '/games',
		component: Layout
	},

	// admin管理后台
	{
		path: '/admin',
		component: _import('admin/index')
	},

	// admin登录
	{
		path: '/admin/login',
		component: _import('admin/login'),
		name: 'login',
		meta: {
			title: 'login',
			keepAlive: false
		}
	}
]

export default new Router({
	mode: 'history', // 后端支持可开
	scrollBehavior: () => ({
		y: 0
	}),
	routes: asyncRouterMap
})