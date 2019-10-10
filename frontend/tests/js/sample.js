import Vue from "vue";
import MovieSearchPage from "pages/MovieSearchPage";
// import MovieList from "../../src/components/MovieList";

describe("MovieSearchPage", () => {
    // 원시 컴포넌트 옵션을 검사합니다.
    it("has a created hook", () => {
        expect(typeof MovieSearchPage.created).toBe("function");
    });

    // 원시 컴포넌트 옵션에서 함수 결과를 테스트합니다.
    it("sets the correct default data", () => {
        expect(typeof MovieSearchPage.data).toBe("function");
        const defaultData = MyComponent.data();
        expect(defaultData.message).toBe("hello!");
    });

    // 마운트 할 때 컴포넌트 인스턴스를 검사합니다.
    it("correctly sets the message when created", () => {
        const vm = new Vue(MovieSearchPage).$mount();
        expect(vm.message).toBe("bye!");
    });

    // 인스턴스를 마운트하고 출력된 결과를 검사합니다.
    it("renders the correct message", () => {
        const Constructor = Vue.extend(MovieSearchPage);
        const vm = new Constructor().$mount();
        expect(vm.$el.textContent).toBe("bye!");
    });
});
