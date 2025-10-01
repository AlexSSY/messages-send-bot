import { createRouter, createWebHistory } from "vue-router";

// Импорт страниц
import Home from "../views/Home.vue";
import Profile from "../views/Profile.vue";
import Add from "../views/Add.vue";
import Code from "../views/Code.vue";

const routes = [
  { path: "/", name: "Home", component: Home },
  { path: "/profile", name: "Profile", component: Profile },
  { path: "/add", name: "Add", component: Add },
  { path: "/code/:phoneNumber", name: "Code", component: Code, props: true },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
