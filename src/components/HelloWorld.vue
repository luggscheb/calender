<template>
  <div>
    <form action="/test" method="post" @submit="checkForm">
      <input type="datetime-local" placeholder="start" v-model="start" />
      <br>
      <input type="datetime-local" placeholder="end" v-model="end" />
      <br>
      <input type="text" placeholder="title" v-model="title" />
      <br>
        <select name="class" id="class" v-model="class_">
          <option value="private">Privat</option>
          <option value="schule">Schule</option>
          <option value="urlaub">Urlaub</option>
          <option value="dafault">Default</option>
        </select>
        <br>
        <input type="submit" @click.prevent="submitted" class="border-black text-black font-bold border-2 rounded-lg bg-backgroundGreenLight  w-40 h-11 text-lg p-2 m-5">
            
    </form>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: 'HelloWorld',
  props: {
    msg: String
  },
  data: () =>{
    return{
      start: "",
      end: "",
      title:"",
      class_: "",
    }
  },
  methods:{
    async submitted(){
      const q = {
        "start":this.start.replace("T"," "),
        "end":this.end.replace("T"," "),
        "title":this.title,
        "class":this.class_
      }
      await axios.post('http://127.0.0.1:5000/' + 'calendarAPI/addEvent',q).catch(e => {
      alert('Error: ' +e)});
        this.$emit("reload",false)
    
    }
  }
}
</script>

<style scoped>

</style>
