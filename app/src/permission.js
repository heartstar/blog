import router from './router'
import store from './store'
import NProgress from 'nprogress' // Progress 进度条
import 'nprogress/nprogress.css'// Progress 进度条样式

router.beforeEach((to, from, next) => {
	NProgress.start()
	if (to.path === '/admin' && !store.getters.isLogin) {
		next({ path: '/blog/admin/login' })
		NProgress.done()
	} else {
		next()
	}
})

router.afterEach(() => {
	NProgress.done() // 结束Progress
})
