<template>
  <div class="questionslist">
    <h1>Questions List</h1>
    <button @click="editQuestion">Edit</button>
    <button @click="deleteQuestion">Delete</button>
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
    editQuestion(){
      console.log("Edit question");
    },
    deleteQuestion(){
      console.log("Delete question");
    },
    async created() {
        console.log("Composant New Quiz page 'Created'")
    }
  }
};
</script>

<style>
@media (min-width: 1024px) {
  .about {
    min-height: 100vh;
    display: flex;
    align-items: center;
  }
}
</style>
