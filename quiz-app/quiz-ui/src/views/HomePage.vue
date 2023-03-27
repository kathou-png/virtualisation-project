<template>

  <head>
    <title>Home</title>
  </head>
  <h1>Home Page</h1>

  <router-link class="startLink" to="/start-new-quiz-page">Démarrer le quiz !</router-link>
  <br /><br />
  <h2>Classement</h2>
  <div v-for="scoreEntry in registeredScores" v-bind:key="scoreEntry.date">
    {{ scoreEntry.playerName }} - {{ scoreEntry.score }}
  </div>


  <br /><br /><br />

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
import quizApiService from "@/services/QuizApiService";
import participationStorageService from '../services/ParticipationStorageService';

export default {
  name: "HomePage",
  data() {
    return {
      registeredScores: []
    };
  },
  async created() {
    console.log("Composant Home page 'Created'")

    var participation = await quizApiService.getQuizInfo();

    for (var score of participation.data.scores) {
      this.registeredScores.push(score);
    }

  }
};
</script>

<style>
body {
  display: inline;
  text-align: center;
  color: darkblue;
}

.startLink {
  background-color: #ffffff;
  border: none;
  color: darkblue;
  text-align: center;
  margin: 4px 2px;
  transition: 0.3s;
  text-decoration: none;

}

.startLink:hover {
  background-color: #c7cdec;
}
</style>