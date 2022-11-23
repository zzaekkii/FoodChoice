const bgermenu = {
    init: function(){
        this.bger();
    },
    bger: function() {
        let burger = $(".burger");
        let closeburger = $(".close-burger");

        // 버거 클릭
        $(".burger").click(function(){
            $(".burgermenu").addClass("on");
            $(".close-burger").addClass("on");
            $(".shadow").css("display", "block");
        });
        // 쉐도우 클릭
        $(".shadow").click(function(){
            $(".burgermenu").removeClass("on");
            $(".shadow").css("display", "none");
        });
        // 닫기 클릭
        $(".close-burger").click(function(){
            $(".burgermenu").removeClass("on");
            $(".shadow").css("display", "none");
        });
    }
}
$(document).ready(function(){
    bgermenu.init();
})