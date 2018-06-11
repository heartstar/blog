import store from '@/store'

export default async (url = '', data = {}, type = 'GET', method = 'fetch') => {
	type = type.toUpperCase()
	url = process.env.BASE_API + url
	if (type === 'GET') {
		let dataStr = '' // 数据拼接字符串
		Object.keys(data).forEach(key => {
			dataStr += key + '=' + data[key] + '&'
		})

		if (dataStr !== '') {
			dataStr = dataStr.substr(0, dataStr.lastIndexOf('&'))
			url = url + '?' + dataStr
		}
	}
	if (window.fetch && method === 'fetch') {
		let requestConfig = {
			credentials: 'include',
			method: type,
			headers: {
				'Accept': 'application/json',
				'Content-Type': 'application/json;charset=utf-8'
			},
			mode: 'cors'
		}

		if (type === 'POST') {
			Object.defineProperty(requestConfig, 'body', {
				value: JSON.stringify(data)
			})
		}
		try {
			if (url.indexOf('save') !== -1 || url.indexOf('add') !== -1 || url.indexOf('delete') !== -1) {
				store.dispatch('setLoading', true)
			}
			const response = await fetch(url, requestConfig)
			const responseJson = await response.json()

			if (responseJson.code === 200) {
				setTimeout(() => {
					store.dispatch('setLoading', false)
				}, 500)
				return Promise.resolve(responseJson)
			} else {
				return Promise.reject(responseJson)
			}
		} catch (error) {
			throw new Error(error)
		}
	} else {
		return new Promise((resolve, reject) => {
			let requestObj
			if (window.XMLHttpRequest) {
				requestObj = new XMLHttpRequest()
			} else {
				this.$message.error('浏览器版本过低')
			}

			let sendData = ''
			if (type === 'POST') {
				sendData = JSON.stringify(data)
			}
			requestObj.setRequestHeader('Content-type', 'application/json;charset=utf-8')
			requestObj.setRequestHeader('Accept', 'application/json')
			requestObj.send(sendData)
			requestObj.onreadystatechange = () => {
				if (requestObj.readyState === 4) {
					if (requestObj.status === 200) {
						let obj = requestObj.response
						if (typeof obj !== 'object') {
							obj = JSON.parse(obj)
						}
						if (obj.code === 1 || obj.code === 200) {
							resolve(obj)
						} else {
							reject(requestObj)
						}
					} else {
						reject(requestObj)
					}
				}
			}
		})
	}
}
