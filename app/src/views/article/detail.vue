<template>
    <div class="articleDetail">
        <div class="container" v-if="detail">
            <div class="post">
                <h2 class="postTitle">{{ detail.title }}</h2>
                <div class="postDesc">
                    <span class="visits">阅读({{ detail.visits }})</span>
                    <el-date-picker v-if="Boolean(detail.update_time)" v-model="detail.update_time" size="mini" type="datetime" disabled placeholder=""></el-date-picker>
                </div>
                
                <div v-html="detail.content"></div>
            </div>
        </div>
        
        <p v-else>{{ time }}秒后跳转到列表页面</p>
    </div>
</template>

<script>
import { getArticleDetail } from '@/api/getData'

export default {
    name: 'articleDetail',

    data() {
        return {
            detail: null,
            time: 5,
        }
    },

    created() {
        this.time = 5;
        getArticleDetail({'id':this.$route.query.id}).then(res =>{           
            if(res.data){
                this.detail = res.data[0];
            }else{
                setInterval(() =>{   
                    this.time--;               
                    if(this.time < 1){
                        this.$router.push('/article')
                    }                            
                }, 1000)
            }
        }).catch(err =>{})
    },

    methods: {

    },

}
</script>

<style lang="scss" scoped>
.articleDetail{
    margin: 0 auto;
    width: 1000px;
    .container{
        width: 100%;
        margin-top: 10px;
        background: white;
        box-shadow: 0px 0px 8px #999;
        -moz-box-shadow: 0px 0px 8px #999;
        -web-kit-shadow: 0px 0px 8px #999;
        border-radius: 6px;
        -moz-border-radius: 6px;
        -web-kit-shadow: 6px;
        display: inline-block;
        .post{
            padding: 32px;
            .postTitle{
                font-size: 20px;
                padding-right: 64px;
                padding-left: 10px;
                border-left-width: 3px;
                border-left-style: solid;
                border-left-color: #2175bc;
            }
            .postDesc{
                border-bottom: 1px dashed #E8E7D0;
                text-align: right;
                margin: 20px 0px;
                padding: 5px 0px;
                .visits{
                    font-size: 12px;
                    color: #c0c4cc;
                    margin: 0 25px 0 0;
                }
            }
        }
    }
}
</style>


