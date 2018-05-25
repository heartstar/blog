<template>
    <section>
        <router-link :to="{path: '/'}" style="padding:20px 0;display: inline-block;"><el-button type="success" size="mini">去主页</el-button></router-link>
        <el-tabs v-model="activeName" type="border-card" @tab-click="tabClick">
            <el-tab-pane label="首页配置" name="menu">
                <admin-menu></admin-menu>
            </el-tab-pane>
            <el-tab-pane label="文章">
                <admin-article></admin-article>
            </el-tab-pane>
            <el-tab-pane label="图片">
                <admin-image></admin-image>
            </el-tab-pane>
            <el-tab-pane label="待定">
                
            </el-tab-pane>          
        </el-tabs>
    </section>   
</template>

<script>

import adminMenu from '@/views/admin/menu'
import adminArticle from '@/views/admin/article'
import adminImage from '@/views/admin/image'

export default {
    name: 'adminIndex',
    components:{
        adminMenu,
        adminArticle,
        adminImage
    },

    data() {
        return {
            activeName: 'menu',
        }
    },

    methods: {
        tabClick(row){
            console.log(row)
        }
    }
}
</script>

<style lang="scss" scoped>

</style>

