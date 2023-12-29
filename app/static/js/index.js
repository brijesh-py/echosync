(function () {
  const messages = document.querySelector(".messages");
  const openFileEditorBtn = document.querySelector(".open__file__editor__btn");
  const closeFileEditorBtn = document.querySelector(".close__file__editor__btn");
  const fileEditorModel = document.querySelector('.file__editor__model');

  setTimeout(() => {
    try {
      messages.style.display = "none";
    } catch {}
  }, 5000);

  openFileEditorBtn.addEventListener('click',() =>{
    fileEditorModel.classList.toggle('hide')
  })

  closeFileEditorBtn.addEventListener('click',() =>{
    fileEditorModel.classList.toggle('hide')
  })

})();
