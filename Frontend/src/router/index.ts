import { createRouter as createVueRouter, createWebHashHistory, Router } from "vue-router";
import Home from "../views/Home.vue";
import Profile from "../views/Profile.vue";
import Analisis from "../views/Analisis.vue";
import AdvancedAnalysis from "../views/AdvancedAnalysis.vue";
import { createAuthGuard } from "@auth0/auth0-vue";
import { App } from 'vue';

export function createRouter(app: App): Router {
  return createVueRouter({
    routes: [
      {
        path: "/",
        name: "home",
        component: Home
      },
      {
        path: "/profile",
        name: "profile",
        component: Profile,
        beforeEnter: createAuthGuard(app)
      },
      {
        path: "/analisis",
        name: "analisis",
        component: Analisis,
        beforeEnter: createAuthGuard(app)
      },
      {
        path: "/advancedAnalysis",
        name: "advancedAnalysis",
        component: AdvancedAnalysis,
        beforeEnter: createAuthGuard(app)
      }
    ],
    history: createWebHashHistory()
  })
}
