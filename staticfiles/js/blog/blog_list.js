 window.addEventListener('load', function () {
      // 이미지가 포함된 div 찾기
      var imageContainer = document.querySelector('.list-line');

      // 이미지가 포함된 div에 "loaded" 클래스 추가
      imageContainer.classList.add('loaded');

      // 실행 여부를 localStorage에서 제거하여 매번 실행되게 함
      localStorage.removeItem('hasExecuted');
    });

// 페이지 로드 후 실행되는 스크립트
    document.addEventListener("DOMContentLoaded", function() {
      var animatedDiv = document.getElementById("animatedDiv");
      animatedDiv.classList.add("show");
    });

    //스크롤 기능
document.addEventListener("DOMContentLoaded", function () {
  // 클래스 이름이 "scrolling-div"인 모든 요소 선택
  var scrollingDivs = document.getElementsByClassName("scrolling-div");

  // 스크롤 이벤트 감지
  window.addEventListener("scroll", function () {
    // 스크롤이 얼마나 내려갔는지 확인
    const scrollPosition = window.scrollY;

    // div가 화면에 나타날 때의 위치
    const triggerPosition = window.innerHeight * 0.5;

    // 각각의 scrollingDiv에 대해 작업 수행
    for (var i = 0; i < scrollingDivs.length; i++) {
      var scrollingDiv = scrollingDivs[i];

      // 현재 순회 중인 div의 위치를 계산
      var divPosition = scrollingDiv.getBoundingClientRect().top;

      // div가 화면에 나타나는지 확인
      if (divPosition < triggerPosition) {
        // div가 화면에 나타나게끔 스타일 조정
        scrollingDiv.style.opacity = 1;
        scrollingDiv.style.transform = "translateY(0)";
      }
    }
  });
});

function searchToggle(obj, evt){
    var container = $(obj).closest('.search-wrapper');
        if(!container.hasClass('active')){
            container.addClass('active');
            evt.preventDefault();
        }
        else if(container.hasClass('active') && $(obj).closest('.input-holder').length == 0){
            container.removeClass('active');
            // clear input
            container.find('.search-input').val('');
        }
}

