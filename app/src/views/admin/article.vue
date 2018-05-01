<template>
    <div class="article">
        <div class="btns">
            <el-button type="primary" size="mini" class="add" @click="addData()">新增</el-button>
            <el-button type="success" size="mini" :disabled="!Boolean(selected)" class="update" @click="updateData">修改</el-button>
            <el-button type="danger" size="mini" :disabled="!Boolean(selected)" class="delete" @click="delData">删除</el-button>
        </div>
        <el-table :data="tableData" border highlight-current-row height="550" style="width: 100%" @row-click="handleSelectionChange">
            <el-table-column
                type="index"
                label="序号"
                width="50">
            </el-table-column>
            <el-table-column prop="category" label="类型" width="80">
            </el-table-column>
            <el-table-column
                prop="title"
                label="标题">
            </el-table-column>
            <el-table-column label="创建日期">
                <template slot-scope="scope">
                    <el-date-picker v-model="scope.row.create_date" size="mini" type="datetime" disabled placeholder=""></el-date-picker>
                </template>
            </el-table-column>
            <el-table-column
                prop="content"
                label="内容">
            </el-table-column>
        </el-table>
        <el-dialog :title="textMap[dialogStatus]" :visible.sync="dialogVisible" width="70%">
            <el-form ref="form" :model="form" label-width="80px">
                <el-form-item label="类别">
                    <!-- <el-cascader expand-trigger="hover" :options="options" v-model="form.category" @change="handleChange"></el-cascader> -->
                    <el-input v-model="form.category"></el-input>
                </el-form-item>
                <el-form-item label="标题">
                    <el-input v-model="form.title"></el-input>
                </el-form-item>     
                <el-form-item label="日期">
                    <el-date-picker v-model="form.createDate" :clearable="false" type="datetime" placeholder="选择日期时间"></el-date-picker>
                </el-form-item>
                <el-form-item label="展示">
                     <el-checkbox v-model="form.show"></el-checkbox>
                </el-form-item> 
                <el-form-item label="内容">
                    <el-input type="textarea" rows="5" v-model="form.content"></el-input>
                </el-form-item>  
                <el-form-item>
                    <el-button type="primary" @click="saveData">提交</el-button>
                    <el-button @click="dialogVisible = false;">取消</el-button>
                </el-form-item>
            </el-form>
        </el-dialog>
    </div>
</template>

<script>
import { getMenu, getArticle, addArticle } from '@/api/getData'

export default {
    name: 'adminArticle',

    data() {
        return {
            tableData: null,
            selected: null,
            selectedOptions: [],
            form: {},
            dialogStatus: '',
            textMap: {
                update: '修改',
                create: '新增'
            },
            dialogVisible: false,
            options: [{
                value: 'zhinan',
                label: 'web前端',
                children: [{
                    value: 'shejiyuanze',
                    label: 'vue',
                    children: [{
                        value: 'yizhi',
                        label: 'css'
                        }, {
                        value: 'fankui',
                        label: 'javascript'
                    }]
                }, {
                    value: 'daohang',
                    label: '导航',
                    children: [{
                    value: 'cexiangdaohang',
                    label: '侧向导航'
                    }, {
                    value: 'dingbudaohang',
                    label: '顶部导航'
                    }]
                }]
                }, {
                value: 'ziyuan',
                label: '资源',
                children: [{
                    value: 'axure',
                    label: 'Axure Components'
                }, {
                    value: 'sketch',
                    label: 'Sketch Templates'
                }, {
                    value: 'jiaohu',
                    label: '组件交互文档'
                }]
            }],
        }
    },

    created() {
        this.init();

        this.form.createDate = new Date();
    },

    methods: {

        init(){
            // getMenu().then(res =>{
            //     console.log(res); 
            // }).catch(err =>{
            //     console.log(err)
            // })

            getArticle().then(res =>{
                this.tableData = res.data; 
            }).catch(err =>{
                console.log(err)
            })
        },

        saveData(){
            console.log(this.form)
            addArticle(this.form).then(res =>{
                this.$message.success('添加成功');
            }).catch(err =>{})
            //this.dialogVisible = false;
        },  

        addData(){      
            this.dialogStatus = 'create';
            this.dialogVisible = true;
        },

        updateData(){
            this.form = this.selected;
            this.dialogStatus = 'update';
            this.dialogVisible = true;
        },

        delData(){
            this.$confirm('是否删除该节点?', '提示', {
                confirmButtonText: '删除',
                cancelButtonText: '取消',
                type: 'warning'
                }).then(() => {
                    
                }).catch(() => {});
        },

        handleSelectionChange(row){
            this.selected = row;
        }
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

