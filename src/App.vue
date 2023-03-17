<template>
  <HelloWorld v-if="add" msg="Welcome to Your Vue.js App" @reload="reload_side()"/>
  <div v-if="!add" class="container">
    <vue-cal class="vuecal--blue-theme" :snap-to-time="15" editable-events :disable-views="['years', 'year','month']" locale="de" :events="events" ></vue-cal>
  </div>
  <div>
    <button class="button" @click="add = !add">Add</button>
  </div>

</template>

<script>
import HelloWorld from '@/components/HelloWorld.vue'
import VueCal from 'vue-cal'
import 'vue-cal/dist/vuecal.css'
import axios from "axios";
export default {
  name: 'App',
  components: {
    HelloWorld,
    VueCal
  },
  data: () =>{
    return{
      events: [],
      add: false
    }
  },
  mounted(){
    this.reload()
  },
  methods:{
    async reload(){
      const response = await axios.get('http://127.0.0.1:5000/' + 'calendarAPI/getAll',{}).catch(e => {
      alert('Error: ' +e)});

      this.events = response.data;
    },
    reload_side(){
      this.add = !this.add
      this.reload()
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

.container{
  height: 50rem;
}

.button{
  border: #2c3e50 1px;
  height: 30px;
  margin: 20px;
}

.schule{
  background-color: #5d8ec29c;
  padding: 10px;
  border-radius: 5px;
  color: white;
}


.private {
  background-color: #6c757d;
  padding: 10px;
  border-radius: 5px;
  color: white;
}

.urlaub {
  background-color: #6ed686b6;
  padding: 10px;
  border-radius: 5px;
  color: white;
}
</style>
