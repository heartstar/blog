<template>
    <div class="article">
        <div v-show="!showData" >
            <div class="btns">
                <el-button type="primary" size="mini" class="add" @click="addData">新增</el-button>
                <el-button type="success" size="mini" :disabled="!Boolean(selected)" class="update" @click="updateData">修改</el-button>
                <el-button type="danger" size="mini" :disabled="!Boolean(selected)" class="delete" @click="delData">删除</el-button>
            </div>
            <el-table :data="tableData" border highlight-current-row max-height="550" style="width: 100%" @row-click="handleSelectionChange">
                <el-table-column
                    type="index"
                    label="序号"
                    width="50">
                </el-table-column>
                <el-table-column label="类型" width="100">
                    <template slot-scope="scope">
                        <el-select v-model="scope.row.category" placeholder="" disabled>
                            <el-option v-for="item in types" :key="item.code" :label="item.caption" :value="item.code"></el-option>
                        </el-select>
                    </template>
                </el-table-column>
                <el-table-column label="显示" width="50">
                    <template slot-scope="scope">
                        <span>{{ scope.row.show?'是':'否' }}</span>
                    </template>
                </el-table-column>
                <el-table-column label="创建日期" width="160">
                    <template slot-scope="scope">
                        <el-date-picker v-model="scope.row.create_date" size="mini" type="datetime" disabled placeholder=""></el-date-picker>
                    </template>
                </el-table-column>
                <el-table-column label="修改日期" width="160">
                    <template slot-scope="scope">
                        <el-date-picker v-model="scope.row.update_time" size="mini" type="datetime" disabled placeholder=""></el-date-picker>
                    </template>
                </el-table-column>
                <el-table-column label="标题">
                    <template slot-scope="scope">
                        <span>{{ scope.row.title.substring(0, 80)+'...' }}</span>
                    </template>
                </el-table-column> 
                <el-table-column
                    prop="keyword"
                    label="关键字">
                </el-table-column> 
                <el-table-column label="内容">
                    <template slot-scope="scope">
                        <span>{{ scope.row.content.substring(0, 50)+'...' }}</span>
                    </template>
                </el-table-column>
            </el-table>
            <el-pagination
                @current-change="handleCurrentChange"               
                :page-size="page.pageSize"
                layout="total, prev, pager, next, jumper"
                :total="page.total">
            </el-pagination>
        </div>     
        <div v-show="showData">
            <div class="btns">
                <el-button type="success" size="mini" class="save" @click="saveData">保存</el-button>
                <el-button size="mini" @click="cancel">取消</el-button>
            </div>
            <el-form ref="form" :model="form" label-width="80px" :rules="rules">
                <el-form-item label="类别" prop="category">
                    <el-select v-model="form.category" size="mini" placeholder="请选择">
                        <el-option v-for="item in types" :key="item.code" :label="item.caption" :value="item.code"></el-option>
                    </el-select>
                </el-form-item>
                <el-form-item label="标题" prop="title">
                    <el-input v-model="form.title" size="mini"></el-input>
                </el-form-item>   
                <el-form-item label="关键字" prop="keyword">
                    <el-input v-model="form.keyword" size="mini"></el-input>
                </el-form-item>  
                <!-- <el-form-item label="编辑器">
                    <el-radio v-model="radio" label="markdown">markdown</el-radio>
                    <el-radio v-model="radio" label="richText">富文本</el-radio>
                </el-form-item>  -->
                <el-form-item label="显示">
                     <el-checkbox v-model="form.show"></el-checkbox>
                </el-form-item> 
                <el-form-item label="内容" prop="content">
                    <markdown-editor id="contentEditor" ref="contentEditor" preview-class="markdown-body" v-model="form.content" :height="300" :zIndex="20" @input="markdown2Html"></markdown-editor>
                </el-form-item>  
                <el-button @click="markdown2Html" style="margin-top:80px;" type="primary" icon="el-icon-document">转为HTML</el-button>
                <div v-html="html"></div>
            </el-form>
        </div>
    </div>
</template>

<script>
import { getMenu, getArticle, addArticle, delArticle } from '@/api/getData'
import markdownEditor from '@/components/MarkdownEditor'

export default {
    name: 'adminArticle',
    components:{
        markdownEditor
    },

    data() {
        return {
            tableData: null,
            selected: null,
            types: null,
            showData: false,
            radio: 'markdown',
            html: '',
            form: {
                show: true,
                content: '',
            },
            page: {
                paramsId: undefined,
                pageNum: 1,
                pageSize: 10,
                total: null,
            },
            rules: {
                category: [
                    { required: true, message: '请选择文章类别', trigger: 'change' }
                ],
                title: [
                    { required: true, message: '请填写文章标题', trigger: 'blur' }
                ],
                keyword: [
                    { required: true, message: '请填写关键字', trigger: 'blur' }
                ],
                content: [
                    { required: true, message: '请填写文章内容', trigger: 'blur' }
                ]
            } 
        }
    },

    created() {
        this.init();

        getMenu().then(res =>{
            this.types = res.data;
        }).catch(err =>{})
    },

    methods: {

        init(){

            getArticle(this.page).then(res =>{
                this.tableData = res.data; 
                this.page.total = res.total;
            }).catch(err =>{
                console.log(err)
            })
            this.selected = null;
        },

        saveData(){
            this.$refs.form.validate((valid) => {
                if (valid) {
                    addArticle(this.form).then(res =>{
                        this.$message.success('保存成功');
                    }).catch(err =>{})
                } else {
                    return false;
                }  
            })  
        },  

        addData(){   
            this.$refs.form.resetFields(); 
            this.form = {};   
            this.form.show = true;
            this.form.content = '';
            this.showData = true;
        },

        updateData(){
            this.$refs.form.resetFields(); 
            this.form = this.selected;
            this.showData = true;
        },

        delData(){
            this.$confirm('是否删除该节点?', '提示', {
                confirmButtonText: '删除',
                cancelButtonText: '取消',
                type: 'warning'
                }).then(() => {
                    delArticle(this.selected.articleId).then(res =>{
                        this.$message.success('删除成功');
                        this.init();
                    }).catch(err =>{
                        this.$message.error('删除失败');
                    });
                }).catch(err =>{});
        },

        handleSelectionChange(row){
            this.selected = row;
        },

        cancel(){
            this.showData = false;
            this.init();
        },

        handleCurrentChange(index){
            this.page.pageNum = index;
            this.init();
        },

        markdown2Html(){
            import('showdown').then(showdown => {
                const converter = new showdown.Converter()
                this.html = converter.makeHtml(this.form.content)
            })
        },
    }
}
//vue-simplemde
</script>

<style lang="scss">
    @import '~github-markdown-css';
</style>




