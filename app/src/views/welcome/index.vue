<template>
    <div class="home-container">
        <el-button size="mini" class="record" @click="dialogFormVisible = true">聊天记录</el-button>
        <div class="msgFig">     
            <el-input v-model="msg" class="msg" placeholder="你想问什么呢" @keyup.enter.native="sendData(msg)"></el-input>
            <p v-if="!loading" class="reMsg">{{ reMsg }}</p>
            <i v-else class="el-icon-loading"></i>
        </div>
        <el-dialog title="聊天记录" :visible.sync="dialogFormVisible">
            <section class="chats" v-if="Boolean(chatList.length)">
                <div v-for="(item, index) in chatList" :key="index" :class="{'letMe':item.type==1, 'letSer':item.type==0}">
                    <p>
                        <span>{{ item.name }}</span>
                        <el-date-picker v-model="item.time" size="mini" type="datetime" disabled placeholder=""></el-date-picker>
                    </p>
                    <p>{{ item.txt }}</p>
                </div>
            </section>
            <center v-else>暂无记录</center>
            <div slot="footer" class="dialog-footer">
                <el-button size="mini" @click="dialogFormVisible = false">关 闭</el-button>
            </div>
        </el-dialog>
    </div>
</template>

<script>
import { sendMsg } from '@/api/getData'
export default {
    name: 'home',
    data() {
        return {
            msg: '',
            reMsg: '',
            loading: false,
            dialogFormVisible: false,
            chatList: [],
        }
    },

    methods: {
        sendData(msg){
            this.loading = true;
            this.chatList.push({name:'你', time:new Date(), txt:msg, type:1})
            sendMsg({'msg': msg}).then(res =>{
                console.log(res)
                this.loading = false;
                this.reMsg = res.data.reply;
                this.chatList.push({name:'服务器', time:new Date(), txt:res.data.reply, type:0})
            }).catch(err =>{
                this.reMsg = '服务器已断开连接...';
                this.chatList.push({name:'服务器', time:new Date(), txt:'服务器已断开连接...', type:0})
                this.loading = false;
            })
            
        }
    }
}
</script>

<style lang="scss">
.home-container{
    .msgFig{
        margin: 10% 30%;
    }
    .record{
        position: fixed;
        right: 10px;
        top: 10px;
    }
    .el-icon-loading{
        margin: 10px 0px;
    }
    .reMsg{
        color: blue;
        padding: 0 15px;
    }
    .msg{
        box-shadow: 10px 10px 5px #e5e5e5;
    }
    .chats{
        border: 1px solid #e5e5e5;
        padding: 10px;
        max-height: 300px;
        overflow-y: auto;
        >div{
            margin-bottom: 10px;
        }
        p{
            margin: 0px;
        }
        .letSer{
            span, .el-input__inner{
                color: blue;
                margin: 0 5px 0 0;
            }
        }
        .letMe{
            span, .el-input__inner{
                color: green;
                margin: 0 5px 0 0;
            }
        }
    }
}
</style>