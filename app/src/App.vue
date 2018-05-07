<template>
    <div id="app">
        <router-view v-loading="loading" element-loading-text="加载中..."></router-view>
    </div>
</template>

<script>
import { mapGetters } from 'vuex';
export default {
    name: 'App',
    computed: {
        ...mapGetters([
            'loading',
        ]),
    },
}
</script>

<style lang="scss">
@import './styles/index.scss'; // 全局自定义样式
</style>
