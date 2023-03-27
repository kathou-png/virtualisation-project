<template>

    <body>
        <h2>{{ question.questionTitle }}</h2>
        <img class="centerImage" v-if="question.questionImage" :src="question.questionImage" />
        <h3>{{ question.questionText }}</h3>
        <p>Veuillez selectionner une réponse :</p>
        <ul class="no-bullets">
            <li v-for="answer in question.possibleAnswers" :key="answer">
                <a class="element" @click="$emit('answer-selected', question.possibleAnswers.indexOf(answer) + 1)">{{
                        answer
                }}</a>
            </li>
        </ul>

    </body>
</template>

<script>
export default {
    name: "QuestionDisplay",
    emits: ["answer-selected"],
    props: {
        question: {
            type: Object
        }
    },
    data() {
        return {
        };
    }
    // methods: {
    //     answerSelected(event) {
    //         this.$emit('answer-selected', question.possibleAnswers);
    //     }
    // }
};
</script>


<style>
.questionImage {
    height: 100%;
    width: 100%;
    max-width: 300px;
    max-height: 300px;
}

body {
    display: inline;
    text-align: center;
    color: darkblue;
}

.centerImage {
    display: block;
    margin-left: auto;
    margin-right: auto;
    max-width: 500px;
    max-height: 300px;
}

.no-bullets {
    list-style-type: none;
    padding: 0;
    /* Remove padding */
    display: table;

    text-align: center;
    margin: 0 auto;
}


.element {
    background-color: #ffffff;
    border: none;
    color: darkblue;
    text-align: center;
    margin: 4px 2px;
    transition: 0.3s;
    text-decoration: none;

}

.element:hover {
    background-color: #c7cdec;
}
</style>