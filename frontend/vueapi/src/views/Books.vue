<template>
    <div class="book">
        <h1>Hello World</h1>
        <div v-for="book in APIData" :key="book.id" >
      <h4>{{book.user}}</h4>
      <h4>{{book.title}}</h4>
      <h4>{{book.description}}</h4>
      <h4>{{book.image}}</h4>

    </div>
    </div>
</template>

<script>
    import {getAPI} from '../axios-api'
    export default {
        name: 'Books',
        data() {
            return {
                APIData: []
            }
        },
            created () {
        getAPI.get('/book/',)
          .then(response => {
            console.log('Book API has recieved data')
            this.APIData = response.data
          })
          .catch(err => {
            console.log(err)
          })
    }
    }
</script>


<style scoped>

</style>