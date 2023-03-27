import { createRouter, createWebHistory } from 'vue-router'
import HomePage from '../views/HomePage.vue'
import NewQuizPage from '../views/NewQuizPage.vue'
// import QuestionsPage from '../views/QuestionsPage.vue'
// import AdminPage from '../views/AdminPage.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "HomePage",
      component: HomePage,
    },
    {
      path: "/start-new-quiz-page",
      name: "NewQuiz",
      component: NewQuizPage,
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/AboutView.vue')
    },
    {
      path: "/questions",
      name: "Questions",
      component: () => import('../views/QuestionsPage.vue')
    },
    {
      path: "/admin",
      name: "Admin",
      component: () => import('../views/Admin.vue')
    },
    // {
    //   path: "/questionslist",
    //   name: "QuestionsList",
    //   component: () => import('../views/QuestionsList.vue')
    // },
    {
      path: "/manager",
      name: "QuestionsManager",
      component: () => import('../views/QuestionsManager.vue')
    },
    {
      path: "/scores",
      name: "Scores",
      component: () => import('../views/ScoresPage.vue')
    }
  ]
})

export default router
