export default {
    
    clear() {
        window.localStorage.clear();
    },

    savePlayerName(playerName) {
        window.localStorage.setItem("playerName", playerName);
    },
    getPlayerName() {
        return window.localStorage.getItem('playerName');
    },

    saveParticipationScore(participationScore) {
        window.localStorage.setItem("participationScore", participationScore);
    },
    getParticipationScore() {
        return window.localStorage.getItem('participationScore');
    },

    saveScores(scores) {
        window.localStorage.setItem("scores", participationScore);
    },
    getScore() {
        return window.localStorage.getItem('scores');
    }


};