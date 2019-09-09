<template>
    <div>
        <v-data-table
            :headers="headers"
            :items="movieData"
            :sort-by="['id']"
            :sort-desc="[false]"
            multi-sort
            class="elevation-1"
        >
            <template v-slot:item.title="props">
                <v-edit-dialog
                    :return-value.sync="props.item.title"
                    @save="save(props.item)"
                    @cancel="cancel"
                    @open="open"
                    @close="close"
                >
                    {{ props.item.title }}
                    <template v-slot:input>
                        <v-text-field
                            v-model="props.item.title"
                            :rules="[max50chars]"
                            label="Edit"
                            single-line
                            counter
                        ></v-text-field>
                    </template>
                </v-edit-dialog>
            </template>
            <template v-slot:item.genres="props">
                <v-edit-dialog
                    :return-value.sync="props.item.genres"
                    large
                    persistent
                    @save="save(props.item)"
                    @cancel="cancel"
                    @open="open"
                    @close="close"
                >
                    <div>{{ props.item.genres }}</div>
                    <template v-slot:input>
                        <div class="mt-4 title">Update Genres</div>
                    </template>
                    <template v-slot:input>
                        <v-text-field
                            v-model="props.item.genres"
                            :rules="[max50chars]"
                            label="Edit"
                            single-line
                            counter
                            autofocus
                        ></v-text-field>
                    </template>
                </v-edit-dialog>
            </template>
        </v-data-table>

        <v-snackbar v-model="snack" :timeout="3000" :color="snackColor">
            {{ snackText }}
            <v-btn text @click="snack = false">Close</v-btn>
        </v-snackbar>
    </div>
</template>

<script>
import api from "../api";

export default {
    props: {
        movieData: {
            type: Array,
            default: () => new Array()
        }
    },
    data() {
        return {
            headers: [
                {
                    text: "번호",
                    align: "left",
                    value: "id"
                },
                { text: "제목", value: "title" },
                { text: "장르", value: "genres", sortable: false },
                { text: "상영수", value: "viewCnt" },
                { text: "평점", value: "rating" }
            ],
            snack: false,
            snackColor: "",
            snackText: "",
            max50chars: v => v.length <= 50 || "Input too long!",
            pagination: {}
        };
    },
    methods: {
        save(data) {
            api.updateMovie(data);
            this.snack = true;
            this.snackColor = "success";
            this.snackText = "Data saved";
        },
        cancel() {
            this.snack = true;
            this.snackColor = "error";
            this.snackText = "Canceled";
        },
        open() {
            this.snack = true;
            this.snackColor = "info";
            this.snackText = "Dialog opened";
        },
        close() {
            console.log("Dialog closed");
        }
    }
};
</script>