<template>
  <v-app id="app">
    <v-app-bar app clipped-left color="#808080">
      <v-app-bar-nav-icon class="white--text" @click="drawer = !drawer" />
      <span class="title ml-3 mr-5 white--text">Movie Recommendation Service ^__^</span>
      <v-spacer />
      <v-btn large color="#666666 white--text" @click="subscribe">Subscribe - ￦8,900</v-btn>
      <div class="signup">
        <v-tooltip bottom>
          <SignUp slot="activator" />
          <span>회원가입</span>
        </v-tooltip>
      </div>
      <div class="login">
        <v-tooltip bottom>
          <Login slot="activator" />
          <span>로그인</span>
        </v-tooltip>
      </div>
    </v-app-bar>


    <v-navigation-drawer v-model="drawer" app clipped color="grey lighten-4">
      <v-list dense class="grey lighten-4">
        <template v-for="(choice, i) in choices">
          <v-list-item
            :key="i"
            @click="() => {
              if (choice.path) {
                goTo(choice.path)
              }
            }"
          >
            <v-list-item-action>
              <v-icon>{{ choice.icon }}</v-icon>
            </v-list-item-action>
            <v-list-item-content>
              <v-list-item-title class="subtitle-2 font-weight-bold black--text">{{ choice.text }}</v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </template>
      </v-list>
    </v-navigation-drawer>

    <v-content>
      <v-container fluid fill-height class="grey lighten-4">
        <v-layout justify-center align-center>
          <!-- each pages will be placed here -->
          <router-view />
        </v-layout>
      </v-container>
    </v-content>
  </v-app>
</template>

<script>
import router from "./router";
import SignUp from "./components/SignUp";
import Login from "./components/Login";

export default {
  name: "App",
  components: {
    SignUp,
    Login
  },
    data: () => ({
        drawer: null,
        choices: [
            {
                icon: "mdi-movie",
                text: "영화 검색",
                path: "movie-search"
            },
            {
                icon: "mdi-movie",
                text: "유저 검색",
                path: "profile-search"
            },
            {
                icon: "mdi-movie",
                text: "관리자 데이터 변경",
                path: "admin-data"
            },
            {
                text: "분류 검색",
                path: "classify-search"
            }
        ]
    }),
    methods: {
        goTo: function(path) {
            router.push({ name: path });
        },

        subscribe: function(){
            Vue.IMP().request_pay({
            pg: 'html5_inicis',
            pay_method: 'card',
            merchant_uid: 'merchant_' + new Date().getTime(),
            name: '구독 서비스',
            amount: 8900,
            buyer_email: 'iamport@siot.do',
            buyer_name: '구매자이름',
            buyer_tel: '010-1234-5678',
            buyer_addr: '서울특별시 강남구 삼성동',
            buyer_postcode: '123-456'
            }, (result_success) => {
            //성공할 때 실행 될 콜백 함수
            var msg = '결제가 완료되었습니다.';
            msg += '고유ID : ' + result_success.imp_uid;
            msg += '상점 거래ID : ' + result_success.merchant_uid;
            msg += '결제 금액 : ' + result_success.paid_amount;
            msg += '카드 승인번호 : ' + result_success.apply_num;
            alert(msg);
            }, (result_failure) => {
            //실패시 실행 될 콜백 함수
            var msg = '결제에 실패하였습니다.';
            msg += '에러내용 : ' + result_failure.error_msg;
            alert(msg);
            })
        }
    }
};
</script>

<style>
.icons {
  float: right;
}
#keep .v-navigation-drawer__border {
  display: none;
}

.signup {
  padding-right: 20px;
}
</style>