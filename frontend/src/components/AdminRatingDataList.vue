<template>
    <div>
        <v-data-table
            :headers="headers"
            :items="ratingData"
            :sort-by="['id']"
            :sort-desc="[true]"
            multi-sort
            class="elevation-1"
        >
            <template v-slot:item.rating="props">
                <v-edit-dialog
                    :return-value.sync="props.item.rating"
                    @save="save(props.item)"
                    @cancel="cancel"
                    @open="open"
                    @close="close"
                >
                    {{ props.item.rating }}
                    <template v-slot:input>
                        <v-text-field
                            v-model="props.item.rating"
                            :rules="[max50chars]"
                            label="Edit"
                            single-line
                            counter
                        ></v-text-field>
                    </template>
                </v-edit-dialog>
            </template>
        </v-data-table>
    </div>
</template>

<script>
import api from "../api";

export default {
    props: {
        ratingData: {
            type: Array,
            default: () => new Array()
        }
    },
    data() {
        return {
            headers: [
                { text: "평점 번호", value: "id" },
                { text: "유저 번호", value: "userid" },
                { text: "영화 번호", value: "movieid" },
                { text: "점수", value: "rating" },
                { text: "등록 시간", value: "timestamp" }
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
            api.updateRating(data);
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