<template>
    <div class="menu">
        <el-row>
            <el-col :span="6">
                <div class="grid-content bg-purple">
                    <el-tree :data="data" class="tree" highlight-current :props="defaultProps" @node-click="handleNodeClick"></el-tree>
                </div>
            </el-col>
            <el-col :span="16">
                <div class="grid-content bg-purple-light">
                    <div class="btn">
                        <el-button type="primary" size="mini" class="add" @click="addData()">添加</el-button>
                        <el-button type="success" size="mini" class="save">保存</el-button>
                        <el-button type="danger" size="mini" :disabled="!Boolean(selected)" class="delete" @click="delData">删除</el-button>
                        <el-button type="info" size="mini" :disabled="!Boolean(selected)" class="cancel" @click="selected = null;">取消选中</el-button>
                    </div>
                    <el-form :model="formLabelAlign" class="searchForm" :inline="true" >
                        <el-form-item label="名称" prop="">
                            <el-input v-model="formLabelAlign.name" size="mini" ></el-input>
                        </el-form-item>
                        <el-form-item label="启用" prop="">
                            <el-checkbox v-model="formLabelAlign.flagUse"></el-checkbox>
                        </el-form-item>
                        <el-form-item label="上级" prop="">
                            <el-input v-model="formLabelAlign.naPar" size="mini" disabled></el-input>
                        </el-form-item>
                    </el-form>
                </div>
            </el-col>
        </el-row>
    </div>
</template>

<script>
import { getMenu } from '@/api/getData'

export default {
    name: 'adminMenu',

    data() {
        return {
            selected: null,
            formLabelAlign: {},
            data: [{
                label: '一级 1',
                children: [{
                    label: '二级 1-1',
                    children: [{
                    label: '三级 1-1-1'
                    }]
                }]
                }, {
                label: '一级 2',
                children: [{
                    label: '二级 2-1',
                    children: [{
                    label: '三级 2-1-1'
                    }]
                }, {
                    label: '二级 2-2',
                    children: [{
                    label: '三级 2-2-1'
                    }]
                }]
                }, {
                label: '一级 3',
                children: [{
                    label: '二级 3-1',
                    children: [{
                    label: '三级 3-1-1'
                    }]
                }, {
                    label: '二级 3-2',
                    children: [{
                    label: '三级 3-2-1'
                    }]
                }]
            }],
            defaultProps: {
                children: 'children',
                label: 'label'
            }
        }
    },

    created() {
        this.init();
    },

    methods: {

        init(){

        },

        addData(){
            if(this.selected){
                this.formLabelAlign.naPar = this.selected.label;
            }

            let fd = new FormData();
            // fd.append('username', 'xx');
            // fd.append('password', 'xx');

            fetch('http://127.0.0.1:8081/blog/api/menu', {
                method: 'post',
                body: fd
            }).then(res =>{
                console.log(res)
            })
            return

            getMenu().then(res =>{
                console.log(res)
            }).catch(err =>{
                
            })
        },

        delData(){
            this.$confirm('是否删除该节点?', '提示', {
                confirmButtonText: '删除',
                cancelButtonText: '取消',
                type: 'warning'
                }).then(() => {
                    
                }).catch(() => {});
        },

        handleNodeClick(val) {
            console.log(val)
            this.selected = val;
        },
    }
}
</script>

<style lang="scss" scoped>
    .el-tree{
        height: 300px;
        margin-right: 20px;
        border: 1px solid #cfcfcf;
    }
</style>

