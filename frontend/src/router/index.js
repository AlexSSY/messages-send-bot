import { createRouter, createWebHistory } from "vue-router";

// Импорт страниц
import HomeView from "../views/HomeView.vue";
import AddView from "../views/AddView.vue";

const routes = [
  { path: "/", name: "Home", component: HomeView },
  { path: "/add", name: "Add", component: AddView },
  // { path: "/code/:phoneNumber", name: "Code", component: Code, props: true },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
