<template>
  <div class="book" >
    <el-row :gutter="20">
      <div v-for="book in APIData" :key="book.id" >
        <el-col :span="8" :key="o" :offset="index > 0 ? 2 : 0">
          <el-card :body-style="{ padding: '0px' }">
            <img v-bind:src=book.image class="image">
            <div style="padding: 14px;">
              <span>{{book.title}}</span>
              <div style="padding: 14px;">
                <span>{{book.author}}</span>  
              </div>
              
              <div class="bottom clearfix">
              <p class="description">{{book.description}}</p>
              </div>
            </div>
          
          </el-card>
        </el-col>
        </div>
      </el-row>
    </div>
</template>

<script>
  import { getAPI } from '../axios-api'
  import { mapState } from 'vuex'
  export default {
    name: 'Books',
    onIdle () {
      this.$store.dispatch('userLogout')
        .then(() => {
          this.$router.push({ name: 'login' })
        })
    },
    components: {

    },
    computed: mapState(['APIData']),
    created () {
        getAPI.get('/book/', { headers: { Authorization: `Bearer ${this.$store.state.accessToken}` } })
          .then(response => {
            this.$store.state.APIData = response.data
          })
          .catch(err => {
            console.log(err)
          })
    }
  }
</script>


<style scoped>
  .description {
    font-size: 35px;
    color: rgb(20, 19, 19);
  }
  
  .image {
    width: 100%;
    display: block;
  }

  .clearfix:before,
  .clearfix:after {
      display: table;
      content: "";
  }
  
  .clearfix:after {
      clear: both
  }

  .book {
      margin: auto;
      width: 60%;
      padding: 10px;
  }
</style>