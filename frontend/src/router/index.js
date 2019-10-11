import Vue from "vue";
import VueRouter from "vue-router";
import EmptyPage from "../components/pages/EmptyPage";
import MovieSearchPage from "../components/pages/MovieSearchPage";
import ProfileSearchPage from "../components/pages/ProfileSearchPage";
import AdminDataPage from "../components/pages/AdminDataPage";
import ClassifySearchPage from "../components/pages/ClassifySearchPage";
import GiveRatingPage from "../components/pages/GiveRatingPage";

Vue.use(VueRouter);

const router = new VueRouter({
    mode: "history",
    routes: [
        { path: "/", component: EmptyPage, name: "home" },
        {
            path: "/movies/search",
            component: MovieSearchPage,
            name: "movie-search"
        },
        {
            path: "/profile/search",
            component: ProfileSearchPage,
            name: "profile-search"
        },
        {
            path: "/admin/data",
            component: AdminDataPage,
            name: "admin-data"
        },
        {
            path: "/classify/search",
            component: ClassifySearchPage,
            name: "classify-search"
        },
        {
            path: "/giverating",
            component: GiveRatingPage,
            name: "give-rating"
        }
    ],
    scrollBehavior() {
        return { x: 0, y: 0 };
    }
});

export default router;
