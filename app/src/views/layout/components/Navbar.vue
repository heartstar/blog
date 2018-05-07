<template>
    <div class="menu" ref="elMenu">
        <el-menu
            :default-active="activeIndex"
            class="el-menu-demo"
            mode="horizontal"   
            @select="handleSelect"
            background-color="#545c64"
            text-color="#fff"
            active-text-color="#ffd04b">
            <el-menu-item index="1"><router-link :to="{path: '/'}" >首页</router-link></el-menu-item>
            <el-submenu index="2">
                <template slot="title">随手小记</template>
                    <el-menu-item index="2-1"><router-link :to="{path: '/article'}" >全部</router-link></el-menu-item>
                    <el-menu-item v-for="(item, index) in menus" :key="index" index="2-" :data-code=item.code><router-link :to="{path: '/article/type/'+ item.code}" >{{ item.caption }}</router-link></el-menu-item>
            </el-submenu>
            <el-menu-item index="3">小工具</el-menu-item>
            <el-menu-item index="4">在路上</el-menu-item>
        </el-menu>
    </div>
</template>

<script>
import { getMenu } from '@/api/getData'
export default {
    data() {
        return {
            activeIndex: '1',
            menus: null,
        };
    },

    mounted () {
        // window.addEventListener('scroll', this.handleScroll)
    },

    created() {
        getMenu().then(res =>{
            this.menus = res.data;
        }).catch(err =>{})
    },

    methods: {
        handleScroll(){
           
        },

        handleSelect(key, keyPath) {
            
        },
    }
}
</script>
<style lang="scss" scoped>
a{
    color: #fff;
}
.el-menu--horizontal a{
    display: inline-block;
    width: 100%;
}
</style>