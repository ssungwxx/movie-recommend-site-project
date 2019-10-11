<template>
    <v-form ref="form">
        <v-select v-model="searchDivision" :items="searchItems" label="검색 구분"></v-select>
        <v-text-field xs6 v-model="param" label="검색어" />
        <v-layout justify-center pa-10>
            <v-btn large color="#666666 white--text" @click="onSubmit">Search</v-btn>
        </v-layout>
    </v-form>
</template>

<script>
export default {
    props: {
        submit: {
            type: Function,
            default: () => {}
        }
    },
    data: () => ({
        param: "",
        searchDivision: "ID",
        searchItems: ["ID"]
    }),
    methods: {
        onSubmit: function() {
            let params = "";
            if (this.searchDivision == "ID") {
                params = {
                    id: this.param-1
                };
            }

            if (!params == "") this.submit(params);
        }
    }
};
</script>