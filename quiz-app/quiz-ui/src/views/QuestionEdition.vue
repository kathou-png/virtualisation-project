<template>
    <div class="questionslist">
        <h1>Questions List</h1>
        <form @submit="checkForm" method="post">
            <p>
                <label for="position">Position</label>
                <input type="number" name="position" id="position" v-model="position" min="0">
            </p>

            <p>
                <label for="title">Title</label>
                <input type="text" name="title" id="title" v-model="title">
            </p>

            <p>
                <label for="content">Content</label>
                <input type="text" name="content" id="content" v-model="content">
            </p>

            <p>
                Image
            </p>

            <p>
                <input type="submit" value="Submit">
                <input type="submit" value="">  
            </p>
        </form>
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
