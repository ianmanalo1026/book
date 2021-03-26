<template>
    <div class="book">
        <h1>Hello World</h1>
        <div v-for="book in APIData" :key="book.id" >
        <h4>{{book.title}}</h4>
        <h4>{{book.description}}</h4>
        <h4>{{book.image}}</h4>
      </div>
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

</style>