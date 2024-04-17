// 파일이 선택되었을 때 실행되는 함수
  function previewImage(event) {
    var file = event.target.files[0]; // 선택된 파일
    var reader = new FileReader(); // 파일을 읽는 객체

    reader.onload = function(event) {
      var imgElement = document.createElement("img"); // 이미지 엘리먼트 생성
      imgElement.src = event.target.result; // 이미지 소스 설정
      document.getElementById("imagePreview").innerHTML = ""; // 이전에 표시된 이미지 제거
      document.getElementById("imagePreview").appendChild(imgElement); // 이미지를 div에 추가
    };

    // 파일 읽기 시작
    reader.readAsDataURL(file);
  }

  // 파일 입력 요소에 이벤트 리스너 추가
  document.getElementById("fileInput").addEventListener("change", previewImage);