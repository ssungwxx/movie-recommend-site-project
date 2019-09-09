<!-- 영화 검색 페이지 -->
<template>
    <v-container grid-list-md text-center>
        <v-layout justify-center wrap>
            <!-- 검색 폼 -->
            <v-flex xs6>
                <div class="display-2 pa-10">유저 검색</div>
                <ProfileSearchForm :submit="searchProfiles" />
            </v-flex>
            <!-- 검색 결과 -->
            <v-flex xs7>
                <ProfileList :profile-list-cards="profileList" />
            </v-flex>
        </v-layout>
    </v-container>
</template>

<script>
import { mapState, mapActions } from "vuex";
import ProfileSearchForm from "../ProfileSearchForm";
import ProfileList from "../ProfileList";
export default {
    components: {
        ProfileList,
        ProfileSearchForm
    },
    data: () => ({}),
    computed: {
        ...mapState({
            profileList: state => state.data.profileSearchList
        })
    },
    methods: mapActions("data", ["searchProfiles"])
};
</script>
