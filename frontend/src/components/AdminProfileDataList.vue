<template>
    <div>
        <v-data-table
            :headers="headers"
            :items="profileData"
            :sort-by="['id']"
            :sort-desc="[false]"
            multi-sort
            class="elevation-1"
        >
            <template v-slot:item.is_staff="props">
                <v-edit-dialog
                    :return-value.sync="props.item.is_staff"
                    large
                    persistent
                    @save="save(props.item)"
                    @cancel="cancel"
                    @open="open"
                    @close="close"
                >
                    <div>{{ props.item.is_staff }}</div>
                    <template v-slot:input>
                        <div class="mt-4 title">Update is_staff</div>
                    </template>
                    <template v-slot:input>
                        <v-text-field
                            v-model="props.item.is_staff"
                            :rules="[max50chars]"
                            label="Edit"
                            single-line
                            counter
                            autofocus
                        ></v-text-field>
                    </template>
                </v-edit-dialog>
            </template>
            <template v-slot:item.gender="props">
                <v-edit-dialog
                    :return-value.sync="props.item.gender"
                    @save="save(props.item)"
                    @cancel="cancel"
                    @open="open"
                    @close="close"
                >
                    {{ props.item.gender }}
                    <template v-slot:input>
                        <v-text-field
                            v-model="props.item.gender"
                            :rules="[max50chars]"
                            label="Edit"
                            single-line
                            counter
                        ></v-text-field>
                    </template>
                </v-edit-dialog>
            </template>
            <template v-slot:item.age="props">
                <v-edit-dialog
                    :return-value.sync="props.item.age"
                    @save="save(props.item)"
                    @cancel="cancel"
                    @open="open"
                    @close="close"
                >
                    {{ props.item.age }}
                    <template v-slot:input>
                        <v-text-field
                            v-model="props.item.age"
                            :rules="[max50chars]"
                            label="Edit"
                            single-line
                            counter
                        ></v-text-field>
                    </template>
                </v-edit-dialog>
            </template>
            <template v-slot:item.occupation="props">
                <v-edit-dialog
                    :return-value.sync="props.item.occupation"
                    @save="save(props.item)"
                    @cancel="cancel"
                    @open="open"
                    @close="close"
                >
                    {{ props.item.occupation }}
                    <template v-slot:input>
                        <v-text-field
                            v-model="props.item.occupation"
                            :rules="[max50chars]"
                            label="Edit"
                            single-line
                            counter
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
        profileData: {
            type: Array,
            default: () => new Array()
        }
    },
    data() {
        return {
            headers: [
                { text: "번호", align: "left", value: "id" },
                { text: "사용자", value: "username" },
                { text: "권한", value: "is_staff" },
                { text: "성별", value: "gender" },
                { text: "나이", value: "age" },
                { text: "직업", value: "occupation" }
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
            api.updateProfile(data);
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