<template>
	<div class="app-main">

		<transition name="fade" mode="out-in">
			<router-view></router-view>
			<!-- <keep-alive :include='cachedViews'>
				<router-view></router-view>
			</keep-alive> -->
		</transition>
	</div>
</template>

<script>
import { getIndex } from '@/api/getData'
export default {
	name: 'AppMain',
	data(){
		return {
			bodyHeight:0
		}
    },
    
    mounted(){
        getIndex().then(res =>{
            console.log(res);
        }).catch(err =>{})
    }
}
</script>

<style rel="stylesheet/scss" lang="scss" scoped>
  .app-main{
	margin:0 15px;
	background:#fff;
	border-radius:0 10px 10px 10px;
  }
</style>