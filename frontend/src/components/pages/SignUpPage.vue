<template>
    <v-container>
        <v-card>
            <br><br>
                <div class="headline" style="width: 100%; text-align:center;" >Sign Up</div>

            <v-card-text>
                <v-container grid-list-md>
                    <v-layout wrap>
                        <v-flex xs1></v-flex>
                        <v-flex xs10>
                            <v-text-field v-model="username" label="username *"></v-text-field>
                        </v-flex>
                        <v-flex xs1></v-flex>
                        <v-flex xs1></v-flex>
                        <v-flex xs10>
                            <v-text-field v-model="password" label="password *" type="password"></v-text-field>
                        </v-flex>
                        <v-flex xs1></v-flex>
                        <!-- <v-flex xs12>
                            <v-text-field v-model="pwCheck" label="비밀번호 확인 password check *" type="password"
                                          :error-messages='pwMatchError()'></v-text-field>
                        </v-flex> -->
                        <v-flex xs12></v-flex>
                        <v-flex xs12></v-flex>
                        <v-flex xs1></v-flex>
                        <v-flex xs1>
                            Gender
                            <v-radio-group v-model="gender">
                                <v-radio label="M" value="M"></v-radio>
                                <v-radio label="F" value="F"></v-radio>
                            </v-radio-group>
                        </v-flex>
                        <v-flex xs2>
                            Age
                            <v-select v-model="age" :items="ages" label="Age" solo></v-select>
                        </v-flex>   
                        <v-flex xs1>
                        </v-flex>
                        <v-flex xs6>
                            Occupation
                            <v-select v-model="occupation" :items="occupations" label="Occupation" solo></v-select>
                        </v-flex>
                    </v-layout>
                </v-container>
            </v-card-text>

            <v-card-actions style="background-color:black;">
                    <v-btn color="blue darken-1" @click="back">Cancel</v-btn>
                    <v-btn color="blue darken-1" @click="join">Save</v-btn>
            </v-card-actions> 
        </v-card>
    </v-container>
</template>

<script>
import axios from 'axios'
import api from '../../api/'

const apiUrl = "/api";
export default {
    name: 'signup',
    components: {
        axios
    },
    data:()=>({
        username:'',
        password:'',
        gender:'',
        age:'',
        occupation :'',
        ages: ['1~17', '18~24', '25~34', '35~44', '45~49', '50~55', '56~'],
        occupations: ['other', 'academic/educator','artist','clerical/admin','college/grad student','customer service','doctor/health care','executive/managerial','farmer','homemaker','K-12 student','lawyer','programmer','retired','sales/marketing','scientist','self-employed','technician/engineer','tradesman/craftsman','unemployed','writer'],
        
    }),
    methods: {

        back: function() {
            this.$router.push({ name : "home" })
        },

        join: async function(){
            
            if (this.username=="" || this.username == null){
                alert("아이디를 입력하세요!");
                return;
            }
            if (this.password == "" || this.password == null){
                alert("비밀번호를 입력하세요");
                return;
            }
            if (this.ages == "" || this.ages == null){
                alert("나이를 입력하세요");
                return;
            }
            if (this.gender == "" || this.gender == null){
                alert("성별을 입력하세요");
                return;
            }
            if (this.occupation == null){
                alert("직업을 입력하세요");
                return;
            }
            if (this.age == null){
                alert("나이를 입력하세요");
                return;
            }
            if(this.age =='1~17'){
                this.age = 1;
            }else if(this.age =='18~24'){
                this.age = 18; 
            }else if(this.age =='25~34'){
                this.age = 25; 
            }else if(this.age =='35~44'){
                this.age = 35; 
            }else if('45~49'){
                this.age = 45; 
            }else if('50~55'){
                this.age = 50; 
            }else{
                this.age = 56; 
            } 

            let params={
               profiles:[
                {
                    username: this.username,
                    password:this.password,
                    gender: this.gender,
                    age: this.age,
                    occupation: this.occupation

                }
               ]
    
            } 

            await api.signup(params);       
        }
    }

};
</script>
