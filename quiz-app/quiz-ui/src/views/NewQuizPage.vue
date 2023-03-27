<template>
  <h1>New Quiz Page</h1>
  <p>Saisissez votre nom :</p>
  <input type="text" v-model="username">
  <p>{{ username }}</p>
  <br>
  <button @click="launchNewQuiz">GO!</button>


  <br> <br> <br> <br>

  <body>
    <img alt="pokeball" class="logo" src="@/assets/pokeball.png" width="120" style="margin-left: 0px;" />
    <img alt="mew" class="logo" src="@/assets/mew.png" width="120" />
    <img alt="eevee" class="logo" src="@/assets/eevee.png" width="120" />
    <img alt="pikachu" class="logo" src="@/assets/pikachu.png" width="120" />
    <img alt="snorlax" class="logo" src="@/assets/snorlax.png" width="120" />
    <img alt="pokeball" class="logo" src="@/assets/pokeball.png" width="120" />
  </body>


</template>

<script>
//import participationStorageService from "@/ParticipationStorageService";

import ParticipationStorageService from '../services/ParticipationStorageService';

export default {

  name: "NewQuizPage",
  data() {
    return {
      username: ''
    };
  },
  methods: {
    launchNewQuiz() {
      console.log("Launch new quiz with", this.username);
      ParticipationStorageService.savePlayerName(this.username);
      // const playerName = participationStorageService.getPlayerName();
      // this.$router.push('/questions');
      this.$router.push('/manager');
    },
  },
  // async created() {
  //   console.log("Composant New Quiz page 'Created'")
  // }
};
</script>

<style>
</style>