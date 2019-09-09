<template>
    <v-container class="pa-2" fluid grid-list-md>
        <v-layout column>
            <v-flex v-for="card in profileListCardsSliced" :key="card.id" pa-2>
                <ProfileListCard
                    :id="card.id"
                    :username="card.username"
                    :is_staff="card.is_staff"
                    :gender="card.gender"
                    :age="card.age"
                    :occupation="card.occupation"
                />
            </v-flex>
            <v-pagination v-if="maxPages > 1" v-model="page" :length="maxPages" />
        </v-layout>
    </v-container>
</template>

<script>
import ProfileListCard from "./ProfileListCard";
export default {
    components: {
        ProfileListCard
    },
    props: {
        profileListCards: {
            type: Array,
            default: () => new Array()
        }
    },
    data: () => ({
        cardsPerPage: 10,
        page: 1
    }),
    computed: {
        // pagination related variables
        profileListEmpty: function() {
            return this.profileListCards.length === 0;
        },
        maxPages: function() {
            return Math.floor(
                (this.profileListCards.length + this.cardsPerPage - 1) /
                    this.cardsPerPage
            );
        },
        profileListCardsSliced: function() {
            return this.profileListCards.slice(
                this.cardsPerPage * (this.page - 1),
                this.cardsPerPage * this.page
            );
        }
    }
};
</script>