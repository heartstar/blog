<template>
    <div class="menu">
        <el-menu
            :default-active="activeIndex2"
            class="el-menu-demo"
            mode="horizontal"
            @select="handleSelect"
            background-color="#545c64"
            text-color="#fff"
            active-text-color="#ffd04b">
            <el-menu-item index="1">首页</el-menu-item>
            <el-submenu index="2">
                <template slot="title">随手小记</template>
                    <el-submenu index="2-1">
                        <template slot="title">web前端</template>
                        <el-menu-item index="2-1-1">vue</el-menu-item>
                        <el-menu-item index="2-1-2">css</el-menu-item>
                        <el-menu-item index="2-1-3">javascript</el-menu-item>
                    </el-submenu>
                    <el-submenu index="2-2">
                        <template slot="title">python</template>
                        <el-menu-item index="2-2-1">django</el-menu-item>
                        <el-menu-item index="2-2-2">tornado</el-menu-item>
                    </el-submenu>
                    <el-menu-item index="2-3">web mobile</el-menu-item>
            </el-submenu>
            <el-menu-item index="3">在路上</el-menu-item>
            <el-menu-item index="4"><a href="https://www.ele.me" target="_blank">订单管理</a></el-menu-item>
        </el-menu>
    </div>
</template>

<script>
import { getMenu } from '@/api/getData'
export default {
    data() {
        return {
        activeIndex: '1',
        activeIndex2: '1'
        };
    },

    mounted() {
        
    },

    methods: {
        handleSelect(key, keyPath) {
            console.log(key, keyPath);
        }
    }
}
</script>