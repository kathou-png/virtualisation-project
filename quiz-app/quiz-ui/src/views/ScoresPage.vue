<template>
  <h1>Scores Page</h1>
  <!--<QuestionManager :question="currentScore" @endQuiz="launchScores" />
  <button @click="launchScores">Get me the score</button>
  <button @click="returnHome">Home</button>
  -->
  <p>Bravo, votre score est de : {{ this.currentScore }}</p>

  <div class="container">
    <div>
      <table>
        <thead>
          <td><b>GLOBAL</b></td>
        </thead>
        <tbody>
          <tr><br></tr>
          <table border = "1">
            <thead>
              <td><b>Date</b></td>
              <td><b>Player Name</b></td>
              <td><b>Score</b></td>
            </thead>
            <tbody v-for="score in scores">
              <tr>
                <td>
                  <p>{{ score.date }}</p>
                </td>
                <td>
                  <p>{{ score.playerName }}</p>
                </td>
                <td>
                  <p>{{ score.score }}</p>
                </td>
              </tr>
            </tbody>
          </table>
        </tbody>
      </table>
    </div>

    <div>
      <table>
        <thead>
          <td><b>PLAYER</b></td>
        </thead>
        <tbody>
          <tr><br></tr>
          <table border = "1">
            <thead>
              <td><b>Date</b></td>
              <td><b>Player Name</b></td>
              <td><b>Score</b></td>
            </thead>
            <tbody v-for="score in scores">
              <tr v-if="score.playerName === this.username">
                <td>
                  <p>{{ score.date }}</p>
                </td>
                <td>
                  <p>{{ score.playerName }}</p>
                </td>
                <td>
                  <p>{{ score.score }}</p>
                </td>
              </tr>
            </tbody>
          </table>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
import quizApiService from "@/services/QuizApiService";
import participationStorageService from '../services/ParticipationStorageService';

export default {
  name: "Scores",
  data() {
    return {
      username: '',
      currentScore: 0,
      participationData: 0,
      scores: []

    };
  },

  async created() {
    this.participation();
  },

  methods: {
    async returnHome() {
      this.$router.push('/');
    },
    async participation() {
      var participation = await quizApiService.getQuizInfo();
      this.currentScore = participationStorageService.getParticipationScore();
      this.username = participationStorageService.getPlayerName();

      for (var score of participation.data.scores) {
        this.scores.push(score);
      }

    },
  }
};
</script>

<style>
table {
  border-collapse: collapse;
  margin-left: auto;
  margin-right: auto;
  text-align: center;
  width: 500px;
}

.container {
  align-content: center;
  display: flex;
}

.container div {
  align-items: center;
  margin: 50px;
}

</style>