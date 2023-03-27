<template>
    <h1>Question {{ currentQuestionPosition }} / {{ totalNumberOfQuestion }} </h1>
    <QuestionDisplay :question="currentQuestion" @answer-selected="answerClickedHandler" />
    <!-- <p @input="$emit('current-score', currentScore)">{{currentScore}}</p> -->
</template>

<script>
import QuestionDisplay from "@/views/QuestionDisplay.vue";
import quizApiService from "@/services/QuizApiService";
import participationStorageService from '../services/ParticipationStorageService';
// import ScoresPage from "@/views/ScoresPage.vue";

// export {
//     currentScore
// }

export default {
    data() {
        return {
            currentQuestion: {
                questionImage: "",
                questionTitle: "No title",
                questionText: "No text",
                possibleAnswers: []
            },
            currentQuestionPosition: 1,
            totalNumberOfQuestion: 0,
            currentScore: 0,
            listAnswersSelected: [],
            currentName: ""
        };
    },
    components: {
        QuestionDisplay
    },
    async created() {
        console.log("Composant created 'Created'")
        var quiz = await quizApiService.getQuizInfo();
        this.totalNumberOfQuestion = quiz.data.size;
        var quizQuestion = await quizApiService.getQuestion(this.currentQuestionPosition);
        this.loadQuestionByPosition(quizQuestion.data.position);
    },
    methods: {
        async loadQuestionByPosition(position) {
            var quizQuestion = await quizApiService.getQuestion(position);
            var answers = [];
            var possibleAnswers = Object.entries(quizQuestion.data.possibleAnswers);
            for (var [key, val] of possibleAnswers)
                answers.push(val.text);
            this.currentQuestion.questionImage = quizQuestion.data.image;
            this.currentQuestion.questionTitle = quizQuestion.data.title;
            this.currentQuestion.questionText = quizQuestion.data.text;
            this.currentQuestion.possibleAnswers = answers;
        },
        async answerClickedHandler(position) {
            var quizQuestion = await quizApiService.getQuestion(this.currentQuestionPosition);
            var possibleAnswers = quizQuestion.data.possibleAnswers;
            var correctAnswer = 0;

            this.listAnswersSelected.push(position);

            // Verifie la reponse
            for (let i = 0; i < possibleAnswers.length; i++) {
                if (possibleAnswers[i].isCorrect == true) {
                    correctAnswer = i;
                    console.log("position de la bonne rep : " + i);
                }
            }

            // Incremente score si correcte
            if ((position - 1) == correctAnswer) {
                this.currentScore += 1;
            }

            // Changement de question
            if (this.currentQuestionPosition >= this.totalNumberOfQuestion) {
                this.endQuiz();
            }
            else {
                this.currentQuestionPosition += 1;
                this.loadQuestionByPosition(this.currentQuestionPosition);
            }
        },

        async endQuiz() {
            participationStorageService.saveParticipationScore(this.currentScore);
            console.log("Composant endQuiz 'Created'");

            console.log(this.listAnswersSelected)
            this.currentName = participationStorageService.getPlayerName();

            var body = { playerName: this.currentName, answers: this.listAnswersSelected };

            var bodyStr = JSON.stringify(body);
            var res = await quizApiService.postParticipation(bodyStr);

            this.$router.push('/scores');
        }
    },
};
</script>


<style>
</style>