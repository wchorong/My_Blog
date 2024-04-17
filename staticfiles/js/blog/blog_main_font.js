const fonts = ['Arial, sans-serif', 'Times New Roman, serif', 'YEONGJUPunggiGinsengTTF', 'CBNUJIKJI'];
const text = ["Django!", "Spring!", "JS!", "Server!"]
        let currentFontIndex = 0;
        const textContainer = document.getElementById('textContainer');

        function changeFont() {
            textContainer.style.fontFamily = fonts[currentFontIndex];
            textContainer.innerHTML = text[currentFontIndex];
            currentFontIndex = (currentFontIndex + 1) % fonts.length;
        }

        // 폰트 변경 함수 호출 및 애니메이션 설정
        setInterval(() => {
            changeFont();
            textContainer.style.transition = 'font-family 3s';
        }, 3000)



