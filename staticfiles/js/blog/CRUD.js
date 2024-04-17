document.querySelector("a[href='#targetDiv']").addEventListener("click", function(event) {
    // 기본 동작(링크 이동)을 막습니다.
    event.preventDefault();

    // 대상 div의 위치를 가져옵니다.
    const targetDiv = document.getElementById("targetDiv");

    // 대상 div의 위치로 스크롤을 이동합니다.
    targetDiv.scrollIntoView({ behavior: 'smooth' });
});
