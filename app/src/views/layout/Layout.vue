<template>
	<div class='app-wrapper'>
		<navbar></navbar>
		<app-main></app-main>
	</div>
</template>

<script>
import { Navbar, AppMain } from './components'

export default {
	name: 'layout',
	components: {
		Navbar,
		AppMain,
	},
}
</script>

<style rel="stylesheet/scss" lang="scss" scoped>
	.app-wrapper {
		position: relative;
		height: 100%;
		width: 100%;
	}
</style>
