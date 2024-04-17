document.addEventListener('DOMContentLoaded', function() {
      const div = document.querySelector('.moving-div');

      function moveDownAndUp() {
        div.classList.add('moved');
        setTimeout(() => {
          div.classList.remove('moved');
        }, 1500);
      }

      setInterval(moveDownAndUp, 2000); // 2초마다 호출
    });