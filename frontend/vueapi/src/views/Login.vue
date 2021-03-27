<template>
<div class="sign-in">
  <el-row :gutter="12">
    <el-col :span="8">
      <el-card shadow="always" class="box-card">
          <p v-if="incorrectAuth">Incorrect username or password entered - please try again</p>
          <form v-on:submit.prevent="login">
            <div style="margin-bottom: 45px;">
              <h1>Sign Here</h1>
            </div>
            <div style="margin-top: 15px;">
              <el-input type="text" name="username" id="user" v-model="username">
                <template slot="prepend">Username</template>
              </el-input>
            </div>
            <div style="margin-top: 15px;">
              <el-input type="password" name="password" id="pass" v-model="password">
                <template slot="prepend">Password</template>
              </el-input>
            </div>
            <div style="margin-top: 50px;">
              <el-button type="success" native-type="submit" round>Login</el-button>
            </div>
        </form>
      </el-card>
    </el-col>
  </el-row>
</div>
</template>

<script>
  export default {
    name: 'login',
    data () {
      return {
        username: '',
        password: '',
        incorrectAuth: false,
        input: '',
      }
    },
    methods: {
      login () { 
        this.$store.dispatch('userLogin', {
          username: this.username,
          password: this.password
        })
        .then(() => {
          this.$router.push({ name: 'books' })
        })
        .catch(err => {
          console.log(err)
          this.incorrectAuth = true
        })
        }
      }
  }
</script>

<style>
body { 
  background-color:#f4f4f4;
}
  .login{
    background-color:#fff;
    margin-top:10%;
  }
  input {
    padding: 25px 10px;
}

.box-card {
  width: 500px;
  height:350px;
}

.sign-in{
  flex: 1;
  display: flex;
  justify-content: center;
  align-items: center;
  margin-top: 150px;
}
</style>
