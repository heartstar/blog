<template>
    <div class="login">
        <el-form :model="ruleForm" status-icon :rules="rules" ref="ruleForm" label-width="100px" class="ruleForm" @keyup.enter.native="submitForm">
            <el-form-item label="用户名" prop="user">
                <el-input v-model="ruleForm.user" size="mini" auto-complete="off"></el-input>
            </el-form-item>
            <el-form-item label="密码" prop="password">
                <el-input v-model="ruleForm.password" size="mini" type="password" ></el-input>
            </el-form-item>
            <el-form-item>
                <el-button type="primary" size="mini" @click="submitForm" >登录</el-button>
            </el-form-item>
        </el-form>
    </div>
</template>

<script>
import md5 from 'js-md5';
export default {
    name: 'adminLogin',

    data() {
        return {
            ruleForm:{},
            rules: {
                user: [
                    { required: true, message: '请填写用户名', trigger: 'blur' }
                ],
                password: [
                    { required: true, message: '请填写密钥', trigger: 'blur' }
                ],
            }
        }
    },

    created() {

    },

    methods: {

        submitForm(){
            this.$refs.ruleForm.validate((valid) => {
                if (valid) {
                    if(md5(this.ruleForm.user) != '4911748366a4b2cd0b4ea988219d14b7' || md5(this.ruleForm.password) != '4911748366a4b2cd0b4ea988219d14b7'){
                        this.$message.error('用户名或密钥错误');
                        this.ruleForm.user = null;
                        this.ruleForm.password = null;
                        this.$nextTick(() =>{
                            this.$refs.ruleForm.resetFields();
                        })
                    } else {
                        this.$store.dispatch('setLogin', true);
                        this.$router.push({ path: '/admin' });
                    }
                } else {
                    return false;
                }
            })
        }

    }
}
</script>

<style lang="scss" scoped>
    .ruleForm{
        width: 20%;
        margin: 200px 40% 0;
        text-align: center;
    }
</style>

