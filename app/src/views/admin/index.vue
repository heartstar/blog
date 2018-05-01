<template>
    <el-tabs v-model="activeName" type="border-card">
        <el-tab-pane label="首页配置" name="menu">
            <admin-menu></admin-menu>
        </el-tab-pane>
        <el-tab-pane label="文章">
            <admin-article></admin-article>
        </el-tab-pane>
        <el-tab-pane label="角色管理">
            
        </el-tab-pane>
        <el-tab-pane label="定时任务补偿">
            
        </el-tab-pane>
    </el-tabs>
</template>

<script>

import adminMenu from '@/views/admin/menu'
import adminArticle from '@/views/admin/article'

export default {
    name: 'adminIndex',
    components:{
        adminMenu,
        adminArticle
    },

    data() {
        return {
            activeName: 'menu',
        }
    }
}
</script>

<style lang="sass" scoped>

</style>

