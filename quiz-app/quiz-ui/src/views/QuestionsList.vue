<template>
  <div class="questionslist">
    <h1>Questions List</h1>
    <button @click="createQuestion">Create</button>
  </div>
</template>

<script>
export default {
  name: "QuestionsListPage",
  data() {
    return {
      username : ''
    };
  },
  methods:{
    createQuestion(){
      console.log("Create question");
    },
    async created() {
        console.log("Composant New Quiz page 'Created'")
    }
  }
};
</script>

<style>
</style>
