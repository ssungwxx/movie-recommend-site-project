<template>
    <v-hover v-slot:default="{ hover }">
        <v-card :elevation="hover ? 8 : 2">
            <v-layout align-center py-4 pl-4>
                <v-flex text-center>
                    <v-container grid-list-lg pa-0>
                        <v-layout column>
                            <v-list-item>
                                <v-list-item-content>
                                    <v-list-item-title class="headline">{{ username }}</v-list-item-title>
                                    <v-list-item-subtitle v-if="is_staff">관리자</v-list-item-subtitle>
                                    <v-list-item-subtitle v-else>회원</v-list-item-subtitle>
                                </v-list-item-content>
                            </v-list-item>
                            <v-card-text>
                                <v-layout justify-center>
                                    성별 : {{gender}}
                                    <br />
                                    나이 : {{age}}
                                    <br />
                                    직업 : {{occupation}}
                                </v-layout>
                            </v-card-text>
                        </v-layout>
                    </v-container>
                </v-flex>
            </v-layout>
        </v-card>
    </v-hover>
</template>

<script>
import { mapActions } from "vuex";
export default {
    props: {
        id: {
            type: Number,
            default: 0
        },
        username: {
            type: String,
            default: ""
        },
        is_staff: {
            type: Boolean,
            default: false
        },
        gender: {
            type: String,
            default: ""
        },
        age: {
            type: Number,
            default: 0
        },
        occupation: {
            type: String,
            default: ""
        }
    }
};
</script>