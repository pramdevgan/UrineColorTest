document.getElementById('id_file').addEventListener('change', function(e) {
    let fileInput = e.target;
    let fileNamePlaceholder = document.getElementById('file-name-placeholder');

    if (fileInput.files.length > 0) {
      let fileName = fileInput.files[0].name;
      fileNamePlaceholder.textContent = "Uploaded file name: " + fileName;
    } else {
      fileNamePlaceholder.textContent = "";
    }
  });


const imageEndpoint  = "http://127.0.0.1:8000/api/strip_image/"
const imageList = document.querySelector("#imageList")
const imageInput = document.querySelector("#imageInput")

const createImage = async (event) => {
  event.preventDefault()
  let image = imageInput.files[0]
  let formData = new FormData()
  formData.append('url', image)

  let newImage = await fetch(imageEndpoint, {
    method: 'POST',
    body: formData
  }).then(response=> response.json()).catch(error=>console.log(error))
  location.reload()
}
