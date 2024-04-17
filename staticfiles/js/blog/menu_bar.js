const hoverLink = document.getElementById('hoverLink');
const popup = document.getElementById('popup');
const popupContent = document.getElementById('popupContent');

hoverLink.addEventListener('mouseover', () => {
    popup.style.display = 'block';
    setTimeout(() => {
        popup.style.opacity = '1'; // 투명도를 서서히 1로 증가시켜 팝업을 나타냄
        popup.style.top = '17%'
    }, 10); // 즉시 시작하지 않도록 작은 지연을 추가
});
popup.addEventListener('mouseover', () => {
    // 팝업 내부에 마우스가 있을 때도 팝업을 유지합니다.
    popup.style.top = '20%';
});
hoverLink.addEventListener('mouseout', () => {
    popup.style.opacity = '0'; // 투명도를 0으로 설정하여 팝업을 숨김
    setTimeout(() => {
        popup.style.display = 'none';
        popup.style.top = '20%'
    }, 500); // 투명도가 0이 된 후 0.5초 후에 팝업을 숨김
});